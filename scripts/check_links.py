"""Check resource pages without fetching dataset or paper files.

python scripts/check_links.py
python scripts/check_links.py --retry-problems

HEAD first; GET fallback reads at most 64 KiB of HTML/text only. Results concern
page reachability, not project identity, metadata correctness or reproducibility.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime as dt
import json
from pathlib import Path
import re
import threading
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
MAX_HTML_BYTES = 65536
TIMEOUT_SECONDS = 18
HOST_LIMIT = 3
LOCK = threading.Lock()
HOST_LOCKS = {}
USER_AGENT = "Mozilla/5.0 (compatible; SafetyBenchmarkLinkChecker/1.0; metadata-links-only)"


def now():
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds")


class Redirects(HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append({"status": code, "from": req.full_url, "to": newurl})
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def request_once(url, method):
    redirects = Redirects()
    opener = build_opener(redirects)
    request = Request(url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/json;q=0.8,*/*;q=0.1"})
    started = time.monotonic()
    response = None
    data = {"method": method, "http_status": None, "final_url": url,
            "redirects": [], "content_type": None, "page_title": None, "error": None,
            "body_bytes_read": 0}
    try:
        try:
            response = opener.open(request, timeout=TIMEOUT_SECONDS)
        except HTTPError as error:
            response = error
        data["http_status"] = response.code
        data["final_url"] = response.geturl()
        data["content_type"] = response.headers.get("Content-Type", "").split(";")[0]
        if method == "GET" and data["content_type"] in {"text/html", "application/xhtml+xml", "text/plain", "application/json"}:
            body = response.read(MAX_HTML_BYTES)
            data["body_bytes_read"] = len(body)
            text = body.decode("utf-8", errors="replace")
            match = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
            if match:
                data["page_title"] = re.sub(r"\s+", " ", match[1]).strip()[:250]
            if re.search(r"Just a moment|Attention Required|Access Denied|Forbidden|Security Verification", data["page_title"] or "", re.I):
                data["challenge_page"] = True
    except (URLError, TimeoutError, OSError, ValueError) as error:
        data["error"] = str(error)[:350]
    finally:
        if response:
            response.close()
        data["redirects"] = redirects.chain
        data["elapsed_seconds"] = round(time.monotonic() - started, 2)
    return data


def status_for(attempt):
    status = attempt["http_status"]
    if status in {404, 410}:
        return "not_found"
    if status in {401, 403, 429, 451} or attempt.get("challenge_page"):
        return "restricted"
    if status and 200 <= status < 400:
        url = urlsplit(attempt["final_url"])
        if re.search(r"(?:^|/)(?:login|signin|sign-in|auth)(?:/|$)", url.path, re.I) or url.hostname == "accounts.google.com":
            return "login_required"
        return "redirected" if attempt["redirects"] else "accessible"
    if status and status >= 500:
        return "server_error"
    if status:
        return "http_error"
    return "network_error"


def check(url):
    host = urlsplit(url).hostname
    with LOCK:
        semaphore = HOST_LOCKS.setdefault(host, threading.BoundedSemaphore(HOST_LIMIT))
    with semaphore:
        attempts = [request_once(url, "HEAD")]
        status = status_for(attempts[-1])
        # Validate failures with GET because some hosts reject HEAD requests.
        if status not in {"accessible", "redirected"}:
            attempts.append(request_once(url, "GET"))
            status = status_for(attempts[-1])
        if status in {"network_error", "server_error"}:
            attempts.append(request_once(url, "HEAD"))
            status = status_for(attempts[-1])
        selected = attempts[-1]
        return {"url": url, "status": status, "checked_at": now(),
                "http_status": selected["http_status"], "final_url": selected["final_url"],
                "content_type": selected["content_type"], "redirects": selected["redirects"],
                "error": selected["error"], "page_title": selected["page_title"],
                "attempts": attempts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--retry-problems", action="store_true")
    args = parser.parse_args()
    catalog = json.loads((ROOT / "data/benchmarks.json").read_text(encoding="utf-8"))
    all_links = {l["url"]: l for e in catalog["entries"] for l in e["links"]}
    output = ROOT / "data/link_checks.json"
    results = {}
    if args.retry_problems and output.exists():
        results = {r["url"]: r for r in json.loads(output.read_text(encoding="utf-8"))["results"] if r["url"] in all_links}
    targets = []
    for url, link in sorted(all_links.items()):
        if link["quality"] in {"placeholder", "misattributed"}:
            results[url] = {"url": url, "status": "skipped_" + link["quality"], "checked_at": None,
                            "http_status": None, "final_url": None, "attempts": []}
        elif not args.retry_problems or url not in results or results[url]["status"] in {"network_error", "server_error", "restricted", "http_error"}:
            targets.append(url)
    print(json.dumps({"check_started_at": now(), "unique_urls": len(all_links), "requests_to_check": len(targets), "workers": args.workers}), flush=True)
    started = time.monotonic()
    def save():
        counts = dict(Counter(r["status"] for r in results.values()))
        payload = {"checked_on": now()[:10], "scope": "page_reachability_only", "dataset_files_downloaded": False,
                   "paper_files_downloaded": False, "total_unique_urls": len(all_links),
                   "completed_urls": len(results), "by_status": counts,
                   "results": [results[u] for u in sorted(results)]}
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return counts
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(check, u): u for u in targets}
        for i, future in enumerate(as_completed(futures), start=1):
            url = futures[future]
            try:
                results[url] = future.result()
            except Exception as error:
                results[url] = {"url": url, "status": "network_error", "checked_at": now(), "error": str(error), "http_status": None, "final_url": url, "attempts": []}
            if i % 25 == 0 or i == len(targets):
                counts = save()
                print(json.dumps({"completed_this_run": i, "target_count": len(targets), "elapsed_seconds": round(time.monotonic() - started), "by_status": counts}), flush=True)
    counts = save()
    print(json.dumps({"finished_at": now(), "by_status": counts}), flush=True)


if __name__ == "__main__":
    main()

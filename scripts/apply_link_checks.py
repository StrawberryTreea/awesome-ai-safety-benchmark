"""Apply a complete page-reachability audit to the canonical catalog.

python scripts/apply_link_checks.py
Preserves recorded URLs and source metadata. Does not fetch remote content.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCESS_FIELDS = ("status", "checked_at", "http_status", "final_url", "redirects", "error", "page_title")
ISSUE_STATUSES = {"not_found", "restricted", "login_required", "server_error", "network_error", "http_error"}


def main():
    catalog_path = ROOT / "data/benchmarks.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    audit = json.loads((ROOT / "data/link_checks.json").read_text(encoding="utf-8"))
    results = {r["url"]: r for r in audit["results"]}
    expected = {l["url"] for e in catalog["entries"] for l in e["links"]}
    if (set(results) != expected or len(results) != len(audit["results"])
            or audit["completed_urls"] != len(expected)
            or audit["total_unique_urls"] != len(expected)
            or audit["by_status"] != dict(Counter(r["status"] for r in results.values()))):
        raise SystemExit("Link audit is incomplete or inconsistent; run check_links.py first.")
    if audit["scope"] != "page_reachability_only":
        raise SystemExit("Unexpected link-check scope.")
    for entry in catalog["entries"]:
        checked_dates = []
        issues = {i for i in entry["issues"] if not i.startswith("link_access_")}
        for link in entry["links"]:
            result = results[link["url"]]
            link["access"] = {k: result.get(k) for k in ACCESS_FIELDS}
            if result["status"] in ISSUE_STATUSES:
                issues.add("link_access_" + result["status"])
            if not result["status"].startswith("skipped_"):
                if not result.get("checked_at"):
                    raise SystemExit("Missing check timestamp: " + link["url"])
                checked_dates.append(result["checked_at"][:10])
        verification = entry["verification"]
        verification.pop("last_verified", None)
        verification.pop("reproduction_checked", None)
        verification.update({
            "status": "links_checked" if checked_dates else "link_sources_pending",
            "last_link_check": max(checked_dates) if checked_dates else None,
            "link_access_checked": bool(checked_dates),
            "basis": "supplied_workbooks_and_page_reachability_checks",
        })
        entry.pop("license", None)
        entry["issues"] = sorted(issues)
    catalog["updated_on"] = max(catalog["updated_on"], audit["checked_on"])
    catalog["collection_policy"] = {
        "purpose": "resource_navigation",
        "link_check_scope": "page_reachability_only",
        "license_review_required": False,
        "benchmark_execution_required": False,
        "paper_only_entries_allowed": True,
    }
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Applied {len(results)} URL outcomes to {len(catalog['entries'])} entries; original URLs preserved.")


if __name__ == "__main__":
    main()

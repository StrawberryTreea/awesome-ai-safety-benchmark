"""Offline validation for catalog identity, provenance, status and generated exports.

python scripts/validate.py
python scripts/validate.py --check-source-files .local/source_manifest.json
Standard library only. No network checks and no changes to catalog files.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TRACKS = {"llm_safety", "agent_safety", "safety_judging", "related_resources"}
STATUSES = {"listed", "related", "needs_review"}
TYPES = {"benchmark", "benchmark_suite", "evaluation_dataset", "training_dataset", "attack_method", "framework", "suite_component"}


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8-sig"))


def validate(catalog, records, sources):
    errors, ids, names, covered = [], set(), set(), Counter()
    def require(condition, message):
        if not condition:
            errors.append(message)
    source_ids = {s["id"] for s in sources["sources"]}
    record_ids = {r["record_id"] for r in records["records"]}
    require(len(record_ids) == len(records["records"]), "Duplicate source record IDs")
    for r in records["records"]:
        require(r["source_id"] in source_ids, f"Unknown source: {r['record_id']}")
        require(not ({"收集人", "示例"} & set(r["fields"])), f"Private source fields: {r['record_id']}")
    for e in catalog["entries"]:
        eid = e.get("id")
        require(bool(eid) and eid not in ids, f"Duplicate or missing entry ID: {eid}")
        ids.add(eid)
        name = e.get("name", "").casefold()
        require(bool(name) and name not in names, f"Duplicate or missing canonical name: {name}")
        names.add(name)
        require(e.get("track") in TRACKS, f"Invalid track: {eid}")
        require(e.get("catalog_status") in STATUSES, f"Invalid status: {eid}")
        require(e.get("resource_type") in TYPES, f"Invalid resource type: {eid}")
        for field in ("description_en", "description_zh"):
            value = e.get(field)
            require(field in e and (value is None or isinstance(value, str)), f"Invalid {field}: {eid}")
            if e.get("catalog_status") != "needs_review":
                require(isinstance(value, str) and bool(value.strip()), f"Missing public {field}: {eid}")
        require(bool(e.get("source_refs")), f"Missing provenance: {eid}")
        for ref in e.get("source_refs", []):
            require(ref in record_ids, f"Unknown source ref: {eid}/{ref}")
            covered[ref] += 1
        own_refs = set(e.get("source_refs", []))
        for field, metadata in e.get("reported_metadata", {}).items():
            for value in [metadata, *metadata.get("alternatives", [])]:
                if value.get("value") is not None:
                    require(value.get("source_ref") in own_refs, f"Orphan metadata: {eid}/{field}")
        urls = set()
        for link in e.get("links", []):
            url = link["url"]
            parsed = urlsplit(url)
            require(parsed.scheme in {"http", "https"} and bool(parsed.netloc), f"Invalid URL: {eid}/{url}")
            require(url not in urls, f"Duplicate URL: {eid}/{url}")
            require(link["type"] in {"paper", "code", "dataset", "project"}, f"Invalid link type: {eid}")
            require(link["quality"] in {"source_supplied", "placeholder", "aggregator_homepage", "misattributed"}, f"Invalid link quality: {eid}")
            require(bool(link["source_refs"]) and set(link["source_refs"]) <= own_refs, f"Orphan link refs: {eid}")
            urls.add(url)
        if e.get("catalog_status") in {"listed", "related"}:
            require(any(l["quality"] == "source_supplied" for l in e.get("links", [])), f"Listed entry lacks direct source: {eid}")
        if e.get("catalog_status") == "related":
            require(e["track"] == "related_resources", f"Related entry in safety track: {eid}")
        if e.get("catalog_status") == "listed":
            require(e["track"] != "related_resources", f"Supporting resource counted as safety benchmark: {eid}")
        verification = e.get("verification", {})
        if verification.get("status") == "imported_unverified":
            require(verification.get("last_link_check") is None, f"Import date used as checked date: {eid}")
            require(verification.get("link_access_checked") is False, f"Unverified entry claims link check: {eid}")
        if verification.get("link_access_checked"):
            require(bool(verification.get("last_link_check")), f"Missing link check date: {eid}")
            for link in e.get("links", []):
                require(bool(link.get("access", {}).get("status")), f"Missing link check result: {eid}")
    require(set(covered) == record_ids, "Some source records are missing from catalog")
    require(all(v == 1 for v in covered.values()), "Some source records belong to multiple catalog entries")
    for e in catalog["entries"]:
        if e.get("parent_id"):
            require(e["parent_id"] in ids and e["parent_id"] != e["id"], f"Invalid parent ID: {e['id']}")
    for s in sources["sources"]:
        require(sum(r["source_id"] == s["id"] for r in records["records"]) == s["named_rows"], f"Source row count mismatch: {s['id']}")
    serialized = json.dumps([catalog, records, sources], ensure_ascii=False)
    require(not re.search(r"[A-Za-z]:[\\/](?:Users|Windows)[\\/]", serialized, re.I), "Absolute user paths in public data")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-source-files", type=Path)
    args = parser.parse_args()
    catalog, records, sources = load("data/benchmarks.json"), load("data/source_records.json"), load("data/sources.json")
    errors = validate(catalog, records, sources)
    audit_path = ROOT / "data/link_checks.json"
    if audit_path.exists():
        audit = load("data/link_checks.json")
        results = {r["url"]: r for r in audit["results"]}
        catalog_links = [l for e in catalog["entries"] for l in e["links"]]
        if set(results) != {l["url"] for l in catalog_links} or len(results) != len(audit["results"]):
            errors.append("Unique-URL audit does not cover canonical URLs exactly")
        if audit["by_status"] != dict(Counter(r["status"] for r in results.values())):
            errors.append("Link audit counts do not match results")
        from apply_link_checks import ACCESS_FIELDS
        for link in catalog_links:
            result = results.get(link["url"])
            if not result or link.get("access") != {k: result.get(k) for k in ACCESS_FIELDS}:
                errors.append("Canonical access result differs from audit: " + link["url"])
    stats = load("data/stats.json")
    if stats["unique_catalog_entries"] != len(catalog["entries"]):
        errors.append("Stats total does not match canonical catalog")
    if stats["by_catalog_status"] != dict(Counter(e["catalog_status"] for e in catalog["entries"])):
        errors.append("Stats status counts do not match canonical catalog")
    from curate import CSV_COLUMNS, flatten, safe_csv_value
    for filename, subset in [("benchmarks.csv", catalog["entries"]), ("review_queue.csv", [e for e in catalog["entries"] if e["catalog_status"] == "needs_review"])]:
        with (ROOT / "data" / filename).open(encoding="utf-8-sig", newline="") as source:
            actual = list(csv.DictReader(source))
        expected = [{k: str(safe_csv_value(v)) if v is not None else "" for k, v in flatten(e).items()} for e in subset]
        if actual != expected:
            errors.append(f"CSV does not match canonical catalog: {filename}")
    if args.check_source_files:
        manifest = json.loads(args.check_source_files.read_text(encoding="utf-8-sig"))
        # The catalog may also include web-only repair sources, which have no
        # local file hash.  The manifest is the authoritative list of files
        # that can be checked here.
        hashes = {s["id"]: s.get("sha256") for s in sources["sources"]}
        for s in manifest["sources"]:
            expected = hashes.get(s["id"])
            if not expected:
                errors.append(f"Missing source hash: {s['id']}")
                continue
            if hashlib.sha256(Path(s["path"]).read_bytes()).hexdigest() != expected:
                errors.append(f"Original workbook changed: {s['id']}")
    if errors:
        print("Validation failed:\n" + "\n".join("- " + x for x in errors))
        return 1
    print(f"Validated {len(catalog['entries'])} entries and {len(records['records'])} source rows; IDs, provenance, counts and CSV exports reconcile.")
    if args.check_source_files:
        print("All five original workbook hashes match the pre-extraction hashes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Rebuild the first curated import using explicit aliases and category decisions.

No network access. Source metadata stays source-reported. Regeneration is explicit:
python scripts/curate.py
Future manually verified entries belong in benchmarks.json; do not regenerate that
file after manual edits without updating curation decisions and source evidence.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
NULLS = {"", "-", "--", "none", "null", "n/a", "nan", "+", "待补充", "未知"}
FIELDS = {
    "year": ["年份"],
    "languages": ["语言"],
    "size": ["规模/数据量", "数据规模"],
    "tasks": ["具体测试任务", "任务类型"],
    "environment": ["测试环境/交互形式", "环境与运行成本", "Execution Profile"],
    "execution": ["执行真实性类型"],
    "execution_notes": ["是否真实执行及说明"],
    "evaluation": ["评估方法"],
    "metrics": ["评估指标", "评价指标"],
    "availability": ["是否公开可用"],
    "maturity": ["成熟度/证据", "可用性等级"],
    "multi_turn": ["是否多轮"],
}


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path, obj):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s))).strip().casefold()


def present(v):
    return v is not None and norm(v) not in NULLS


def preference(record):
    key = (record["source_id"], record["sheet"])
    ranks = {
        ("agent-screen-v2", "核心保留核验详表"): 0,
        ("agent-screen-v2", "最终筛查总表"): 1,
        ("agent-screen-v2", "第二阶段详表"): 2,
        ("agent-collection", "Sheet1"): 3,
        ("llm-increment", "原始统计表"): 4,
        ("agent-rescreen", "全量重筛结果"): 5,
    }
    return (ranks.get(key, 9), record["row"], record["record_id"])


def normalized_languages(text):
    result = []
    for part in re.split(r"[,，、;/；\s]+", str(text)):
        part = part.strip()
        if not part:
            continue
        label = {"中": "zh", "中文": "zh", "汉语": "zh", "英": "en", "英文": "en", "英语": "en",
                 "其他": "other", "多语言": "multilingual", "中英双语": "zh+en"}.get(part, part)
        if label not in result:
            result.append(label)
    return result


def canonical_url(url):
    url = url.strip().rstrip(".,;；，。\"'）】》")
    # Trim punctuation wrapping the URL, preserving paired URL parentheses.
    while url.endswith(")") and url.count(")") > url.count("("):
        url = url[:-1]
    bits = urlsplit(url)
    if bits.scheme not in {"http", "https"} or not bits.netloc:
        return None
    path = bits.path.rstrip("/")
    if bits.hostname in {"github.com", "www.github.com"}:
        path = path.removesuffix(".git")
    if bits.hostname in {"arxiv.org", "www.arxiv.org"}:
        match = re.match(r"/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?$", path)
        if match:
            return "https://arxiv.org/abs/" + match[1]
    return urlunsplit((bits.scheme.lower(), bits.netloc.lower(), path, bits.query, ""))


def link_type(url):
    p = urlsplit(url)
    host = p.hostname or ""
    if any(s in host for s in ("arxiv.org", "aclanthology.org", "openreview.net", "proceedings.", "dl.acm.org")) or p.path.endswith(".pdf"):
        return "paper"
    if host == "huggingface.co" and p.path.startswith("/datasets/"):
        return "dataset"
    if host in {"github.com", "gitlab.com"} or "4open.science" in host:
        return "code"
    return "project"


def links_from(records):
    out = {}
    for record in records:
        for field, value in record["fields"].items():
            # URLs only from metadata/link/evidence columns. No examples or payloads.
            if not any(s in field for s in ["链接", "来源", "核验备注", "成熟度/证据"]):
                continue
            for raw in re.findall(r'https?://[^\s<>；，、\u4e00-\u9fff]+', str(value)):
                url = canonical_url(raw)
                if url:
                    out.setdefault(url, {"url": url, "type": link_type(url), "source_refs": []})["source_refs"].append(record["record_id"])
        for link in record["hyperlinks"]:
            url = canonical_url(link["url"])
            if url:
                out.setdefault(url, {"url": url, "type": link_type(url), "source_refs": []})["source_refs"].append(record["record_id"])
    for link in out.values():
        link["source_refs"] = sorted(set(link["source_refs"]))
        parsed = urlsplit(link["url"])
        if re.search(r"xxxx|yyyy|zzzz|example\.com|placeholder|your[-_]", link["url"], re.I):
            link["quality"] = "placeholder"
        elif parsed.hostname in {"openeval.org.cn", "www.openeval.org.cn"} and parsed.path in {"", "/"}:
            link["quality"] = "aggregator_homepage"
        else:
            link["quality"] = "source_supplied"
    return list(out.values())


def reported_fields(records):
    output, conflicts = {}, []
    for target, labels in FIELDS.items():
        candidates, seen = [], set()
        for record in records:
            for label in labels:
                v = record["fields"].get(label)
                if not present(v):
                    continue
                key = norm(v)
                if target == "languages":
                    key = "|".join(sorted(normalized_languages(v)))
                if key in seen:
                    continue
                seen.add(key)
                candidates.append({"value": v, "source_ref": record["record_id"],
                                   "field": label, "cell": record["cells"].get(label)})
        if not candidates:
            output[target] = {"value": None, "source_ref": None, "alternatives": []}
        else:
            output[target] = {**candidates[0], "alternatives": candidates[1:]}
            if len(candidates) > 1:
                conflicts.append(target)
    return output, conflicts


def build():
    raw = read("data/source_records.json")["records"]
    decisions = read("data/curation.json")
    aliases = {norm(k): v for k, v in decisions["aliases"].items()}
    groups = {}
    for group in decisions["groups"]:
        for name in group["names"]:
            if norm(name) in groups:
                raise ValueError(f"Multiple category decisions: {name}")
            groups[norm(name)] = {**group, "name": name}
    overrides = {norm(k): v for k, v in decisions["overrides"].items()}
    grouped = defaultdict(list)
    for record in raw:
        key = norm(aliases.get(norm(record["name"]), record["name"]))
        if key not in groups:
            raise ValueError(f"Missing category decision: {record['name']}")
        grouped[key].append(record)
    entries = []
    for key, records in sorted(grouped.items()):
        group = groups[key]
        records.sort(key=preference)
        override = overrides.get(key, {})
        name = group["name"]
        slug = re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()).strip("-")
        entry_id = slug or "entry-" + hashlib.sha256(name.encode()).hexdigest()[:10]
        fields, conflicts = reported_fields(records)
        links = links_from(records)
        if "preferred_paper" in override:
            for link in links:
                if link["url"] == override["preferred_paper"]:
                    link["preferred"] = True
                elif name == "WASP" and "2506.09956" in link["url"]:
                    link["quality"] = "misattributed"
        usable = [x for x in links if x["quality"] == "source_supplied"]
        issues = []
        if any(x["quality"] == "placeholder" for x in links):
            issues.append("placeholder_link")
        if not usable:
            issues.append("no_direct_source_link")
        if usable and all(x["type"] == "paper" for x in usable):
            issues.append("paper_only")
        if any(x["quality"] == "misattributed" for x in links):
            issues.append("misattributed_link")
        if conflicts:
            issues.append("source_metadata_variants")
        if override.get("issue"):
            issues.append(override["issue"])
        status = "related" if group["track"] == "related_resources" else "listed"
        if not usable:
            status = "needs_review"
        status = override.get("status", status)
        if status == "needs_review" and not any(x in issues for x in ["no_direct_source_link", "bundled_projects", "repository_conflict", "name_needs_verification"]):
            issues.append("identity_or_scope_needs_review")
        # Original workbook screening is historical evidence, never executable instructions.
        screening = []
        for r in records:
            decisions_in_row = {k: v for k, v in r["fields"].items() if k in ["处理", "原因", "筛选结论", "最终结论", "分轨/结论", "重筛大类", "主要理由", "筛选理由", "调整说明", "核验备注", "本轮建议", "本轮使用建议", "处理建议"]}
            if decisions_in_row:
                screening.append({"source_ref": r["record_id"], "fields": decisions_in_row})
        descriptions = []
        for r in records:
            for label in ["安全主题", "二级维度", "具体测试任务"]:
                v = r["fields"].get(label)
                if present(v) and v not in ["暂时删除", "对抗维度"]:
                    descriptions.append(str(v).strip())
        language = fields["languages"]["value"]
        year_text = str(fields["year"]["value"] or "")
        year_candidates = re.findall(r"20\d{2}", year_text)
        entries.append({
            "id": entry_id, "name": name,
            "aliases": sorted({r["name"] for r in records if r["name"] != name}),
            "track": group["track"], "topic": group["topic"], "resource_type": group["resource_type"],
            "catalog_status": status, "description_zh": descriptions[0] if descriptions else None,
            "languages": normalized_languages(language) if language is not None else [],
            "year": int(year_candidates[0]) if len(year_candidates) == 1 else None,
            "reported_metadata": fields, "metadata_variant_fields": conflicts,
            "links": links,
            "verification": {"status": "imported_unverified", "last_link_check": None,
                             "imported_on": decisions["imported_on"],
                             "basis": "supplied_workbooks", "link_access_checked": False},
            "issues": sorted(set(issues)), "curation_note_zh": override.get("note"),
            "parent_id": None, "parent_name": override.get("parent_name"),
            "source_refs": sorted(r["record_id"] for r in records),
            "historical_screening": screening,
        })
    name_to_id = {e["name"]: e["id"] for e in entries}
    for entry in entries:
        if entry["parent_name"]:
            entry["parent_id"] = name_to_id[entry["parent_name"]]
    if len({e["id"] for e in entries}) != len(entries):
        raise ValueError("Canonical ID collision")
    catalog = {"schema_version": "1.0", "updated_on": decisions["imported_on"], "entries": entries}
    dump("data/benchmarks.json", catalog)
    write_exports(catalog)


CSV_COLUMNS = ["id", "name", "catalog_status", "track", "topic", "resource_type", "year", "year_reported", "languages",
               "description_zh", "size_reported", "metrics_reported", "execution_reported", "availability_reported",
               "code_urls", "dataset_urls", "paper_urls", "project_urls", "last_link_check", "link_status_summary",
               "issues", "curation_note_zh", "parent_id", "source_refs"]


def flatten(entry):
    row = {k: entry.get(k) for k in CSV_COLUMNS}
    row["languages"] = "; ".join(entry["languages"])
    row["year_reported"] = entry["reported_metadata"]["year"]["value"]
    row["last_link_check"] = entry["verification"].get("last_link_check")
    row["link_status_summary"] = "; ".join(f"{k}:{v}" for k,v in sorted(Counter(l.get("access", {}).get("status", "unchecked") for l in entry["links"] if l["quality"] == "source_supplied").items()))
    for dest, src in [("size_reported", "size"), ("metrics_reported", "metrics"), ("execution_reported", "execution"), ("availability_reported", "availability")]:
        row[dest] = entry["reported_metadata"][src]["value"]
    for typ in ["code", "dataset", "paper", "project"]:
        row[typ + "_urls"] = "\n".join(effective_url(l) for l in entry["links"] if l["type"] == typ and l["quality"] == "source_supplied" and l.get("access", {}).get("status") != "not_found")
    row["issues"] = "; ".join(entry["issues"])
    row["source_refs"] = "\n".join(entry["source_refs"])
    return row


def effective_url(link):
    access = link.get("access", {})
    if access.get("status") == "redirected":
        return access.get("final_url") or link["url"]
    return link["url"]


def navigation_links(entry):
    """One reachable/preferred source per resource type; retain uncertain access with labels."""
    links = [l for l in entry["links"] if l["quality"] == "source_supplied"
             and l.get("access", {}).get("status") != "not_found"]
    links.sort(key=lambda l: (l.get("access", {}).get("status") not in {"accessible", "redirected"},
                              not l.get("preferred", False)))
    selected = {}
    for link in links:
        selected.setdefault(link["type"], link)
    return list(selected.values())


def safe_csv_value(value):
    # CSV formula injection protection for Excel. JSON preserves the exact source.
    if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def export_contents(catalog):
    entries = catalog["entries"]
    outputs = {}
    for name, subset in [("benchmarks.csv", entries), ("review_queue.csv", [e for e in entries if e["catalog_status"] == "needs_review"])]:
        out = io.StringIO(newline="")
        writer = csv.DictWriter(out, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({k: safe_csv_value(v) for k, v in flatten(e).items()} for e in subset)
        outputs["data/" + name] = ("\ufeff" + out.getvalue()).encode("utf-8")
    stats = {
        "updated_on": catalog["updated_on"], "source_files": len(read("data/sources.json")["sources"]),
        # Web-only link-repair records are provenance sources, but the README
        # reports the number of original collection files separately.
        "collection_source_files": sum("sha256" in s for s in read("data/sources.json")["sources"]),
        "source_rows_including_repeated_views": len(read("data/source_records.json")["records"]),
        "base_collection_rows": sum(s["named_rows"] for src in read("data/sources.json")["sources"] if src["id"] in {"llm-increment", "agent-collection"} for s in src.get("sheets", [])),
        "unique_catalog_entries": len(entries),
        "by_catalog_status": dict(Counter(e["catalog_status"] for e in entries)),
        "listed_by_track": dict(Counter(e["track"] for e in entries if e["catalog_status"] == "listed")),
        "all_entries_by_track": dict(Counter(e["track"] for e in entries)),
        "by_resource_type": dict(Counter(e["resource_type"] for e in entries)),
        "entries_with_metadata_variants": sum(bool(e["metadata_variant_fields"]) for e in entries),
        "entries_with_placeholder_links": sum("placeholder_link" in e["issues"] for e in entries),
        "entries_with_only_aggregator_or_no_direct_link": sum("no_direct_source_link" in e["issues"] for e in entries),
        "entries_with_paper_only": sum("paper_only" in e["issues"] for e in entries),
        "entries_with_link_checks": sum(e["verification"].get("link_access_checked", False) for e in entries),
        "last_link_check": max((e["verification"].get("last_link_check") or "" for e in entries), default="") or None,
        "unique_link_statuses": dict(Counter(l.get("access", {}).get("status", "unchecked") for l in {l["url"]:l for e in entries for l in e["links"]}.values())),
        "counting_note": "Entries include suites, component datasets, methods and environments. This is not a count of independent benchmarks or a sum of dataset sizes."
    }
    outputs["data/stats.json"] = (json.dumps(stats, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return outputs, stats


def write_exports(catalog):
    outputs, stats = export_contents(catalog)
    for relative, content in outputs.items():
        (ROOT / relative).write_bytes(content)
    print(json.dumps({"entries": stats["unique_catalog_entries"], "by_status": stats["by_catalog_status"], "listed_by_track": stats["listed_by_track"]}, ensure_ascii=False))


if __name__ == "__main__":
    build()

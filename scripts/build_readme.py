"""Generate bilingual GitHub pages and maintenance documents from the canonical catalog.

python scripts/build_readme.py
python scripts/build_readme.py --check
Standard library only. Never fetches remote content or changes canonical records.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
from curate import effective_url, navigation_links

ROOT = Path(__file__).resolve().parents[1]
TRACKS = {
    "llm_safety": ("LLM Safety", "LLM 安全"),
    "agent_safety": ("Agent Safety & Security", "Agent 安全"),
    "safety_judging": ("Safety Judging & Guardrails", "安全审查与护栏"),
    "related_resources": ("Related Resources", "相关资源"),
}
TOPICS = {
    "comprehensive": ("Comprehensive safety", "综合安全"),
    "harmful_content": ("Harmful content and toxicity", "有害内容与毒性"),
    "jailbreak": ("Jailbreaks and adversarial prompts", "越狱与对抗提示"),
    "prompt_injection": ("Prompt injection and instruction boundaries", "提示注入与指令边界"),
    "bias_fairness": ("Bias and fairness", "偏见与公平"),
    "values_ethics": ("Values, ethics and cultural norms", "价值观、伦理与文化规范"),
    "privacy": ("Privacy", "隐私"),
    "overrefusal": ("Over-refusal", "过度拒答"),
    "autonomy_alignment": ("Autonomy and alignment", "自主性与对齐"),
    "domain_risk": ("Domain risks", "领域风险"),
    "general": ("General agent safety and misuse", "综合 Agent 安全与滥用"),
    "tool_mcp": ("Tool, API and MCP safety", "工具、API 与 MCP 安全"),
    "privacy_memory": ("Privacy and memory", "隐私与记忆"),
    "web_computer_mobile": ("Web, computer and mobile agents", "网页、桌面与移动 Agent"),
    "embodied": ("Embodied safety", "具身安全"),
    "agent_trajectory": ("Agent trajectories and action safety", "Agent 轨迹与动作安全"),
    "content_guardrail": ("Content guardrail evaluation", "内容护栏评测"),
    "training_data": ("Training datasets", "训练数据"),
    "attack_methods": ("Attack methods", "攻击方法"),
    "frameworks": ("Frameworks and mixed resources", "框架及混合资源"),
    "attack_data": ("Attack challenges and data", "攻击挑战与数据"),
    "capability_environments": ("Capability baselines and environments", "能力基线与环境"),
    "reliability": ("Factuality and general trace diagnostics", "事实性与通用轨迹诊断"),
    "domain_capability": ("Domain capability benchmarks", "领域能力基准"),
    "suite_components": ("Components of listed suites", "已收录基准的子集"),
}
TYPES = {
    "benchmark": ("Benchmark", "基准"), "benchmark_suite": ("Suite", "基准套件"),
    "evaluation_dataset": ("Eval data", "评测数据"), "training_dataset": ("Train data", "训练数据"),
    "attack_method": ("Method", "方法"), "framework": ("Framework", "框架"),
    "suite_component": ("Component", "子集"),
}


def esc(value):
    return str(value if value is not None else "—").replace("|", "\\|").replace("\r", " ").replace("\n", "<br>")


def link_summary(stats, lang):
    counts = stats["unique_link_statuses"]
    date = stats.get("last_link_check") or "pending"
    checked = sum(v for k, v in counts.items() if not k.startswith("skipped_"))
    reachable = counts.get("accessible", 0) + counts.get("redirected", 0)
    skipped = sum(v for k, v in counts.items() if k.startswith("skipped_"))
    if lang == 0:
        return (f'**Link check ({date}):** {checked} distinct URLs checked, '
                f'{reachable} reachable or redirected, {counts.get("not_found", 0)} missing, '
                f'{counts.get("restricted", 0)} restricted, {counts.get("server_error", 0)} server error; '
                f'{skipped} placeholder/misattributed URLs skipped. [Details](docs/link-check-report.md).')
    return (f'**链接检查（{date}）：**检查 {checked} 个不同网址，'
            f'{reachable} 个可访问或正常跳转、{counts.get("not_found", 0)} 个返回 404/410、'
            f'{counts.get("restricted", 0)} 个访问受限、{counts.get("server_error", 0)} 个服务器错误；'
            f'另跳过 {skipped} 个占位或误归属网址。详见[检查报告](docs/link-check-report.md)。')


def resource_links(entry, lang=0):
    labels = {"paper": ("Paper", "论文"), "code": ("Code", "代码"), "dataset": ("Data", "数据"), "project": ("Project", "项目")}
    annotations = {"restricted": ("access restricted", "访问受限"), "login_required": ("login required", "需登录"),
                   "server_error": ("server error", "服务器错误"), "network_error": ("connection failed", "连接失败"),
                   "http_error": ("HTTP error", "HTTP 异常")}
    parts = []
    for link in navigation_links(entry):
        typ = link["type"]
        note = annotations.get(link.get("access", {}).get("status"))
        suffix = f' ({note[lang]})' if note else ""
        parts.append(f'[{labels[typ][lang]}](<{effective_url(link)}>)' + suffix)
    return " · ".join(parts) or ("Needs source" if lang == 0 else "待补来源")


def link_report(catalog, audit):
    counts = Counter(r["status"] for r in audit["results"])
    checked = sum(v for k, v in counts.items() if not k.startswith("skipped_"))
    associated = defaultdict(list)
    for entry in catalog["entries"]:
        for link in entry["links"]:
            associated[link["url"]].append(entry)
    lines = ["# 在线链接检查报告", "", f'检查日期：{audit["checked_on"]}。', "",
             f'目录共有 {audit["total_unique_urls"]} 个不同的原始网址，实际检查 {checked} 个，跳过 {sum(v for k, v in counts.items() if k.startswith("skipped_"))} 个占位网址。重复出现在多个条目的网址只请求一次。', "",
             "HEAD 优先；失败时用 GET 复核，仅读取最多 64 KiB 的网页文本。网络或服务器错误重试一次，完整结果保存在 [data/link_checks.json](../data/link_checks.json)。未下载数据集或论文文件。", "",
             "HTTP 成功响应只说明当时的页面入口可达，不代表题名、项目身份或元数据已核实。401/403 等访问限制与 404/410 分开记录。许可证审查和 benchmark 可运行性不属于本次检查范围。", "",
             "## 结果", "", "| 状态 | 不同网址数 |", "| --- | ---: |"]
    labels = {"accessible": "可访问", "redirected": "正常跳转", "not_found": "404/410", "restricted": "访问受限",
              "login_required": "需登录", "server_error": "服务器错误", "network_error": "连接失败", "http_error": "HTTP 异常",
              "skipped_placeholder": "占位网址，跳过", "skipped_misattributed": "误归属，跳过"}
    for status in labels:
        if counts[status]:
            lines.append(f'| {labels[status]} | {counts[status]} |')
    latest = max(r["checked_at"] for r in audit["results"] if r.get("checked_at"))
    lines += ["", f'最后一条检查时间：{latest}。', "", "## 返回 404/410 的入口", "",
              "已从 README、CSV 和 Excel 导航中省略这些入口，原始网址及检查证据仍保留在 JSON。条目已有可访问的替代入口，继续收录。", "",
              "| 条目 | 原始网址 | HTTP | 保留的导航 |", "| --- | --- | ---: | --- |"]
    for result in audit["results"]:
        if result["status"] == "not_found":
            entries = associated[result["url"]]
            lines.append(f'| {esc(", ".join(e["name"] for e in entries))} | `{result["url"]}` | {result["http_status"]} | ' + "<br>".join(resource_links(e, 1) for e in entries) + " |")
    lines += ["", "## 访问限制与暂时错误", "", "| 条目 | 原始网址 | 状态 | HTTP |", "| --- | --- | --- | ---: |"]
    for result in audit["results"]:
        if result["status"] in {"restricted", "login_required", "server_error", "network_error", "http_error"}:
            names = ", ".join(e["name"] for e in associated[result["url"]])
            lines.append(f'| {esc(names)} | [入口](<{result["url"]}>) | {labels[result["status"]]} | {result["http_status"] or "—"} |')
    lines += ["", "- OS-Harm 的 Hugging Face 入口返回 401，其 HTML 标题为 404。由于访问控制可能隐藏资源存在性，记录为受限，未确认缺失。其余项目或仓库入口保留，仓库归属问题继续列入身份核验。",
              "- OpenEval 首页返回 502，影响 11 个历史记录。对其中已找到的项目已补充论文、仓库或数据页入口；原始聚合首页仍保留在 JSON 作为历史来源和访问证据。", "",
              "## 正常跳转", "", "导航使用最终地址，JSON 同时保留原始网址、HTTP 状态与跳转链。", "",
              "| 条目 | 原始网址 | 最终地址 |", "| --- | --- | --- |"]
    for result in audit["results"]:
        if result["status"] == "redirected":
            names = ", ".join(e["name"] for e in associated[result["url"]])
            lines.append(f'| {esc(names)} | `{result["url"]}` | [最终入口](<{result["final_url"]}>) |')
    lines += ["", "## 后续处理", "",
              "继续补齐占位网址、仅有聚合首页的来源、名称与链接不一致的记录。页面访问检查与项目身份核验分别记录；论文入口可以独立收录。", ""]
    return "\n".join(lines)


def bilingual_links(entry):
    """Render every public link with one bilingual label convention."""
    labels = {
        "paper": "Paper \\| 论文",
        "code": "Code \\| 代码",
        "dataset": "Data \\| 数据",
        "project": "Project \\| 项目",
    }
    annotations = {
        "restricted": "access restricted \\| 访问受限",
        "login_required": "login required \\| 需登录",
        "server_error": "server error \\| 服务器错误",
        "network_error": "connection failed \\| 连接失败",
        "http_error": "HTTP error \\| HTTP 异常",
    }
    parts = []
    for link in navigation_links(entry):
        note = annotations.get(link.get("access", {}).get("status"))
        suffix = f" ({note})" if note else ""
        parts.append(f'[{labels[link["type"]]}](<{effective_url(link)}>)' + suffix)
    return " · ".join(parts) or "Source pending \\| 待补来源"


def bilingual_cell(english, chinese):
    return f"{esc(english)} \\| {esc(chinese)}"


def catalog_table(entries):
    """Render a compact, consistent table for one topic subsection."""
    headers = [
        "Resource \\| 条目", "Type \\| 类型", "Year \\| 年份",
        "Language \\| 语言", "Links \\| 链接",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for entry in sorted(entries, key=lambda e: e["name"].casefold()):
        year = entry["reported_metadata"]["year"]["value"]
        languages = ", ".join(entry["languages"]) or "—"
        cells = [
            esc(entry["name"]),
            bilingual_cell(*TYPES[entry["resource_type"]]),
            esc(year),
            esc(languages),
            bilingual_links(entry),
        ]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def make_readme(catalog, stats):
    del stats  # README is a project landing page; maintenance counts stay in docs.
    intro = [
        "# Awesome LLM & Agent Safety Benchmarks | LLM 与 Agent 安全 Benchmark",
        "",
        "[English](README.md) · [简体中文](README.zh-CN.md)",
        "",
        "| English | 中文 |",
        "| --- | --- |",
        "| A continuously updated collection of benchmarks, evaluation datasets and supporting resources for LLM and agent safety. | 持续收集 LLM 与 Agent 安全相关的 benchmark、评测数据和配套资源。 |",
        "| The catalog covers model safety, agent safety and security, safety judging, guardrails, attack methods, training data and related research resources. | 内容覆盖模型安全、Agent 安全与安全防护、安全审查、护栏、攻击方法、训练数据及相关研究资源。 |",
        "| Entries are organized by evaluation target and topic, with direct links to papers, code, datasets and project pages. | 条目按评测对象与主题导航，并提供论文、代码、数据和项目页面的直接链接。 |",
        "",
        "## Catalog | 目录",
        "",
    ]
    entries = [e for e in catalog["entries"] if e["catalog_status"] != "needs_review"]
    topic_order = {key: index for index, key in enumerate(TOPICS)}
    for track, track_labels in TRACKS.items():
        track_entries = [e for e in entries if e["track"] == track]
        if not track_entries:
            continue
        intro += [f"## {track_labels[0]} | {track_labels[1]}", ""]
        topics = defaultdict(list)
        for entry in track_entries:
            topics[entry["topic"]].append(entry)
        for topic in sorted(topics, key=lambda key: topic_order.get(key, 99)):
            topic_labels = TOPICS[topic]
            intro += [f"### {topic_labels[0]} | {topic_labels[1]}", "", catalog_table(topics[topic]), ""]
    return "\n".join(intro)


def review_queue(entries):
    queue = [e for e in entries if e["catalog_status"] == "needs_review"]
    lines = ["# 待核验清单", "", f"共 {len(queue)} 项。原始记录仍在总库中；待补来源或定位后再进入正式导航。", "",
             "占位链接不作为有效链接展示。只有聚合站首页的条目需补到具体项目或数据页。", "",
             "| 条目 | 待处理事项 | 现有链接 | 原表位置 |", "| --- | --- | --- | --- |"]
    for e in queue:
        note = e["curation_note_zh"] or "仅有聚合站首页或缺少具体来源，需补正式论文、仓库或数据页。"
        lines.append(f'| {esc(e["name"])} | {esc(note)} | {resource_links(e, 1)} | {esc(e["source_refs"][0])} |')
    lines += ["", "在线链接结果见[链接检查报告](link-check-report.md)。本清单处理项目身份、具体来源和主题定位；许可证及本地可运行性不作为待办或收录门槛。仅有论文入口可以收录。", ""]
    return "\n".join(lines)


def import_report(catalog, stats, sources):
    lines = ["# 首批导入报告", "", f'更新日期：{catalog["updated_on"]}。', "", "## 来源与记录数", "",
             "| 来源 ID | 原文件 | 带名称记录数（含重复视图） |", "| --- | --- | ---: |"]
    for source in sources["sources"]:
        lines.append(f'| {source["id"]} | {source["filename"]} | {source["named_rows"]} |')
    lines += ["", f'- 两份原始收集表共有 {stats["base_collection_rows"]} 条记录；LLM 表 166 条、Agent 表 75 条。',
              f'- 来源共含 {sum(len(s.get("sheets", [])) for s in sources["sources"])} 个工作表，提取 {stats["source_rows_including_repeated_views"]} 条带名称记录，包含筛查、摘要子表等重复视图。',
              f'- 精确名称规范化及显式别名合并后得到 {stats["unique_catalog_entries"]} 个目录条目。未使用模糊名称自动合并。', "", "## 整理结果", "",
              "| 收录状态 | 条目数 |", "| --- | ---: |"]
    for status, label in [("listed", "安全收录"), ("related", "相关资源"), ("needs_review", "待核验")]:
        lines.append(f'| {label} | {stats["by_catalog_status"].get(status, 0)} |')
    lines += ["", "安全收录按评测对象划分：", ""]
    for track in ["llm_safety", "agent_safety", "safety_judging"]:
        lines.append(f'- {TRACKS[track][1]}：{stats["listed_by_track"].get(track, 0)} 项。')
    lines += ["", "## 关键处理", "",
              "- 合并 AgentHarm 补充行、ASB 不同写法、tau-bench、BFCL、MSB、TraceSafe 等名称变体，并保留每个原表位置。",
              "- 区分 X-Teaming 的 XGuard-Train 与 Alibaba AAIG 的 XGuard-Train-Open-200K。",
              "- DecodingTrust 隐私子集、JBB-Behaviors 以 parent_id 指向上级项目，避免把子集当作新增独立基准。",
              "- 攻击方法、训练数据、通用能力基线和诊断资源单列。AgentPoison/MemoryGraft 按攻击研究资源整理。",
              "- 将旧表因环境不匹配而暂缓的移动端、GUI、具身安全资源按当前合集目标重新归类。",
              "- 使用 v2 核验详表优先补充任务、执行、指标和规模；冲突和其他口径保留在 reported_metadata.alternatives。",
              "- 区分是否公开可用与原表成熟度判断；不把成熟度评价转写为许可证或当前开放状态。",
              "- 保留 WASP 与 LLMail-Inject 的独立身份，WASP 优先展示原表已修正的 2504.18575 论文。",
              "- OS-Harm 的不同仓库、TAP/PAIR 的合写以及 AirGapAgent-R 的名称与数据链接关系列入待核验。",
              "- 收集人、示例、嵌入图片和完整原始快照保留在本机原文件或 .local，不进入公开元数据。",
              "", "## 质量与核验边界", "",
              f'- {stats["entries_with_metadata_variants"]} 项存在多种元数据表述，含版本、拆分口径或描述差异，不能全部解释为事实冲突。',
              f'- {stats["entries_with_placeholder_links"]} 项含占位链接；{stats["entries_with_only_aggregator_or_no_direct_link"]} 项缺少具体直达来源；{stats["entries_with_paper_only"]} 项目前只有论文链接。这些诊断可能重叠。',
              "- 已进行在线页面可访问性检查，逐链接保存 HTTP 状态、跳转地址及检查时间，见[链接检查报告](link-check-report.md)。占位链接跳过，未将其标为已检查。",
              "- 网页响应不等于项目身份、元数据或数据可下载性已核实。未下载数据、运行评测或核对论文全文。",
              "- 原表置信度、成熟度和公开可用声明作为历史证据。许可证审查和可运行性不作为收录门槛，未相加数据规模。",
              "- JSON 保留原表值和来源。CSV 防止以公式起始字符开头的文本被 Excel 作为公式执行。",
              "", "## 后续增量顺序", "",
              "1. 处理待核验清单，补项目身份、占位链接和仓库归属。",
              "2. 补充官方来源、年份、语言、模态和 split/版本口径；记录来源与检查日期。",
              "3. 按主题增量收录新项目，定期复查失效、跳转或受限的访问入口。", ""]
    return "\n".join(lines)


def outputs():
    catalog = json.loads((ROOT / "data/benchmarks.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))
    # Stats and CSV are regenerated from canonical JSON, never reimport old files.
    from curate import export_contents
    exports, stats = export_contents(catalog)
    documents = {
        "README.md": make_readme(catalog, stats),
        "README.zh-CN.md": make_readme(catalog, stats),
        "docs/import-report.md": import_report(catalog, stats, sources),
        "docs/link-check-report.md": link_report(catalog, json.loads((ROOT / "data/link_checks.json").read_text(encoding="utf-8"))),
    }
    return {**exports, **{k: v.encode("utf-8") for k, v in documents.items()}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    generated = outputs()
    for relative, content in generated.items():
        target = ROOT / relative
        if args.check:
            if not target.exists() or target.read_bytes() != content:
                stale.append(relative)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    legacy_public_queue = ROOT / "docs" / "review-queue.md"
    if legacy_public_queue.exists():
        if args.check:
            stale.append("docs/review-queue.md (obsolete public review page)")
        else:
            legacy_public_queue.unlink()
    if not args.check:
        private_queue = ROOT / ".local" / "review_queue.md"
        private_queue.parent.mkdir(parents=True, exist_ok=True)
        private_queue.write_text(review_queue(json.loads((ROOT / "data/benchmarks.json").read_text(encoding="utf-8"))["entries"]), encoding="utf-8")
    if stale:
        raise SystemExit("Generated pages are out of date: " + ", ".join(stale))
    print("Generated pages are current." if args.check else "Generated bilingual pages and maintenance documents.")

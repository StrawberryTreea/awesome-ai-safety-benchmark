"""Generate the bilingual GitHub README and maintenance documents from the canonical catalog.

python scripts/build_readme.py
python scripts/build_readme.py --check
Standard library only. Never fetches remote content or changes canonical records.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import html
import json
import math
from pathlib import Path
import re
from curate import effective_url, navigation_links

ROOT = Path(__file__).resolve().parents[1]
TRACKS = {
    "llm_safety": ("LLM Safety", "LLM 安全"),
    "agent_safety": ("Agent Safety & Security", "Agent 安全"),
    "safety_judging": ("Safety Judging & Guardrails", "安全审查与护栏"),
    "related_resources": ("Related Resources", "相关资源"),
}
EXPLORE_CARDS = (
    ("llm_safety", "🧩", "LLM Safety", "LLM 安全",
     "How models hold up under harm, jailbreak, bias, privacy and alignment pressure — full suites and targeted probes.",
     "模型在有害内容、越狱、偏见、隐私与对齐压力下的表现——综合套件与针对性探针。", "listed_by_track", "llm_safety"),
    ("agent_safety", "🤖", "Agent Safety", "Agent 安全",
     "Where agents break: tool / MCP calls, memory, web & desktop use, and misuse scenarios.",
     "Agent 在何处失守：工具 / MCP 调用、记忆、网页与桌面操作，以及滥用场景。", "listed_by_track", "agent_safety"),
    ("safety_judging", "⚖️", "Guardrails & Judging", "安全审查与护栏",
     "Judging and filtering: trajectory-level safety, content moderation, and safety classifiers.",
     "判定与过滤：轨迹级安全、内容审核与安全分类器。", "listed_by_track", "safety_judging"),
    ("related_resources", "🧰", "Related Resources", "相关资源",
     "The surrounding toolkit: training data, attack methods, environments, and diagnostics.",
     "周边工具链：训练数据、攻击方法、评测环境与诊断资源。", "by_catalog_status", "related"),
)
EXPLORE_PATHS = (
    ("#llm_safety-jailbreak", "🧨 Jailbreaks · 越狱"),
    ("#llm_safety-prompt_injection", "🧱 Prompt injection · 提示注入"),
    ("#llm_safety-privacy", "🔒 Privacy · 隐私"),
    ("#agent_safety-tool_mcp", "🛠️ Tools/MCP · 工具/MCP"),
    ("#safety_judging-agent_trajectory", "🧭 Trajectories · 轨迹"),
    ("#safety_judging-content_guardrail", "🛡️ Guardrails · 护栏"),
)
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


def catalog_links_html(entry):
    """Render public links as short HTML anchors for fixed-width catalog tables."""
    labels = {
        "paper": "Paper",
        "code": "Code",
        "dataset": "Data",
        "project": "Project",
    }
    annotations = {
        "restricted": "access restricted",
        "login_required": "login required",
        "server_error": "server error",
        "network_error": "connection failed",
        "http_error": "HTTP error",
    }
    parts = []
    for link in navigation_links(entry):
        note = annotations.get(link.get("access", {}).get("status"))
        suffix = f" ({note})" if note else ""
        url = html.escape(effective_url(link), quote=True)
        label = labels[link["type"]]
        parts.append(f'<a href="{url}">{label}</a>{html.escape(suffix)}')
    return "<br>".join(parts) or "Source pending"


def catalog_name(name):
    parts = re.split(r"(?<=[a-z])(?=[A-Z])|(?<=[_/-])", str(name))
    return "&#8203;".join(html.escape(part) for part in parts)


def catalog_year(value):
    original = "—" if value is None else str(value)
    years = list(dict.fromkeys(re.findall(r"(?<!\d)(?:19|20)\d{2}(?!\d)", original)))
    display = ", ".join(years) or original
    return f'<span title="{html.escape(original, quote=True)}">{html.escape(display)}</span>'


def catalog_languages(values):
    mappings = {
        "英语为主": ["en"],
        "多语言函数调用场景": ["other"],
        "英文(含少量多语言混淆)": ["en", "other"],
        "英文+中文": ["zh", "en"],
        "中文为主": ["zh"],
        "中英混合": ["zh", "en"],
    }
    normalized = {code for value in values for code in mappings.get(value, [value])}
    ordered = [code for code in ("zh", "en", "other") if code in normalized]
    ordered.extend(sorted(normalized - {"zh", "en", "other"}))
    display = ", ".join(ordered) or "—"
    original = ", ".join(values) or "—"
    return f'<span title="{html.escape(original, quote=True)}">{html.escape(display)}</span>'


def catalog_description(value):
    return html.escape(" ".join(value.split()))


def catalog_rows(entries):
    """Render catalog entries into the shared five-column table."""
    widths = ["18%", "46%", "10%", "10%", "16%"]
    lines = []
    for entry in sorted(entries, key=lambda e: e["name"].casefold()):
        description = (catalog_description(entry["description_en"])
                       + " | " + catalog_description(entry["description_zh"]))
        cells = [
            catalog_name(entry["name"]),
            description,
            catalog_year(entry["reported_metadata"]["year"]["value"]),
            catalog_languages(entry["languages"]),
            catalog_links_html(entry),
        ]
        lines.append("<tr>" + "".join(f'<td width="{width}">{cell}</td>' for width, cell in zip(widths, cells)) + "</tr>")
    return lines


def catalog_section(level, label, section_id):
    tag = "th" if level == 2 else "td"
    return (f'<tr><{tag} colspan="5" align="left" id="{section_id}">'
            f'<strong>{html.escape(label)}</strong></{tag}></tr>')


def explore_section(stats):
    lines = [
        '<table width="100%">',
        '<tr>',
    ]
    for index, (anchor, icon, title_en, title_zh, description_en, description_zh, count_group, count_key) in enumerate(EXPLORE_CARDS):
        if index and index % 2 == 0:
            lines.extend(['</tr>', '<tr>'])
        count = stats[count_group].get(count_key, 0)
        lines.append(
            f'<td width="50%" valign="top"><a href="#{anchor}"><strong>{icon} {title_en}</strong></a>'
            f'<br><sub>{title_zh} · {count} resources</sub>'
            f'<br><br>{description_en}<br>{description_zh}</td>'
        )
    lines += [
        '</tr>',
        '</table>',
        '',
        '<p><strong>By risk area · 按风险领域直达</strong></p>',
        '<p>' + ' · '.join(f'<a href="{href}">{label}</a>' for href, label in EXPLORE_PATHS) + '</p>',
    ]
    return lines


def catalog_overview_svg(catalog):
    """Render a dependency-free, styled SVG overview: track donut + year bars.

    Generated from the live catalog on every build, so it refreshes with the data
    whenever the maintainer re-runs ``build_readme.py`` after updating the catalog.
    """
    entries = [e for e in catalog["entries"] if e["catalog_status"] != "needs_review"]
    total = len(entries)
    track_counts = {key: 0 for key in TRACKS}
    for entry in entries:
        track_counts[entry["track"]] = track_counts.get(entry["track"], 0) + 1
    year_counter = Counter()
    for entry in entries:
        value = entry["reported_metadata"]["year"]["value"]
        found = re.findall(r"(?:19|20)\d{2}", str(value)) if value is not None else []
        valid = [int(y) for y in found if 2010 <= int(y) <= 2027]
        if valid:
            year_counter[min(valid)] += 1

    TRACK_STYLE = [
        ("llm_safety", "LLM Safety", "#2563eb"),
        ("agent_safety", "Agent Safety", "#7c3aed"),
        ("safety_judging", "Guardrails", "#0891b2"),
        ("related_resources", "Related", "#f59e0b"),
    ]
    FONT = "font-family='Segoe UI, -apple-system, Helvetica, Arial, sans-serif'"

    def donut_segment(cx, cy, r_out, r_in, t0, t1, color):
        def pt(r, t):
            a = math.radians(t)
            return cx + r * math.sin(a), cy - r * math.cos(a)
        if t1 - t0 >= 359.5:
            return (f"<path d='M {cx-r_out:.2f} {cy:.2f} "
                    f"A {r_out} {r_out} 0 1 1 {cx+r_out:.2f} {cy:.2f} "
                    f"A {r_out} {r_out} 0 1 1 {cx-r_out:.2f} {cy:.2f} Z "
                    f"M {cx-r_in:.2f} {cy:.2f} "
                    f"A {r_in} {r_in} 0 1 0 {cx+r_in:.2f} {cy:.2f} "
                    f"A {r_in} {r_in} 0 1 0 {cx-r_in:.2f} {cy:.2f} Z' "
                    f"fill='{color}' fill-rule='evenodd'/>")
        x0o, y0o = pt(r_out, t0)
        x1o, y1o = pt(r_out, t1)
        x1i, y1i = pt(r_in, t1)
        x0i, y0i = pt(r_in, t0)
        large = 1 if (t1 - t0) > 180 else 0
        return (f"<path d='M {x0o:.2f} {y0o:.2f} "
                f"A {r_out} {r_out} 0 {large} 1 {x1o:.2f} {y1o:.2f} "
                f"L {x1i:.2f} {y1i:.2f} "
                f"A {r_in} {r_in} 0 {large} 0 {x0i:.2f} {y0i:.2f} Z' "
                f"fill='{color}'/>")

    def bar(x, y_top, w, h, r, fill):
        r = min(r, w / 2, h)
        return (f"<path d='M {x:.1f} {y_top+r:.1f} "
                f"A {r} {r} 0 0 1 {x+r:.1f} {y_top:.1f} "
                f"L {x+w-r:.1f} {y_top:.1f} "
                f"A {r} {r} 0 0 1 {x+w:.1f} {y_top+r:.1f} "
                f"L {x+w:.1f} {y_top+h:.1f} "
                f"L {x:.1f} {y_top+h:.1f} Z' fill='{fill}'/>")

    parts = [
        "<svg xmlns='http://www.w3.org/2000/svg' width='680' height='360' "
        "viewBox='0 0 680 360' role='img' aria-label='Catalog overview'>",
        "<defs>",
        "<linearGradient id='barGrad' x1='0' y1='0' x2='0' y2='1'>",
        "<stop offset='0' stop-color='#60a5fa'/>",
        "<stop offset='1' stop-color='#2563eb'/>",
        "</linearGradient>",
        "</defs>",
        "<rect x='0' y='0' width='680' height='360' rx='18' fill='#ffffff' "
        "stroke='#e5e7eb' stroke-width='1'/>",
        f"<text x='28' y='40' {FONT} font-size='17' font-weight='700' fill='#0f172a'>Catalog Overview · 全景概览</text>",
        f"<text x='652' y='40' {FONT} font-size='12' fill='#64748b' text-anchor='end'>{total} resources</text>",
        "<line x1='24' y1='56' x2='656' y2='56' stroke='#f1f5f9' stroke-width='1'/>",
        f"<text x='28' y='90' {FONT} font-size='13' font-weight='700' fill='#334155'>By track</text>",
    ]
    cx, cy, r_out, r_in = 92, 200, 66, 46
    angle = 0.0
    for key, label, color in TRACK_STYLE:
        cnt = track_counts.get(key, 0)
        frac = cnt / total if total else 0
        sweep = frac * 360
        t0 = angle
        t1 = angle + sweep
        gap = 0.0 if frac >= 0.999 else 0.8
        parts.append(donut_segment(cx, cy, r_out, r_in, t0, min(t1 + gap, t0 + 360), color))
        angle = t1
    parts.append(f"<text x='{cx}' y='{cy-2}' {FONT} font-size='22' font-weight='700' fill='#0f172a' text-anchor='middle'>{total}</text>")
    parts.append(f"<text x='{cx}' y='{cy+15}' {FONT} font-size='10' fill='#94a3b8' text-anchor='middle'>resources</text>")
    lx, lw = 176, 160
    ly = 146
    for key, label, color in TRACK_STYLE:
        cnt = track_counts.get(key, 0)
        pct = f"{round(100*cnt/total)}%" if total else "0%"
        parts.append(f"<rect x='{lx}' y='{ly-11}' width='14' height='14' rx='3' fill='{color}'/>")
        parts.append(f"<text x='{lx+22}' y='{ly}' {FONT} font-size='12' fill='#334155'>{label}</text>")
        parts.append(f"<text x='{lx+lw}' y='{ly}' {FONT} font-size='12' fill='#64748b' text-anchor='end'>{cnt} · {pct}</text>")
        ly += 40
    parts.append("<line x1='340' y1='72' x2='340' y2='330' stroke='#f1f5f9' stroke-width='1'/>")
    parts.append(f"<text x='364' y='90' {FONT} font-size='13' font-weight='700' fill='#334155'>By first-publication year</text>")
    years = sorted(year_counter)
    if years:
        bx0, bx1, base_y, top_y = 366, 652, 305, 130
        chart_w = bx1 - bx0
        H = base_y - top_y
        maxv = max(year_counter.values()) or 1
        n = len(years)
        slot = chart_w / n
        bw = min(slot * 0.56, 30)
        parts.append(f"<line x1='{bx0}' y1='{base_y}' x2='{bx1}' y2='{base_y}' stroke='#e2e8f0' stroke-width='1'/>")
        for i, yr in enumerate(years):
            v = year_counter[yr]
            bh = max(2, int(H * v / maxv))
            x = bx0 + i * slot + (slot - bw) / 2
            y_top = base_y - bh
            parts.append(bar(x, y_top, bw, bh, 4, "url(#barGrad)"))
            parts.append(f"<text x='{x+bw/2:.1f}' y='{y_top-6:.1f}' {FONT} font-size='10' fill='#475569' text-anchor='middle'>{v}</text>")
            parts.append(f"<text x='{x+bw/2:.1f}' y='{base_y+16:.1f}' {FONT} font-size='10' fill='#64748b' text-anchor='middle'>{yr}</text>")
    parts.append("</svg>")
    return "\n".join(parts)


def toc_section(catalog):
    entries = [e for e in catalog["entries"] if e["catalog_status"] != "needs_review"]
    topic_order = {key: index for index, key in enumerate(TOPICS)}
    lines = [
        "<details>",
        "<summary><strong>Table of contents · 目录</strong></summary>",
        "",
        "| Track | Topics |",
        "| --- | --- |",
    ]
    for track, labels in TRACKS.items():
        topics = {}
        for entry in entries:
            if entry["track"] == track:
                topics[entry["topic"]] = topics.get(entry["topic"], 0) + 1
        if not topics:
            continue
        links = " · ".join(
            f"[{TOPICS[t][0]}](#{track}-{t}) <sub>{topics[t]}</sub>"
            for t in sorted(topics, key=lambda k: topic_order.get(k, 99))
        )
        lines.append(f"| **[{labels[0]}](#{track})** | {links} |")
    lines += ["", "</details>"]
    return lines


def badges_svg(updated_on):
    """Locally-rendered badge strip (no external CDN) so it displays on GitHub
    even where img.shields.io is blocked. Regenerated on every build."""
    pills = [
        ("License", "MIT", "#0969da"),
        ("语言 Lang", "中 / EN", "#8250df"),
        ("维护 Maint.", "Weekly", "#1a7f37"),
    ]

    def text_w(s):
        return sum(12.0 if ord(c) > 0x2E80 else 6.6 for c in s)

    h, r, pad, gap = 22, 6, 9, 6
    font = ("font-family='-apple-system, Segoe UI, Helvetica, Arial, sans-serif' "
            "font-size='12'")
    x = 0.0
    frags = []
    for label, value, color in pills:
        lw = text_w(label) + pad * 2
        vw = text_w(value) + pad * 2
        w = lw + vw
        frags.append(f"<rect x='{x:.0f}' y='0' width='{w:.0f}' height='{h}' rx='{r}' "
                     f"fill='#f6f8fa' stroke='#d0d7de'/>")
        frags.append(f"<text x='{x+pad:.0f}' y='15' {font} fill='#57606a'>{label}</text>")
        frags.append(f"<text x='{x+lw:.0f}' y='15' {font} font-weight='600' "
                     f"fill='{color}'>{value}</text>")
        x += w + gap
    width = max(0, x - gap)
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='{width:.0f}' height='{h}' "
            f"viewBox='0 0 {width:.0f} {h}' role='img' aria-label='Repository badges'>\n"
            + "\n".join(frags) + "\n</svg>")


def make_readme(catalog, stats):
    listed = stats["by_catalog_status"].get("listed", 0)
    related = stats["by_catalog_status"].get("related", 0)
    public_entries = listed + related
    checked_links = sum(
        count for status, count in stats["unique_link_statuses"].items()
        if not status.startswith("skipped_")
    )
    updated_on = stats.get("updated_on", "—")
    entries_all = [e for e in catalog["entries"] if e["catalog_status"] != "needs_review"]
    used_topics = len({e["topic"] for e in entries_all})
    track_count = len({e["track"] for e in entries_all})
    intro = [
        "<div align=\"center\">",
        "",
        "<h1>🛡️ Awesome LLM &amp; Agent Safety Benchmarks</h1>",
        "",
        "<h3>大模型与智能体安全评测目录 · 基准 / 数据集 / 工具</h3>",
        "",
        "A maintained, bilingual catalog of LLM &amp; agent safety evaluation — benchmarks, datasets and tools, each traced to its paper, code or data.",
        "",
        f"<img src=\"assets/badges.svg\" alt=\"License MIT · 中/EN · maintained weekly\" width=\"398\">",
        "",
        f"<img src=\"assets/catalog-overview.svg\" alt=\"Catalog overview\" width=\"680\">",
        "",
        f"<sub>{public_entries} resources · {track_count} tracks · {used_topics} topics · {checked_links} links verified</sub>",
        "",
        "</div>",
        "",
        "> **Scope · 收录范围：** Evaluation benchmarks, datasets and tools for LLM / agent safety — jailbreaks, prompt injection, privacy, guardrails, bias, values and agent misuse. Training corpora, attack toolkits and capability baselines appear only as *context* under Related Resources, not as core safety evaluations.",
        ">",
        "> **收录范围：** 面向大模型 / 智能体安全的评测基准、数据集与工具——涵盖越狱、提示注入、隐私、护栏、偏见、价值观与 Agent 滥用。训练语料、攻击工具与能力基线仅作为「背景」列在 Related Resources，不算核心安全评测。",
        "",
        f"<sub>Last updated {updated_on} · maintained weekly · <a href=\"CONTRIBUTING.md\">suggest a resource or correction</a></sub>",
        "",
        "## Start here | 从这里开始",
        "",
        "| 你想做什么 · What you want | 从这里开始 · Start here | 下结论前先确认 · Check before concluding |",
        "| --- | --- | --- |",
        "| 评估模型抗越狱 / 提示注入 | LLM Safety → Jailbreaks / Prompt injection | 评分器是否验证过、有无数据污染 |",
        "| 给 Agent 做红队 / 安全评测 | Agent Safety → Tool/MCP, Trajectories | 工具权限、良性效用、重复试验次数 |",
        "| 选 / 对比一个护栏或安全评判器 | Guardrails & Judging | 在什么数据分布上测的、误拦率多少 |",
        "| 找训练数据 / 攻击方法做对照 | Related Resources | 仅作背景，不算核心安全评测 |",
        "",
        "<sub>状态图例 · Status: Listed = 核心安全评测 · Related = 背景资料 · Needs review = 待核验</sub>",
        "",
        "## Explore | 快速浏览",
        "",
        *explore_section(stats),
        "",
        "<p align=\"center\"><sub><a href=\"data/benchmarks.csv\">Download CSV · 下载目录</a> · <a href=\"docs/taxonomy.md\">Taxonomy · 分类说明</a> · <a href=\"CONTRIBUTING.md\">Contribute · 参与共建</a></sub></p>",
        "",
        *toc_section(catalog),
        "",
        "## Taxonomy & Evidence | 分类与依据",
        "",
        f"> Resources are filed along **{track_count} tracks and {used_topics} topics**, with a separate risk-taxonomy proposal still under review. The links below explain the structure, the rationale, and how each entry maps back to its source.",
        ">",
        f"> 资源按 **{track_count} 个主轨、{used_topics} 个主题** 归类，并附一套仍在评审中的风险分类提案。下列链接说明分类结构、设计依据，以及每条资源如何回溯到来源。",
        "",
        "| 🧭 Understand the catalog | 🔎 Examine the design | 📚 Trace the evidence |",
        "| --- | --- | --- |",
        "| [**分类总览 · Overview**](docs/taxonomy.md)<br>评测主轨与资源实例 | [**设计依据 · Rationale**](docs/taxonomy-rationale.md)<br>多轴结构的依据与分类边界 | [**来源与映射 · Sources**](docs/taxonomy-research-2026-10-16.md#source-matrix)<br>标准、研究框架与版本范围 |",
        "",
        "[Candidate taxonomy · 候选分类](docs/taxonomy-proposal.md) · [Validation roadmap · 验证计划](docs/taxonomy-validation.md) · [JSON definition · 机器定义](docs/taxonomy-proposal-v0.1.json)",
        "",
        "> **Proposal status · 提案状态：** The 12-domain / 39-subtype risk taxonomy is a proposal under review — the catalog itself is still organized by track and topic, not by that taxonomy yet. Counts and boundaries will be adjusted as validation proceeds.",
        ">",
        "> 当前 12 域 / 39 子类的风险分类是一份待验证提案——目录目前仍按主轨与主题组织，尚未套用该分类。类别数量与边界将随验证推进调整。",
        "",
        "## Catalog | 目录",
        "",
        '<table width="100%">',
        '<thead>',
        '<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>',
        '</thead>',
        '<tbody>',
    ]
    entries = [e for e in catalog["entries"] if e["catalog_status"] != "needs_review"]
    topic_order = {key: index for index, key in enumerate(TOPICS)}
    track_number = 0
    for track, track_labels in TRACKS.items():
        track_entries = [e for e in entries if e["track"] == track]
        if not track_entries:
            continue
        track_number += 1
        intro.append(catalog_section(2, f"{track_number}. {track_labels[0]} | {track_labels[1]}", track))
        topics = defaultdict(list)
        for entry in track_entries:
            topics[entry["topic"]].append(entry)
        for topic_number, topic in enumerate(sorted(topics, key=lambda key: topic_order.get(key, 99)), 1):
            topic_labels = TOPICS[topic]
            intro.append(catalog_section(3, f"{track_number}.{topic_number} {topic_labels[0]} | {topic_labels[1]}", f"{track}-{topic}"))
            intro.extend(catalog_rows(topics[topic]))
    intro += ["</tbody>", "</table>", ""]
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
        "docs/import-report.md": import_report(catalog, stats, sources),
        "docs/link-check-report.md": link_report(catalog, json.loads((ROOT / "data/link_checks.json").read_text(encoding="utf-8"))),
        "assets/catalog-overview.svg": catalog_overview_svg(catalog),
        "assets/badges.svg": badges_svg(stats.get("updated_on", "—")),
    }
    from build_taxonomy import outputs as taxonomy_outputs
    return {**exports, **{k: v.encode("utf-8") for k, v in documents.items()}, **taxonomy_outputs()}


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
    print("Generated pages are current." if args.check else "Generated README and maintenance documents.")

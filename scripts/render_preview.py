#!/usr/bin/env python3
"""Render README.md into a standalone GitHub-flavored HTML preview.

Pure stdlib. Output is a single self-contained .html file:
  * shields.io <img> badges -> CSS pills (works offline)
  * assets/catalog-overview.svg inlined (renders without the asset dir)
  * <details> opened by default so the TOC is visible
  * GitHub-flavored pipe tables (| a | b |) -> <table>
  * basic inline markdown (**bold**, `code`) rendered
Used for local visual review; not committed to the repo.
"""
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
OUT = os.path.join(ROOT, ".workbuddy", "scratch", "readme_preview", "README-preview.html")


def inline(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    return text


def inline_svg(text: str) -> str:
    """Inline every <img src="assets/*.svg"> so the preview renders without the
    asset directory and without any external CDN."""
    for m in re.finditer(r'<img src="(assets/[^"]+\.svg)"[^>]*>', text):
        svg_path = os.path.join(ROOT, m.group(1))
        if os.path.exists(svg_path):
            svg = open(svg_path, encoding="utf-8").read()
            text = text.replace(m.group(0), svg)
    return text


def md_table_to_html(tbl_lines):
    rows = [l.strip() for l in tbl_lines if l.strip()]
    if len(rows) < 2:
        return None

    def split_row(row):
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        return [c.strip() for c in row.split("|")]

    header = split_row(rows[0])
    # rows[1] is the --- separator
    body = [split_row(r) for r in rows[2:]]
    out = ["<table>"]
    out.append("<thead><tr>")
    for c in header:
        out.append(f"<th>{inline(c)}</th>")
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>")
        for c in r:
            out.append(f"<td>{inline(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def convert_md_tables(text: str) -> str:
    lines = text.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        if lines[i].lstrip().startswith("|"):
            tbl = []
            while i < n and lines[i].lstrip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            html_tbl = md_table_to_html(tbl)
            out.append(html_tbl if html_tbl else "\n".join(tbl))
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def is_html_line(line: str) -> bool:
    return line.lstrip().startswith("<")


def convert(md: str) -> str:
    lines = md.split("\n")
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        # markdown pipe-table (standalone)
        if line.lstrip().startswith("|"):
            tbl = []
            while i < n and lines[i].lstrip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            html_tbl = md_table_to_html(tbl)
            out.append(html_tbl if html_tbl else "\n".join(tbl))
            continue
        # HTML block (may contain <details> with inner pipe-tables)
        if is_html_line(line):
            block = []
            depth = 0
            while i < n:
                cur = lines[i]
                if is_html_line(cur):
                    if re.search(r"<details(\s|>)", cur):
                        depth += 1
                    if "</details>" in cur:
                        depth = max(0, depth - 1)
                    block.append(cur)
                    i += 1
                    # after a closing top-level tag, peek: stop if next is prose
                    if depth == 0 and cur.strip().startswith("</"):
                        j = i
                        while j < n and not lines[j].strip():
                            j += 1
                        if j < n and not (is_html_line(lines[j]) or lines[j].lstrip().startswith("|")):
                            break
                elif cur.strip() == "":
                    block.append(cur)
                    i += 1
                elif cur.lstrip().startswith("|") and depth > 0:
                    block.append(cur)
                    i += 1
                else:
                    break
            html_block = "\n".join(block).strip()
            html_block = html_block.replace("<details>", "<details open>")
            html_block = convert_md_tables(html_block)
            out.append(html_block)
            continue
        # markdown header
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        # blockquote
        if line.lstrip().startswith(">"):
            qb = []
            while i < n and lines[i].lstrip().startswith(">"):
                qb.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>" + convert("\n".join(qb)) + "</blockquote>")
            continue
        # plain paragraph
        para = []
        while i < n and lines[i].strip() and not is_html_line(lines[i]) \
                and not lines[i].lstrip().startswith("|") \
                and not lines[i].lstrip().startswith(">") \
                and not re.match(r"^#{1,6}\s", lines[i]):
            para.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(para)) + "</p>")
    return "\n".join(out)


PAGE_CSS = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome LLM &amp; Agent Safety Benchmarks — Preview</title>
<style>
  :root { color-scheme: light; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans",
      Helvetica, Arial, sans-serif;
    font-size: 16px; line-height: 1.5; color: #1f2328; background: #ffffff;
    margin: 0;
  }
  .markdown-body {
    max-width: 1012px; margin: 0 auto; padding: 32px 24px 80px;
  }
  .markdown-body h1, .markdown-body h2, .markdown-body h3 {
    margin-top: 24px; margin-bottom: 16px; font-weight: 600; line-height: 1.25;
  }
  .markdown-body h1 { font-size: 2em; padding-bottom: .3em; }
  .markdown-body h2 { font-size: 1.5em; padding-bottom: .3em; border-bottom: 1px solid #d1d9e0; }
  .markdown-body h3 { font-size: 1.25em; }
  .markdown-body p { margin: 0 0 16px; }
  .markdown-body a { color: #0969da; text-decoration: none; }
  .markdown-body a:hover { text-decoration: underline; }
  .markdown-body blockquote {
    margin: 0 0 16px; padding: 0 1em; color: #59636e;
    border-left: 4px solid #d1d9e0;
  }
  .markdown-body table {
    border-collapse: collapse; width: 100%; margin: 16px 0;
    display: block; overflow-x: auto; font-size: 14px;
  }
  .markdown-body th, .markdown-body td {
    border: 1px solid #d1d9e0; padding: 6px 13px;
  }
  .markdown-body tr:nth-child(2n) { background: #f6f8fa; }
  .markdown-body thead th { background: #f6f8fa; font-weight: 600; }
  .markdown-body sub { font-size: 12px; }
  .markdown-body div[align="center"] { text-align: center; }
  .markdown-body code {
    background: rgba(129,139,152,.18); padding: .2em .4em; border-radius: 4px;
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    font-size: 85%;
  }
  .gh-badge {
    display: inline-block; background: #59636e; color: #fff; font-size: 12px;
    font-weight: 600; padding: 3px 9px; border-radius: 4px; margin: 3px 3px;
    letter-spacing: .2px; vertical-align: middle;
  }
  .markdown-body details {
    border: 1px solid #d1d9e0; border-radius: 6px; padding: 8px 12px;
    margin: 16px 0; background: #f6f8fa;
  }
  .markdown-body summary { cursor: pointer; font-weight: 600; }
  .markdown-body img { max-width: 100%; }
  .topbar {
    background: #f6f8fa; border-bottom: 1px solid #d1d9e0; padding: 8px 16px;
    font-size: 13px; color: #59636e; position: sticky; top: 0; z-index: 5;
  }
  .topbar b { color: #1f2328; }
</style>
</head>
<body>
<div class="topbar">📄 README 预览（GitHub 风格）· 数据来自本地 README.md · 徽章与图表均为仓库内 SVG（国内 GitHub 可直接显示）</div>
<div class="markdown-body">
"""


def main():
    md = open(README, encoding="utf-8").read()
    body = convert(md)
    body = inline_svg(body)
    doc = PAGE_CSS + body + "\n</div>\n</body>\n</html>\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(doc)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

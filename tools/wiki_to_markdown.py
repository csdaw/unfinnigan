#!/usr/bin/env python3
"""Convert Internet Archive copies of the unfinnigan Google Code wiki to Markdown.

Reads the raw crawler output in wiki/<PageName>[?can=N]/index.html and writes
one clean .md file per page plus an index to docs/wiki/.

- Deduplicates webcrawler capture variants (?can=N) per page, keeping the newest revision.
- Extracts the #wikicontent region, cleans Google Code / Wayback artifacts.
- Rewrites internal wiki links to relative .md links.
- Writes one .md file per page plus an index to the output directory.

Usage:
    python3 tools/wiki_to_markdown.py [WIKI_SRC] [OUT_DIR]

Requires: beautifulsoup4, markdownify, lxml
"""

import json
import os
import re
import sys
from datetime import datetime
from urllib.parse import unquote

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_WIKI_SRC = os.path.join(REPO_ROOT, "wiki")
DEFAULT_OUT_DIR = os.path.join(REPO_ROOT, "docs", "wiki")

# Optional manifest mapping original image URLs -> local paths relative to
# OUT_DIR (e.g. {"http://.../x.png": "images/x.png"}). Built by the image
# rescue pass; when present, converted pages reference local copies.
IMAGE_MANIFEST_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "wiki_images.json"
)
try:
    with open(IMAGE_MANIFEST_PATH, encoding="utf-8") as _f:
        IMAGE_MANIFEST = json.load(_f)
except OSError:
    IMAGE_MANIFEST = {}

CANON_RE = re.compile(r"[?&](can|tm)=\d+")
UPDATED_RE = re.compile(
    r'Updated\s*<span title="([^"]+)">(.*?)</span>\s*by\s*(?:<a[^>]*>)?(.*?)(?:</a>)?\s*</div>',
    re.S,
)


def canon_name(dirname):
    name = CANON_RE.sub("", dirname)
    return name.rstrip("?.").strip()


def parse_updated(raw_html):
    m = UPDATED_RE.search(raw_html)
    if not m:
        return None, None
    date_raw = m.group(1).strip()
    author = re.sub(r"<[^>]+>", "", m.group(3)).strip()
    try:
        dt = datetime.strptime(date_raw, "%a %b %d %H:%M:%S %Y")
        return dt, author
    except ValueError:
        return None, author


class WikiConverter(MarkdownConverter):
    """markdownify tuned for Google Code wiki pages."""

    def __init__(self, page_name):
        super().__init__(
            heading_style="ATX",
            bullets="-",
            strip=["span"],
            escape_underscores=False,
            table_infer_header=True,
        )
        self.page_name = page_name

    # --- link rewriting -------------------------------------------------
    def convert_a(self, el, text, parent_tags=None):
        href = el.get("href") or ""
        new = self.rewrite_href(href)
        if new is None:  # dead link, keep text only
            return text
        if not text.strip():
            return ""
        if new == self.page_name + ".md":  # self reference -> plain text
            return text
        return f"[{text}]({new})"

    def rewrite_href(self, href):
        href = href.strip()
        if not href or href.startswith("#"):
            return href or None
        if href in IMAGE_MANIFEST:
            return IMAGE_MANIFEST[href]
        # Wayback wrapper: /web/<timestamp><mod>/<original>
        m = re.match(
            r"https?://web\.archive\.org/web/\d+(?:[a-z]{2}_)?/(.+)", href
        )
        if m:
            href = m.group(1)
            if href.startswith("/"):
                href = "https://web.archive.org" + href
                # still wayback-relative; resolve below generically
        if href.startswith("/"):
            # site-relative Google Code URLs
            m = re.match(r"^/p/unfinnigan/wiki/([^/?#]+)$", href)
            if m:
                return m.group(1) + ".md"
            if href.startswith("/p/unfinnigan/w/list"):
                return "index.md"
            return None  # google-code internal chrome -> drop
        # absolute code.google.com links
        m = re.match(
            r"https?://(?:code\.google\.com|web\.archive\.org/web/\d+/https?://code\.google\.com)"
            r"/p/unfinnigan/wiki/([^/?#]+)$",
            href,
        )
        if m:
            return unquote(m.group(1)) + ".md"
        if "code.google.com/p/unfinnigan/w/list" in href:
            return "index.md"
        if "code.google.com/p/unfinnigan/" in href:
            return None
        return href

    # --- images -----------------------------------------------------------
    def convert_img(self, el, text, parent_tags=None):
        src = (el.get("src") or "").strip()
        if src in IMAGE_MANIFEST:
            return f"![{el.get('alt') or ''}]({IMAGE_MANIFEST[src]})"
        return f"![{el.get('alt') or ''}]({src})"

    # --- inline code -----------------------------------------------------
    def convert_tt(self, el, text, parent_tags=None):
        return f"`{text}`" if text.strip() else ""

    def convert_code(self, el, text, parent_tags=None):
        return f"`{text}`" if text.strip() else ""


def clean_content(soup):
    # drop anchor chrome
    for a in soup.find_all("a", class_="section_anchor"):
        a.decompose()
    for a in soup.find_all("a", attrs={"name": True}):
        if not a.get_text(strip=True):
            a.unwrap() if a.parent and a.parent.name in ("h2", "h3", "h4") else a.decompose()
    # style attributes are noise for md
    for tag in soup.find_all(True):
        for attr in ("style", "class", "border", "cellpadding", "cellspacing",
                     "title", "onclick", "rel"):
            tag.attrs.pop(attr, None)


def convert_page(page_name, raw_html):
    conv = WikiConverter(page_name)
    meta_dt, meta_author = parse_updated(raw_html)

    soup = BeautifulSoup(raw_html, "lxml")
    content = soup.find(id="wikicontent")
    if content is None:
        return None, None, None
    main = content.find(id="wikimaincol") or content

    # unwrap paragraph-wrapped tables which break pipe-table conversion
    for p in main.find_all("p"):
        if p.find("table") and not p.get_text(strip=True).replace(
            "".join(t.get_text() for t in p.find_all("table")), ""
        ).strip():
            p.unwrap()

    clean_content(main)

    body = conv.convert_soup(main)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

    # front matter
    fm_lines = ["---", f"title: {page_name}"]
    orig_url = f"https://code.google.com/p/unfinnigan/wiki/{page_name}"
    fm_lines.append(f"original: {orig_url}")
    if meta_dt:
        fm_lines.append(f"updated: {meta_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    if meta_author:
        fm_lines.append(f"author: {meta_author}")
    fm_lines.append("source: Internet Archive copy of Google Code wiki")
    fm = "\n".join(fm_lines) + "\n---\n\n"

    return fm + body, meta_dt, meta_author


def pick_best(candidates):
    """candidates: list of (dirname, path). Returns (path, raw_html, dt)."""
    best = None
    for dirname, path in candidates:
        try:
            raw = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        dt, _ = parse_updated(raw)
        score = (
            dt.toordinal() if dt else -1,
            len(raw),
        )
        key = (score, dirname)
        if best is None or key > best[0]:
            best = (key, path, raw, dt)
    if best is None:
        return None
    return best[1], best[2], best[3]


def main():
    wiki_src = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_WIKI_SRC
    out_dir = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT_DIR

    os.makedirs(out_dir, exist_ok=True)
    groups = {}
    for entry in sorted(os.listdir(wiki_src)):
        full = os.path.join(wiki_src, entry)
        idx = os.path.join(full, "index.html")
        if not os.path.isfile(idx):
            continue
        groups.setdefault(canon_name(entry), []).append((entry, idx))

    written = []
    skipped = []
    for page in sorted(groups):
        result = pick_best(groups[page])
        if not result:
            skipped.append(page)
            continue
        _, raw, dt = result
        md, _, _ = convert_page(page, raw)
        if not md or len(md.strip()) < 40:
            skipped.append(page)
            continue
        out_path = os.path.join(out_dir, page + ".md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        written.append((page, dt))

    # index
    lines = [
        "---",
        "title: unfinnigan wiki",
        "original: https://code.google.com/p/unfinnigan/w/list",
        "source: Internet Archive copy of Google Code wiki",
        "---",
        "",
        "# unfinnigan wiki",
        "",
        "Documentation recovered from the Google Code project "
        "*unfinnigan* (Painless extraction of mass spectra from Thermo \"raw\" files).",
        "",
        f"{len(written)} pages:",
        "",
    ]
    for page, dt in written:
        date = dt.strftime("%Y-%m-%d") if dt else "unknown"
        lines.append(f"- [{page}]({page}.md) _(updated {date})_")
    lines.append("")
    with open(os.path.join(out_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {len(written)} pages + index.md to {out_dir}")
    if skipped:
        print("Skipped:", ", ".join(skipped))


if __name__ == "__main__":
    sys.exit(main())

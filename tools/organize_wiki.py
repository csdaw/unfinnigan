#!/usr/bin/env python3
"""Reorganize the converted wiki Markdown into thematic directories.

Runs on the flat output of wiki_to_markdown.py and produces:

    docs/wiki/
    ├── index.md        regenerated landing page with grouped navigation
    ├── overview/       start-here pages
    ├── structures/     binary data structure reference
    ├── decoder-api/    Finnigan::* Perl decoder documentation
    ├── tools/          uf-* command-line tools and external utilities
    ├── meta/           historical site artifacts (WikiSidebar)
    └── images/

All cross-page links and image links are rewritten to the new relative
locations. Original filenames are preserved for traceability with the
Google Code wiki URLs recorded in each page's front matter.

Usage:
    python3 tools/organize_wiki.py [DOCS_DIR]
"""

import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DOCS = os.path.join(REPO_ROOT, "docs", "wiki")

LINK_RE = re.compile(r"(\]\()(?:((?:\.\./)?images/[^)]+)|([A-Za-z0-9_]+\.md))(\))")

OVERVIEW = {
    "WikiHome", "FileStructureTOC", "FileLayoutOverview",
    "SupportedVersions", "CommonStructures", "Problems",
}
META = {"WikiSidebar"}
TOOLS = {
    "Tools", "ConversionTools", "MzXMLUnpack", "HachoirParser",
    "bgrep", "Hexdump", "Iconv", "UnixStrings",
}

STRUCTURE_GROUPS = [
    ("File-level structures", [
        "AuditTag", "ASInfo", "ASInfoPreamble", "FileHeader", "InjectionData",
        "InstrumentMethodData", "MethodFile", "MethodFileStructure",
        "RawFileInfo", "RawFileInfoPreamble", "SeqRow",
    ]),
    ("Index and metadata", [
        "Error", "ErrorLog", "SampleInfo", "RunHeader", "InstID",
        "InstrumentLog", "InstrumentLogRecord", "TuneFile",
    ]),
    ("Scan data streams", [
        "PeakData", "PeakList", "FractionCollector", "Profile", "ProfileChunk",
        "Reaction", "ScanData", "ScanDataPacket", "PacketHeader", "ScanIndex",
        "ScanIndexEntry", "ScanIndexStream", "ScanParameters",
        "ScanParametersStream", "ScanEvent", "ScanEventPreamble",
        "ScanEventTemplate", "ScanEventStream", "ScanEventHierarchy",
    ]),
    ("Generic (self-describing) records", [
        "GenericData", "GenericDataDescriptor", "GenericDataHeader",
        "GenericRecord", "GenericRecordExample",
    ]),
    ("Shared field types", [
        "PascalStringWin32", "RawBytes", "TimestampWin64",
    ]),
]

INTRO = (
    "Documentation recovered from the Google Code project *unfinnigan* "
    "(Painless extraction of mass spectra from Thermo \u201craw\u201d files), "
    "converted from Internet Archive copies of the original HTML pages."
)


def classify(name):
    if name in OVERVIEW:
        return "overview"
    if name in META:
        return "meta"
    if name.startswith("Finnigan") or name in ("DecoderTOC", "APIChanges"):
        return "decoder-api"
    if name.startswith("Unfinnigan") or name in TOOLS:
        return "tools"
    return "structures"


def main():
    docs = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DOCS
    placement = {}

    # classify existing flat pages
    for entry in sorted(os.listdir(docs)):
        path = os.path.join(docs, entry)
        if not (os.path.isfile(path) and entry.endswith(".md")):
            continue
        name = entry[:-3]
        if name == "index":
            continue
        placement[name] = classify(name)

    # move files
    for name, subdir in sorted(placement.items()):
        dest_dir = os.path.join(docs, subdir)
        os.makedirs(dest_dir, exist_ok=True)
        os.rename(os.path.join(docs, name + ".md"),
                  os.path.join(dest_dir, name + ".md"))

    def target_rel(from_subdir, root_path):
        """New relative link text for a docs-root-relative target."""
        return os.path.relpath(root_path, from_subdir or ".")

    # rewrite links inside every moved page
    for name, subdir in sorted(placement.items()):
        path = os.path.join(docs, subdir, name + ".md")
        text = open(path, encoding="utf-8").read()

        def sub(m):
            pre, img, page, post = m.groups()
            if img:
                root_path = img[len("../"):] if img.startswith("../") else img
                return f"{pre}{target_rel(subdir, root_path)}{post}"
            stem = page[:-3]
            if stem == "index":
                root_path = "index.md"
            else:
                root_path = os.path.join(placement[stem], page)
            return f"{pre}{target_rel(subdir, root_path)}{post}"

        open(path, "w", encoding="utf-8").write(LINK_RE.sub(sub, text))

    # rebuild index.md
    lines = [
        "---",
        "title: unfinnigan wiki",
        "original: https://code.google.com/p/unfinnigan/w/list",
        "source: Internet Archive copy of Google Code wiki",
        "---",
        "",
        "# unfinnigan wiki",
        "",
        INTRO,
        "",
        "## Start here",
        "",
    ]
    for name in ["WikiHome", "FileLayoutOverview", "FileStructureTOC",
                 "CommonStructures", "SupportedVersions", "Problems"]:
        lines.append(f"- [{name}](overview/{name}.md)")
    lines += ["", "## File structure reference", ""]
    listed = set()
    for group, members in STRUCTURE_GROUPS:
        lines += [f"### {group}", ""]
        for n in sorted(members):
            lines.append(f"- [{n}](structures/{n}.md)")
            listed.add(n)
        lines.append("")
    extra = sorted(set(placement) - listed
                   - {n for n in placement if placement[n] != "structures"})
    if extra:
        lines += ["### Other", ""]
        for n in extra:
            lines.append(f"- [{n}](structures/{n}.md)")
        lines.append("")
    lines += ["## Decoder API (Perl)", "",
              "- [DecoderTOC](decoder-api/DecoderTOC.md) -- start here"]
    for n in sorted(n for n in placement if placement[n] == "decoder-api"):
        if n not in ("DecoderTOC", "APIChanges"):
            lines.append(f"- [{n}](decoder-api/{n}.md)")
    lines += ["- [APIChanges](decoder-api/APIChanges.md)", "",
              "## Tools", ""]
    for n in sorted(n for n in placement if placement[n] == "tools"
                    and n.startswith("Unfinnigan")):
        lines.append(f"- [{n}](tools/{n}.md)")
    lines.append("")
    for n in sorted(n for n in placement if placement[n] == "tools"
                    and not n.startswith("Unfinnigan")):
        lines.append(f"- [{n}](tools/{n}.md)")
    lines += ["", "## Meta", "",
              "- [WikiSidebar](meta/WikiSidebar.md) -- original site navigation", ""]
    with open(os.path.join(docs, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    counts = {}
    for subdir in placement.values():
        counts[subdir] = counts.get(subdir, 0) + 1
    print(f"Organized {sum(counts.values())} pages:", ", ".join(
        f"{k}={v}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    sys.exit(main())

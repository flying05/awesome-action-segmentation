#!/usr/bin/env python3
"""Validate schema, identity, provenance, generated files and local PDFs."""

from __future__ import annotations

import argparse
import hashlib
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from pypdf import PdfReader

from _common import (
    CUTOFF_DATE, DATA, REQUIRED_FIELDS, ROOT, VENUE_TIERS,
    load_papers, normalize_title, sha256_file,
)

REQUIRED_FILES = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "CITATION.cff",
    "data/papers.yaml", "data/papers.json", "data/papers.jsonl",
    "data/papers.csv", "data/papers.bib", "docs/survey_zh.md",
    "docs/history_timeline.md", "docs/taxonomy.md",
    "docs/datasets_and_metrics.md", "docs/verification_report.md",
]


def validate() -> list[str]:
    errors: list[str] = []
    papers = load_papers()
    ids = Counter(p.get("id", "") for p in papers)
    titles = Counter(normalize_title(p.get("title", "")) for p in papers)
    for duplicate in [k for k, count in ids.items() if count > 1]:
        errors.append(f"duplicate id: {duplicate}")
    for duplicate in [k for k, count in titles.items() if count > 1 and k]:
        errors.append(f"duplicate normalized title: {duplicate}")
    for paper in papers:
        missing = [field for field in REQUIRED_FIELDS if field not in paper]
        if missing:
            errors.append(f"{paper.get('id', '?')}: missing fields {missing}")
            continue
        if not paper["title"] or not paper["year"] or not paper["venue"]:
            errors.append(f"{paper['id']}: title/year/venue must be non-empty")
        if paper["venue_tier"] not in VENUE_TIERS:
            errors.append(f"{paper['id']}: invalid venue_tier {paper['venue_tier']}")
        if paper["year"] > int(CUTOFF_DATE[:4]):
            errors.append(f"{paper['id']}: after cutoff year")
        formal = paper["venue_tier"] not in {"Preprint", "Related-but-not-core"}
        if formal and not any(paper["verification_sources"]):
            errors.append(f"{paper['id']}: formal record has no first-party source")
        if formal and paper["publication_type"] == "preprint":
            errors.append(f"{paper['id']}: preprint leaked into formal list")
        for key in ["official_publication_url", "official_pdf_url", "arxiv_url", "code_url", "project_url"]:
            value = paper[key]
            if value and urlparse(value).scheme not in {"http", "https"}:
                errors.append(f"{paper['id']}: malformed URL in {key}")
        if not paper["inclusion_reason"]:
            errors.append(f"{paper['id']}: empty inclusion_reason")
        if ("supervoxel" in paper["title"].casefold() and
                paper["venue_tier"] != "Related-but-not-core"):
            errors.append(f"{paper['id']}: obvious spatial segmentation paper is in core TAS")
        if paper["pdf_downloaded"]:
            path = ROOT / paper["local_pdf_path"]
            if not path.exists():
                errors.append(f"{paper['id']}: recorded PDF missing")
            else:
                digest = sha256_file(path)
                if digest != paper["pdf_sha256"]:
                    errors.append(f"{paper['id']}: PDF SHA256 mismatch")
                try:
                    PdfReader(str(path))
                except Exception as exc:
                    errors.append(f"{paper['id']}: unreadable PDF: {exc}")
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"missing generated file: {relative}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    formal_count = sum(1 for p in papers if p["venue_tier"] not in {"Preprint", "Related-but-not-core"})
    marker = re.search(r"\*\*Verified conference papers:\*\*\s*(\d+)", readme)
    if not marker or int(marker.group(1)) != formal_count:
        errors.append("README formal paper count does not match metadata")
    bib = (DATA / "papers.bib").read_text(encoding="utf-8") if (DATA / "papers.bib").exists() else ""
    keys = re.findall(r"@\w+\{([^,]+),", bib)
    if len(keys) != len(set(keys)) or len(keys) != len(papers):
        errors.append("BibTeX keys are not unique or count differs from metadata")
    for match in re.finditer(r"\]\((?!https?://|#)([^)]+)\)", readme):
        target = match.group(1).split("#", 1)[0]
        if target and not (ROOT / target).exists():
            errors.append(f"README relative link missing: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    errors = validate()
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        print(f"[Validate] failures={len(errors)}")
        return 1
    if not args.quiet:
        print(f"[Validate] passed papers={len(load_papers())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

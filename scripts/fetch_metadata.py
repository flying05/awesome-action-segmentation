#!/usr/bin/env python3
"""Normalize and complete metadata fields without inventing unknown values."""

from __future__ import annotations

import argparse
import logging

from _common import REQUIRED_FIELDS, infer_fields, load_papers, save_serializations, setup_logging


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only-unverified", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    papers = load_papers()
    changed = 0
    for paper in papers:
        if args.only_unverified and paper.get("metadata_verified"):
            continue
        before = repr(paper)
        for field in REQUIRED_FIELDS:
            if field not in paper:
                paper[field] = [] if field in {
                    "authors", "keywords", "task_categories", "supervision",
                    "modality", "setting", "method_family", "datasets", "metrics",
                    "main_contributions", "limitations", "verification_sources",
                } else False if field in {
                    "related_to_core_tas", "pdf_downloaded", "metadata_verified",
                } else ""
        if not paper.get("abstract"):
            paper["abstract"] = "unknown"
        infer_fields(paper)
        changed += before != repr(paper)
    logging.info("[Metadata] records=%s normalized=%s", len(papers), changed)
    if not args.dry_run:
        save_serializations(papers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Deduplicate paper metadata using DOI, arXiv ID and normalized title."""

from __future__ import annotations

import argparse
import csv
import logging

from _common import LOGS, deduplicate, load_papers, save_serializations, setup_logging


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    papers, duplicates = deduplicate(load_papers())
    logging.info("[Deduplicate] kept=%s merged=%s", len(papers), len(duplicates))
    if not args.dry_run:
        save_serializations(papers)
        with (LOGS / "duplicate_report.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["kept_id", "merged_id", "rule", "details"])
            for kept, merged, rule in duplicates:
                writer.writerow([kept, merged, rule, "same normalized identity"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


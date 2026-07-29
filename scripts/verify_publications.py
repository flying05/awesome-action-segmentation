#!/usr/bin/env python3
"""Verify first-party publication links and record failures."""

from __future__ import annotations

import argparse
import csv
import logging
from datetime import datetime, timezone

from _common import CUTOFF_DATE, LOGS, load_papers, request, save_serializations, setup_logging


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only-unverified", action="store_true")
    parser.add_argument("--retry-failures", action="store_true")
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    papers = load_papers()
    failures: list[list[str]] = []
    checked = verified = 0
    for paper in papers:
        if paper.get("publication_type") in {
            "preprint", "conference-claimed", "journal-claimed",
        }:
            continue
        if args.only_unverified and paper.get("metadata_verified"):
            continue
        sources = [s for s in paper.get("verification_sources", []) if s]
        checked += 1
        ok = False
        for source in sources:
            try:
                response = request(source, timeout=args.timeout, retries=2, stream=True)
                ok = 200 <= response.status_code < 400
                response.close()
                if ok:
                    break
            except Exception as exc:
                failures.append([paper["id"], source, str(exc), datetime.now(timezone.utc).isoformat()])
        paper["metadata_verified"] = bool(ok)
        paper["verification_date"] = CUTOFF_DATE
        if ok:
            verified += 1
        else:
            paper["needs_manual_review"] = True
            paper["review_reason"] = "First-party URL could not be revalidated in this run."
    logging.info("[Verify] checked=%s verified=%s failures=%s", checked, verified, len(failures))
    if not args.dry_run:
        save_serializations(papers)
        with (LOGS / "verification_failures.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["paper_id", "source_url", "reason", "checked_at"])
            writer.writerows(failures)
    return 0 if not failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

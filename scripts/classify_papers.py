#!/usr/bin/env python3
"""Apply conservative metadata classification rules."""

from __future__ import annotations

import argparse
import logging

from _common import infer_fields, load_papers, save_serializations, setup_logging


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    papers = load_papers()
    for paper in papers:
        infer_fields(paper)
        if paper["title"] == "Human Action Segmentation With Hierarchical Supervoxel Consistency":
            paper.update({
                "venue_tier": "Related-but-not-core",
                "related_to_core_tas": False,
                "task_categories": ["Spatial human action segmentation"],
                "inclusion_reason": (
                    "This work segments the human/action region in video using "
                    "supervoxels and actionness rather than assigning semantic "
                    "action labels densely along the temporal axis."
                ),
                "notes": "Excluded from core TAS: spatial action-region segmentation.",
            })
    logging.info("[Classify] classified=%s", len(papers))
    if not args.dry_run:
        save_serializations(papers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run the reproducible search, verification, download and generation pipeline."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script: str, args: list[str]) -> None:
    command = [sys.executable, str(ROOT / "scripts" / script), *args]
    print("[Run]", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff-date", default="2026-07-28")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-download", action="store_true")
    parser.add_argument("--venues", default="CVPR,ICCV,WACV")
    parser.add_argument("--start-year", type=int, default=2010)
    parser.add_argument("--end-year", type=int, default=2026)
    parser.add_argument("--only-unverified", action="store_true")
    parser.add_argument("--retry-failures", action="store_true")
    args = parser.parse_args()
    if args.cutoff_date > "2026-07-28":
        raise SystemExit("This snapshot is configured only through 2026-07-28; update source policy before advancing cutoff.")
    common = ["--dry-run"] if args.dry_run else []
    run("search_candidates.py", [
        "--start-year", str(args.start_year), "--end-year", str(args.end_year),
        "--venues", args.venues, *common,
    ])
    metadata_args = [*common]
    if args.only_unverified:
        metadata_args.append("--only-unverified")
    run("fetch_metadata.py", metadata_args)
    verify_args = [*common]
    if args.only_unverified:
        verify_args.append("--only-unverified")
    if args.retry_failures:
        verify_args.append("--retry-failures")
    run("verify_publications.py", verify_args)
    run("deduplicate.py", common)
    if not args.skip_download:
        download_args = ["--only-missing", *common]
        if args.retry_failures:
            download_args.append("--retry-failures")
        run("download_pdfs.py", download_args)
    run("classify_papers.py", common)
    run("generate_readme.py", common)
    run("generate_docs.py", common)
    if not args.dry_run:
        run("validate_repository.py", [])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


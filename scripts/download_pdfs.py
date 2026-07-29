#!/usr/bin/env python3
"""Download legally public paper PDFs with retries, hashes and a manifest."""

from __future__ import annotations

import argparse
import csv
import logging
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

from _common import (
    LOGS, PDF_DIR, ROOT, load_papers, request, save_serializations,
    sha256_file, slug, setup_logging,
)


def filename(paper: dict) -> str:
    first = slug(paper["authors"][0].split()[-1] if paper["authors"] else "Unknown", 24).title()
    venue = re.sub(r"[^A-Za-z0-9]+", "", paper["venue"]) or "Preprint"
    short = slug(paper["title"], 55).replace("-", "_")
    return f"{paper['year']}_{venue}_{first}_{short}.pdf"


def is_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1024:
        return False
    try:
        PdfReader(str(path))
        return True
    except Exception:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only-missing", action="store_true")
    parser.add_argument("--retry-failures", action="store_true")
    parser.add_argument("--timeout", type=float, default=60)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--rate-limit", type=float, default=0.35)
    parser.add_argument("--max-papers", type=int, default=0)
    parser.add_argument("--max-mb", type=int, default=50)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    papers = load_papers()
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[list[object]] = []
    failures: list[list[str]] = []
    success = attempted = 0
    for paper in papers:
        if args.max_papers and attempted >= args.max_papers:
            break
        source = paper.get("official_pdf_url") or (
            paper.get("arxiv_url", "").replace("/abs/", "/pdf/") if paper.get("arxiv_url") else ""
        )
        if not source:
            rows.append([paper["id"], paper["title"], paper["year"], paper["venue"], "", "", 0, "", "skipped", "no public PDF URL"])
            continue
        recorded = (
            ROOT / paper["local_pdf_path"]
            if paper.get("local_pdf_path")
            else None
        )
        if recorded and is_pdf(recorded):
            digest = sha256_file(recorded)
            paper.update({
                "pdf_downloaded": True,
                "local_pdf_path": recorded.relative_to(ROOT).as_posix(),
                "pdf_sha256": digest,
            })
            rows.append([
                paper["id"], paper["title"], paper["year"], paper["venue"],
                source, paper["local_pdf_path"], recorded.stat().st_size,
                digest, "existing", "",
            ])
            success += 1
            continue
        target = PDF_DIR / filename(paper)
        if target.exists() and is_pdf(target):
            digest = sha256_file(target)
            paper.update({
                "pdf_downloaded": True,
                "local_pdf_path": target.relative_to(ROOT).as_posix(),
                "pdf_sha256": digest,
            })
            rows.append([paper["id"], paper["title"], paper["year"], paper["venue"], source, paper["local_pdf_path"], target.stat().st_size, digest, "existing", ""])
            success += 1
            continue
        if args.dry_run:
            rows.append([paper["id"], paper["title"], paper["year"], paper["venue"], source, target.relative_to(ROOT).as_posix(), 0, "", "dry-run", ""])
            continue
        attempted += 1
        part = target.with_suffix(".pdf.part")
        try:
            response = request(source, timeout=args.timeout, retries=args.retries, stream=True)
            content_type = response.headers.get("content-type", "").casefold()
            length = int(response.headers.get("content-length", "0") or 0)
            if length > args.max_mb * 1024 * 1024:
                raise ValueError(f"file exceeds {args.max_mb} MB safety limit")
            with part.open("wb") as handle:
                size = 0
                for chunk in response.iter_content(1024 * 256):
                    if chunk:
                        size += len(chunk)
                        if size > args.max_mb * 1024 * 1024:
                            raise ValueError(f"stream exceeds {args.max_mb} MB safety limit")
                        handle.write(chunk)
            response.close()
            if "pdf" not in content_type and part.read_bytes()[:5] != b"%PDF-":
                raise ValueError(f"not a PDF response ({content_type or 'unknown content type'})")
            part.replace(target)
            if not is_pdf(target):
                raise ValueError("PDF parser could not open the file")
            digest = sha256_file(target)
            paper.update({
                "pdf_downloaded": True,
                "local_pdf_path": target.relative_to(ROOT).as_posix(),
                "pdf_sha256": digest,
            })
            rows.append([paper["id"], paper["title"], paper["year"], paper["venue"], source, paper["local_pdf_path"], target.stat().st_size, digest, "downloaded", ""])
            success += 1
        except Exception as exc:
            if part.exists():
                part.unlink()
            message = str(exc).replace("\n", " ")
            failures.append([paper["id"], source, message, datetime.now(timezone.utc).isoformat()])
            rows.append([paper["id"], paper["title"], paper["year"], paper["venue"], source, "", 0, "", "failed", message])
            paper.update({"pdf_downloaded": False, "local_pdf_path": "", "pdf_sha256": ""})
            logging.warning("%s: %s", paper["id"], message)
        time.sleep(max(0.0, args.rate_limit))
    logging.info("[Download] success=%s attempted=%s failures=%s", success, attempted, len(failures))
    if not args.dry_run:
        save_serializations(papers)
        with (ROOT / "library" / "pdf_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["paper_id", "title", "year", "venue", "source_url", "local_path", "file_size", "sha256", "status", "error"])
            writer.writerows(rows)
        with (LOGS / "download_failures.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["paper_id", "source_url", "reason", "checked_at"])
            writer.writerows(failures)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

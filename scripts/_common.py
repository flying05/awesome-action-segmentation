"""Shared repository utilities.

The repository deliberately keeps YAML as the single editable source and
generates all other serializations deterministically.
"""

from __future__ import annotations

import csv
import hashlib
import json
import logging
import re
import time
import unicodedata
from pathlib import Path
from typing import Any, Iterable

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
LOGS = ROOT / "logs"
PDF_DIR = ROOT / "library" / "pdfs"
CUTOFF_DATE = "2026-07-28"

REQUIRED_FIELDS = [
    "id", "title", "authors", "year", "venue", "venue_tier",
    "publication_type", "official_publication_url", "official_pdf_url",
    "arxiv_url", "doi", "code_url", "project_url", "abstract", "keywords",
    "task_categories", "supervision", "modality", "setting", "method_family",
    "backbone", "datasets", "metrics", "main_contributions", "limitations",
    "inclusion_reason", "related_to_core_tas", "pdf_downloaded",
    "local_pdf_path", "pdf_sha256", "metadata_verified",
    "verification_sources", "verification_date", "notes",
]

VENUE_TIERS = {
    "CCF-A", "Top-Vision", "Extended-Vision", "Medical",
    "Robotics-Embodied", "Preprint", "Related-but-not-core",
}

CORE_VENUES = {
    "CVPR": "CCF-A", "ICCV": "CCF-A", "NeurIPS": "CCF-A",
    "NIPS": "CCF-A", "ICML": "CCF-A", "AAAI": "CCF-A",
    "IJCAI": "CCF-A", "ACM MM": "CCF-A",
    "ECCV": "Top-Vision", "WACV": "Top-Vision", "BMVC": "Top-Vision",
    "ACCV": "Extended-Vision", "ICPR": "Extended-Vision",
    "ICME": "Extended-Vision", "ACM ICMR": "Extended-Vision",
    "FG": "Extended-Vision", "3DV": "Extended-Vision",
    "MICCAI": "Medical", "ICRA": "Robotics-Embodied",
    "IROS": "Robotics-Embodied", "CoRL": "Robotics-Embodied",
    "ISKE": "Extended-Vision", "DICTA": "Extended-Vision",
    "CVWW": "Extended-Vision",
}


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def dump_yaml(value: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        yaml.safe_dump(
            value, handle, allow_unicode=True, sort_keys=False, width=120,
        )


def normalize_title(title: str) -> str:
    text = unicodedata.normalize("NFKD", title).casefold()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def slug(text: str, limit: int = 52) -> str:
    value = normalize_title(text).replace(" ", "-").strip("-")
    return value[:limit].rstrip("-") or "paper"


def stable_id(year: int, venue: str, title: str) -> str:
    acronym = re.sub(r"[^a-z0-9]+", "-", venue.casefold()).strip("-")
    words = [
        w for w in normalize_title(title).split()
        if w not in {"a", "an", "the", "for", "of", "and", "with", "via",
                     "to", "in", "on", "from", "temporal", "action",
                     "segmentation", "video"}
    ]
    short = "-".join(words[:5]) or slug(title, 35)
    return f"{year}-{acronym}-{short}"


def default_record(
    *,
    title: str,
    authors: list[str],
    year: int,
    venue: str,
    official_publication_url: str = "",
    official_pdf_url: str = "",
    abstract: str = "",
) -> dict[str, Any]:
    tier = CORE_VENUES.get(venue, "Related-but-not-core")
    return {
        "id": stable_id(year, venue, title),
        "title": title.strip(),
        "authors": authors,
        "year": int(year),
        "venue": venue,
        "venue_tier": tier,
        "publication_type": "conference",
        "official_publication_url": official_publication_url,
        "official_pdf_url": official_pdf_url,
        "arxiv_url": "",
        "doi": "",
        "code_url": "",
        "project_url": "",
        "abstract": abstract.strip(),
        "keywords": ["temporal action segmentation"],
        "task_categories": ["Temporal Action Segmentation"],
        "supervision": ["fully-supervised"],
        "modality": ["unknown"],
        "setting": ["offline", "long-video"],
        "method_family": ["unknown"],
        "backbone": "unknown",
        "datasets": [],
        "metrics": ["Edit", "F1@10", "F1@25", "F1@50", "frame accuracy"],
        "main_contributions": [],
        "limitations": ["See the original paper for scope and assumptions."],
        "inclusion_reason": (
            "The paper predicts temporally dense action labels or contiguous "
            "semantic action segments and evaluates temporal segmentation."
        ),
        "related_to_core_tas": True,
        "pdf_downloaded": False,
        "local_pdf_path": "",
        "pdf_sha256": "",
        "metadata_verified": True,
        "verification_sources": [official_publication_url or official_pdf_url],
        "verification_date": CUTOFF_DATE,
        "notes": "",
        "needs_manual_review": False,
        "review_reason": "",
    }


def infer_fields(record: dict[str, Any]) -> dict[str, Any]:
    text = f"{record.get('title', '')} {record.get('abstract', '')}".casefold()
    if "timestamp" in text:
        record["supervision"] = ["timestamp-supervised"]
    elif "weakly-supervised" in text or "weakly supervised" in text:
        record["supervision"] = ["weakly-supervised"]
    elif "semi-supervised" in text or "semi supervised" in text:
        record["supervision"] = ["semi-supervised"]
    elif "self-supervised" in text or "self supervised" in text:
        record["supervision"] = ["self-supervised"]
    elif "unsupervised" in text:
        record["supervision"] = ["unsupervised"]
    elif "few-shot" in text or "few shot" in text:
        record["supervision"] = ["few-shot"]
    elif "zero-shot" in text or "zero shot" in text:
        record["supervision"] = ["zero-shot"]

    families: list[str] = []
    mapping = {
        "transformer": "Transformer",
        "cross-attention": "cross-attention",
        "cross attention": "cross-attention",
        "diffusion": "diffusion",
        "optimal transport": "optimal-transport",
        "clustering": "clustering",
        "prototype": "prototype-learning",
        "boundary": "boundary-modeling",
        "duration": "duration-modeling",
        "grammar": "structured-decoding",
        "viterbi": "structured-decoding",
        "temporal convolution": "TCN",
        "multi-stage": "multi-stage-TCN",
        "multistage": "multi-stage-TCN",
        "token": "VQ-tokenization",
        "causal": "causal-model",
        "condens": "dataset-condensation",
    }
    for needle, family in mapping.items():
        if needle in text and family not in families:
            families.append(family)
    record["method_family"] = families or record.get("method_family") or ["unknown"]

    modalities = list(record.get("modality", []))
    if "skeleton" in text:
        modalities = ["skeleton"]
        record["task_categories"] = ["Skeleton-based Temporal Action Segmentation"]
    if "egocentric" in text:
        record["setting"] = sorted(set(record["setting"] + ["egocentric"]))
    if "online" in text:
        record["setting"] = [
            value for value in record["setting"] if value != "offline"
        ]
        record["setting"] = sorted(set(record["setting"] + ["online", "streaming"]))
    if "few-shot" in text or "zero-shot" in text or "open-set" in text:
        record["setting"] = sorted(set(record["setting"] + ["open-vocabulary"]))
    if "multi-modal" in text or "multimodal" in text:
        modalities.append("multimodal")
    if "vision-language" in text or "vision language" in text or "language model" in text:
        modalities.append("video-language")
    for needle, label in [
        ("rgb", "RGB"), ("i3d", "I3D-features"),
        ("audio", "audio"), ("gaze", "gaze"), ("imu", "IMU"),
        ("depth", "depth"), ("optical flow", "optical-flow"),
    ]:
        if needle in text:
            modalities.append(label)
    if len(modalities) > 1 and "unknown" in modalities:
        modalities.remove("unknown")
    record["modality"] = list(dict.fromkeys(modalities))
    return record


def request(
    url: str,
    *,
    timeout: float = 30.0,
    retries: int = 3,
    delay: float = 0.8,
    stream: bool = False,
) -> requests.Response:
    headers = {
        "User-Agent": (
            "AwesomeActionSegmentation/0.1 "
            "(academic metadata curation; respectful low-rate client)"
        )
    }
    error: Exception | None = None
    for attempt in range(retries):
        try:
            response = requests.get(
                url, timeout=timeout, headers=headers, stream=stream,
            )
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            error = exc
            if attempt + 1 < retries:
                time.sleep(delay * (2 ** attempt))
    assert error is not None
    raise error


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deduplicate(records: Iterable[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[tuple[str, str, str]]]:
    def merge_complementary(keeper: dict[str, Any], other: dict[str, Any]) -> None:
        """Preserve provenance and local artifacts when identities merge."""
        for field in [
            "arxiv_url", "doi", "code_url", "project_url", "abstract",
        ]:
            if not keeper.get(field) and other.get(field):
                keeper[field] = other[field]
        for field in ["datasets", "verification_sources"]:
            values = [
                *keeper.get(field, []),
                *other.get(field, []),
            ]
            keeper[field] = list(dict.fromkeys(value for value in values if value))
        if other.get("pdf_downloaded") and not keeper.get("pdf_downloaded"):
            keeper["pdf_downloaded"] = True
            keeper["local_pdf_path"] = other.get("local_pdf_path", "")
            keeper["pdf_sha256"] = other.get("pdf_sha256", "")

    kept: list[dict[str, Any]] = []
    seen: dict[str, dict[str, Any]] = {}
    duplicates: list[tuple[str, str, str]] = []
    for record in records:
        keys = []
        if record.get("doi"):
            keys.append("doi:" + record["doi"].casefold().strip())
        if record.get("arxiv_url"):
            match = re.search(r"(\d{4}\.\d{4,5})", record["arxiv_url"])
            if match:
                keys.append("arxiv:" + match.group(1))
        keys.append("title:" + normalize_title(record["title"]))
        duplicate = next((seen[k] for k in keys if k in seen), None)
        if duplicate:
            # Prefer a verified formal publication over a preprint.
            if (record.get("metadata_verified") and
                    duplicate.get("venue_tier") == "Preprint"):
                merge_complementary(record, duplicate)
                kept.remove(duplicate)
                kept.append(record)
                duplicates.append((record["id"], duplicate["id"], "formal-over-preprint"))
                for key, value in list(seen.items()):
                    if value is duplicate:
                        seen[key] = record
            else:
                merge_complementary(duplicate, record)
                duplicates.append((duplicate["id"], record["id"], "identity-key"))
            continue
        kept.append(record)
        for key in keys:
            seen[key] = record
    return kept, duplicates


def save_serializations(records: list[dict[str, Any]]) -> None:
    records = sorted(records, key=lambda p: (-int(p["year"]), p["venue"], p["title"]))
    dump_yaml(records, DATA / "papers.yaml")
    with (DATA / "papers.json").open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(records, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with (DATA / "papers.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    columns = REQUIRED_FIELDS + [
        "needs_manual_review", "review_reason", "publication_claim",
    ]
    with (DATA / "papers.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            row = dict(record)
            for key, value in row.items():
                if isinstance(value, (list, dict)):
                    row[key] = json.dumps(value, ensure_ascii=False)
            writer.writerow(row)
    with (DATA / "papers.bib").open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            entry = "article" if record["publication_type"] == "preprint" else "inproceedings"
            authors = " and ".join(record["authors"]) or "Unknown"
            handle.write(
                f"@{entry}{{{record['id'].replace('-', '_')},\n"
                f"  title = {{{record['title']}}},\n"
                f"  author = {{{authors}}},\n"
                f"  year = {{{record['year']}}},\n"
                f"  booktitle = {{{record['venue']}}},\n"
                f"  url = {{{record['official_publication_url'] or record['arxiv_url']}}}\n"
                "}\n\n"
            )


def load_papers() -> list[dict[str, Any]]:
    value = load_yaml(DATA / "papers.yaml")
    return value or []

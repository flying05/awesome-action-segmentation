#!/usr/bin/env python3
"""Scan official CVF proceedings and merge a curated first-party seed list."""

from __future__ import annotations

import argparse
import json
import logging
import re
import time
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from _common import (
    CUTOFF_DATE,
    DATA,
    LOGS,
    deduplicate,
    default_record,
    dump_yaml,
    infer_fields,
    load_yaml,
    request,
    save_serializations,
    setup_logging,
)
from _curated import FORMAL, PREPRINTS

CVF = "https://openaccess.thecvf.com/"

EXACT_FRAGMENTS = [
    "temporal convolutional networks for action segmentation",
    "temporal deformable residual networks for action segmentation",
    "ms-tcn:",
    "improving action segmentation",
    "action segmentation with",
    "global2local:",
    "action shuffle alternating",
    "temporally-weighted hierarchical clustering",
    "joint visual-temporal embedding",
    "learning discriminative prototypes with dynamic time warping",
    "anchor-constrained viterbi",
    "set-constrained viterbi",
    "neuralnetwork-viterbi",
    "weakly supervised action learning with rnn",
    "d3tw:",
    "sct: set constrained",
    "unsupervised learning and segmentation of complex activities",
    "unsupervised learning of action classes",
    "unsupervised procedure learning",
    "unsupervised semantic parsing of video collections",
    "unsupervised learning from narrated instruction videos",
    "action sets: weakly supervised",
    "weakly-supervised action segmentation",
    "weakly supervised energy-based",
    "temporal action segmentation",
    "action segmentation",
    "procedure learning from egocentric",
    "set-supervised action learning",
    "complex actions from instructional task videos",
    "coherent temporal synthesis for incremental action segmentation",
    "action segmentation datasets",
    "action boundary detection for action segmentation",
    "skeleton motion words",
    "duoclr:",
    "diffusion action segmentation",
    "activity grammars",
    "condensing action segmentation",
]

DATASET_TITLES = {
    "the language of actions: recovering the syntax and semantics of goal-directed human activities",
    "assembly101: a large-scale multi-view video dataset for understanding procedural activities",
    "coin: a large-scale dataset for comprehensive instructional video analysis",
}

EXCLUSIONS = [
    "actor-action segmentation",
    "spatio-temporal instance segmentation",
    "spatio-temporal action localization",
    "referring video object segmentation",
    "action recognition",
    "semantic segmentation",
]

CODE_URLS = {
    "ms-tcn: multi-stage temporal convolutional network for action segmentation":
        "https://github.com/yabufarha/ms-tcn",
    "global2local: efficient structure search for video action segmentation":
        "https://github.com/Thinksky5124/G2L",
    "alleviating over-segmentation errors by detecting action boundaries":
        "https://github.com/yiskw713/asrf",
    "diffusion action segmentation": "https://github.com/Finspire13/DiffAct",
    "fact: frame-action cross-attention temporal modeling for efficient action segmentation":
        "https://github.com/ZijiaLewisLu/CVPR2024-FACT",
    "temporally consistent unbalanced optimal transport for unsupervised action segmentation":
        "https://github.com/mingu6/action-segmentation-ot",
    "multi-modal few-shot temporal action segmentation":
        "https://github.com/ZijiaLewisLu/ICCV2025-MMF-TAS",
    "end-to-end action segmentation transformer": "https://github.com/tqosu/EAST",
}

# Old CVF indexes use several incompatible layouts, and transient index failures
# should not erase known TAS lineage papers. These are first-party detail pages,
# parsed with the same code as year-scan discoveries.
KNOWN_CVF_PAGES = [
    ("CVPR", 2018, f"{CVF}content_cvpr_2018/html/Lei_Temporal_Deformable_Residual_Networks_for_Action_Segmentation_in_Videos_CVPR_2018_paper.html"),
    ("CVPR", 2018, f"{CVF}content_cvpr_2018/html/Richard_Action_Sets_Weakly_CVPR_2018_paper.html"),
    ("CVPR", 2018, f"{CVF}content_cvpr_2018/html/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.html"),
    ("CVPR", 2018, f"{CVF}content_cvpr_2018/html/Ding_Weakly-Supervised_Action_Segmentation_CVPR_2018_paper.html"),
    ("CVPR", 2018, f"{CVF}content_cvpr_2018/html/Sener_Unsupervised_Learning_and_CVPR_2018_paper.html"),
    ("CVPR", 2019, f"{CVF}content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html"),
    ("CVPR", 2019, f"{CVF}content_CVPR_2019/html/Chang_D3TW_Discriminative_Differentiable_Dynamic_Time_Warping_for_Weakly_Supervised_Action_CVPR_2019_paper.html"),
    ("CVPR", 2019, f"{CVF}content_CVPR_2019/html/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.html"),
    ("ICCV", 2019, f"{CVF}content_ICCV_2019/html/Li_Weakly_Supervised_Energy-Based_Learning_for_Action_Segmentation_ICCV_2019_paper.html"),
    ("ICCV", 2019, f"{CVF}content_ICCV_2019/html/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.html"),
    ("CVPR", 2020, f"{CVF}content_CVPR_2020/html/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.html"),
    ("CVPR", 2020, f"{CVF}content_CVPR_2020/html/Chen_Action_Segmentation_With_Joint_Self-Supervised_Temporal_Domain_Adaptation_CVPR_2020_paper.html"),
    ("CVPR", 2020, f"{CVF}content_CVPR_2020/html/Fayyaz_SCT_Set_Constrained_Temporal_Transformer_for_Set_Supervised_Action_Segmentation_CVPR_2020_paper.html"),
    ("CVPR", 2020, f"{CVF}content_CVPR_2020/html/Li_Set-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2020_paper.html"),
    ("ICCV", 2023, f"{CVF}content/ICCV2023/html/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.html"),
    ("ICCV", 2023, f"{CVF}content/ICCV2023/html/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.html"),
    ("ICCV", 2023, f"{CVF}content/ICCV2023/html/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.html"),
    ("ICCV", 2023, f"{CVF}content/ICCV2023/html/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.html"),
    ("CVPR", 2024, f"{CVF}content/CVPR2024/html/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.html"),
    ("CVPR", 2024, f"{CVF}content/CVPR2024/html/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.html"),
    ("CVPR", 2024, f"{CVF}content/CVPR2024/html/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.html"),
    ("CVPR", 2024, f"{CVF}content/CVPR2024/html/Xu_Efficient_and_Effective_Weakly-Supervised_Action_Segmentation_via_Action-Transition-Aware_Boundary_Alignment_CVPR_2024_paper.html"),
    ("CVPR", 2024, f"{CVF}content/CVPR2024/html/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.html"),
]


def index_specs(start_year: int, end_year: int, venues: set[str]) -> list[tuple[str, int, str]]:
    specs: list[tuple[str, int, str]] = []
    for year in range(start_year, end_year + 1):
        if "CVPR" in venues and year >= 2013:
            specs.append(("CVPR", year, f"{CVF}CVPR{year}?day=all"))
        if "ICCV" in venues and year >= 2013 and year % 2 == 1:
            specs.append(("ICCV", year, f"{CVF}ICCV{year}?day=all"))
        if "WACV" in venues and year >= 2016:
            specs.append(("WACV", year, f"{CVF}WACV{year}?day=all"))
    return specs


def should_include(title: str) -> bool:
    folded = title.casefold()
    if any(term in folded for term in EXCLUSIONS):
        return False
    return folded in DATASET_TITLES or any(term in folded for term in EXACT_FRAGMENTS)


def parse_detail(page_url: str, venue: str, year: int) -> dict:
    response = request(page_url)
    soup = BeautifulSoup(response.text, "html.parser")
    title_node = soup.find(id="papertitle")
    title = title_node.get_text(" ", strip=True) if title_node else ""
    author_node = soup.find(id="authors")
    author_text = ""
    if author_node:
        italic = author_node.find("i")
        author_text = (italic or author_node).get_text(" ", strip=True)
    authors = [a.strip() for a in re.split(r"[,;]", author_text) if a.strip()]
    abstract_node = soup.find(id="abstract")
    abstract = abstract_node.get_text(" ", strip=True) if abstract_node else ""
    pdf_url = ""
    for link in soup.select("a[href]"):
        label = link.get_text(" ", strip=True).casefold()
        href = link.get("href", "")
        if label == "pdf" and href.casefold().endswith(".pdf"):
            pdf_url = urljoin(page_url, href)
            break
    record = default_record(
        title=title,
        authors=authors,
        year=year,
        venue=venue,
        official_publication_url=page_url,
        official_pdf_url=pdf_url,
        abstract=abstract,
    )
    infer_fields(record)
    record["code_url"] = CODE_URLS.get(title.casefold(), "")
    record["verification_sources"] = [page_url]
    for dataset in ["Breakfast", "50Salads", "GTEA", "Assembly101", "COIN", "CrossTask"]:
        if dataset.casefold() in abstract.casefold():
            record["datasets"].append(dataset)
    if title.casefold() in DATASET_TITLES:
        record.update({
            "venue_tier": "Related-but-not-core",
            "related_to_core_tas": False,
            "task_categories": ["Dataset / benchmark"],
            "inclusion_reason": (
                "This dataset paper directly enabled or standardized temporal "
                "action/step segmentation evaluation, but its primary contribution "
                "is a benchmark rather than a core TAS method."
            ),
        })
    return record


def scan_cvf(
    *, start_year: int, end_year: int, venues: set[str],
    dry_run: bool, cache_dir: Path,
) -> list[dict]:
    records: list[dict] = []
    cache_dir.mkdir(parents=True, exist_ok=True)
    for venue, year, url in index_specs(start_year, end_year, venues):
        cache_file = cache_dir / f"{venue}{year}.html"
        try:
            if cache_file.exists():
                html = cache_file.read_text(encoding="utf-8")
            else:
                html = request(url).text
                if not dry_run:
                    cache_file.write_text(html, encoding="utf-8")
                time.sleep(0.25)
            soup = BeautifulSoup(html, "html.parser")
            links = soup.select("dt.ptitle a[href]")
            selected = [
                (a.get_text(" ", strip=True), urljoin(url, a["href"]))
                for a in links if should_include(a.get_text(" ", strip=True))
            ]
            logging.info("[Search] %s %s: scanned=%s selected=%s", venue, year, len(links), len(selected))
            for title, page_url in selected:
                try:
                    record = parse_detail(page_url, venue, year)
                    if record["title"]:
                        records.append(record)
                    time.sleep(0.15)
                except Exception as exc:  # continue the year scan
                    logging.warning("detail failed %s: %s", page_url, exc)
                    with (LOGS / "search_log.jsonl").open("a", encoding="utf-8") as log:
                        log.write(json.dumps({
                            "stage": "detail", "title": title, "url": page_url,
                            "status": "failed", "error": str(exc),
                            "checked_at": CUTOFF_DATE,
                        }, ensure_ascii=False) + "\n")
        except Exception as exc:
            logging.warning("index failed %s: %s", url, exc)
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2010)
    parser.add_argument("--end-year", type=int, default=2026)
    parser.add_argument("--venues", default="CVPR,ICCV,WACV")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    venues = {v.strip() for v in args.venues.split(",") if v.strip()}
    cvf_records = scan_cvf(
        start_year=args.start_year,
        end_year=args.end_year,
        venues=venues,
        dry_run=args.dry_run,
        cache_dir=DATA.parent / ".cache" / "cvf",
    )
    for venue, year, page_url in KNOWN_CVF_PAGES:
        if venue not in venues or not (args.start_year <= year <= args.end_year):
            continue
        try:
            cvf_records.append(parse_detail(page_url, venue, year))
            time.sleep(0.15)
        except Exception as exc:
            logging.warning("known detail failed %s: %s", page_url, exc)
    existing = []
    papers_path = DATA / "papers.yaml"
    if papers_path.exists():
        existing = load_yaml(papers_path) or []
    records, duplicates = deduplicate([*cvf_records, *FORMAL, *PREPRINTS, *existing])
    logging.info(
        "[Search] discovered=%s official-CVF=%s curated-first-party=%s preprints=%s",
        len(records), len(cvf_records), len(FORMAL), len(PREPRINTS),
    )
    logging.info("[Deduplicate] merged=%s", len(duplicates))
    if not args.dry_run:
        dump_yaml(records, DATA / "candidates.yaml")
        save_serializations(records)
        with (LOGS / "duplicate_report.csv").open("w", encoding="utf-8", newline="") as handle:
            handle.write("kept_id,merged_id,rule,details\n")
            for kept, merged, rule in duplicates:
                handle.write(f"{kept},{merged},{rule},same normalized identity\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

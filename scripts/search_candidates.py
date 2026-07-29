#!/usr/bin/env python3
"""Scan official CVF proceedings and merge a curated first-party seed list."""

from __future__ import annotations

import argparse
import json
import logging
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlencode, urljoin

from bs4 import BeautifulSoup

from _common import (
    CORE_VENUES,
    CUTOFF_DATE,
    DATA,
    LOGS,
    deduplicate,
    default_record,
    dump_yaml,
    infer_fields,
    load_yaml,
    normalize_title,
    request,
    save_serializations,
    setup_logging,
    stable_id,
)
from _curated import FORMAL, PREPRINTS

CVF = "https://openaccess.thecvf.com/"
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

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
    "supervoxel",
]

ARXIV_QUERIES = [
    'all:"temporal action segmentation"',
    'ti:"action segmentation"',
    'ti:"action parsing"',
    'all:"skeleton-based action segmentation"',
    'all:"surgical phase segmentation"',
]

ARXIV_DIRECT_TITLE_PATTERNS = [
    r"\btemporal action segmentation\b",
    r"\baction segmentation\b",
    r"\baction parsing\b",
    r"\bsurgical (?:workflow|phase|step) segmentation\b",
]

ARXIV_TITLE_EXCLUSIONS = [
    r"\bspatio-?temporal action (?:detection|localization)\b",
    r"\bactor-action segmentation\b",
    r"\baction instance segmentation\b",
    r"\bfrom a single image\b",
    r"\bpart-level action parsing\b",
    r"\breferring human action segmentation\b",
    r"\bpeer-aware student behavioral engagement\b",
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

FORMAL_ARXIV_IDS = {
    "Segmental Spatiotemporal CNNs for Fine-Grained Action Segmentation": "1602.02995",
    "Temporal Convolutional Networks for Action Segmentation and Detection": "1611.05267",
    "End-to-End Fine-Grained Action Segmentation and Recognition Using Conditional Random Field Models and Discriminative Sparse Coding": "1801.09571",
    "Coupled Generative Adversarial Network for Continuous Fine-Grained Action Segmentation": "1909.09283",
    "MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation": "1903.01945",
    "Intra- and Inter-Action Understanding via Temporal Action Parsing": "2005.10229",
    "Temporal Relational Modeling with Self-Supervision for Action Segmentation": "2012.07508",
    "Alleviating Over-Segmentation Errors by Detecting Action Boundaries": "2007.06866",
    "SCT: Set Constrained Temporal Transformer for Set Supervised Action Segmentation": "2003.14266",
    "Temporal Action Segmentation From Timestamp Supervision": "2103.06669",
    "SSCAP: Self-Supervised Co-Occurrence Action Parsing for Unsupervised Temporal Action Segmentation": "2105.14158",
    "ASFormer: Transformer for Action Segmentation": "2110.08568",
    "Timestamp-Supervised Action Segmentation in the Perspective of Clustering": "2212.11694",
    "Turning to a Teacher for Timestamp Supervised Temporal Action Segmentation": "2207.00712",
    "Streaming Video Temporal Action Segmentation in Real Time": "2209.13808",
    "Action Parsing Using Context Features": "2205.10008",
    "Diffusion Action Segmentation": "2303.17959",
    "TAEC: Unsupervised Action Segmentation with Temporal-Aware Embedding and Clustering": "2303.05166",
    "HOI-aware Adaptive Network for Weakly-supervised Action Segmentation": "2604.26227",
    "Action Segmentation Using 2D Skeleton Heatmaps and Multi-Modality Fusion": "2309.06462",
    "Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment": "2305.19478",
    "How Much Temporal Long-Term Context is Needed for Action Segmentation?": "2308.11358",
    "Activity Grammars for Temporal Action Segmentation": "2312.04266",
    "OnlineTAS: An Online Baseline for Temporal Action Segmentation": "2411.01122",
    "Efficient Temporal Action Segmentation via Boundary-aware Query Voting": "2405.15995",
    "ActFusion: a Unified Diffusion Model for Action Segmentation and Anticipation": "2412.04353",
    "Hierarchical Vector Quantization for Unsupervised Action Segmentation": "2412.17640",
    "Stitch, Contrast, and Segment: Learning a Human Action Segmentation Model Using Trimmed Skeleton Videos": "2412.14988",
    "Long-Tail Temporal Action Segmentation with Group-wise Temporal Logit Adjustment": "2408.09919",
    "Cost-Sensitive Learning for Long-Tailed Temporal Action Segmentation": "2503.18358",
    "3D Pose-Based Temporal Action Segmentation for Figure Skating: A Fine-Grained and Jump Procedure-Aware Annotation Approach": "2408.16638",
    "M2R2: MultiModal Robotic Representation for Temporal Action Segmentation": "2504.18662",
    "Multi-Modal Graph Convolutional Network with Sinusoidal Encoding for Robust Human Action Segmentation": "2507.00752",
    "Towards Open-World Human Action Segmentation Using Graph Convolutional Networks": "2507.00756",
    "Learning Action Hierarchies via Hybrid Geometric Diffusion": "2601.01914",
    "Combining Boundary Supervision and Segment-Level Regularization for Fine-Grained Action Segmentation": "2604.01859",
    "Deep Kernel Video Approximation for Unsupervised Action Segmentation": "2604.21572",
    "Improving Temporal Action Segmentation via Constraint-Aware Decoding": "2605.10149",
}

ARXIV_SUPERSEDED_BY_FORMAL = {
    "1608.08242": (
        "Earlier TCN manuscript/version represented by the verified CVPR 2017 "
        "conference record."
    ),
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
    arxiv_url = ""
    for link in soup.select("a[href]"):
        label = link.get_text(" ", strip=True).casefold()
        href = link.get("href", "")
        if label == "pdf" and href.casefold().endswith(".pdf"):
            pdf_url = urljoin(page_url, href)
        if label == "arxiv" or "arxiv.org/abs/" in href:
            arxiv_url = urljoin(page_url, href)
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
    for dataset in [
        "Breakfast", "50Salads", "GTEA", "Assembly101", "IKEA ASM",
        "COIN", "CrossTask", "Cholec80", "EgoExo4D", "CMU-MMAC",
        "CaptainCook4D", "PKU-MMD", "LARa",
    ]:
        if dataset.casefold() in abstract.casefold():
            record["datasets"].append(dataset)
    record["datasets"] = list(dict.fromkeys(record["datasets"]))
    record["arxiv_url"] = arxiv_url
    record["code_url"] = CODE_URLS.get(title.casefold(), "")
    record["verification_sources"] = [page_url]
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


def _atom_text(entry: ET.Element, path: str) -> str:
    node = entry.find(path, ATOM_NS)
    return " ".join(node.text.split()) if node is not None and node.text else ""


def _arxiv_id(entry: ET.Element) -> str:
    value = _atom_text(entry, "atom:id").rsplit("/", 1)[-1]
    return re.sub(r"v\d+$", "", value)


def arxiv_is_direct(title: str) -> tuple[bool, str]:
    folded = title.casefold()
    if any(re.search(pattern, folded) for pattern in ARXIV_TITLE_EXCLUSIONS):
        return False, "excluded neighboring spatial/localization task"
    if any(re.search(pattern, folded) for pattern in ARXIV_DIRECT_TITLE_PATTERNS):
        return True, "title explicitly names temporal/action segmentation"
    return False, "query hit but title does not explicitly define a TAS task"


PUBLICATION_VENUE_PATTERNS = [
    ("Pattern Recognition Letters", r"\bpattern recognition letters\b"),
    ("Pattern Recognition", r"\bpattern recognition(?: journal)?\b"),
    ("IEEE Transactions on Multimedia", r"\b(?:ieee )?transactions on multimedia\b|\bTMM\b"),
    ("IEEE TPAMI", r"\b(?:ieee )?(?:transactions on pattern analysis and machine intelligence|TPAMI)\b"),
    ("IEEE TNNLS", r"\b(?:ieee )?(?:transactions on neural networks and learning systems|TNNLS)\b"),
    ("CVPR Workshop", r"\bCVPR(?:\s*20\d{2})?\s+workshops?\b|\bCVPRW\b"),
    ("Ego4D/EPIC Workshop", r"\bEgo4D\b.*\bEPIC\b.*\bworkshop\b"),
    ("CVWW", r"\b(?:computer vision winter workshop|CVWW)\b"),
    ("NeurIPS", r"\b(?:NeurIPS|NIPS)\b"),
    ("IJCAI", r"\bIJCAI\b"),
    ("AAAI", r"\bAAAI\b"),
    ("ECCV", r"\bECCV\b"),
    ("ICCV", r"\bICCV\b"),
    ("CVPR", r"\bCVPR\b"),
    ("WACV", r"\bWACV\b"),
    ("BMVC", r"\bBMVC\b"),
    ("ICML", r"\bICML\b"),
    ("ICPR", r"\bICPR\b"),
    ("IROS", r"\bIROS\b"),
    ("ICRA", r"\bICRA\b"),
    ("ICME", r"\bICME\b"),
    ("DICTA", r"\bDICTA\b|digital image computing"),
    ("ISKE", r"\bISKE\b"),
    ("TAHRI", r"\bTAHRI\b"),
    ("LUV Workshop", r"\bLUV workshop\b"),
]

JOURNAL_CLAIM_VENUES = {
    "Pattern Recognition Letters",
    "Pattern Recognition",
    "IEEE Transactions on Multimedia",
    "IEEE TPAMI",
    "IEEE TNNLS",
}


def extract_publication_claim(comment: str, journal_ref: str) -> dict:
    """Turn free-form arXiv publication notes into an auditable claim."""
    fields = [("journal_ref", journal_ref), ("comment", comment)]
    combined = " | ".join(value for _, value in fields if value)
    if not combined:
        return {}
    venue = ""
    for canonical, pattern in PUBLICATION_VENUE_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            venue = canonical
            break
    if not venue:
        return {}
    year_match = re.search(r"\b(20\d{2})\b", combined)
    if not year_match:
        year_match = re.search(
            r"\b(?:CVPR|ICCV|ECCV|WACV|BMVC|NeurIPS|NIPS|AAAI|IJCAI|"
            r"ICML|ICPR|IROS|ICRA|ICME|ISKE)[\s'’_-]*(\d{2})\b",
            combined,
            re.IGNORECASE,
        )
    year = 0
    if year_match:
        raw_year = int(year_match.group(1))
        year = raw_year if raw_year >= 2000 else 2000 + raw_year
    lowered = combined.casefold()
    if re.search(r"\b(submit(?:ted)? to|under review|possible publication|journal submission|preprint for)\b", lowered):
        status = "submission-only"
    elif journal_ref:
        status = "bibliographic-reference"
    elif re.search(
        r"\b(accepted|camera[- ]ready|published|proceedings|appearing|"
        r"presented|oral|poster)\b",
        lowered,
    ):
        status = "author-claimed-accepted"
    else:
        status = "venue-mentioned"
    source_field, evidence = next(
        (field, value)
        for field, value in fields
        if value and re.search(
            next(pattern for canonical, pattern in PUBLICATION_VENUE_PATTERNS if canonical == venue),
            value,
            re.IGNORECASE,
        )
    )
    return {
        "venue": venue,
        "year": year or None,
        "status": status,
        "source_field": source_field,
        "evidence": evidence,
    }


def claim_classification(claim: dict) -> tuple[str, str]:
    """Return publication type and tier for a non-submission venue claim."""
    if not claim or claim.get("status") == "submission-only":
        return "preprint", "Preprint"
    venue = claim["venue"]
    if venue in JOURNAL_CLAIM_VENUES:
        return "journal-claimed", "Journal"
    if venue in CORE_VENUES:
        return "conference-claimed", CORE_VENUES[venue]
    if "Workshop" in venue or venue in {"TAHRI", "LUV Workshop", "CVWW"}:
        return "conference-claimed", "Extended-Vision"
    return "conference-claimed", "Extended-Vision"


def parse_arxiv_entry(entry: ET.Element, cutoff_date: str) -> tuple[dict, dict]:
    title = _atom_text(entry, "atom:title")
    abstract = _atom_text(entry, "atom:summary")
    submitted = _atom_text(entry, "atom:published")[:10]
    updated = _atom_text(entry, "atom:updated")[:10]
    arxiv_id = _arxiv_id(entry)
    authors = [
        _atom_text(author, "atom:name")
        for author in entry.findall("atom:author", ATOM_NS)
    ]
    authors = [author for author in authors if author]
    direct, reason = arxiv_is_direct(title)
    in_cutoff = bool(submitted and submitted <= cutoff_date)
    decision = "include-pending-verification" if direct and in_cutoff else "candidate-only"
    if not in_cutoff:
        reason = f"first submitted after cutoff {cutoff_date}"
    if arxiv_id in ARXIV_SUPERSEDED_BY_FORMAL:
        decision = "candidate-only"
        reason = ARXIV_SUPERSEDED_BY_FORMAL[arxiv_id]
    comment = _atom_text(entry, "arxiv:comment")
    journal_ref = _atom_text(entry, "arxiv:journal_ref")
    doi = _atom_text(entry, "arxiv:doi")
    publication_claim = extract_publication_claim(comment, journal_ref)
    if publication_claim:
        publication_claim["verification"] = (
            "officially-verified"
            if arxiv_id in set(FORMAL_ARXIV_IDS.values())
            else "unverified-author-metadata"
        )
    candidate = {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "first_submitted": submitted,
        "last_updated": updated,
        "comment": comment,
        "journal_ref": journal_ref,
        "doi": doi,
        "publication_claim": publication_claim,
        "decision": decision,
        "decision_reason": reason,
        "verification_date": cutoff_date,
    }
    record = default_record(
        title=title,
        authors=authors,
        year=int(submitted[:4]),
        venue="Preprint",
        official_publication_url="",
        official_pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
        abstract=abstract,
    )
    record.update({
        "venue_tier": "Preprint",
        "publication_type": "preprint",
        "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}",
        "doi": doi,
        "metadata_verified": False,
        "verification_sources": [f"https://arxiv.org/abs/{arxiv_id}"],
        "verification_date": cutoff_date,
        "notes": (
            f"arXiv {arxiv_id}; first submitted {submitted}; last updated "
            f"{updated}; comment={comment or 'none'}; journal_ref="
            f"{journal_ref or 'none'}. No formal conference proceedings "
            f"placement has been verified."
        ),
        "needs_manual_review": True,
        "review_reason": (
            "Direct TAS arXiv hit; formal publication status requires "
            "first-party proceedings verification."
        ),
    })
    if publication_claim:
        record["publication_claim"] = publication_claim
        claimed = " ".join(
            str(value) for value in [
                publication_claim["venue"], publication_claim.get("year"),
            ] if value
        )
        if publication_claim["verification"] != "officially-verified":
            record["review_reason"] = (
                f"arXiv {publication_claim['source_field']} names {claimed} "
                f"({publication_claim['status']}); no matching first-party "
                "publication record has yet been attached."
            )
    infer_fields(record)
    for dataset in [
        "Breakfast", "50Salads", "GTEA", "Assembly101", "IKEA ASM",
        "COIN", "CrossTask", "Cholec80", "EgoExo4D", "CMU-MMAC",
        "CaptainCook4D", "PKU-MMD", "LARa",
    ]:
        if dataset.casefold() in abstract.casefold():
            record["datasets"].append(dataset)
    record["datasets"] = list(dict.fromkeys(record["datasets"]))
    # infer_fields does not alter publication/provenance status.
    record["venue"] = "Preprint"
    record["venue_tier"] = "Preprint"
    record["publication_type"] = "preprint"
    record["metadata_verified"] = False
    claimed_type, claimed_tier = claim_classification(publication_claim)
    if claimed_type != "preprint":
        claimed_year = publication_claim.get("year") or int(submitted[:4])
        record.update({
            "id": stable_id(claimed_year, publication_claim["venue"], title),
            "year": claimed_year,
            "venue": publication_claim["venue"],
            "venue_tier": claimed_tier,
            "publication_type": claimed_type,
            "notes": (
                f"arXiv {arxiv_id}; {publication_claim['source_field']} states "
                f"{publication_claim['evidence']}. Classified under "
                f"{publication_claim['venue']} rather than Preprint; official "
                "publication verification is still pending."
            ),
        })
    return record, candidate


def scan_arxiv(
    *, cutoff_date: str, dry_run: bool, cache_dir: Path,
    refresh: bool = False,
) -> tuple[list[dict], list[dict]]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    entries_by_id: dict[str, ET.Element] = {}
    for index, query in enumerate(ARXIV_QUERIES):
        params = {
            "search_query": query,
            "start": 0,
            "max_results": 300,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = f"{ARXIV_API}?{urlencode(params)}"
        cache_file = cache_dir / f"query_{index}.xml"
        try:
            if cache_file.exists() and not refresh:
                payload = cache_file.read_bytes()
            else:
                payload = request(url, timeout=45, retries=4, delay=2.0).content
                if not dry_run:
                    cache_file.write_bytes(payload)
                time.sleep(3.0)
            root = ET.fromstring(payload)
            entries = root.findall("atom:entry", ATOM_NS)
            for entry in entries:
                entries_by_id[_arxiv_id(entry)] = entry
            logging.info("[arXiv] query=%s returned=%s", query, len(entries))
        except Exception as exc:
            logging.warning("arXiv query failed %s: %s", query, exc)
    records: list[dict] = []
    candidates: list[dict] = []
    for arxiv_id, entry in entries_by_id.items():
        try:
            record, candidate = parse_arxiv_entry(entry, cutoff_date)
            candidates.append(candidate)
            if candidate["decision"] == "include-pending-verification":
                records.append(record)
        except Exception as exc:
            logging.warning("arXiv entry failed %s: %s", arxiv_id, exc)
    logging.info(
        "[arXiv] unique-candidates=%s direct-pending=%s",
        len(candidates), len(records),
    )
    return records, candidates


def verify_arxiv_claim_matches(
    candidates: list[dict], formal_records: list[dict],
) -> None:
    """Mark claims whose identity matches a first-party formal record."""
    formal_titles = {
        normalize_title(record["title"]) for record in formal_records
        if record.get("metadata_verified")
    }
    formal_dois = {
        record["doi"].casefold().strip() for record in formal_records
        if record.get("metadata_verified") and record.get("doi")
    }
    formal_arxiv_ids = set(FORMAL_ARXIV_IDS.values())
    for candidate in candidates:
        claim = candidate.get("publication_claim")
        if not claim:
            continue
        matched_by = ""
        if candidate["arxiv_id"] in formal_arxiv_ids:
            matched_by = "arxiv-id"
        elif candidate.get("doi", "").casefold().strip() in formal_dois:
            matched_by = "doi"
        elif normalize_title(candidate["title"]) in formal_titles:
            matched_by = "normalized-title"
        if matched_by:
            claim["verification"] = "officially-verified"
            claim["matched_by"] = matched_by


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2010)
    parser.add_argument("--end-year", type=int, default=2026)
    parser.add_argument("--venues", default="CVPR,ICCV,WACV")
    parser.add_argument("--cutoff-date", default=CUTOFF_DATE)
    parser.add_argument("--skip-arxiv", action="store_true")
    parser.add_argument("--refresh-arxiv", action="store_true")
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
    arxiv_records: list[dict] = []
    arxiv_candidates: list[dict] = []
    if not args.skip_arxiv:
        arxiv_records, arxiv_candidates = scan_arxiv(
            cutoff_date=args.cutoff_date,
            dry_run=args.dry_run,
            cache_dir=DATA.parent / ".cache" / "arxiv",
            refresh=args.refresh_arxiv,
        )
    existing = []
    papers_path = DATA / "papers.yaml"
    if papers_path.exists():
        existing = load_yaml(papers_path) or []
    # Remove previously discovered CVF false positives when the inclusion
    # rules are tightened; otherwise merge-only updates would preserve them.
    existing = [
        paper for paper in existing
        if not (
            "openaccess.thecvf.com" in paper.get("official_publication_url", "")
            and any(
                term in paper.get("title", "").casefold()
                for term in EXCLUSIONS
            )
        )
    ]
    # Rebuild API-managed preprints from the current auditable candidate set.
    # This lets rule fixes remove false positives without deleting hand-curated
    # or formally verified records.
    api_arxiv_ids = {item["arxiv_id"] for item in arxiv_candidates}
    api_existing_runtime: list[dict] = []
    if api_arxiv_ids:
        def is_api_preprint(paper: dict) -> bool:
            if paper.get("publication_type") not in {
                "preprint", "conference-claimed", "journal-claimed",
            }:
                return False
            match = re.search(r"(\d{4}\.\d{4,5})", paper.get("arxiv_url", ""))
            return bool(match and match.group(1) in api_arxiv_ids)
        included_arxiv_ids = {
            item["arxiv_id"] for item in arxiv_candidates
            if item["decision"] == "include-pending-verification"
        }
        api_existing_runtime = [
            paper for paper in existing
            if is_api_preprint(paper)
            and re.search(
                r"(\d{4}\.\d{4,5})", paper.get("arxiv_url", "")
            ).group(1) in included_arxiv_ids
        ]
        existing = [paper for paper in existing if not is_api_preprint(paper)]
    for paper in [*cvf_records, *FORMAL, *existing]:
        arxiv_id = FORMAL_ARXIV_IDS.get(paper.get("title", ""))
        if arxiv_id:
            paper["arxiv_url"] = f"https://arxiv.org/abs/{arxiv_id}"
    verify_arxiv_claim_matches(
        arxiv_candidates,
        [*cvf_records, *FORMAL, *existing],
    )
    records, duplicates = deduplicate([
        *cvf_records, *FORMAL, *PREPRINTS, *arxiv_records,
        *api_existing_runtime, *existing,
    ])
    logging.info(
        "[Search] discovered=%s official-CVF=%s curated-first-party=%s preprints=%s",
        len(records), len(cvf_records), len(FORMAL), len(PREPRINTS),
    )
    logging.info("[Deduplicate] merged=%s", len(duplicates))
    if not args.dry_run:
        dump_yaml(records, DATA / "candidates.yaml")
        dump_yaml(
            sorted(
                arxiv_candidates,
                key=lambda item: (item["first_submitted"], item["title"]),
                reverse=True,
            ),
            DATA / "arxiv_candidates.yaml",
        )
        save_serializations(records)
        with (LOGS / "duplicate_report.csv").open("w", encoding="utf-8", newline="") as handle:
            handle.write("kept_id,merged_id,rule,details\n")
            for kept, merged, rule in duplicates:
                handle.write(f"{kept},{merged},{rule},same normalized identity\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

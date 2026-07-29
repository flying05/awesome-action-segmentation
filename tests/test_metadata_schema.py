from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from _common import REQUIRED_FIELDS, VENUE_TIERS  # noqa: E402
from search_candidates import extract_publication_claim  # noqa: E402


def test_required_fields_and_tiers():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    assert papers
    for paper in papers:
        assert not (set(REQUIRED_FIELDS) - set(paper)), paper["id"]
        assert paper["venue_tier"] in VENUE_TIERS
        assert paper["title"] and paper["year"] and paper["venue"]


def test_formal_records_have_first_party_source():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    for paper in papers:
        if paper.get("metadata_verified") and paper["venue_tier"] != "Related-but-not-core":
            assert any(paper["verification_sources"]), paper["id"]
            assert paper["publication_type"] != "preprint"


def test_arxiv_audit_and_ego_metas_are_present():
    candidates = yaml.safe_load(
        (ROOT / "data" / "arxiv_candidates.yaml").read_text(encoding="utf-8")
    )
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    assert any(item["arxiv_id"] == "2606.02246" for item in candidates)
    ego = next(paper for paper in papers if "Ego-METAS" in paper["title"])
    assert ego["venue_tier"] == "Preprint"
    assert ego["arxiv_url"].endswith("2606.02246")
    assert ego["needs_manual_review"] is True


def test_arxiv_comment_publication_claims_are_structured():
    claim = extract_publication_claim(
        "16 pages, accepted to ECCV 2026", ""
    )
    assert claim["venue"] == "ECCV"
    assert claim["year"] == 2026
    assert claim["status"] == "author-claimed-accepted"

    submission = extract_publication_claim(
        "Submitted to Pattern Recognition", ""
    )
    assert submission["venue"] == "Pattern Recognition"
    assert submission["status"] == "submission-only"


def test_comment_claims_with_official_sources_are_promoted():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    expected = {
        "HOI-aware Adaptive Network for Weakly-supervised Action Segmentation": "IJCAI",
        "Stitch, Contrast, and Segment: Learning a Human Action Segmentation Model Using Trimmed Skeleton Videos": "AAAI",
        "Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment": "WACV",
        "Deep Kernel Video Approximation for Unsupervised Action Segmentation": "ICPR",
    }
    by_title = {paper["title"]: paper for paper in papers}
    for title, venue in expected.items():
        assert by_title[title]["venue"] == venue
        assert by_title[title]["venue_tier"] != "Preprint"
        assert by_title[title]["verification_sources"]


def test_unverified_venue_claims_are_not_classified_as_preprints():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    adaptive = next(
        paper for paper in papers
        if paper["title"].startswith("Adaptive Latent Trajectory Anchoring")
    )
    assert adaptive["venue"] == "ECCV"
    assert adaptive["venue_tier"] == "Top-Vision"
    assert adaptive["publication_type"] == "conference-claimed"
    assert adaptive["metadata_verified"] is False

    submitted = next(
        paper for paper in papers
        if paper["title"].startswith("MS-TCRNet")
    )
    assert submitted["venue"] == "Preprint"
    assert submitted["publication_type"] == "preprint"

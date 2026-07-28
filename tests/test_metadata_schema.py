from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from _common import REQUIRED_FIELDS, VENUE_TIERS  # noqa: E402


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
        if paper["venue_tier"] not in {"Preprint", "Related-but-not-core"}:
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

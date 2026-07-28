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


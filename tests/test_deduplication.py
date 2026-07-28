from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from _common import deduplicate, normalize_title  # noqa: E402


def test_title_normalization_and_deduplication():
    assert normalize_title("MS–TCN: Action") == normalize_title("ms-tcn action")
    base = {
        "id": "a", "title": "A Test—Paper", "doi": "", "arxiv_url": "",
        "metadata_verified": True, "venue_tier": "CCF-A",
    }
    duplicate = dict(base, id="b", title="A test paper")
    kept, report = deduplicate([base, duplicate])
    assert len(kept) == 1
    assert len(report) == 1


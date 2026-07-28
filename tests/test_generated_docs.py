from pathlib import Path
import json
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_serialization_counts_match():
    yaml_records = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    json_records = json.loads((ROOT / "data" / "papers.json").read_text(encoding="utf-8"))
    jsonl_records = [
        json.loads(line) for line in (ROOT / "data" / "papers.jsonl").read_text(encoding="utf-8").splitlines() if line
    ]
    assert len(yaml_records) == len(json_records) == len(jsonl_records)


def test_readme_count_and_doc_ids():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    formal = [p for p in papers if p["venue_tier"] not in {"Preprint", "Related-but-not-core"}]
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    count = int(re.search(r"\*\*Verified conference papers:\*\*\s*(\d+)", readme).group(1))
    assert count == len(formal)
    assert all(f'paper-{paper["id"]}' in readme for paper in papers)


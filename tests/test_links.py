from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_metadata_url_syntax():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    for paper in papers:
        for field in ["official_publication_url", "official_pdf_url", "arxiv_url", "code_url", "project_url"]:
            value = paper[field]
            if value:
                assert urlparse(value).scheme in {"http", "https"}, (paper["id"], field)


def test_readme_local_links_exist():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in [
        "CONTRIBUTING.md", "docs/survey_zh.md", "docs/history_timeline.md",
        "docs/taxonomy.md", "docs/datasets_and_metrics.md",
        "docs/search_methodology.md", "docs/verification_report.md",
    ]:
        assert relative in text
        assert (ROOT / relative).exists()


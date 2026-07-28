#!/usr/bin/env python3
"""Generate README.md from the canonical paper metadata."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

from _common import CUTOFF_DATE, ROOT, load_papers

SUPERVISION_ORDER = [
    ("fully-supervised", "Fully Supervised"),
    ("weakly-supervised", "Weakly Supervised"),
    ("timestamp-supervised", "Weakly Supervised"),
    ("transcript-supervised", "Weakly Supervised"),
    ("semi-supervised", "Semi-Supervised"),
    ("self-supervised", "Self-Supervised"),
    ("unsupervised", "Unsupervised"),
    ("few-shot", "Few-Shot and Zero-Shot"),
    ("zero-shot", "Few-Shot and Zero-Shot"),
    ("training-free", "Training-Free"),
]


def anchor(paper: dict) -> str:
    return f"paper-{paper['id']}"


def paper_entry(paper: dict) -> list[str]:
    authors = ", ".join(paper["authors"][:3])
    if len(paper["authors"]) > 3:
        authors += ", et al."
    links = []
    if paper["official_publication_url"]:
        links.append(f"[Paper]({paper['official_publication_url']})")
    if paper["official_pdf_url"]:
        links.append(f"[PDF]({paper['official_pdf_url']})")
    if paper["arxiv_url"]:
        links.append(f"[arXiv]({paper['arxiv_url']})")
    if paper["code_url"]:
        links.append(f"[Code]({paper['code_url']})")
    if paper["project_url"]:
        links.append(f"[Project]({paper['project_url']})")
    tags = paper["supervision"] + paper["method_family"][:2] + paper["modality"][:1] + paper["datasets"][:2]
    return [
        f'<a id="{anchor(paper)}"></a>',
        f"- **{paper['title']}** — {authors}, {paper['venue']} {paper['year']}.  ",
        f"  {' '.join(links)}  " if links else "  ",
        "  " + " ".join(f"`{tag}`" for tag in tags),
    ]


def primary_group(paper: dict) -> str:
    labels = paper.get("supervision", [])
    for key, heading in SUPERVISION_ORDER:
        if key in labels:
            return heading
    return "Fully Supervised"


def cross_index(papers: list[dict], field: str, headings: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = []
    for key, heading in headings:
        matches = [p for p in papers if key in p.get(field, [])]
        lines.append(f"### {heading}\n")
        if matches:
            lines.extend(
                f"- [{p['title']}](#{anchor(p)})" for p in sorted(matches, key=lambda p: (-p["year"], p["title"]))
            )
        else:
            lines.append("- _No verified paper in the current snapshot._")
        lines.append("")
    return lines


def render() -> str:
    papers = load_papers()
    formal = [p for p in papers if p["venue_tier"] not in {"Preprint", "Related-but-not-core"}]
    preprints = [p for p in papers if p["venue_tier"] == "Preprint"]
    related = [p for p in papers if p["venue_tier"] == "Related-but-not-core"]
    venues = Counter(p["venue"] for p in formal)
    years = Counter(p["year"] for p in formal)
    lines = [
        "# Awesome Action Segmentation",
        "",
        "一个经过一手来源核验、可重复生成的 Temporal Action Segmentation（TAS）论文与资料索引。"
        "TAS 在长视频、骨架或多模态序列上预测逐帧/逐时间步动作类别，并同时确定连续动作片段的边界。",
        "",
        f"**Data cutoff:** {CUTOFF_DATE}  ",
        f"**Verified conference papers:** {len(formal)}  ",
        f"**Preprints / pending verification:** {len(preprints)}  ",
        f"**Related benchmark or boundary papers:** {len(related)}",
        "",
        "## Scope and inclusion criteria",
        "",
        "纳入的核心工作必须输出稠密动作标签或连续动作片段，并以帧准确率、MoF、Edit、segmental F1、"
        "mIoU 或动作边界指标进行评价。仅做整段动作识别、proposal、时序动作定位、时空框检测、"
        "图像/人体空间分割或无动作语义的章节切分不进入核心列表。每条正式记录至少保留一个会议"
        "proceedings、学会数字图书馆或正式论文页作为验证来源。",
        "",
        "会议范围包括 CVPR、ICCV、NeurIPS、ICML、AAAI、IJCAI、ACM MM，以及 ECCV、WACV、"
        "BMVC；与 TAS 直接相关的 MICCAI、IROS 等工作置于扩展类别。2026 年只收录在截点前已能"
        "由正式 proceedings 确认的论文。arXiv-only 工作严格置于独立的 Pending Verification 区。",
        "",
        "## Statistics",
        "",
        "| View | Counts |",
        "|---|---|",
        f"| By venue | {'; '.join(f'{k}: {v}' for k, v in sorted(venues.items()))} |",
        f"| By year | {'; '.join(f'{k}: {v}' for k, v in sorted(years.items(), reverse=True))} |",
        "",
        "## Paper index by supervision",
        "",
        "这是唯一完整主索引；后面的技术路线和应用场景索引只链接到此处，避免重复维护同一条目。",
        "",
    ]
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in formal:
        grouped[primary_group(paper)].append(paper)
    headings = [h for _, h in SUPERVISION_ORDER]
    for heading in dict.fromkeys(headings):
        lines.append(f"### {heading}\n")
        for paper in sorted(grouped.get(heading, []), key=lambda p: (-p["year"], p["venue"], p["title"])):
            lines.extend(paper_entry(paper))
        if not grouped.get(heading):
            lines.append("- _No verified paper in the current snapshot._")
        lines.append("")

    lines.extend(["## Cross-index by technical route", ""])
    lines.extend(cross_index(formal, "method_family", [
        ("TCN", "TCN and Multi-Stage Refinement"),
        ("Transformer", "Transformer and Cross-Attention"),
        ("diffusion", "Diffusion Models"),
        ("optimal-transport", "Optimal Transport"),
        ("clustering", "Clustering and Prototype Learning"),
        ("boundary-modeling", "Boundary and Duration Modeling"),
        ("structured-decoding", "Structured Decoding"),
        ("VQ-tokenization", "Action Tokenization and VQ"),
        ("vision-language-model", "Vision-Language and Open Vocabulary"),
        ("causal-model", "Online and Streaming"),
        ("dataset-condensation", "Efficient and Long-Video Methods"),
    ]))
    lines.extend(["## Cross-index by application", ""])
    lines.extend(cross_index(formal, "setting", [
        ("exocentric", "General RGB Video"),
        ("egocentric", "Egocentric Video"),
        ("surgical", "Surgical Workflow"),
        ("multi-view", "Assembly and Manufacturing"),
        ("embodied", "Robotics and Embodied Agents"),
        ("streaming", "Online and Streaming"),
    ]))
    lines.extend(["## Preprints / Pending Verification", ""])
    for paper in sorted(preprints, key=lambda p: (-p["year"], p["title"])):
        lines.extend(paper_entry(paper))
        lines.append(f"  _Status:_ {paper['notes']}")
    if not preprints:
        lines.append("- None.")
    lines.extend(["", "## Related-but-not-core", ""])
    for paper in sorted(related, key=lambda p: (-p["year"], p["title"])):
        lines.extend(paper_entry(paper))
        lines.append(f"  _Why related:_ {paper['inclusion_reason']}")
    lines.extend([
        "",
        "## Documentation",
        "",
        "- [中文系统综述](docs/survey_zh.md)",
        "- [历史时间线](docs/history_timeline.md)",
        "- [任务分类体系](docs/taxonomy.md)",
        "- [数据集与指标](docs/datasets_and_metrics.md)",
        "- [检索方法](docs/search_methodology.md)",
        "- [验证报告](docs/verification_report.md)",
        "",
        "## Updating and reporting errors",
        "",
        "完整更新：`python scripts/update_repository.py --cutoff-date 2026-07-28`。"
        "跳过 PDF：追加 `--skip-download`；联网前预演：追加 `--dry-run`。"
        "若发现遗漏、误收或失效链接，请按 [CONTRIBUTING.md](CONTRIBUTING.md) 提供标题、"
        "任务输出、实验数据集/指标和一手发表来源。",
        "",
        "PDF 仅保存在本地 `library/pdfs/`，默认被 Git 忽略；仓库不创建远程、不上传 PDF。",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    text = render()
    if args.dry_run:
        print(text[:1000])
    else:
        (ROOT / "README.md").write_text(text, encoding="utf-8", newline="\n")
        print(f"[README] generated papers={len(load_papers())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


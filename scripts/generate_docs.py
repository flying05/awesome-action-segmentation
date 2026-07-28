#!/usr/bin/env python3
"""Generate timeline, category indexes, dataset notes and verification report."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict

import yaml

from _common import DATA, DOCS, LOGS, ROOT, load_papers

CATEGORY_DOCS = {
    "supervised_action_segmentation.md": (
        "监督式动作分割", {"fully-supervised"},
        "密集帧标注允许模型直接学习类别与边界，但标签成本高，且容易继承数据集的粒度偏置。"
        "主要路线从 Encoder–Decoder TCN、MS-TCN 迭代细化发展到 Transformer、"
        "帧—动作双表示、扩散解码与显式结构约束。"
    ),
    "weakly_supervised_action_segmentation.md": (
        "弱监督动作分割", {"weakly-supervised", "timestamp-supervised", "transcript-supervised"},
        "监督信号可以是 transcript、动作集合或每段一个时间戳。核心困难不是生成任意伪标签，"
        "而是控制确认偏差、处理漏标短动作，并在跨视频动作顺序变化时保持一致。"
    ),
    "unsupervised_action_segmentation.md": (
        "无监督动作分割", {"unsupervised", "self-supervised"},
        "表示学习必须把外观差异与动作语义分开；聚类还需兼顾 temporal consistency、动作顺序、"
        "背景与重复动作。balanced OT 会错误强迫等量簇，unbalanced OT 更能容忍时长和缺失差异；"
        "Gromov–Wasserstein 可编码帧—帧与类—类结构。伪标签反馈环会放大早期错误，闭环细化、"
        "不确定性估计和多层动作 token 是缓解方向。未知类别数仍是根本难题；Hungarian matching "
        "只解决标签置换后的评估对齐，并不证明聚类得到的人类语义类别正确。"
    ),
    "online_and_streaming.md": (
        "在线与流式动作分割", {"fully-supervised", "weakly-supervised"},
        "在线系统只能使用当前与过去帧，因此离线双向上下文的精度不可直接比较。除 Edit/F1 外，"
        "应报告因果延迟、吞吐、峰值显存和状态缓存。"
    ),
    "open_vocabulary_and_generalization.md": (
        "开放词汇与泛化", {"few-shot", "zero-shot"},
        "需要区分 unseen task、unseen view 与 unseen action。视觉语言原型能命名动作，"
        "但文本相似不等同于正确的程序顺序；discover-then-name 还需独立评估发现和命名误差。"
    ),
    "skeleton_action_segmentation.md": (
        "骨架动作分割", {"unsupervised", "fully-supervised"},
        "骨架降低外观干扰，却带来关节噪声、跨视角坐标差异和相似微动作边界模糊。"
        "图卷积、运动词/token 与跨主体对齐是主要路线。"
    ),
    "surgical_workflow_segmentation.md": (
        "手术工作流分割", {"fully-supervised"},
        "手术 phase/step 序列具有强流程先验，但设备、术式与医院域偏移显著。"
        "通用 TAS 指标应与临床阶段 Jaccard、延迟和安全相关错误分开报告。"
    ),
    "embodied_and_multimodal.md": (
        "具身与多模态动作分割", {"fully-supervised", "timestamp-supervised"},
        "RGB、音频、IMU、深度和 gaze 的采样率与缺失机制不同。融合模型不仅要提升平均分，"
        "还应说明传感器失效时的退化，以及在线机器人系统的因果约束。"
    ),
    "efficient_and_long_video.md": (
        "高效与长视频方法", {"fully-supervised"},
        "长视频的主要瓶颈是特征提取、二次注意力和多阶段反复推理。"
        "除 FLOPs 外还应报告实际延迟、峰值显存、特征缓存与能耗。"
    ),
}


def paper_link(paper: dict) -> str:
    url = paper["official_publication_url"] or paper["arxiv_url"]
    return f"[{paper['title']}]({url})"


def write_timeline(papers: list[dict]) -> None:
    formal = [p for p in papers if p["venue_tier"] != "Preprint"]
    lines = ["# History Timeline", ""]
    by_year: dict[int, list[dict]] = defaultdict(list)
    for p in formal:
        by_year[p["year"]].append(p)
    for year in sorted(by_year, reverse=True):
        lines.append(f"## {year}\n")
        by_venue: dict[str, list[dict]] = defaultdict(list)
        for p in by_year[year]:
            by_venue[p["venue"]].append(p)
        for venue in sorted(by_venue):
            lines.append(f"### {venue}\n")
            for p in sorted(by_venue[venue], key=lambda x: x["title"]):
                contribution = p["main_contributions"][0] if p["main_contributions"] else p["inclusion_reason"]
                lines.append(f"- {paper_link(p)} — {contribution}")
            lines.append("")
    year_counts = Counter(p["year"] for p in formal)
    venue_counts = Counter(p["venue"] for p in formal)
    supervision = Counter(s for p in formal for s in p["supervision"])
    dataset_counts = Counter(d for p in formal for d in p["datasets"])
    first_family: dict[str, int] = {}
    for p in sorted(formal, key=lambda x: x["year"]):
        for family in p["method_family"]:
            first_family.setdefault(family, p["year"])
    lines.extend([
        "## Statistics",
        "",
        "| Dimension | Counts / first year |",
        "|---|---|",
        f"| Papers per year | {'; '.join(f'{k}: {v}' for k, v in sorted(year_counts.items()))} |",
        f"| Papers per venue | {'; '.join(f'{k}: {v}' for k, v in sorted(venue_counts.items()))} |",
        f"| Supervision | {'; '.join(f'{k}: {v}' for k, v in sorted(supervision.items()))} |",
        f"| First observed method-family year | {'; '.join(f'{k}: {v}' for k, v in sorted(first_family.items()))} |",
        f"| Dataset mentions | {'; '.join(f'{k}: {v}' for k, v in dataset_counts.most_common()) or 'Metadata incomplete'} |",
        "",
    ])
    (DOCS / "history_timeline.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_taxonomy() -> None:
    text = r"""# Taxonomy

## Task axis

- Dense temporal action segmentation: output \(y_{1:T}\) for input \(x_{1:T}\).
- Procedural/step segmentation: segments are semantic steps in a goal-directed procedure.
- Boundary-aware segmentation: jointly estimates labels and transition likelihood.
- Online/streaming segmentation: prediction at time \(t\) cannot use future observations.
- Discovery: action identities and sometimes the number of classes are latent.

## Supervision axis

Fully supervised uses frame labels; transcript supervision gives ordered actions without boundaries;
set supervision removes ordering; timestamp supervision labels sparse frames; semi-supervised mixes
dense labeled and unlabeled videos; unsupervised methods rely on representation, clustering or optimal
transport. Few/zero-shot settings must state whether tasks, views, or actions are unseen.

## Method axis

TCN and multi-stage refinement; Transformer/cross-attention; diffusion; optimal transport; clustering
and prototypes; boundary/duration modeling; structured decoding; action tokenization; vision-language
models; causal online models; data condensation and efficient long-video inference.

## Task boundary

Temporal localization returns sparse intervals and may leave background uncovered; TAS assigns a label
densely. Action recognition predicts one clip label. Spatio-temporal detection and image/person/hand
segmentation are spatial tasks. Borderline benchmark and representation papers are marked
`Related-but-not-core`, not silently mixed into the core method count.
"""
    (DOCS / "taxonomy.md").write_text(text, encoding="utf-8", newline="\n")


def write_datasets() -> None:
    datasets = yaml.safe_load((DATA / "datasets.yaml").read_text(encoding="utf-8"))
    lines = [
        "# Datasets and Metrics", "",
        "数字采用数据集官方页或原始论文口径；当不同粒度/预处理协议产生不同数字时，不把其中一个写成唯一事实。",
        "",
        "## Datasets", "",
    ]
    for d in datasets:
        lines.extend([
            f"### {d['name']}", "",
            f"- Domain / modality / view: {d['domain']}; {d['modality']}; {d['view']}",
            f"- Scale: {d['number_of_videos']} videos; {d['number_of_actions']} actions; {d['average_video_length']}",
            f"- Annotation: {d['annotation_type']}",
            f"- Splits: {d['commonly_used_splits']}",
            f"- Metrics: {', '.join(d['common_metrics'])}",
            f"- [Official source]({d['official_url']})",
            f"- Notes: {d['notes']}",
            "",
        ])
    lines.extend([
        "## Metrics", "",
        "- **MoF / Frame Accuracy**：正确帧比例；长动作占比高时会掩盖短动作遗漏和过分割。",
        "- **Edit Score**：先压缩连续重复标签，再用归一化 Levenshtein 距离衡量动作序列；关注顺序而弱化精确边界。",
        "- **F1@10/25/50**：按时序 IoU 阈值匹配预测段和真值段，对重复碎片计假阳性，因此能揭示过分割。",
        "- **mIoU / Jaccard**：类别或片段交并比；必须注明宏/微平均和背景处理。",
        "- **Boundary precision/recall**：在容忍窗口内匹配转换点；窗口大小会显著改变结论。",
        "- **Online latency**：需与吞吐、因果缓冲长度、峰值显存一起报告。",
        "- **Efficiency**：FLOPs 不包含所有 I/O 与特征提取成本，建议同时给 wall-clock、显存和能耗。",
        "",
        "只看帧准确率时，把一个长动作预测正确可以抵消大量短动作错误；把同一动作切成多个碎片也可能几乎不改变"
        "正确帧数。因此 TAS 至少应联合报告 Frame Accuracy、Edit 和多个阈值的 segmental F1。",
        "",
    ])
    (DOCS / "datasets_and_metrics.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_categories(papers: list[dict]) -> None:
    for filename, (title, labels, overview) in CATEGORY_DOCS.items():
        selected = [p for p in papers if labels.intersection(p["supervision"])]
        if "skeleton" in filename:
            selected = [p for p in papers if "skeleton" in " ".join(p["modality"]).casefold() or "skeleton" in p["title"].casefold()]
        elif "surgical" in filename:
            selected = [p for p in papers if "surgical" in p["setting"]]
        elif "online" in filename:
            selected = [p for p in papers if {"online", "streaming"}.intersection(p["setting"])]
        elif "open_vocabulary" in filename:
            selected = [p for p in papers if {"few-shot", "zero-shot"}.intersection(p["supervision"]) or "open-vocabulary" in p["setting"]]
        lines = [
            f"# {title}", "", "## 任务定义与关键困难", "", overview, "",
            "## 方法演化与比较", "",
            "不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；"
            "要区分表征增益、解码先验和额外监督带来的收益。", "",
            "## 常用数据集与指标", "",
            "通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、"
            "Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。", "",
            "## 代表论文索引", "",
        ]
        for p in sorted(selected, key=lambda x: (-x["year"], x["title"])):
            lines.append(f"- {paper_link(p)} — {p['venue']} {p['year']}; `{', '.join(p['method_family'])}`")
        lines.extend([
            "", "## 未解决问题", "",
            "短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、"
            "新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。", "",
        ])
        (DOCS / filename).write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_methodology() -> None:
    text = """# Search Methodology

## Scope and cutoff

Cutoff: 2026-07-28. Core venue/year scans cover CVPR, ICCV and WACV official CVF indexes from
2010 (or the first available electronic index) through 2026. ECCV, BMVC, NeurIPS, AAAI and IJCAI
records are verified against ECVA/BMVC/NeurIPS/OpenReview/AAAI/IJCAI first-party pages. Extended
MICCAI and IROS records are kept separate.

## Four complementary searches

1. Keyword combinations in `data/search_queries.yaml`.
2. Official proceedings title scans by venue and year.
3. Live arXiv Atom API searches for exact TAS/action-segmentation/action-parsing phrases. Results are
   deduplicated by arXiv ID, filtered by first-submission cutoff, and written to
   `data/arxiv_candidates.yaml` with an inclusion or exclusion reason. Direct title matches enter
   `Preprints / Pending Verification`; ambiguous hits stay in the candidate audit log.
4. Backward, forward and author snowballing from MS-TCN, ASFormer, DiffAct, FACT, ASOT and the TAS survey.
5. Reverse searches from Breakfast, 50Salads, GTEA, Assembly101, COIN, CrossTask and surgical datasets.

Discovery indexes and search engines are candidate generators only. A formal record requires a first-party
proceedings or society page. arXiv-only records remain `Preprint` even when an author claims acceptance,
until the claim is independently verifiable. Every candidate is judged from title, abstract, output form,
datasets and metrics; keyword coincidence alone is insufficient.

## Known retrieval limitations

CVF changed URL layouts before 2020, and some old WACV indexes return 404; known official PDF/detail URLs
are therefore used as explicit seeds. arXiv and publisher endpoints can rate-limit automated access, so
successful Atom responses are cached and a failed refresh never erases the last candidate audit. ACM and
Springer can also rate-limit automated access. Failed checks are retained in CSV logs and never converted
into invented metadata. The update pipeline rebuilds API-managed preprints from the current candidate set
while merging formally verified records, so transient network failures cannot delete verified publications
and rule corrections can remove false-positive preprints.
"""
    (DOCS / "search_methodology.md").write_text(text, encoding="utf-8", newline="\n")


def write_unresolved() -> None:
    text = r"""# Unresolved Problems

- 长视频计算：需要端到端包含特征提取的延迟、显存与能耗报告。
- 短动作和边界保持：平滑损失与粗采样容易抹掉短段。
- 粒度歧义：同一过程可按 phase、step、手部动作或对象状态标注。
- 未知类别数和层次状态：固定 \(K\) 的聚类并不等于开放世界发现。
- 伪标签确认偏差与跨视频语义对齐。
- 新任务、新视角、新动作的分解式泛化评估。
- discover-then-name：发现质量与语言命名质量必须分别测量。
- 在线因果推理、多模态传感器选择与缺失模态鲁棒性。
- TAS 与世界模型：动作 token 是否对应可预测、可干预的状态变化仍需验证。
- benchmark 饱和、特征泄漏和数据集偏置。
- 大模型特征是否真正理解程序顺序，还是利用场景与对象共现捷径。

这些是跨论文归纳出的研究问题，不代表已经证实的统一结论。
"""
    (DOCS / "unresolved_problems.md").write_text(text, encoding="utf-8", newline="\n")


def write_verification(papers: list[dict]) -> None:
    formal = [p for p in papers if p["venue_tier"] not in {"Preprint", "Related-but-not-core"}]
    extended = [p for p in formal if p["venue_tier"] in {"Extended-Vision", "Medical", "Robotics-Embodied"}]
    preprints = [p for p in papers if p["venue_tier"] == "Preprint"]
    related = [p for p in papers if p["venue_tier"] == "Related-but-not-core"]
    manifest = []
    manifest_path = ROOT / "library" / "pdf_manifest.csv"
    if manifest_path.exists():
        with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
            manifest = list(csv.DictReader(handle))
    downloaded = sum(1 for p in papers if p.get("pdf_downloaded"))
    failures = sum(1 for row in manifest if row.get("status") == "failed")
    manual = sum(1 for p in papers if p.get("needs_manual_review"))
    arxiv_candidates = []
    arxiv_path = DATA / "arxiv_candidates.yaml"
    if arxiv_path.exists():
        arxiv_candidates = yaml.safe_load(arxiv_path.read_text(encoding="utf-8")) or []
    arxiv_included = sum(
        1 for item in arxiv_candidates
        if item.get("decision") == "include-pending-verification"
    )
    arxiv_candidate_only = len(arxiv_candidates) - arxiv_included
    duplicates = 0
    dup_path = LOGS / "duplicate_report.csv"
    if dup_path.exists():
        with dup_path.open(encoding="utf-8-sig", newline="") as handle:
            duplicates = max(0, sum(1 for _ in handle) - 1)
    by_venue = Counter(p["venue"] for p in formal)
    by_year = Counter(p["year"] for p in formal)
    lines = [
        "# Verification Report", "",
        "| Item | Count |", "|---|---:|",
        f"| Candidate records | {len(papers)} |",
        f"| Verified formal core + extension | {len(formal)} |",
        f"| Extended venue papers | {len(extended)} |",
        f"| Preprints / pending verification | {len(preprints)} |",
        f"| Related-but-not-core / excluded from core count | {len(related)} |",
        f"| Duplicate records merged in last report | {duplicates} |",
        f"| PDFs downloaded and parsed | {downloaded} |",
        f"| PDF download failures in manifest | {failures} |",
        f"| Papers requiring manual review | {manual} |", "",
        f"| arXiv API unique candidates audited | {len(arxiv_candidates)} |",
        f"| arXiv direct TAS hits before deduplication | {arxiv_included} |",
        f"| arXiv ambiguous/excluded candidates retained in audit | {arxiv_candidate_only} |", "",
        "## Venue and year statistics", "",
        f"- Venues: {'; '.join(f'{k}: {v}' for k, v in sorted(by_venue.items()))}",
        f"- Years: {'; '.join(f'{k}: {v}' for k, v in sorted(by_year.items()))}", "",
        "## Verification rules", "",
        "正式记录必须有一手来源；预印本不进入正式计数。验证失败不会中止流水线，也不会伪造本地路径。"
        "PDF 存在时会重新计算 SHA256 并尝试解析。截止日期后的记录不得进入正式结果。", "",
        "## Remaining possible omissions", "",
        "- 旧版 ACM MM、BMVC 和 WACV 搜索界面的全文召回可能不完整。",
        "- 标题不含 segmentation、但摘要定义了逐帧程序解析的工作仍可能漏检。",
        "- MICCAI 手术 phase/step 工作数量很大，本快照仅收录直接采用 TAS 式密集工作流建模的代表项。",
        "- 2026 ECCV/AAAI/IJCAI 等只有在截点前可由官方 proceedings 确认时才应加入；"
        "本报告不把录用传闻当作正式发表。",
        "",
        "Retry: `python scripts/update_repository.py --cutoff-date 2026-07-28 "
        "--only-unverified --retry-failures`。", "",
    ]
    (DOCS / "verification_report.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    papers = load_papers()
    if args.dry_run:
        print(f"[Docs dry-run] papers={len(papers)}")
        return 0
    DOCS.mkdir(parents=True, exist_ok=True)
    write_timeline(papers)
    write_taxonomy()
    write_datasets()
    write_categories(papers)
    write_methodology()
    write_unresolved()
    write_verification(papers)
    print(f"[Docs] generated papers={len(papers)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Curated non-CVF records and preprints.

Every formal record below uses an official proceedings or society page as its
verification source. CVF records are discovered directly from CVF indexes by
search_candidates.py.
"""

from __future__ import annotations

from _common import CUTOFF_DATE, default_record, infer_fields


def _paper(
    title: str,
    authors: str,
    year: int,
    venue: str,
    page: str,
    pdf: str = "",
    supervision: str = "",
    family: str = "",
    code: str = "",
) -> dict:
    record = default_record(
        title=title,
        authors=[a.strip() for a in authors.split(";")],
        year=year,
        venue=venue,
        official_publication_url=page,
        official_pdf_url=pdf,
    )
    infer_fields(record)
    if supervision:
        record["supervision"] = [supervision]
    if family:
        record["method_family"] = family.split(",")
    record["code_url"] = code
    record["verification_sources"] = [page]
    return record


FORMAL = [
    _paper(
        "Connectionist Temporal Modeling for Weakly Supervised Action Labeling",
        "De-An Huang; Fei-Fei Li; Juan Carlos Niebles", 2016, "ECCV",
        "https://www.ecva.net/papers/eccv_2016/papers_ECCV/html/Huang_Connectionist_Temporal_Modeling_ECCV_2016_paper.php",
        "https://www.ecva.net/papers/eccv_2016/papers_ECCV/papers/123560511.pdf",
        "weakly-supervised", "TCN,structured-decoding",
    ),
    _paper(
        "Fast Weakly Supervised Action Segmentation Using Mutual Consistency",
        "Yaser Souri; Mohsen Fayyaz; Luca Minciullo; Gianpiero Francesca; Juergen Gall",
        2020, "ECCV",
        "https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1061_ECCV_2020_paper.php",
        "https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123570664.pdf",
        "weakly-supervised", "TCN,structured-decoding",
        "https://github.com/yassersouri/MuCon",
    ),
    _paper(
        "Boundary-Aware Cascade Networks for Temporal Action Segmentation",
        "Zhenzhi Wang; Ziteng Gao; Limin Wang; Zhifeng Li; Gangshan Wu", 2020, "ECCV",
        "https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/35_ECCV_2020_paper.php",
        "https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123700035.pdf",
        "fully-supervised", "TCN,boundary-modeling",
        "https://github.com/MCG-NJU/BCN",
    ),
    _paper(
        "Temporal Aggregate Representations for Long-Range Video Understanding",
        "Fadime Sener; Dipika Singhania; Angela Yao", 2020, "ECCV",
        "https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/154_ECCV_2020_paper.php",
        "https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610154.pdf",
        "fully-supervised", "TCN",
    ),
    _paper(
        "A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation",
        "Rahul Rahaman; Dipika Singhania; Alexandre Thiery; Angela Yao", 2022, "ECCV",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4788_ECCV_2022_paper.php",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136640276.pdf",
        "timestamp-supervised", "TCN,uncertainty-modeling",
        "https://github.com/rahulrahaman/Timestamp-and-SkipTag",
    ),
    _paper(
        "Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation",
        "Nadine Behrmann; S. Alireza Golestaneh; Zico Kolter; Juergen Gall; Mehdi Noroozi",
        2022, "ECCV",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3672_ECCV_2022_paper.php",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950052.pdf",
        "timestamp-supervised", "Transformer,structured-decoding,duration-modeling",
    ),
    _paper(
        "Leveraging Action Affinity and Continuity for Semi-Supervised Temporal Action Segmentation",
        "Guodong Ding; Angela Yao", 2022, "ECCV",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3254_ECCV_2022_paper.php",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950017.pdf",
        "semi-supervised", "contrastive-learning,boundary-modeling",
        "https://github.com/dinggd/semitas",
    ),
    _paper(
        "My View Is the Best View: Procedure Learning from Egocentric Videos",
        "Siddhant Bansal; Chetan Arora; C. V. Jawahar", 2022, "ECCV",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1910_ECCV_2022_paper.php",
        "https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136730656.pdf",
        "unsupervised", "clustering,contrastive-learning",
        "https://sid2697.github.io/egoprocel",
    ),
    _paper(
        "ASFormer: Transformer for Action Segmentation",
        "Fangqiu Yi; Hongyu Wen; Tingting Jiang", 2021, "BMVC",
        "https://www.bmvc2021-virtualconference.com/conference/papers/paper_0578.html",
        "https://www.bmvc2021-virtualconference.com/assets/papers/0578.pdf",
        "fully-supervised", "Transformer",
        "https://github.com/ChinaYi/ASFormer",
    ),
    _paper(
        "Robust Action Segmentation from Timestamp Supervision",
        "Yaser Souri; Yazan Abu Farha; Emad Bahrami; Gianpiero Francesca; Juergen Gall",
        2022, "BMVC", "https://bmvc2022.mpi-inf.mpg.de/392/",
        "https://bmvc2022.mpi-inf.mpg.de/0392.pdf",
        "timestamp-supervised", "TCN,boundary-modeling",
    ),
    _paper(
        "Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation",
        "Ziwei Xu; Yogesh S. Rawat; Yongkang Wong; Mohan S. Kankanhalli; Mubarak Shah",
        2022, "NeurIPS", "https://openreview.net/forum?id=PCQyUvAmKs",
        "https://openreview.net/pdf?id=PCQyUvAmKs",
        "fully-supervised", "structured-decoding",
        "https://diff-tl.github.io/",
    ),
    _paper(
        "Activity Grammars for Temporal Action Segmentation",
        "Dayoung Gong; Joonseok Lee; Deunsol Jung; Suha Kwak; Minsu Cho",
        2023, "NeurIPS",
        "https://papers.nips.cc/paper_files/paper/2023/hash/ee6c4b99b4c0d3d60efd22c1ecdd9891-Abstract-Conference.html",
        "https://papers.nips.cc/paper_files/paper/2023/file/ee6c4b99b4c0d3d60efd22c1ecdd9891-Paper-Conference.pdf",
        "fully-supervised", "structured-decoding",
        "http://cvlab.postech.ac.kr/research/KARI",
    ),
    _paper(
        "OnlineTAS: An Online Baseline for Temporal Action Segmentation",
        "Shijie Li; Yazan Abu Farha; Juergen Gall", 2024, "NeurIPS",
        "https://papers.nips.cc/paper_files/paper/2024/hash/6c6c5fccf3c8661fcae219be7ca226f7-Abstract-Conference.html",
        "https://papers.nips.cc/paper_files/paper/2024/file/6c6c5fccf3c8661fcae219be7ca226f7-Paper-Conference.pdf",
        "fully-supervised", "TCN,causal-model",
    ),
    _paper(
        "Uncertainty-Aware Representation Learning for Action Segmentation",
        "Lei Chen; Muheng Li; Yueqi Duan; Jie Zhou; Jiwen Lu", 2022, "IJCAI",
        "https://www.ijcai.org/proceedings/2022/115",
        "https://www.ijcai.org/proceedings/2022/0115.pdf",
        "fully-supervised", "uncertainty-modeling,boundary-modeling",
    ),
    _paper(
        "Timestamp-Supervised Action Segmentation in the Perspective of Clustering",
        "Dazhao Du; Enhan Li; Lingyu Si; Fanjiang Xu; Fuchun Sun", 2023, "IJCAI",
        "https://www.ijcai.org/proceedings/2023/77",
        "https://www.ijcai.org/proceedings/2023/0077.pdf",
        "timestamp-supervised", "clustering,prototype-learning",
        "https://github.com/ddz16/TSASPC",
    ),
    _paper(
        "Iterative Contrast-Classify for Semi-Supervised Temporal Action Segmentation",
        "Dipika Singhania; Rahul Rahaman; Angela Yao", 2022, "AAAI",
        "https://ojs.aaai.org/index.php/AAAI/article/view/20124",
        "https://ojs.aaai.org/index.php/AAAI/article/download/20124/19883",
        "semi-supervised", "contrastive-learning,clustering",
        "https://github.com/dipika-singhania/ICC-Semi-Supervised-TAS",
    ),
    _paper(
        "TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks",
        "Tobias Czempiel; Magdalini Paschali; Matthias Keicher; Seong Tae Kim; Benjamin Busam; Nassir Navab",
        2020, "MICCAI",
        "https://link.springer.com/chapter/10.1007/978-3-030-59716-0_33",
        "", "fully-supervised", "multi-stage-TCN",
        "https://github.com/tobiascz/MICCAI2020-TeCNO",
    ),
    _paper(
        "Timestamp-Supervised Action Segmentation with Graph Convolutional Networks",
        "Hamza Khan; Sanjay Haresh; Awais Ahmed; Shakeeb Siddiqui; Andrey Konin; M. Zeeshan Zia; Quoc-Huy Tran",
        2022, "IROS",
        "https://doi.org/10.1109/IROS47612.2022.9981176",
        "https://arxiv.org/pdf/2206.15031",
        "timestamp-supervised", "graphical-model,TCN",
    ),
]

for record in FORMAL:
    if record["venue"] == "MICCAI":
        record["venue_tier"] = "Medical"
        record["setting"] = ["offline", "surgical", "long-video"]
        record["task_categories"] = ["Surgical Workflow / Phase Segmentation"]
        record["datasets"] = ["Cholec80"]
        record["inclusion_reason"] = (
            "The method assigns a surgical workflow phase to every video frame; "
            "it is included in the separate medical extension."
        )
    elif record["venue"] == "IROS":
        record["venue_tier"] = "Robotics-Embodied"
        record["setting"] = ["offline", "embodied", "long-video"]


def _preprint(
    title: str, authors: str, year: int, arxiv_id: str, submitted: str,
    updated: str, supervision: str, family: str,
) -> dict:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    record = default_record(
        title=title, authors=[a.strip() for a in authors.split(";")],
        year=year, venue="Preprint", official_publication_url="",
        official_pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
    )
    record.update({
        "venue_tier": "Preprint",
        "publication_type": "preprint",
        "arxiv_url": url,
        "supervision": [supervision],
        "method_family": family.split(","),
        "metadata_verified": False,
        "verification_sources": [url],
        "notes": (
            f"arXiv {arxiv_id}; first submitted {submitted}; last update "
            f"{updated}; no formal proceedings placement verified by "
            f"{CUTOFF_DATE}."
        ),
        "needs_manual_review": True,
        "review_reason": "No formal conference proceedings placement verified.",
    })
    return record


PREPRINTS = [
    _preprint(
        "Coarse to Fine Multi-Resolution Temporal Convolutional Network",
        "Dipika Singhania; Rahul Rahaman; Angela Yao", 2021, "2105.10859",
        "2021-05-23", "2021-05-23", "fully-supervised", "TCN",
    ),
    _preprint(
        "Semantic2Graph: Graph-based Multi-modal Feature Fusion for Action Segmentation in Videos",
        "Junbin Zhang; Pei-Hsuan Tsai; Meng-Hsun Tsai", 2022, "2209.05653",
        "2022-09-12", "2023-03-15", "fully-supervised", "graphical-model",
    ),
    _preprint(
        "Text-Augmented Action Segmentation Optimal Transport for Unsupervised Surgical Phase Recognition",
        "Omar Mohamed; collaborators", 2026, "2602.24138",
        "2026-02-27", "2026-02-27", "unsupervised",
        "optimal-transport,vision-language-model",
    ),
]


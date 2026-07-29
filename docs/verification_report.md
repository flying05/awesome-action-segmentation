# Verification Report

| Item | Count |
|---|---:|
| Candidate records | 174 |
| Conference/journal core + extension | 120 |
| Independently matched to official publication pages | 111 |
| Extended venue papers | 21 |
| Records merged by arXiv comment/journal_ref venue metadata | 9 |
| Preprints without an accepted venue claim | 52 |
| Related-but-not-core / excluded from core count | 2 |
| Duplicate records merged in last report | 186 |
| PDFs downloaded and parsed | 168 |
| PDF download failures in manifest | 5 |
| Papers requiring manual review | 61 |

| arXiv API unique candidates audited | 166 |
| arXiv direct TAS hits before deduplication | 134 |
| arXiv ambiguous/excluded candidates retained in audit | 32 |
| arXiv publication claims extracted from comment/journal_ref | 80 |
| Publication claims matched to official records | 59 |
| Unmatched claims across the full candidate audit | 21 |
| Venue-classified publication metadata records | 9 |

## Venue and year statistics

- Venues: AAAI: 4; ACM MM Workshop: 1; BMVC: 3; CVPR: 39; CVPR Workshop: 3; CVWW: 1; DICTA: 1; ECCV: 12; Ego4D/EPIC Workshop: 1; ICCV: 16; ICCV Workshop: 1; ICME: 1; ICPR: 2; ICRA: 3; IEEE TPAMI: 1; IEEE Transactions on Multimedia: 1; IJCAI: 3; IROS: 3; ISKE: 1; LUV Workshop: 1; MICCAI: 1; NeurIPS: 5; Pattern Recognition: 1; Pattern Recognition Letters: 1; TAHRI: 1; WACV: 13
- Years: 2014: 1; 2015: 1; 2016: 3; 2017: 3; 2018: 5; 2019: 7; 2020: 12; 2021: 12; 2022: 17; 2023: 17; 2024: 18; 2025: 12; 2026: 12

## Verification rules

正式论文页、proceedings 或 arXiv comment/journal_ref 中明确的非投稿性会议/期刊去向，都直接进入对应 venue 的主论文计数；纯预印本不进入该计数。验证失败不会中止流水线，也不会伪造本地路径。PDF 存在时会重新计算 SHA256 并尝试解析。截止日期后的记录不得进入正式结果。

## Remaining possible omissions

- 旧版 ACM MM、BMVC 和 WACV 搜索界面的全文召回可能不完整。
- 标题不含 segmentation、但摘要定义了逐帧程序解析的工作仍可能漏检。
- MICCAI 手术 phase/step 工作数量很大，本快照仅收录直接采用 TAS 式密集工作流建模的代表项。
- 2026 ECCV/AAAI/IJCAI 等 comment 中的录用信息会直接归入对应 venue，同时保留结构化声明和独立官方页面匹配状态，方便后续追溯与升级。

Retry: `python scripts/update_repository.py --cutoff-date 2026-07-28 --only-unverified --retry-failures`。

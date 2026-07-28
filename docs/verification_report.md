# Verification Report

| Item | Count |
|---|---:|
| Candidate records | 172 |
| Verified formal core + extension | 91 |
| Extended venue papers | 8 |
| Preprints / pending verification | 78 |
| Related-but-not-core / excluded from core count | 3 |
| Duplicate records merged in last report | 93 |
| PDFs downloaded and parsed | 166 |
| PDF download failures in manifest | 5 |
| Papers requiring manual review | 78 |

| arXiv API unique candidates audited | 166 |
| arXiv direct TAS hits before deduplication | 134 |
| arXiv ambiguous/excluded candidates retained in audit | 32 |

## Venue and year statistics

- Venues: AAAI: 2; ACM MM Workshop: 1; BMVC: 3; CVPR: 36; CVPR Workshop: 3; ECCV: 10; ICCV: 15; ICCV Workshop: 1; ICRA: 1; IJCAI: 2; IROS: 1; MICCAI: 1; NeurIPS: 5; WACV: 10
- Years: 2014: 1; 2015: 1; 2016: 2; 2017: 2; 2018: 4; 2019: 5; 2020: 10; 2021: 10; 2022: 16; 2023: 8; 2024: 15; 2025: 9; 2026: 8

## Verification rules

正式记录必须有一手来源；预印本不进入正式计数。验证失败不会中止流水线，也不会伪造本地路径。PDF 存在时会重新计算 SHA256 并尝试解析。截止日期后的记录不得进入正式结果。

## Remaining possible omissions

- 旧版 ACM MM、BMVC 和 WACV 搜索界面的全文召回可能不完整。
- 标题不含 segmentation、但摘要定义了逐帧程序解析的工作仍可能漏检。
- MICCAI 手术 phase/step 工作数量很大，本快照仅收录直接采用 TAS 式密集工作流建模的代表项。
- 2026 ECCV/AAAI/IJCAI 等只有在截点前可由官方 proceedings 确认时才应加入；本报告不把录用传闻当作正式发表。

Retry: `python scripts/update_repository.py --cutoff-date 2026-07-28 --only-unverified --retry-failures`。

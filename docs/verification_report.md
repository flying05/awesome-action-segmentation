# Verification Report

| Item | Count |
|---|---:|
| Candidate records | 174 |
| Verified formal core + extension | 111 |
| Extended venue papers | 17 |
| Conference/journal claims pending official verification | 9 |
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
| Venue-classified unverified publication claims | 9 |

## Venue and year statistics

- Venues: AAAI: 4; ACM MM Workshop: 1; BMVC: 3; CVPR: 39; CVPR Workshop: 3; CVWW: 1; DICTA: 1; ECCV: 11; ICCV: 16; ICCV Workshop: 1; ICME: 1; ICPR: 2; ICRA: 2; IJCAI: 3; IROS: 3; ISKE: 1; MICCAI: 1; NeurIPS: 5; WACV: 13
- Years: 2014: 1; 2015: 1; 2016: 3; 2017: 3; 2018: 5; 2019: 6; 2020: 11; 2021: 11; 2022: 17; 2023: 14; 2024: 17; 2025: 12; 2026: 10

## Verification rules

正式记录必须有一手来源；会议/期刊声明按 venue 分类，但不进入 verified 正式计数。纯预印本同样不进入正式计数。验证失败不会中止流水线，也不会伪造本地路径。PDF 存在时会重新计算 SHA256 并尝试解析。截止日期后的记录不得进入正式结果。

## Remaining possible omissions

- 旧版 ACM MM、BMVC 和 WACV 搜索界面的全文召回可能不完整。
- 标题不含 segmentation、但摘要定义了逐帧程序解析的工作仍可能漏检。
- MICCAI 手术 phase/step 工作数量很大，本快照仅收录直接采用 TAS 式密集工作流建模的代表项。
- 2026 ECCV/AAAI/IJCAI 等 comment 中的录用信息会进入结构化核验队列；只有匹配到官方论文集、出版方页面或官方录用名单后才升级，不能把作者自述直接当作正式发表。

Retry: `python scripts/update_repository.py --cutoff-date 2026-07-28 --only-unverified --retry-failures`。

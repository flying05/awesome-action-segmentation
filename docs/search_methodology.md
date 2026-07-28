# Search Methodology

## Scope and cutoff

Cutoff: 2026-07-28. Core venue/year scans cover CVPR, ICCV and WACV official CVF indexes from
2010 (or the first available electronic index) through 2026. ECCV, BMVC, NeurIPS, AAAI and IJCAI
records are verified against ECVA/BMVC/NeurIPS/OpenReview/AAAI/IJCAI first-party pages. Extended
MICCAI and IROS records are kept separate.

## Four complementary searches

1. Keyword combinations in `data/search_queries.yaml`.
2. Official proceedings title scans by venue and year.
3. Backward, forward and author snowballing from MS-TCN, ASFormer, DiffAct, FACT, ASOT and the TAS survey.
4. Reverse searches from Breakfast, 50Salads, GTEA, Assembly101, COIN, CrossTask and surgical datasets.

Discovery indexes and search engines are candidate generators only. A formal record requires a first-party
proceedings or society page. arXiv-only records remain `Preprint` even when an author claims acceptance,
until the claim is independently verifiable. Every candidate is judged from title, abstract, output form,
datasets and metrics; keyword coincidence alone is insufficient.

## Known retrieval limitations

CVF changed URL layouts before 2020, and some old WACV indexes return 404; known official PDF/detail URLs
are therefore used as explicit seeds. ACM and Springer can rate-limit automated access. Failed checks are
retained in CSV logs and never converted into invented metadata. The update pipeline merges successful
new results with the previous snapshot so transient network failures cannot delete earlier verified records.

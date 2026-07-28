# Search Methodology

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

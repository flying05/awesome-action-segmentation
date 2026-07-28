# Taxonomy

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

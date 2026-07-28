# Datasets and Metrics

数字采用数据集官方页或原始论文口径；当不同粒度/预处理协议产生不同数字时，不把其中一个写成唯一事实。

## Datasets

### Breakfast Actions

- Domain / modality / view: daily activities; RGB; multi-view exocentric
- Scale: 1712 videos; 48 actions; about 2.3 minutes; protocol-dependent after feature sampling
- Annotation: frame-level fine-grained actions
- Splits: four-fold cross-validation
- Metrics: MoF, Edit, F1@10, F1@25, F1@50
- [Official source](https://serre-lab.clps.brown.edu/resource/breakfast-actions-dataset/)
- Notes: 1712 videos and 48 fine-grained classes are reported by the dataset paper; some works exclude silence/background differently.

### 50Salads

- Domain / modality / view: food preparation; RGB, depth, accelerometer; exocentric
- Scale: 50 videos; 17 actions; 5–10 minutes
- Annotation: frame-level actions at multiple granularities
- Splits: five-fold cross-validation
- Metrics: MoF, Edit, F1@10, F1@25, F1@50
- [Official source](https://cvip.computing.dundee.ac.uk/datasets/foodpreparation/50salads/)
- Notes: The widely used mid-level protocol has 17 action classes; counts differ for coarse/fine granularity.

### GTEA

- Domain / modality / view: egocentric kitchen activities; RGB; egocentric
- Scale: 28 videos; 11 actions; about 1 minute
- Annotation: frame-level actions
- Splits: four-fold cross-validation
- Metrics: MoF, Edit, F1@10, F1@25, F1@50
- [Official source](https://cbs.ic.gatech.edu/fpv/)
- Notes: The 28-video/11-class TAS protocol is the common processed subset, not every GTEA annotation variant.

### Assembly101

- Domain / modality / view: toy assembly and disassembly; RGB; multi-view egocentric and exocentric
- Scale: 4321 videos; 202 actions; multi-minute procedures
- Annotation: coarse and fine-grained temporal actions
- Splits: official train/validation/test split
- Metrics: frame_accuracy, Edit, F1@10, F1@25, F1@50
- [Official source](https://assembly-101.github.io/)
- Notes: The dataset paper reports 4,321 videos, 1,380 hours, and 202 fine-grained action classes.

### COIN

- Domain / modality / view: instructional procedures; RGB; web video
- Scale: 11827 videos; 778 actions; about 2.36 minutes
- Annotation: temporal step segments
- Splits: official split
- Metrics: frame_accuracy, segment_recall, mIoU
- [Official source](https://coin-dataset.github.io/)
- Notes: The paper reports 11,827 videos, 180 tasks and 778 step labels.

### Cholec80

- Domain / modality / view: laparoscopic cholecystectomy; RGB; endoscopic
- Scale: 80 videos; 7 actions; about 39 minutes
- Annotation: surgical phase labels
- Splits: 40 train / 40 test
- Metrics: accuracy, precision, recall, Jaccard
- [Official source](http://camma.u-strasbg.fr/datasets)
- Notes: Seven phases are standard; workflow papers may additionally report tool presence.

## Metrics

- **MoF / Frame Accuracy**：正确帧比例；长动作占比高时会掩盖短动作遗漏和过分割。
- **Edit Score**：先压缩连续重复标签，再用归一化 Levenshtein 距离衡量动作序列；关注顺序而弱化精确边界。
- **F1@10/25/50**：按时序 IoU 阈值匹配预测段和真值段，对重复碎片计假阳性，因此能揭示过分割。
- **mIoU / Jaccard**：类别或片段交并比；必须注明宏/微平均和背景处理。
- **Boundary precision/recall**：在容忍窗口内匹配转换点；窗口大小会显著改变结论。
- **Online latency**：需与吞吐、因果缓冲长度、峰值显存一起报告。
- **Efficiency**：FLOPs 不包含所有 I/O 与特征提取成本，建议同时给 wall-clock、显存和能耗。

只看帧准确率时，把一个长动作预测正确可以抵消大量短动作错误；把同一动作切成多个碎片也可能几乎不改变正确帧数。因此 TAS 至少应联合报告 Frame Accuracy、Edit 和多个阈值的 segmental F1。

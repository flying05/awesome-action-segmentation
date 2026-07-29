# 开放词汇与泛化

## 任务定义与关键困难

需要区分 unseen task、unseen view 与 unseen action。视觉语言原型能命名动作，但文本相似不等同于正确的程序顺序；discover-then-name 还需独立评估发现和命名误差。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [Exploring Vision-Language Models for Open-Vocabulary Zero-Shot Action Segmentation](https://arxiv.org/abs/2602.21406) — ICRA 2026; `unknown`
- [Multi-Modal Few-Shot Temporal Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_Multi-Modal_Few-Shot_Temporal_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `Transformer, prototype-learning`
- [An Efficient Framework for Few-shot Skeleton-based Temporal Action Segmentation](https://arxiv.org/abs/2207.09925) — Preprint 2022; `unknown`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

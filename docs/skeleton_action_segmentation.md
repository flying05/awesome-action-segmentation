# 骨架动作分割

## 任务定义与关键困难

骨架降低外观干扰，却带来关节噪声、跨视角坐标差异和相似微动作边界模糊。图卷积、运动词/token 与跨主体对齐是主要路线。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.html) — CVPR 2026; `boundary-modeling`
- [Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.html) — CVPR 2026; `boundary-modeling`
- [DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `unknown`
- [Skeleton Motion Words for Unsupervised Skeleton-Based Temporal Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Gokay_Skeleton_Motion_Words_for_Unsupervised_Skeleton-Based_Temporal_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `unknown`
- [LAC - Latent Action Composition for Skeleton-based Action Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.html) — ICCV 2023; `unknown`
- [Stacked Spatio-Temporal Graph Convolutional Networks for Action Segmentation](https://openaccess.thecvf.com/content_WACV_2020/html/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.html) — WACV 2020; `unknown`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

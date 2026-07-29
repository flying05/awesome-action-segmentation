# 在线与流式动作分割

## 任务定义与关键困难

在线系统只能使用当前与过去帧，因此离线双向上下文的精度不可直接比较。除 Edit/F1 外，应报告因果延迟、吞吐、峰值显存和状态缓存。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [Ego-METAS: Egocentric online Multimodal Energy-efficient Temporal Action Segmentation benchmark](https://arxiv.org/abs/2606.02246) — Preprint 2026; `unknown`
- [Pose-Aware Weakly-Supervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2025W/MULA2025/html/Zhao_Pose-Aware_Weakly-Supervised_Action_Segmentation_CVPRW_2025_paper.html) — CVPR Workshop 2025; `contrastive-learning, boundary-modeling`
- [Friends Across Time: Multi-Scale Action Segmentation Transformer for Surgical Phase Recognition](https://arxiv.org/abs/2401.11644) — Preprint 2024; `Transformer, cross-attention, causal-model`
- [O-TALC: Steps Towards Combating Oversegmentation within Online Action Segmentation](https://arxiv.org/abs/2404.06894) — TAHRI 2024; `boundary-modeling`
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](https://papers.nips.cc/paper_files/paper/2024/hash/6c6c5fccf3c8661fcae219be7ca226f7-Abstract-Conference.html) — NeurIPS 2024; `TCN, causal-model`
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](https://openaccess.thecvf.com/content/CVPR2024/html/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.html) — CVPR 2024; `causal-model`
- [End-to-End Streaming Video Temporal Action Segmentation with Reinforce Learning](https://arxiv.org/abs/2309.15683) — Preprint 2023; `unknown`
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos](https://openaccess.thecvf.com/content/ICCV2023/html/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.html) — ICCV 2023; `structured-decoding`
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Du_Fast_and_Unsupervised_Action_Boundary_Detection_for_Action_Segmentation_CVPR_2022_paper.html) — CVPR 2022; `clustering, boundary-modeling`
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](https://openaccess.thecvf.com/content/CVPR2022/html/Kumar_Unsupervised_Action_Segmentation_by_Joint_Representation_Learning_and_Online_Clustering_CVPR_2022_paper.html) — CVPR 2022; `optimal-transport, clustering`
- [Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos](https://openaccess.thecvf.com/content/CVPR2022/html/Ghoddoosian_Weakly-Supervised_Online_Action_Segmentation_in_Multi-View_Instructional_Videos_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.html) — CVPR 2018; `structured-decoding`
- [Temporal Human Action Segmentation via Dynamic Clustering](https://arxiv.org/abs/1803.05790) — Preprint 2018; `clustering`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

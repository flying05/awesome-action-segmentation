# 高效与长视频方法

## 任务定义与关键困难

长视频的主要瓶颈是特征提取、二次注意力和多阶段反复推理。除 FLOPs 外还应报告实际延迟、峰值显存、特征缓存与能耗。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.html) — CVPR 2026; `boundary-modeling`
- [Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_Polyphony_Diffusion-based_Dual-Hand_Action_Segmentation_with_Alternating_Vision_Transformer_and_CVPR_2026_paper.html) — CVPR 2026; `Transformer, diffusion`
- [Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.html) — CVPR 2026; `boundary-modeling`
- [Condensing Action Segmentation Datasets via Generative Network Inversion](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_Condensing_Action_Segmentation_Datasets_via_Generative_Network_Inversion_CVPR_2025_paper.html) — CVPR 2025; `dataset-condensation`
- [DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `unknown`
- [Coherent Temporal Synthesis for Incremental Action Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.html) — CVPR 2024; `unknown`
- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.html) — CVPR 2024; `Transformer, cross-attention, VQ-tokenization`
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](https://papers.nips.cc/paper_files/paper/2024/hash/6c6c5fccf3c8661fcae219be7ca226f7-Abstract-Conference.html) — NeurIPS 2024; `TCN, causal-model`
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](https://openaccess.thecvf.com/content/CVPR2024/html/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.html) — CVPR 2024; `causal-model`
- [Activity Grammars for Temporal Action Segmentation](https://papers.nips.cc/paper_files/paper/2023/hash/ee6c4b99b4c0d3d60efd22c1ecdd9891-Abstract-Conference.html) — NeurIPS 2023; `structured-decoding`
- [Diffusion Action Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.html) — ICCV 2023; `diffusion, boundary-modeling, multi-stage-TCN`
- [Video Action Segmentation via Contextually Refined Temporal Keypoints](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.html) — ICCV 2023; `unknown`
- [Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation](https://openreview.net/forum?id=PCQyUvAmKs) — NeurIPS 2022; `structured-decoding`
- [Semantic2Graph: Graph-based Multi-modal Feature Fusion for Action Segmentation in Videos](https://arxiv.org/abs/2209.05653) — Preprint 2022; `graphical-model`
- [Set-Supervised Action Learning in Procedural Task Videos via Pairwise Order Consistency](https://openaccess.thecvf.com/content/CVPR2022/html/Lu_Set-Supervised_Action_Learning_in_Procedural_Task_Videos_via_Pairwise_Order_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [Uncertainty-Aware Representation Learning for Action Segmentation](https://www.ijcai.org/proceedings/2022/115) — IJCAI 2022; `uncertainty-modeling, boundary-modeling`
- [ASFormer: Transformer for Action Segmentation](https://www.bmvc2021-virtualconference.com/conference/papers/paper_0578.html) — BMVC 2021; `Transformer`
- [Anchor-Constrained Viterbi for Set-Supervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Anchor-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2021_paper.html) — CVPR 2021; `structured-decoding`
- [Coarse to Fine Multi-Resolution Temporal Convolutional Network](https://arxiv.org/abs/2105.10859) — Preprint 2021; `TCN`
- [Global2Local: Efficient Structure Search for Video Action Segmentation](https://openaccess.thecvf.com/content/CVPR2021/html/Gao_Global2Local_Efficient_Structure_Search_for_Video_Action_Segmentation_CVPR_2021_paper.html) — CVPR 2021; `unknown`
- [Refining Action Segmentation With Hierarchical Video Representations](https://openaccess.thecvf.com/content/ICCV2021/html/Ahn_Refining_Action_Segmentation_With_Hierarchical_Video_Representations_ICCV_2021_paper.html) — ICCV 2021; `unknown`
- [Action Segmentation with Mixed Temporal Domain Adaptation](https://openaccess.thecvf.com/content_WACV_2020/html/Chen_Action_Segmentation_with_Mixed_Temporal_Domain_Adaptation_WACV_2020_paper.html) — WACV 2020; `unknown`
- [Boundary-Aware Cascade Networks for Temporal Action Segmentation](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/35_ECCV_2020_paper.php) — ECCV 2020; `boundary-modeling`
- [Improving Action Segmentation via Graph-Based Temporal Reasoning](https://openaccess.thecvf.com/content_CVPR_2020/html/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.html) — CVPR 2020; `boundary-modeling`
- [Stacked Spatio-Temporal Graph Convolutional Networks for Action Segmentation](https://openaccess.thecvf.com/content_WACV_2020/html/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.html) — WACV 2020; `unknown`
- [TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_33) — MICCAI 2020; `TCN, multi-stage-TCN`
- [Temporal Aggregate Representations for Long-Range Video Understanding](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/154_ECCV_2020_paper.php) — ECCV 2020; `TCN`
- [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html) — CVPR 2019; `TCN, multi-stage-TCN`
- [Temporal Convolutional Networks for Action Segmentation and Detection](https://openaccess.thecvf.com/content_cvpr_2017/html/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.html) — CVPR 2017; `duration-modeling, TCN`
- [Human Action Segmentation With Hierarchical Supervoxel Consistency](https://openaccess.thecvf.com/content_cvpr_2015/html/Lu_Human_Action_Segmentation_2015_CVPR_paper.html) — CVPR 2015; `unknown`
- [Leveraging Hierarchical Parametric Networks for Skeletal Joints Based Action Segmentation and Recognition](https://openaccess.thecvf.com/content_cvpr_2014/html/Wu_Leveraging_Hierarchical_Parametric_2014_CVPR_paper.html) — CVPR 2014; `unknown`
- [The Language of Actions: Recovering the Syntax and Semantics of Goal-Directed Human Activities](https://openaccess.thecvf.com/content_cvpr_2014/html/Kuehne_The_Language_of_2014_CVPR_paper.html) — CVPR 2014; `structured-decoding`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

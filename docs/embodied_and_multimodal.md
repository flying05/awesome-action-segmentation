# 具身与多模态动作分割

## 任务定义与关键困难

RGB、音频、IMU、深度和 gaze 的采样率与缺失机制不同。融合模型不仅要提升平均分，还应说明传感器失效时的退化，以及在线机器人系统的因果约束。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation](https://arxiv.org/abs/2604.26637) — Preprint 2026; `boundary-modeling`
- [Adaptive Latent Trajectory Anchoring for Action Segmentation Dataset Condensation](https://arxiv.org/abs/2607.09081) — Preprint 2026; `diffusion, dataset-condensation`
- [Boundary-Centric Clip-Budgeted Active Learning for Temporal Action Segmentation](https://arxiv.org/abs/2604.15173) — Preprint 2026; `boundary-modeling`
- [Combining Boundary Supervision and Segment-Level Regularization for Fine-Grained Action Segmentation](https://openaccess.thecvf.com/content/CVPR2026W/SAUAFG/html/Mitsuoka_Combining_Boundary_Supervision_and_Segment-Level_Regularization_for_Fine-Grained_Action_Segmentation_CVPRW_2026_paper.html) — CVPR Workshop 2026; `boundary-modeling`
- [Ego-METAS: Egocentric online Multimodal Energy-efficient Temporal Action Segmentation benchmark](https://arxiv.org/abs/2606.02246) — Preprint 2026; `unknown`
- [Fine-Grained Action Segmentation for Renorrhaphy in Robot-Assisted Partial Nephrectomy](https://arxiv.org/abs/2604.09051) — Preprint 2026; `duration-modeling`
- [IMPACT-Scribe: Interactive Temporal Action Segmentation with Boundary Scribbles and Query Planning](https://arxiv.org/abs/2605.01668) — Preprint 2026; `boundary-modeling`
- [LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.html) — CVPR 2026; `boundary-modeling`
- [Learning Action Hierarchies via Hybrid Geometric Diffusion](https://openaccess.thecvf.com/content/WACV2026/html/Kaushik_Learning_Action_Hierarchies_via_Hybrid_Geometric_Diffusion_WACV_2026_paper.html) — WACV 2026; `diffusion`
- [M2R2: MultiModal Robotic Representation for Temporal Action Segmentation](https://dsliwowski1.github.io/) — ICRA 2026; `multimodal, prototype-learning`
- [Point-Supervised Skeleton-Based Human Action Segmentation](https://arxiv.org/abs/2603.06201) — Preprint 2026; `clustering, prototype-learning`
- [Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_Polyphony_Diffusion-based_Dual-Hand_Action_Segmentation_with_Alternating_Vision_Transformer_and_CVPR_2026_paper.html) — CVPR 2026; `Transformer, diffusion`
- [Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.html) — CVPR 2026; `boundary-modeling`
- [Timestamp Query Transformer for Temporal Action Segmentation](https://openaccess.thecvf.com/content/WACV2026/html/Wang_Timestamp_Query_Transformer_for_Temporal_Action_Segmentation_WACV_2026_paper.html) — WACV 2026; `Transformer, cross-attention, VQ-tokenization`
- [Unsupervised Skeleton-Based Action Segmentation via Hierarchical Spatiotemporal Vector Quantization](https://arxiv.org/abs/2604.15196) — Preprint 2026; `clustering`
- [Condensing Action Segmentation Datasets via Generative Network Inversion](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_Condensing_Action_Segmentation_Datasets_via_Generative_Network_Inversion_CVPR_2025_paper.html) — CVPR 2025; `dataset-condensation`
- [Dual-Stream Alignment for Action Segmentation](https://arxiv.org/abs/2510.07652) — Preprint 2025; `cross-attention`
- [DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `unknown`
- [End-to-End Action Segmentation Transformer](https://openaccess.thecvf.com/content/ICCV2025W/SVU/html/Wang_End-to-End_Action_Segmentation_Transformer_ICCVW_2025_paper.html) — ICCV Workshop 2025; `Transformer`
- [HRTR: A Single-stage Transformer for Fine-grained Sub-second Action Segmentation in Stroke Rehabilitation](https://arxiv.org/abs/2506.02472) — Preprint 2025; `Transformer, multi-stage-TCN`
- [Multi-Modal Graph Convolutional Network with Sinusoidal Encoding for Robust Human Action Segmentation](https://arxiv.org/abs/2507.00752) — Preprint 2025; `unknown`
- [Multi-Stage Boundary-Aware Transformer Network for Action Segmentation in Untrimmed Surgical Videos](https://arxiv.org/abs/2504.18756) — Preprint 2025; `Transformer, boundary-modeling, duration-modeling, multi-stage-TCN`
- [Text-Derived Relational Graph-Enhanced Network for Skeleton-Based Action Segmentation](https://arxiv.org/abs/2503.15126) — Preprint 2025; `unknown`
- [Towards Generalizing Temporal Action Segmentation to Unseen Views](https://arxiv.org/abs/2504.02512) — Preprint 2025; `unknown`
- [Towards Open-World Human Action Segmentation Using Graph Convolutional Networks](https://arxiv.org/abs/2507.00756) — Preprint 2025; `clustering`
- [VIFSS: View-Invariant and Figure Skating-Specific Pose Representation Learning for Temporal Action Segmentation](https://arxiv.org/abs/2508.10281) — Preprint 2025; `unknown`
- [3D Pose-Based Temporal Action Segmentation for Figure Skating: A Fine-Grained and Jump Procedure-Aware Annotation Approach](https://dl.acm.org/doi/10.1145/3689061.3689077) — ACM MM Workshop 2024; `prototype-learning`
- [ActFusion: a Unified Diffusion Model for Action Segmentation and Anticipation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a3a661eb3308d0bb686f6a4bac521032-Abstract-Conference.html) — NeurIPS 2024; `diffusion`
- [Coherent Temporal Synthesis for Incremental Action Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.html) — CVPR 2024; `unknown`
- [Cost-Sensitive Learning for Long-Tailed Temporal Action Segmentation](https://bmvc2024.org/proceedings/227/) — BMVC 2024; `structured-decoding`
- [Efficient Temporal Action Segmentation via Boundary-aware Query Voting](https://proceedings.neurips.cc/paper_files/paper/2024/hash/42770daf4a3384b712ea9c36e9279998-Abstract-Conference.html) — NeurIPS 2024; `boundary-modeling`
- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.html) — CVPR 2024; `Transformer, cross-attention, VQ-tokenization`
- [Faster Diffusion Action Segmentation](https://arxiv.org/abs/2408.02024) — Preprint 2024; `Transformer, diffusion`
- [Friends Across Time: Multi-Scale Action Segmentation Transformer for Surgical Phase Recognition](https://arxiv.org/abs/2401.11644) — Preprint 2024; `Transformer, cross-attention, causal-model`
- [Language-Assisted Human Part Motion Learning for Skeleton-Based Temporal Action Segmentation](https://arxiv.org/abs/2410.06353) — Preprint 2024; `unknown`
- [Language-Assisted Skeleton Action Understanding for Skeleton-Based Temporal Action Segmentation](https://eccv.ecva.net/virtual/2024/poster/1462) — ECCV 2024; `language-model, contrastive-learning`
- [Long-Tail Temporal Action Segmentation with Group-wise Temporal Logit Adjustment](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4389_ECCV_2024_paper.php) — ECCV 2024; `structured-decoding`
- [O-TALC: Steps Towards Combating Oversegmentation within Online Action Segmentation](https://arxiv.org/abs/2404.06894) — Preprint 2024; `boundary-modeling`
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](https://papers.nips.cc/paper_files/paper/2024/hash/6c6c5fccf3c8661fcae219be7ca226f7-Abstract-Conference.html) — NeurIPS 2024; `TCN, causal-model`
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](https://openaccess.thecvf.com/content/CVPR2024/html/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.html) — CVPR 2024; `causal-model`
- [Random Walks for Temporal Action Segmentation With Timestamp Supervision](https://openaccess.thecvf.com/content/WACV2024/html/Hirsch_Random_Walks_for_Temporal_Action_Segmentation_With_Timestamp_Supervision_WACV_2024_paper.html) — WACV 2024; `unknown`
- [Stitch Contrast and Segment_Learning a Human Action Segmentation Model Using Trimmed Skeleton Videos](https://arxiv.org/abs/2412.14988) — Preprint 2024; `unknown`
- [A Decoupled Spatio-Temporal Framework for Skeleton-based Action Segmentation](https://arxiv.org/abs/2312.05830) — Preprint 2023; `unknown`
- [Action Segmentation Using 2D Skeleton Heatmaps and Multi-Modality Fusion](https://arxiv.org/abs/2309.06462) — Preprint 2023; `TCN`
- [Activity Grammars for Temporal Action Segmentation](https://papers.nips.cc/paper_files/paper/2023/hash/ee6c4b99b4c0d3d60efd22c1ecdd9891-Abstract-Conference.html) — NeurIPS 2023; `structured-decoding`
- [BIT: Bi-Level Temporal Modeling for Efficient Supervised Action Segmentation](https://arxiv.org/abs/2308.14900) — Preprint 2023; `Transformer, cross-attention, VQ-tokenization`
- [CASR: Refining Action Segmentation via Marginalizing Frame-levle Causal Relationships](https://arxiv.org/abs/2311.12401) — Preprint 2023; `causal-model`
- [DIR-AS: Decoupling Individual Identification and Temporal Reasoning for Action Segmentation](https://arxiv.org/abs/2304.02110) — Preprint 2023; `boundary-modeling, multi-stage-TCN`
- [DPMix: Mixture of Depth and Point Cloud Video Experts for 4D Action Segmentation](https://arxiv.org/abs/2307.16803) — Preprint 2023; `unknown`
- [Diffusion Action Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.html) — ICCV 2023; `diffusion, boundary-modeling, multi-stage-TCN`
- [End-to-End Streaming Video Temporal Action Segmentation with Reinforce Learning](https://arxiv.org/abs/2309.15683) — Preprint 2023; `unknown`
- [Enhancing Transformer Backbone for Egocentric Video Action Segmentation](https://arxiv.org/abs/2305.11365) — Preprint 2023; `Transformer`
- [How Much Temporal Long-Term Context is Needed for Action Segmentation?](https://openaccess.thecvf.com/content/ICCV2023/html/Bahrami_How_Much_Temporal_Long-Term_Context_is_Needed_for_Action_Segmentation_ICCV_2023_paper.html) — ICCV 2023; `TCN`
- [MS-TCRNet: Multi-Stage Temporal Convolutional Recurrent Networks for Action Segmentation Using Sensor-Augmented Kinematics](https://arxiv.org/abs/2303.07814) — Preprint 2023; `TCN, multi-stage-TCN`
- [Prompt-enhanced Hierarchical Transformer Elevating Cardiopulmonary Resuscitation Instruction via Temporal Action Segmentation](https://arxiv.org/abs/2308.16552) — Preprint 2023; `Transformer`
- [SigFormer: Sparse Signal-Guided Transformer for Multi-Modal Human Action Segmentation](https://arxiv.org/abs/2311.17428) — Preprint 2023; `Transformer, cross-attention, boundary-modeling`
- [Temporal Segment Transformer for Action Segmentation](https://arxiv.org/abs/2302.13074) — Preprint 2023; `Transformer`
- [Timestamp-Supervised Action Segmentation in the Perspective of Clustering](https://www.ijcai.org/proceedings/2023/77) — IJCAI 2023; `clustering`
- [Video Action Segmentation via Contextually Refined Temporal Keypoints](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.html) — ICCV 2023; `unknown`
- [A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4788_ECCV_2022_paper.php) — ECCV 2022; `TCN, uncertainty-modeling`
- [Action parsing using context features](https://arxiv.org/abs/2205.10008) — Preprint 2022; `unknown`
- [Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [Cross-Enhancement Transformer for Action Segmentation](https://arxiv.org/abs/2205.09445) — Preprint 2022; `Transformer, TCN`
- [Do we really need temporal convolutions in action segmentation?](https://arxiv.org/abs/2205.13425) — Preprint 2022; `Transformer, boundary-modeling, TCN`
- [Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation](https://openreview.net/forum?id=PCQyUvAmKs) — NeurIPS 2022; `structured-decoding`
- [Hand Guided High Resolution Feature Enhancement for Fine-Grained Atomic Action Segmentation within Complex Human Assemblies](https://arxiv.org/abs/2211.13694) — Preprint 2022; `unknown`
- [Robust Action Segmentation from Timestamp Supervision](https://bmvc2022.mpi-inf.mpg.de/392/) — BMVC 2022; `TCN, boundary-modeling`
- [Semantic2Graph: Graph-based Multi-modal Feature Fusion for Action Segmentation in Videos](https://arxiv.org/abs/2209.05653) — Preprint 2022; `graphical-model`
- [Set-Supervised Action Learning in Procedural Task Videos via Pairwise Order Consistency](https://openaccess.thecvf.com/content/CVPR2022/html/Lu_Set-Supervised_Action_Learning_in_Procedural_Task_Videos_via_Pairwise_Order_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [Skeleton-Based Action Segmentation with Multi-Stage Spatial-Temporal Graph Convolutional Neural Networks](https://arxiv.org/abs/2202.01727) — Preprint 2022; `TCN, multi-stage-TCN`
- [Streaming Video Temporal Action Segmentation In Real Time](https://arxiv.org/abs/2209.13808) — Preprint 2022; `unknown`
- [Temporal Action Segmentation: An Analysis of Modern Techniques](https://arxiv.org/abs/2210.10352) — Preprint 2022; `unknown`
- [Timestamp-Supervised Action Segmentation with Graph Convolutional Networks](https://doi.org/10.1109/IROS47612.2022.9981176) — IROS 2022; `graphical-model, TCN`
- [Turning to a Teacher for Timestamp Supervised Temporal Action Segmentation](https://arxiv.org/abs/2207.00712) — Preprint 2022; `unknown`
- [Uncertainty-Aware Representation Learning for Action Segmentation](https://www.ijcai.org/proceedings/2022/115) — IJCAI 2022; `uncertainty-modeling, boundary-modeling`
- [Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3672_ECCV_2022_paper.php) — ECCV 2022; `Transformer, structured-decoding, duration-modeling`
- [ASFormer: Transformer for Action Segmentation](https://www.bmvc2021-virtualconference.com/conference/papers/paper_0578.html) — BMVC 2021; `Transformer`
- [Anchor-Constrained Viterbi for Set-Supervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Anchor-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2021_paper.html) — CVPR 2021; `structured-decoding`
- [Coarse to Fine Multi-Resolution Temporal Convolutional Network](https://arxiv.org/abs/2105.10859) — Preprint 2021; `TCN`
- [Global2Local: Efficient Structure Search for Video Action Segmentation](https://openaccess.thecvf.com/content/CVPR2021/html/Gao_Global2Local_Efficient_Structure_Search_for_Video_Action_Segmentation_CVPR_2021_paper.html) — CVPR 2021; `unknown`
- [Refining Action Segmentation With Hierarchical Video Representations](https://openaccess.thecvf.com/content/ICCV2021/html/Ahn_Refining_Action_Segmentation_With_Hierarchical_Video_Representations_ICCV_2021_paper.html) — ICCV 2021; `unknown`
- [Temporal Action Segmentation From Timestamp Supervision](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.html) — CVPR 2021; `unknown`
- [Temporal Action Segmentation with High-level Complex Activity Labels](https://arxiv.org/abs/2108.06706) — Preprint 2021; `prototype-learning`
- [Action Segmentation with Mixed Temporal Domain Adaptation](https://openaccess.thecvf.com/content_WACV_2020/html/Chen_Action_Segmentation_with_Mixed_Temporal_Domain_Adaptation_WACV_2020_paper.html) — WACV 2020; `unknown`
- [Boundary-Aware Cascade Networks for Temporal Action Segmentation](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/35_ECCV_2020_paper.php) — ECCV 2020; `boundary-modeling`
- [Hierarchical Attention Network for Action Segmentation](https://arxiv.org/abs/2005.03209) — Preprint 2020; `unknown`
- [Improving Action Segmentation via Graph-Based Temporal Reasoning](https://openaccess.thecvf.com/content_CVPR_2020/html/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.html) — CVPR 2020; `boundary-modeling`
- [Intra- and Inter-Action Understanding via Temporal Action Parsing](https://arxiv.org/abs/2005.10229) — Preprint 2020; `unknown`
- [Stacked Spatio-Temporal Graph Convolutional Networks for Action Segmentation](https://openaccess.thecvf.com/content_WACV_2020/html/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.html) — WACV 2020; `unknown`
- [TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_33) — MICCAI 2020; `TCN, multi-stage-TCN`
- [Temporal Aggregate Representations for Long-Range Video Understanding](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/154_ECCV_2020_paper.php) — ECCV 2020; `TCN`
- [Coupled Generative Adversarial Network for Continuous Fine-grained Action Segmentation](https://arxiv.org/abs/1909.09283) — Preprint 2019; `unknown`
- [Frontal Low-rank Random Tensors for Fine-grained Action Segmentation](https://arxiv.org/abs/1906.01004) — Preprint 2019; `unknown`
- [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html) — CVPR 2019; `TCN, multi-stage-TCN`
- [End-to-End Fine-Grained Action Segmentation and Recognition Using Conditional Random Field Models and Discriminative Sparse Coding](https://arxiv.org/abs/1801.09571) — Preprint 2018; `unknown`
- [Local Temporal Bilinear Pooling for Fine-grained Action Parsing](https://arxiv.org/abs/1812.01922) — Preprint 2018; `TCN`
- [Temporal Convolutional Networks for Action Segmentation and Detection](https://openaccess.thecvf.com/content_cvpr_2017/html/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.html) — CVPR 2017; `duration-modeling, TCN`
- [TricorNet: A Hybrid Temporal Convolutional and Recurrent Network for Video Action Segmentation](https://arxiv.org/abs/1705.07818) — Preprint 2017; `TCN`
- [Segmental Spatiotemporal CNNs for Fine-grained Action Segmentation](https://arxiv.org/abs/1602.02995) — Preprint 2016; `unknown`
- [Human Action Segmentation With Hierarchical Supervoxel Consistency](https://openaccess.thecvf.com/content_cvpr_2015/html/Lu_Human_Action_Segmentation_2015_CVPR_paper.html) — CVPR 2015; `unknown`
- [Leveraging Hierarchical Parametric Networks for Skeletal Joints Based Action Segmentation and Recognition](https://openaccess.thecvf.com/content_cvpr_2014/html/Wu_Leveraging_Hierarchical_Parametric_2014_CVPR_paper.html) — CVPR 2014; `unknown`
- [The Language of Actions: Recovering the Syntax and Semantics of Goal-Directed Human Activities](https://openaccess.thecvf.com/content_cvpr_2014/html/Kuehne_The_Language_of_2014_CVPR_paper.html) — CVPR 2014; `structured-decoding`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

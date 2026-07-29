# 无监督动作分割

## 任务定义与关键困难

表示学习必须把外观差异与动作语义分开；聚类还需兼顾 temporal consistency、动作顺序、背景与重复动作。balanced OT 会错误强迫等量簇，unbalanced OT 更能容忍时长和缺失差异；Gromov–Wasserstein 可编码帧—帧与类—类结构。伪标签反馈环会放大早期错误，闭环细化、不确定性估计和多层动作 token 是缓解方向。未知类别数仍是根本难题；Hungarian matching 只解决标签置换后的评估对齐，并不证明聚类得到的人类语义类别正确。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [Data-Efficient Surgical Phase Segmentation in Small-Incision Cataract Surgery: A Controlled Study of Vision Foundation Models](https://arxiv.org/abs/2604.10514) — Preprint 2026; `unknown`
- [Deep Kernel Video Approximation for Unsupervised Action Segmentation](https://icpr2026.org/acceptedPapers.html) — ICPR 2026; `kernel-method, MMD`
- [Learning Probabilistic Embeddings for Unsupervised Action Segmentation](https://arxiv.org/abs/2607.05263) — ECCV 2026; `optimal-transport, clustering`
- [Text-Augmented Action Segmentation Optimal Transport for Unsupervised Surgical Phase Recognition](https://arxiv.org/abs/2602.24138) — Preprint 2026; `optimal-transport, vision-language-model`
- [CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Bueno-Benito_CLOT_Closed_Loop_Optimal_Transport_for_Unsupervised_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `cross-attention, optimal-transport, clustering`
- [Hierarchical Vector Quantization for Unsupervised Action Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32751) — AAAI 2025; `VQ-tokenization, clustering`
- [Improving action segmentation via explicit similarity measurement](https://arxiv.org/abs/2502.10713) — Preprint 2025; `Transformer, boundary-modeling, TCN`
- [Joint Self-Supervised Video Alignment and Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Ali_Joint_Self-Supervised_Video_Alignment_and_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `optimal-transport`
- [Skeleton Motion Words for Unsupervised Skeleton-Based Temporal Action Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Gokay_Skeleton_Motion_Words_for_Unsupervised_Skeleton-Based_Temporal_Action_Segmentation_ICCV_2025_paper.html) — ICCV 2025; `unknown`
- [OTAS: Unsupervised Boundary Detection for Object-Centric Temporal Action Segmentation](https://openaccess.thecvf.com/content/WACV2024/html/Li_OTAS_Unsupervised_Boundary_Detection_for_Object-Centric_Temporal_Action_Segmentation_WACV_2024_paper.html) — WACV 2024; `boundary-modeling`
- [Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment](https://openaccess.thecvf.com/content/WACV2024/html/Tran_Permutation-Aware_Activity_Segmentation_via_Unsupervised_Frame-To-Segment_Alignment_WACV_2024_paper.html) — WACV 2024; `Transformer, optimal-transport`
- [Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.html) — CVPR 2024; `optimal-transport`
- [United We Stand, Divided We Fall: UnityGraph for Unsupervised Procedure Learning From Videos](https://openaccess.thecvf.com/content/WACV2024/html/Bansal_United_We_Stand_Divided_We_Fall_UnityGraph_for_Unsupervised_Procedure_WACV_2024_paper.html) — WACV 2024; `unknown`
- [LAC - Latent Action Composition for Skeleton-based Action Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.html) — ICCV 2023; `unknown`
- [Leveraging Triplet Loss for Unsupervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2023W/L3D-IVU/html/Bueno-Benito_Leveraging_Triplet_Loss_for_Unsupervised_Action_Segmentation_CVPRW_2023_paper.html) — CVPR Workshop 2023; `contrastive-learning, clustering`
- [SFGANS Self-supervised Future Generator for human ActioN Segmentation](https://arxiv.org/abs/2401.00438) — Preprint 2023; `unknown`
- [Synchronization is All You Need: Exocentric-to-Egocentric Transfer for Temporal Action Segmentation with Unlabeled Synchronized Video Pairs](https://arxiv.org/abs/2312.02638) — Preprint 2023; `unknown`
- [TAEC: Unsupervised Action Segmentation with Temporal-Aware Embedding and Clustering](https://ceur-ws.org/Vol-3349/) — CVWW 2023; `clustering, representation-learning`
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Du_Fast_and_Unsupervised_Action_Boundary_Detection_for_Action_Segmentation_CVPR_2022_paper.html) — CVPR 2022; `clustering, boundary-modeling`
- [My View Is the Best View: Procedure Learning from Egocentric Videos](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1910_ECCV_2022_paper.php) — ECCV 2022; `clustering, contrastive-learning`
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](https://openaccess.thecvf.com/content/CVPR2022/html/Kumar_Unsupervised_Action_Segmentation_by_Joint_Representation_Learning_and_Online_Clustering_CVPR_2022_paper.html) — CVPR 2022; `optimal-transport, clustering`
- [Action Shuffle Alternating Learning for Unsupervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Action_Shuffle_Alternating_Learning_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.html) — CVPR 2021; `structured-decoding`
- [Joint Visual-Temporal Embedding for Unsupervised Learning of Actions in Untrimmed Sequences](https://openaccess.thecvf.com/content/WACV2021/html/VidalMata_Joint_Visual-Temporal_Embedding_for_Unsupervised_Learning_of_Actions_in_Untrimmed_WACV_2021_paper.html) — WACV 2021; `unknown`
- [Temporally-Weighted Hierarchical Clustering for Unsupervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2021/html/Sarfraz_Temporally-Weighted_Hierarchical_Clustering_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.html) — CVPR 2021; `clustering`
- [Unsupervised Action Segmentation for Instructional Videos](https://arxiv.org/abs/2106.03738) — LUV Workshop 2021; `unknown`
- [Action Segmentation With Joint Self-Supervised Temporal Domain Adaptation](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_Action_Segmentation_With_Joint_Self-Supervised_Temporal_Domain_Adaptation_CVPR_2020_paper.html) — CVPR 2020; `unknown`
- [Intra- and Inter-Action Understanding via Temporal Action Parsing](https://openaccess.thecvf.com/content_CVPR_2020/html/Shao_Intra-_and_Inter-Action_Understanding_via_Temporal_Action_Parsing_CVPR_2020_paper.html) — CVPR 2020; `clustering, boundary-modeling`
- [Unsupervised Learning of Action Classes With Continuous Temporal Embedding](https://openaccess.thecvf.com/content_CVPR_2019/html/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.html) — CVPR 2019; `unknown`
- [Unsupervised Procedure Learning via Joint Dynamic Summarization](https://openaccess.thecvf.com/content_ICCV_2019/html/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.html) — ICCV 2019; `unknown`
- [Temporal Human Action Segmentation via Dynamic Clustering](https://arxiv.org/abs/1803.05790) — Preprint 2018; `clustering`
- [Unsupervised Learning From Narrated Instruction Videos](https://openaccess.thecvf.com/content_cvpr_2016/html/Alayrac_Unsupervised_Learning_From_CVPR_2016_paper.html) — CVPR 2016; `clustering`
- [Unsupervised Semantic Parsing of Video Collections](https://openaccess.thecvf.com/content_iccv_2015/html/Sener_Unsupervised_Semantic_Parsing_ICCV_2015_paper.html) — ICCV 2015; `unknown`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

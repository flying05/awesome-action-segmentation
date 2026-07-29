# Awesome Action Segmentation

一个经过一手来源核验、可重复生成的 Temporal Action Segmentation（TAS）论文与资料索引。TAS 在长视频、骨架或多模态序列上预测逐帧/逐时间步动作类别，并同时确定连续动作片段的边界。

- **Data cutoff:** 2026-07-28
- **Verified conference papers:** 111
- **Preprints / pending verification:** 61
- **Related benchmark or boundary papers:** 2

## Scope and inclusion criteria

纳入的核心工作必须输出稠密动作标签或连续动作片段，并以帧准确率、MoF、Edit、segmental F1、mIoU 或动作边界指标进行评价。仅做整段动作识别、proposal、时序动作定位、时空框检测、图像/人体空间分割或无动作语义的章节切分不进入核心列表。每条正式记录至少保留一个会议proceedings、学会数字图书馆或正式论文页作为验证来源。

会议范围包括 CVPR、ICCV、NeurIPS、ICML、AAAI、IJCAI、ACM MM，以及 ECCV、WACV、BMVC；与 TAS 直接相关的 MICCAI、IROS 等工作置于扩展类别。2026 年只收录在截点前已能由正式 proceedings 确认的论文。arXiv-only 工作严格置于独立的 Pending Verification 区。

## Statistics

| View | Counts |
|---|---|
| By venue | AAAI: 4; ACM MM Workshop: 1; BMVC: 3; CVPR: 39; CVPR Workshop: 3; CVWW: 1; DICTA: 1; ECCV: 11; ICCV: 16; ICCV Workshop: 1; ICME: 1; ICPR: 2; ICRA: 2; IJCAI: 3; IROS: 3; ISKE: 1; MICCAI: 1; NeurIPS: 5; WACV: 13 |
| By year | 2026: 10; 2025: 12; 2024: 17; 2023: 14; 2022: 17; 2021: 11; 2020: 11; 2019: 6; 2018: 5; 2017: 3; 2016: 3; 2015: 1; 2014: 1 |

## Paper index by supervision

这是唯一完整主索引；后面的技术路线和应用场景索引只链接到此处，避免重复维护同一条目。

### Fully Supervised

<a id="paper-2026-cvpr-lady-lagrangian-dynamic-informed-network"></a>
- **LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation** — Haoyu Ji, Xueting Liu, Yu Gao, et al., CVPR 2026.
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.pdf) [arXiv](https://arxiv.org/abs/2603.24097)
  `fully-supervised` `boundary-modeling` `skeleton`
<a id="paper-2026-cvpr-polyphony-diffusion-based-dual-hand"></a>
- **Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning** — Hao Zheng, Hu Wang, Tiantian Zheng, et al., CVPR 2026.
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_Polyphony_Diffusion-based_Dual-Hand_Action_Segmentation_with_Alternating_Vision_Transformer_and_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_Polyphony_Diffusion-based_Dual-Hand_Action_Segmentation_with_Alternating_Vision_Transformer_and_CVPR_2026_paper.pdf) [arXiv](https://arxiv.org/abs/2605.31115)
  `fully-supervised` `Transformer` `diffusion` `unknown` `Breakfast`
<a id="paper-2026-cvpr-spectral-scalpel-amplifying-adjacent-discrepancy"></a>
- **Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation** — Haoyu Ji, Bowen Chen, Zhihao Yang, et al., CVPR 2026.
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.pdf) [arXiv](https://arxiv.org/abs/2603.24134)
  `fully-supervised` `boundary-modeling` `skeleton`
<a id="paper-2026-cvpr-workshop-combining-boundary-supervision-segment-level"></a>
- **Combining Boundary Supervision and Segment-Level Regularization for Fine-Grained Action Segmentation** — Hinako Mitsuoka, Kazuhiro Hotta, CVPR Workshop 2026.
  [Paper](https://openaccess.thecvf.com/content/CVPR2026W/SAUAFG/html/Mitsuoka_Combining_Boundary_Supervision_and_Segment-Level_Regularization_for_Fine-Grained_Action_Segmentation_CVPRW_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026W/SAUAFG/papers/Mitsuoka_Combining_Boundary_Supervision_and_Segment-Level_Regularization_for_Fine-Grained_Action_Segmentation_CVPRW_2026_paper.pdf) [arXiv](https://arxiv.org/abs/2604.01859)
  `fully-supervised` `boundary-modeling` `unknown`
<a id="paper-2026-icra-m2r2-multimodal-robotic-representation"></a>
- **M2R2: MultiModal Robotic Representation for Temporal Action Segmentation** — Daniel Sliwowski, Dongheui Lee, ICRA 2026.
  [Paper](https://dsliwowski1.github.io/) [PDF](https://arxiv.org/pdf/2504.18662) [arXiv](https://arxiv.org/abs/2504.18662)
  `fully-supervised` `multimodal` `prototype-learning` `multimodal`
<a id="paper-2026-wacv-learning-hierarchies-hybrid-geometric-diffusion"></a>
- **Learning Action Hierarchies via Hybrid Geometric Diffusion** — Arjun Ramesh Kaushik, Nalini K. Ratha, Venu Govindaraju, WACV 2026.
  [Paper](https://openaccess.thecvf.com/content/WACV2026/html/Kaushik_Learning_Action_Hierarchies_via_Hybrid_Geometric_Diffusion_WACV_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2026/papers/Kaushik_Learning_Action_Hierarchies_via_Hybrid_Geometric_Diffusion_WACV_2026_paper.pdf) [arXiv](https://arxiv.org/abs/2601.01914)
  `fully-supervised` `diffusion` `unknown`
<a id="paper-2025-aaai-stitch-contrast-segment-learning-human"></a>
- **Stitch, Contrast, and Segment: Learning a Human Action Segmentation Model Using Trimmed Skeleton Videos** — Haitao Tian, Pierre Payeur, AAAI 2025.
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/32792) [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/32792/34947) [arXiv](https://arxiv.org/abs/2412.14988)
  `fully-supervised` `contrastive-learning` `skeleton` `skeleton`
<a id="paper-2025-cvpr-condensing-datasets-generative-network-inversion"></a>
- **Condensing Action Segmentation Datasets via Generative Network Inversion** — Guodong Ding, Rongyu Chen, Angela Yao, CVPR 2025.
  [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_Condensing_Action_Segmentation_Datasets_via_Generative_Network_Inversion_CVPR_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Ding_Condensing_Action_Segmentation_Datasets_via_Generative_Network_Inversion_CVPR_2025_paper.pdf) [arXiv](http://arxiv.org/abs/2503.14112)
  `fully-supervised` `dataset-condensation` `unknown` `Breakfast`
<a id="paper-2025-iccv-duoclr-dual-surrogate-contrastive-learning"></a>
- **DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation** — Haitao Tian, ICCV 2025.
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.pdf) [arXiv](http://arxiv.org/abs/2509.05543)
  `fully-supervised` `unknown` `skeleton`
<a id="paper-2025-iccv-workshop-end-end-transformer"></a>
- **End-to-End Action Segmentation Transformer** — Tieqiao Wang, Sinisa Todorovic, ICCV Workshop 2025.
  [Paper](https://openaccess.thecvf.com/content/ICCV2025W/SVU/html/Wang_End-to-End_Action_Segmentation_Transformer_ICCVW_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025W/SVU/papers/Wang_End-to-End_Action_Segmentation_Transformer_ICCVW_2025_paper.pdf) [arXiv](https://arxiv.org/abs/2503.06316) [Code](https://github.com/tqosu/EAST)
  `fully-supervised` `Transformer` `unknown` `Breakfast` `50Salads`
<a id="paper-2025-iros-multi-modal-graph-convolutional-network"></a>
- **Multi-Modal Graph Convolutional Network with Sinusoidal Encoding for Robust Human Action Segmentation** — Hao Xing, Kai Zhe Boey, Yuankai Wu, et al., IROS 2025.
  [Paper](https://doi.org/10.1109/IROS60139.2025.11245867) [PDF](https://arxiv.org/pdf/2507.00752) [arXiv](https://arxiv.org/abs/2507.00752)
  `fully-supervised` `graphical-model` `multimodal` `skeleton`
<a id="paper-2025-iros-towards-open-world-human-using"></a>
- **Towards Open-World Human Action Segmentation Using Graph Convolutional Networks** — Hao Xing, Kai Zhe Boey, Gordon Cheng, IROS 2025.
  [Paper](https://doi.org/10.1109/IROS60139.2025.11247257) [PDF](https://arxiv.org/pdf/2507.00756) [arXiv](https://arxiv.org/abs/2507.00756)
  `fully-supervised` `clustering` `depth`
<a id="paper-2024-acm-mm-workshop-3d-pose-based-figure-skating"></a>
- **3D Pose-Based Temporal Action Segmentation for Figure Skating: A Fine-Grained and Jump Procedure-Aware Annotation Approach** — Ryota Tanaka, Tomohiro Suzuki, Keisuke Fujii, ACM MM Workshop 2024.
  [Paper](https://dl.acm.org/doi/10.1145/3689061.3689077) [PDF](https://arxiv.org/pdf/2408.16638) [arXiv](https://arxiv.org/abs/2408.16638)
  `fully-supervised` `prototype-learning` `unknown`
<a id="paper-2024-bmvc-cost-sensitive-learning-long-tailed"></a>
- **Cost-Sensitive Learning for Long-Tailed Temporal Action Segmentation** — Zhanzhong Pang, Fadime Sener, Shrinivas Ramasubramanian, et al., BMVC 2024.
  [Paper](https://bmvc2024.org/proceedings/227/) [PDF](https://bmva-archive.org.uk/bmvc/2024/papers/Paper_227/paper.pdf) [arXiv](https://arxiv.org/abs/2503.18358)
  `fully-supervised` `duration-modeling` `unknown`
<a id="paper-2024-cvpr-coherent-synthesis-incremental"></a>
- **Coherent Temporal Synthesis for Incremental Action Segmentation** — Guodong Ding, Hans Golong, Angela Yao, CVPR 2024.
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.pdf) [arXiv](http://arxiv.org/abs/2403.06102)
  `fully-supervised` `unknown` `unknown` `Breakfast`
<a id="paper-2024-cvpr-fact-frame-cross-attention-modeling"></a>
- **FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation** — Zijia Lu, Ehsan Elhamifar, CVPR 2024.
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.pdf) [Code](https://github.com/ZijiaLewisLu/CVPR2024-FACT)
  `fully-supervised` `Transformer` `cross-attention` `unknown`
<a id="paper-2024-cvpr-progress-aware-online-egocentric-procedural"></a>
- **Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos** — Yuhan Shen, Ehsan Elhamifar, CVPR 2024.
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.pdf)
  `fully-supervised` `causal-model` `unknown`
<a id="paper-2024-eccv-language-assisted-skeleton-understanding-skeleton"></a>
- **Language-Assisted Skeleton Action Understanding for Skeleton-Based Temporal Action Segmentation** — Haoyu Ji, Bowen Chen, Xinglong Xu, et al., ECCV 2024.
  [Paper](https://eccv.ecva.net/virtual/2024/poster/1462) [PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07145.pdf)
  `fully-supervised` `language-model` `contrastive-learning` `skeleton`
<a id="paper-2024-eccv-long-tail-group-wise-logit"></a>
- **Long-Tail Temporal Action Segmentation with Group-wise Temporal Logit Adjustment** — Zhanzhong Pang, Fadime Sener, Shrinivas Ramasubramanian, et al., ECCV 2024.
  [Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4389_ECCV_2024_paper.php) [PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04389.pdf) [arXiv](https://arxiv.org/abs/2408.09919) [Code](https://github.com/pangzhan27/GTLA)
  `fully-supervised` `duration-modeling` `unknown`
<a id="paper-2024-icra-using-2d-skeleton-heatmaps-multi"></a>
- **Action Segmentation Using 2D Skeleton Heatmaps and Multi-Modality Fusion** — Syed Waleed Hyder, Muhammad Usama, Anas Zafar, et al., ICRA 2024.
  [Paper](https://doi.org/10.1109/ICRA57147.2024.10610644) [PDF](https://arxiv.org/pdf/2309.06462) [arXiv](https://arxiv.org/abs/2309.06462)
  `fully-supervised` `TCN` `skeleton`
<a id="paper-2024-neurips-actfusion-unified-diffusion-model-anticipation"></a>
- **ActFusion: a Unified Diffusion Model for Action Segmentation and Anticipation** — Dayoung Gong, Suha Kwak, Minsu Cho, NeurIPS 2024.
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a3a661eb3308d0bb686f6a4bac521032-Abstract-Conference.html) [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3a661eb3308d0bb686f6a4bac521032-Paper-Conference.pdf) [arXiv](https://arxiv.org/abs/2412.04353)
  `fully-supervised` `diffusion` `VQ-tokenization` `unknown` `Breakfast` `GTEA`
<a id="paper-2024-neurips-efficient-boundary-aware-query-voting"></a>
- **Efficient Temporal Action Segmentation via Boundary-aware Query Voting** — Peiyao Wang, Yuewei Lin, Erik Blasch, et al., NeurIPS 2024.
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/42770daf4a3384b712ea9c36e9279998-Abstract-Conference.html) [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/42770daf4a3384b712ea9c36e9279998-Paper-Conference.pdf) [arXiv](https://arxiv.org/abs/2405.15995) [Code](https://github.com/peiyao-w/BaFormer)
  `fully-supervised` `Transformer` `boundary-modeling` `unknown`
<a id="paper-2024-neurips-onlinetas-online-baseline"></a>
- **OnlineTAS: An Online Baseline for Temporal Action Segmentation** — Shijie Li, Yazan Abu Farha, Juergen Gall, NeurIPS 2024.
  [Paper](https://papers.nips.cc/paper_files/paper/2024/hash/6c6c5fccf3c8661fcae219be7ca226f7-Abstract-Conference.html) [PDF](https://papers.nips.cc/paper_files/paper/2024/file/6c6c5fccf3c8661fcae219be7ca226f7-Paper-Conference.pdf) [arXiv](https://arxiv.org/abs/2411.01122)
  `fully-supervised` `TCN` `causal-model` `unknown`
<a id="paper-2023-cvpr-aspnet-shared-private-representation-multiple"></a>
- **ASPnet: Action Segmentation With Shared-Private Representation of Multiple Data Sources** — Beatrice van Amsterdam, Abdolrahim Kadkhodamohammadi, Imanol Luengo, et al., CVPR 2023.
  [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/van_Amsterdam_ASPnet_Action_Segmentation_With_Shared-Private_Representation_of_Multiple_Data_Sources_CVPR_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/van_Amsterdam_ASPnet_Action_Segmentation_With_Shared-Private_Representation_of_Multiple_Data_Sources_CVPR_2023_paper.pdf)
  `fully-supervised` `unknown` `multimodal` `Breakfast` `50Salads`
<a id="paper-2023-iccv-diffusion"></a>
- **Diffusion Action Segmentation** — Daochang Liu, Qiyue Li, Anh-Dung Dinh, et al., ICCV 2023.
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.pdf) [arXiv](https://arxiv.org/abs/2303.17959) [Code](https://github.com/Finspire13/DiffAct)
  `fully-supervised` `diffusion` `boundary-modeling` `unknown` `Breakfast` `50Salads`
<a id="paper-2023-iccv-how-much-long-term-context"></a>
- **How Much Temporal Long-Term Context is Needed for Action Segmentation?** — Emad Bahrami, Gianpiero Francesca, Juergen Gall, ICCV 2023.
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Bahrami_How_Much_Temporal_Long-Term_Context_is_Needed_for_Action_Segmentation_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Bahrami_How_Much_Temporal_Long-Term_Context_is_Needed_for_Action_Segmentation_ICCV_2023_paper.pdf) [arXiv](https://arxiv.org/abs/2308.11358)
  `fully-supervised` `Transformer` `TCN` `unknown` `Breakfast` `50Salads`
<a id="paper-2023-iccv-markov-game-augmentation"></a>
- **Markov Game Video Augmentation for Action Segmentation** — Nicolas Aziere, Sinisa Todorovic, ICCV 2023.
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Aziere_Markov_Game_Video_Augmentation_for_Action_Segmentation_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Aziere_Markov_Game_Video_Augmentation_for_Action_Segmentation_ICCV_2023_paper.pdf)
  `fully-supervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2023-iccv-contextually-refined-keypoints"></a>
- **Video Action Segmentation via Contextually Refined Temporal Keypoints** — Borui Jiang, Yang Jin, Zhentao Tan, et al., ICCV 2023.
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.pdf)
  `fully-supervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2023-iske-streaming-real-time"></a>
- **Streaming Video Temporal Action Segmentation in Real Time** — Wujun Wen, Yunheng Li, Zhuben Dong, et al., ISKE 2023.
  [Paper](https://doi.org/10.1109/ISKE60036.2023.10481438) [PDF](https://arxiv.org/pdf/2209.13808) [arXiv](https://arxiv.org/abs/2209.13808)
  `fully-supervised` `TCN` `causal-model` `multimodal`
<a id="paper-2023-neurips-activity-grammars"></a>
- **Activity Grammars for Temporal Action Segmentation** — Dayoung Gong, Joonseok Lee, Deunsol Jung, et al., NeurIPS 2023.
  [Paper](https://papers.nips.cc/paper_files/paper/2023/hash/ee6c4b99b4c0d3d60efd22c1ecdd9891-Abstract-Conference.html) [PDF](https://papers.nips.cc/paper_files/paper/2023/file/ee6c4b99b4c0d3d60efd22c1ecdd9891-Paper-Conference.pdf) [arXiv](https://arxiv.org/abs/2312.04266) [Code](http://cvlab.postech.ac.kr/research/KARI)
  `fully-supervised` `structured-decoding` `unknown` `Breakfast`
<a id="paper-2022-cvpr-set-supervised-learning-procedural-task"></a>
- **Set-Supervised Action Learning in Procedural Task Videos via Pairwise Order Consistency** — Zijia Lu, Ehsan Elhamifar, CVPR 2022.
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lu_Set-Supervised_Action_Learning_in_Procedural_Task_Videos_via_Pairwise_Order_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lu_Set-Supervised_Action_Learning_in_Procedural_Task_Videos_via_Pairwise_Order_CVPR_2022_paper.pdf)
  `fully-supervised` `unknown` `unknown`
<a id="paper-2022-ijcai-uncertainty-aware-representation-learning"></a>
- **Uncertainty-Aware Representation Learning for Action Segmentation** — Lei Chen, Muheng Li, Yueqi Duan, et al., IJCAI 2022.
  [Paper](https://www.ijcai.org/proceedings/2022/115) [PDF](https://www.ijcai.org/proceedings/2022/0115.pdf)
  `fully-supervised` `uncertainty-modeling` `boundary-modeling` `unknown`
<a id="paper-2022-neurips-don-t-pour-cereal-into"></a>
- **Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation** — Ziwei Xu, Yogesh S. Rawat, Yongkang Wong, et al., NeurIPS 2022.
  [Paper](https://openreview.net/forum?id=PCQyUvAmKs) [PDF](https://openreview.net/pdf?id=PCQyUvAmKs) [Code](https://diff-tl.github.io/)
  `fully-supervised` `structured-decoding` `unknown`
<a id="paper-2021-bmvc-asformer-transformer"></a>
- **ASFormer: Transformer for Action Segmentation** — Fangqiu Yi, Hongyu Wen, Tingting Jiang, BMVC 2021.
  [Paper](https://www.bmvc2021-virtualconference.com/conference/papers/paper_0578.html) [PDF](https://www.bmvc2021-virtualconference.com/assets/papers/0578.pdf) [arXiv](https://arxiv.org/abs/2110.08568) [Code](https://github.com/ChinaYi/ASFormer)
  `fully-supervised` `Transformer` `unknown`
<a id="paper-2021-cvpr-anchor-constrained-viterbi-set-supervised"></a>
- **Anchor-Constrained Viterbi for Set-Supervised Action Segmentation** — Jun Li, Sinisa Todorovic, CVPR 2021.
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Anchor-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Anchor-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2021_paper.pdf) [arXiv](http://arxiv.org/abs/2104.02113)
  `fully-supervised` `structured-decoding` `IMU` `Breakfast`
<a id="paper-2021-cvpr-global2local-efficient-structure-search"></a>
- **Global2Local: Efficient Structure Search for Video Action Segmentation** — Shang-Hua Gao, Qi Han, Zhong-Yu Li, et al., CVPR 2021.
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Gao_Global2Local_Efficient_Structure_Search_for_Video_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Gao_Global2Local_Efficient_Structure_Search_for_Video_Action_Segmentation_CVPR_2021_paper.pdf) [arXiv](http://arxiv.org/abs/2101.00910) [Code](https://github.com/Thinksky5124/G2L)
  `fully-supervised` `unknown` `unknown`
<a id="paper-2021-iccv-refining-hierarchical-representations"></a>
- **Refining Action Segmentation With Hierarchical Video Representations** — Hyemin Ahn, Dongheui Lee, ICCV 2021.
  [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Ahn_Refining_Action_Segmentation_With_Hierarchical_Video_Representations_ICCV_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Ahn_Refining_Action_Segmentation_With_Hierarchical_Video_Representations_ICCV_2021_paper.pdf)
  `fully-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2020-cvpr-improving-graph-based-reasoning"></a>
- **Improving Action Segmentation via Graph-Based Temporal Reasoning** — Yifei Huang, Yusuke Sugano, Yoichi Sato, CVPR 2020.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.pdf)
  `fully-supervised` `boundary-modeling` `unknown` `Breakfast` `50Salads`
<a id="paper-2020-eccv-boundary-aware-cascade-networks"></a>
- **Boundary-Aware Cascade Networks for Temporal Action Segmentation** — Zhenzhi Wang, Ziteng Gao, Limin Wang, et al., ECCV 2020.
  [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/35_ECCV_2020_paper.php) [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123700035.pdf) [Code](https://github.com/MCG-NJU/BCN)
  `fully-supervised` `boundary-modeling` `unknown`
<a id="paper-2020-eccv-aggregate-representations-long-range-understanding"></a>
- **Temporal Aggregate Representations for Long-Range Video Understanding** — Fadime Sener, Dipika Singhania, Angela Yao, ECCV 2020.
  [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/154_ECCV_2020_paper.php) [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610154.pdf)
  `fully-supervised` `TCN` `unknown`
<a id="paper-2020-miccai-tecno-surgical-phase-recognition-multi"></a>
- **TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks** — Tobias Czempiel, Magdalini Paschali, Matthias Keicher, et al., MICCAI 2020.
  [Paper](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_33) [Code](https://github.com/tobiascz/MICCAI2020-TeCNO)
  `fully-supervised` `TCN` `multi-stage-TCN` `unknown` `Cholec80`
<a id="paper-2020-wacv-mixed-domain-adaptation"></a>
- **Action Segmentation with Mixed Temporal Domain Adaptation** — Min-Hung Chen, Baopu Li, Yingze Bao, et al., WACV 2020.
  [Paper](https://openaccess.thecvf.com/content_WACV_2020/html/Chen_Action_Segmentation_with_Mixed_Temporal_Domain_Adaptation_WACV_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_WACV_2020/papers/Chen_Action_Segmentation_with_Mixed_Temporal_Domain_Adaptation_WACV_2020_paper.pdf) [arXiv](https://arxiv.org/abs/2104.07461)
  `fully-supervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2020-wacv-stacked-spatio-graph-convolutional-networks"></a>
- **Stacked Spatio-Temporal Graph Convolutional Networks for Action Segmentation** — Pallabi Ghosh, Yi Yao, Larry Davis, et al., WACV 2020.
  [Paper](https://openaccess.thecvf.com/content_WACV_2020/html/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_WACV_2020/papers/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.pdf) [arXiv](https://arxiv.org/abs/1811.10575)
  `fully-supervised` `unknown` `skeleton`
<a id="paper-2019-cvpr-ms-tcn-multi-stage-convolutional"></a>
- **MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation** — Yazan Abu Farha, Jurgen Gall, CVPR 2019.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.pdf) [arXiv](https://arxiv.org/abs/1903.01945) [Code](https://github.com/yabufarha/ms-tcn)
  `fully-supervised` `TCN` `multi-stage-TCN` `unknown` `Breakfast` `50Salads`
<a id="paper-2019-wacv-coupled-generative-adversarial-network-continuous"></a>
- **Coupled Generative Adversarial Network for Continuous Fine-Grained Action Segmentation** — Harshala Gammulle, Tharindu Fernando, Simon Denman, et al., WACV 2019.
  [Paper](https://doi.org/10.1109/WACV.2019.00027) [PDF](https://arxiv.org/pdf/1909.09283) [arXiv](https://arxiv.org/abs/1909.09283)
  `fully-supervised` `GAN` `multimodal` `multimodal`
<a id="paper-2018-wacv-end-end-fine-grained-recognition"></a>
- **End-to-End Fine-Grained Action Segmentation and Recognition Using Conditional Random Field Models and Discriminative Sparse Coding** — Effrosyni Mavroudi, Divya Bhaskara, Shahin Sefati, et al., WACV 2018.
  [Paper](https://doi.org/10.1109/WACV.2018.00174) [PDF](https://arxiv.org/pdf/1801.09571) [arXiv](https://arxiv.org/abs/1801.09571)
  `fully-supervised` `structured-decoding` `unknown`
<a id="paper-2017-cvpr-convolutional-networks-detection"></a>
- **Temporal Convolutional Networks for Action Segmentation and Detection** — Colin Lea, Michael D. Flynn, Rene Vidal, et al., CVPR 2017.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2017/papers/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.pdf) [arXiv](https://arxiv.org/abs/1611.05267)
  `fully-supervised` `duration-modeling` `TCN` `unknown`
<a id="paper-2017-dicta-parsing-using-context-features"></a>
- **Action Parsing Using Context Features** — Nagita Mehrseresht, DICTA 2017.
  [Paper](https://doi.org/10.1109/DICTA.2017.8227399) [PDF](https://arxiv.org/pdf/2205.10008) [arXiv](https://arxiv.org/abs/2205.10008)
  `fully-supervised` `structured-decoding` `unknown` `Breakfast`
<a id="paper-2016-eccv-segmental-spatiotemporal-cnns-fine-grained"></a>
- **Segmental Spatiotemporal CNNs for Fine-Grained Action Segmentation** — Colin Lea, Austin Reiter, Rene Vidal, et al., ECCV 2016.
  [Paper](https://link.springer.com/chapter/10.1007/978-3-319-46487-9_3) [PDF](https://arxiv.org/pdf/1602.02995) [arXiv](https://arxiv.org/abs/1602.02995)
  `fully-supervised` `structured-decoding` `unknown`
<a id="paper-2014-cvpr-leveraging-hierarchical-parametric-networks-skeletal"></a>
- **Leveraging Hierarchical Parametric Networks for Skeletal Joints Based Action Segmentation and Recognition** — Di Wu, Ling Shao, CVPR 2014.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2014/html/Wu_Leveraging_Hierarchical_Parametric_2014_CVPR_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2014/papers/Wu_Leveraging_Hierarchical_Parametric_2014_CVPR_paper.pdf)
  `fully-supervised` `unknown` `IMU`

### Weakly Supervised

<a id="paper-2026-cvpr-hierarchical-learning-weakly-supervised"></a>
- **Hierarchical Action Learning for Weakly-Supervised Action Segmentation** — Junxian Huang, Ruichu Cai, Juntao Fang, et al., CVPR 2026.
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Hierarchical_Action_Learning_for_Weakly-Supervised_Action_Segmentation_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Hierarchical_Action_Learning_for_Weakly-Supervised_Action_Segmentation_CVPR_2026_paper.pdf) [arXiv](https://arxiv.org/abs/2602.24275)
  `weakly-supervised` `Transformer` `causal-model` `unknown`
<a id="paper-2026-wacv-timestamp-query-transformer"></a>
- **Timestamp Query Transformer for Temporal Action Segmentation** — Tieqiao Wang, Sinisa Todorovic, WACV 2026.
  [Paper](https://openaccess.thecvf.com/content/WACV2026/html/Wang_Timestamp_Query_Transformer_for_Temporal_Action_Segmentation_WACV_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2026/papers/Wang_Timestamp_Query_Transformer_for_Temporal_Action_Segmentation_WACV_2026_paper.pdf)
  `timestamp-supervised` `Transformer` `cross-attention` `unknown` `Breakfast` `50Salads`
<a id="paper-2025-cvpr-workshop-pose-aware-weakly-supervised"></a>
- **Pose-Aware Weakly-Supervised Action Segmentation** — Zhihao Zhao, Reza Ghoddoosian, Isht Dwivedi, et al., CVPR Workshop 2025.
  [Paper](https://openaccess.thecvf.com/content/CVPR2025W/MULA2025/html/Zhao_Pose-Aware_Weakly-Supervised_Action_Segmentation_CVPRW_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2025W/MULA2025/papers/Zhao_Pose-Aware_Weakly-Supervised_Action_Segmentation_CVPRW_2025_paper.pdf) [arXiv](https://arxiv.org/abs/2504.05700)
  `weakly-supervised` `contrastive-learning` `boundary-modeling` `unknown`
<a id="paper-2024-cvpr-efficient-effective-weakly-supervised-transition"></a>
- **Efficient and Effective Weakly-Supervised Action Segmentation via Action-Transition-Aware Boundary Alignment** — Angchi Xu, Wei-Shi Zheng, CVPR 2024.
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Efficient_and_Effective_Weakly-Supervised_Action_Segmentation_via_Action-Transition-Aware_Boundary_Alignment_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Efficient_and_Effective_Weakly-Supervised_Action_Segmentation_via_Action-Transition-Aware_Boundary_Alignment_CVPR_2024_paper.pdf) [arXiv](http://arxiv.org/abs/2403.19225)
  `weakly-supervised` `boundary-modeling` `unknown`
<a id="paper-2024-wacv-random-walks-timestamp-supervision"></a>
- **Random Walks for Temporal Action Segmentation With Timestamp Supervision** — Roy Hirsch, Regev Cohen, Tomer Golany, et al., WACV 2024.
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Hirsch_Random_Walks_for_Temporal_Action_Segmentation_With_Timestamp_Supervision_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Hirsch_Random_Walks_for_Temporal_Action_Segmentation_With_Timestamp_Supervision_WACV_2024_paper.pdf)
  `timestamp-supervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2023-cvpr-reducing-label-bias-timestamp-supervised"></a>
- **Reducing the Label Bias for Timestamp Supervised Temporal Action Segmentation** — Kaiyuan Liu, Yunheng Li, Shenglan Liu, et al., CVPR 2023.
  [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_Reducing_the_Label_Bias_for_Timestamp_Supervised_Temporal_Action_Segmentation_CVPR_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_Reducing_the_Label_Bias_for_Timestamp_Supervised_Temporal_Action_Segmentation_CVPR_2023_paper.pdf)
  `timestamp-supervised` `unknown` `unknown`
<a id="paper-2023-iccv-weakly-supervised-unseen-error-detection"></a>
- **Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos** — Reza Ghoddoosian, Isht Dwivedi, Nakul Agarwal, et al., ICCV 2023.
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.pdf)
  `weakly-supervised` `structured-decoding` `unknown`
<a id="paper-2023-ijcai-hoi-aware-adaptive-network-weakly"></a>
- **HOI-aware Adaptive Network for Weakly-supervised Action Segmentation** — Runzhong Zhang, Suchen Wang, Yueqi Duan, et al., IJCAI 2023.
  [Paper](https://www.ijcai.org/proceedings/2023/191) [PDF](https://www.ijcai.org/proceedings/2023/0191.pdf) [arXiv](https://arxiv.org/abs/2604.26227)
  `weakly-supervised` `hypernetwork` `HOI` `unknown` `Breakfast` `50Salads`
<a id="paper-2023-ijcai-timestamp-supervised-perspective-clustering"></a>
- **Timestamp-Supervised Action Segmentation in the Perspective of Clustering** — Dazhao Du, Enhan Li, Lingyu Si, et al., IJCAI 2023.
  [Paper](https://www.ijcai.org/proceedings/2023/77) [PDF](https://www.ijcai.org/proceedings/2023/0077.pdf) [arXiv](https://arxiv.org/abs/2212.11694) [Code](https://github.com/ddz16/TSASPC)
  `timestamp-supervised` `clustering` `unknown`
<a id="paper-2022-bmvc-robust-timestamp-supervision"></a>
- **Robust Action Segmentation from Timestamp Supervision** — Yaser Souri, Yazan Abu Farha, Emad Bahrami, et al., BMVC 2022.
  [Paper](https://bmvc2022.mpi-inf.mpg.de/392/) [PDF](https://bmvc2022.mpi-inf.mpg.de/0392.pdf) [arXiv](https://arxiv.org/abs/2210.06501)
  `timestamp-supervised` `TCN` `boundary-modeling` `unknown`
<a id="paper-2022-cvpr-semi-weakly-supervised-learning-complex"></a>
- **Semi-Weakly-Supervised Learning of Complex Actions From Instructional Task Videos** — Yuhan Shen, Ehsan Elhamifar, CVPR 2022.
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shen_Semi-Weakly-Supervised_Learning_of_Complex_Actions_From_Instructional_Task_Videos_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Shen_Semi-Weakly-Supervised_Learning_of_Complex_Actions_From_Instructional_Task_Videos_CVPR_2022_paper.pdf)
  `weakly-supervised` `unknown` `unknown`
<a id="paper-2022-cvpr-weakly-supervised-online-multi-view"></a>
- **Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos** — Reza Ghoddoosian, Isht Dwivedi, Nakul Agarwal, et al., CVPR 2022.
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Ghoddoosian_Weakly-Supervised_Online_Action_Segmentation_in_Multi-View_Instructional_Videos_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Ghoddoosian_Weakly-Supervised_Online_Action_Segmentation_in_Multi-View_Instructional_Videos_CVPR_2022_paper.pdf) [arXiv](http://arxiv.org/abs/2203.13309)
  `weakly-supervised` `unknown` `unknown` `Breakfast` `IKEA ASM`
<a id="paper-2022-eccv-generalized-robust-framework-timestamp-supervision"></a>
- **A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation** — Rahul Rahaman, Dipika Singhania, Alexandre Thiery, et al., ECCV 2022.
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4788_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136640276.pdf) [arXiv](https://arxiv.org/abs/2207.10137) [Code](https://github.com/rahulrahaman/Timestamp-and-SkipTag)
  `timestamp-supervised` `TCN` `uncertainty-modeling` `unknown`
<a id="paper-2022-eccv-unified-fully-timestamp-supervised-sequence"></a>
- **Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation** — Nadine Behrmann, S. Alireza Golestaneh, Zico Kolter, et al., ECCV 2022.
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3672_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950052.pdf) [arXiv](https://arxiv.org/abs/2209.00638)
  `timestamp-supervised` `Transformer` `duration-modeling` `unknown`
<a id="paper-2022-icme-turning-teacher-timestamp-supervised"></a>
- **Turning to a Teacher for Timestamp Supervised Temporal Action Segmentation** — Yang Zhao, Yan Song, ICME 2022.
  [Paper](https://doi.org/10.1109/ICME52920.2022.9859626) [PDF](https://arxiv.org/pdf/2207.00712) [arXiv](https://arxiv.org/abs/2207.00712)
  `timestamp-supervised` `teacher-student` `boundary-modeling` `unknown`
<a id="paper-2022-iros-timestamp-supervised-graph-convolutional-networks"></a>
- **Timestamp-Supervised Action Segmentation with Graph Convolutional Networks** — Hamza Khan, Sanjay Haresh, Awais Ahmed, et al., IROS 2022.
  [Paper](https://doi.org/10.1109/IROS47612.2022.9981351) [PDF](https://arxiv.org/pdf/2206.15031) [arXiv](https://arxiv.org/abs/2206.15031)
  `timestamp-supervised` `graphical-model` `TCN` `unknown` `Breakfast` `GTEA`
<a id="paper-2022-wacv-hierarchical-modeling-task-recognition-weakly"></a>
- **Hierarchical Modeling for Task Recognition and Action Segmentation in Weakly-Labeled Instructional Videos** — Reza Ghoddoosian, Saif Sayed, Vassilis Athitsos, WACV 2022.
  [Paper](https://openaccess.thecvf.com/content/WACV2022/html/Ghoddoosian_Hierarchical_Modeling_for_Task_Recognition_and_Action_Segmentation_in_Weakly-Labeled_WACV_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2022/papers/Ghoddoosian_Hierarchical_Modeling_for_Task_Recognition_and_Action_Segmentation_in_Weakly-Labeled_WACV_2022_paper.pdf) [arXiv](http://arxiv.org/abs/2110.05697)
  `weakly-supervised` `unknown` `unknown` `Breakfast`
<a id="paper-2022-wacv-sscap-self-supervised-co-occurrence"></a>
- **SSCAP: Self-Supervised Co-Occurrence Action Parsing for Unsupervised Temporal Action Segmentation** — Zhe Wang, Hao Chen, Xinyu Li, et al., WACV 2022.
  [Paper](https://openaccess.thecvf.com/content/WACV2022/html/Wang_SSCAP_Self-Supervised_Co-Occurrence_Action_Parsing_for_Unsupervised_Temporal_Action_Segmentation_WACV_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2022/papers/Wang_SSCAP_Self-Supervised_Co-Occurrence_Action_Parsing_for_Unsupervised_Temporal_Action_Segmentation_WACV_2022_paper.pdf) [arXiv](https://arxiv.org/abs/2105.14158)
  `weakly-supervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2021-cvpr-learning-discriminative-prototypes-dynamic-time"></a>
- **Learning Discriminative Prototypes With Dynamic Time Warping** — Xiaobin Chang, Frederick Tung, Greg Mori, CVPR 2021.
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Chang_Learning_Discriminative_Prototypes_With_Dynamic_Time_Warping_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Chang_Learning_Discriminative_Prototypes_With_Dynamic_Time_Warping_CVPR_2021_paper.pdf)
  `weakly-supervised` `prototype-learning` `I3D-features`
<a id="paper-2021-cvpr-timestamp-supervision"></a>
- **Temporal Action Segmentation From Timestamp Supervision** — Zhe Li, Yazan Abu Farha, Jurgen Gall, CVPR 2021.
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.pdf) [arXiv](https://arxiv.org/abs/2103.06669)
  `timestamp-supervised` `unknown` `I3D-features`
<a id="paper-2021-iccv-weakly-supervised-alignment-transcript-aware"></a>
- **Weakly-Supervised Action Segmentation and Alignment via Transcript-Aware Union-of-Subspaces Learning** — Zijia Lu, Ehsan Elhamifar, ICCV 2021.
  [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Lu_Weakly-Supervised_Action_Segmentation_and_Alignment_via_Transcript-Aware_Union-of-Subspaces_Learning_ICCV_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Lu_Weakly-Supervised_Action_Segmentation_and_Alignment_via_Transcript-Aware_Union-of-Subspaces_Learning_ICCV_2021_paper.pdf)
  `weakly-supervised` `duration-modeling` `I3D-features`
<a id="paper-2020-cvpr-sct-set-constrained-transformer-set"></a>
- **SCT: Set Constrained Temporal Transformer for Set Supervised Action Segmentation** — Mohsen Fayyaz, Jurgen Gall, CVPR 2020.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Fayyaz_SCT_Set_Constrained_Temporal_Transformer_for_Set_Supervised_Action_Segmentation_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fayyaz_SCT_Set_Constrained_Temporal_Transformer_for_Set_Supervised_Action_Segmentation_CVPR_2020_paper.pdf) [arXiv](https://arxiv.org/abs/2003.14266)
  `weakly-supervised` `Transformer` `unknown`
<a id="paper-2020-cvpr-set-constrained-viterbi-set-supervised"></a>
- **Set-Constrained Viterbi for Set-Supervised Action Segmentation** — Jun Li, Sinisa Todorovic, CVPR 2020.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Set-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Li_Set-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2020_paper.pdf) [arXiv](http://arxiv.org/abs/2002.11925)
  `weakly-supervised` `structured-decoding` `unknown` `Breakfast`
<a id="paper-2020-eccv-fast-weakly-supervised-using-mutual"></a>
- **Fast Weakly Supervised Action Segmentation Using Mutual Consistency** — Yaser Souri, Mohsen Fayyaz, Luca Minciullo, et al., ECCV 2020.
  [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1061_ECCV_2020_paper.php) [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123570664.pdf) [arXiv](https://arxiv.org/abs/1904.03116) [Code](https://github.com/yassersouri/MuCon)
  `weakly-supervised` `TCN` `structured-decoding` `unknown`
<a id="paper-2019-cvpr-d3tw-discriminative-differentiable-dynamic-time"></a>
- **D3TW: Discriminative Differentiable Dynamic Time Warping for Weakly Supervised Action Alignment and Segmentation** — Chien-Yi Chang, De-An Huang, Yanan Sui, et al., CVPR 2019.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Chang_D3TW_Discriminative_Differentiable_Dynamic_Time_Warping_for_Weakly_Supervised_Action_CVPR_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Chang_D3TW_Discriminative_Differentiable_Dynamic_Time_Warping_for_Weakly_Supervised_Action_CVPR_2019_paper.pdf)
  `weakly-supervised` `unknown` `unknown`
<a id="paper-2019-iccv-weakly-supervised-energy-based-learning"></a>
- **Weakly Supervised Energy-Based Learning for Action Segmentation** — Jun Li, Peng Lei, Sinisa Todorovic, ICCV 2019.
  [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Li_Weakly_Supervised_Energy-Based_Learning_for_Action_Segmentation_ICCV_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Li_Weakly_Supervised_Energy-Based_Learning_for_Action_Segmentation_ICCV_2019_paper.pdf) [arXiv](https://arxiv.org/abs/1909.13155)
  `weakly-supervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2018-cvpr-sets-weakly-supervised-without-ordering"></a>
- **Action Sets: Weakly Supervised Action Segmentation Without Ordering Constraints** — Alexander Richard, Hilde Kuehne, Juergen Gall, CVPR 2018.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_Action_Sets_Weakly_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Richard_Action_Sets_Weakly_CVPR_2018_paper.pdf) [arXiv](http://arxiv.org/abs/1706.00699v2)
  `weakly-supervised` `unknown` `unknown`
<a id="paper-2018-cvpr-neuralnetwork-viterbi-framework-weakly-supervised"></a>
- **NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning** — Alexander Richard, Hilde Kuehne, Ahsan Iqbal, et al., CVPR 2018.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.pdf) [arXiv](https://arxiv.org/abs/arXiv:1805.06875)
  `weakly-supervised` `structured-decoding` `unknown`
<a id="paper-2018-cvpr-unsupervised-learning-complex-activities"></a>
- **Unsupervised Learning and Segmentation of Complex Activities From Video** — Fadime Sener, Angela Yao, CVPR 2018.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Sener_Unsupervised_Learning_and_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Sener_Unsupervised_Learning_and_CVPR_2018_paper.pdf) [arXiv](http://arxiv.org/abs/1803.09490v1)
  `weakly-supervised` `unknown` `unknown` `Breakfast`
<a id="paper-2018-cvpr-weakly-supervised-iterative-soft-boundary"></a>
- **Weakly-Supervised Action Segmentation With Iterative Soft Boundary Assignment** — Li Ding, Chenliang Xu, CVPR 2018.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Ding_Weakly-Supervised_Action_Segmentation_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Ding_Weakly-Supervised_Action_Segmentation_CVPR_2018_paper.pdf) [arXiv](http://arxiv.org/abs/1803.10699v1)
  `weakly-supervised` `boundary-modeling` `TCN` `unknown` `Breakfast`
<a id="paper-2017-cvpr-weakly-supervised-learning-rnn-based"></a>
- **Weakly Supervised Action Learning With RNN Based Fine-To-Coarse Modeling** — Alexander Richard, Hilde Kuehne, Juergen Gall, CVPR 2017.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Richard_Weakly_Supervised_Action_CVPR_2017_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2017/papers/Richard_Weakly_Supervised_Action_CVPR_2017_paper.pdf) [arXiv](http://arxiv.org/abs/1703.08132v3)
  `weakly-supervised` `unknown` `unknown` `Breakfast`
<a id="paper-2016-eccv-connectionist-modeling-weakly-supervised-labeling"></a>
- **Connectionist Temporal Modeling for Weakly Supervised Action Labeling** — De-An Huang, Fei-Fei Li, Juan Carlos Niebles, ECCV 2016.
  [Paper](https://www.ecva.net/papers/eccv_2016/papers_ECCV/html/Huang_Connectionist_Temporal_Modeling_ECCV_2016_paper.php) [PDF](https://www.ecva.net/papers/eccv_2016/papers_ECCV/papers/123560511.pdf)
  `weakly-supervised` `TCN` `structured-decoding` `unknown`

### Semi-Supervised

<a id="paper-2026-icpr-improving-constraint-aware-decoding"></a>
- **Improving Temporal Action Segmentation via Constraint-Aware Decoding** — Yeo Keat Ee, Debaditya Roy, Chen Li, et al., ICPR 2026.
  [Paper](https://icpr2026.org/acceptedPapersTrack.html) [PDF](https://arxiv.org/pdf/2605.10149) [arXiv](https://arxiv.org/abs/2605.10149) [Code](https://github.com/LUNAProject22/CAD)
  `semi-supervised` `boundary-modeling` `duration-modeling` `unknown`
<a id="paper-2022-aaai-iterative-contrast-classify-semi-supervised"></a>
- **Iterative Contrast-Classify for Semi-Supervised Temporal Action Segmentation** — Dipika Singhania, Rahul Rahaman, Angela Yao, AAAI 2022.
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/20124) [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/20124/19883) [arXiv](https://arxiv.org/abs/2112.01402) [Code](https://github.com/dipika-singhania/ICC-Semi-Supervised-TAS)
  `semi-supervised` `clustering` `TCN` `unknown` `Breakfast` `50Salads`
<a id="paper-2022-eccv-leveraging-affinity-continuity-semi-supervised"></a>
- **Leveraging Action Affinity and Continuity for Semi-Supervised Temporal Action Segmentation** — Guodong Ding, Angela Yao, ECCV 2022.
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3254_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950017.pdf) [arXiv](https://arxiv.org/abs/2207.08653) [Code](https://github.com/dinggd/semitas)
  `semi-supervised` `boundary-modeling` `unknown`

### Self-Supervised

<a id="paper-2025-iccv-joint-self-supervised-alignment"></a>
- **Joint Self-Supervised Video Alignment and Action Segmentation** — Ali Shah Ali, Syed Ahmed Mahmood, Mubin Saeed, et al., ICCV 2025.
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ali_Joint_Self-Supervised_Video_Alignment_and_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ali_Joint_Self-Supervised_Video_Alignment_and_Action_Segmentation_ICCV_2025_paper.pdf) [arXiv](http://arxiv.org/abs/2503.16832)
  `self-supervised` `optimal-transport` `IMU`
<a id="paper-2024-wacv-otas-unsupervised-boundary-detection-object"></a>
- **OTAS: Unsupervised Boundary Detection for Object-Centric Temporal Action Segmentation** — Yuerong Li, Zhengrong Xue, Huazhe Xu, WACV 2024.
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Li_OTAS_Unsupervised_Boundary_Detection_for_Object-Centric_Temporal_Action_Segmentation_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Li_OTAS_Unsupervised_Boundary_Detection_for_Object-Centric_Temporal_Action_Segmentation_WACV_2024_paper.pdf) [arXiv](http://arxiv.org/abs/2309.06276)
  `self-supervised` `boundary-modeling` `unknown`
<a id="paper-2023-iccv-lac-latent-composition-skeleton-based"></a>
- **LAC - Latent Action Composition for Skeleton-based Action Segmentation** — Di Yang, Yaohui Wang, Antitza Dantcheva, et al., ICCV 2023.
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.pdf) [arXiv](http://arxiv.org/abs/2308.14500)
  `self-supervised` `unknown` `skeleton` `PKU-MMD`
<a id="paper-2021-aaai-relational-modeling-self-supervision"></a>
- **Temporal Relational Modeling with Self-Supervision for Action Segmentation** — Dong Wang, Di Hu, Xingjian Li, et al., AAAI 2021.
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/16377) [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/16377/16184) [arXiv](https://arxiv.org/abs/2012.07508) [Code](https://github.com/redwang/DTGRM)
  `self-supervised` `graphical-model` `self-supervised` `unknown` `Breakfast` `50Salads`
<a id="paper-2021-cvpr-shuffle-alternating-learning-unsupervised"></a>
- **Action Shuffle Alternating Learning for Unsupervised Action Segmentation** — Jun Li, Sinisa Todorovic, CVPR 2021.
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Action_Shuffle_Alternating_Learning_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Action_Shuffle_Alternating_Learning_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.pdf) [arXiv](http://arxiv.org/abs/2104.02116)
  `self-supervised` `structured-decoding` `unknown` `Breakfast` `50Salads`
<a id="paper-2020-cvpr-joint-self-supervised-domain-adaptation"></a>
- **Action Segmentation With Joint Self-Supervised Temporal Domain Adaptation** — Min-Hung Chen, Baopu Li, Yingze Bao, et al., CVPR 2020.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_Action_Segmentation_With_Joint_Self-Supervised_Temporal_Domain_Adaptation_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chen_Action_Segmentation_With_Joint_Self-Supervised_Temporal_Domain_Adaptation_CVPR_2020_paper.pdf) [arXiv](http://arxiv.org/abs/2003.02824)
  `self-supervised` `unknown` `unknown` `Breakfast` `50Salads`

### Unsupervised

<a id="paper-2026-icpr-deep-kernel-approximation-unsupervised"></a>
- **Deep Kernel Video Approximation for Unsupervised Action Segmentation** — Silvia L. Pintea, Jouke Dijkstra, ICPR 2026.
  [Paper](https://icpr2026.org/acceptedPapers.html) [PDF](https://silvialaurapintea.github.io/pub/icpr26.pdf) [arXiv](https://arxiv.org/abs/2604.21572)
  `unsupervised` `optimal-transport` `IMU`
<a id="paper-2025-aaai-hierarchical-vector-quantization-unsupervised"></a>
- **Hierarchical Vector Quantization for Unsupervised Action Segmentation** — Federico Spurio, Emad Bahrami, Gianpiero Francesca, et al., AAAI 2025.
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/32751) [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/32751/34906) [arXiv](https://arxiv.org/abs/2412.17640)
  `unsupervised` `clustering` `unknown` `Breakfast` `IKEA ASM`
<a id="paper-2025-iccv-clot-closed-loop-optimal-transport"></a>
- **CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation** — Elena Bueno-Benito, Mariella Dimiccoli, ICCV 2025.
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Bueno-Benito_CLOT_Closed_Loop_Optimal_Transport_for_Unsupervised_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Bueno-Benito_CLOT_Closed_Loop_Optimal_Transport_for_Unsupervised_Action_Segmentation_ICCV_2025_paper.pdf) [arXiv](http://arxiv.org/abs/2507.03539)
  `unsupervised` `cross-attention` `optimal-transport` `IMU`
<a id="paper-2025-iccv-skeleton-motion-words-unsupervised-skeleton"></a>
- **Skeleton Motion Words for Unsupervised Skeleton-Based Temporal Action Segmentation** — Uzay Gökay, Federico Spurio, Dominik R. Bach, et al., ICCV 2025.
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Gokay_Skeleton_Motion_Words_for_Unsupervised_Skeleton-Based_Temporal_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Gokay_Skeleton_Motion_Words_for_Unsupervised_Skeleton-Based_Temporal_Action_Segmentation_ICCV_2025_paper.pdf) [arXiv](https://arxiv.org/abs/2508.04513)
  `unsupervised` `unknown` `skeleton` `LARa`
<a id="paper-2024-cvpr-temporally-consistent-unbalanced-optimal-transport"></a>
- **Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation** — Ming Xu, Stephen Gould, CVPR 2024.
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.pdf) [arXiv](http://arxiv.org/abs/2404.01518) [Code](https://github.com/mingu6/action-segmentation-ot)
  `unsupervised` `optimal-transport` `unknown` `Breakfast`
<a id="paper-2024-wacv-permutation-aware-activity-unsupervised-frame"></a>
- **Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment** — Quoc-Huy Tran, Ahmed Mehmood, Muhammad Ahmed, et al., WACV 2024.
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Tran_Permutation-Aware_Activity_Segmentation_via_Unsupervised_Frame-To-Segment_Alignment_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Tran_Permutation-Aware_Activity_Segmentation_via_Unsupervised_Frame-To-Segment_Alignment_WACV_2024_paper.pdf) [arXiv](https://arxiv.org/abs/2305.19478)
  `unsupervised` `Transformer` `optimal-transport` `unknown` `Breakfast`
<a id="paper-2024-wacv-united-we-stand-divided-we"></a>
- **United We Stand, Divided We Fall: UnityGraph for Unsupervised Procedure Learning From Videos** — Siddhant Bansal, Chetan Arora, C. V. Jawahar, WACV 2024.
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Bansal_United_We_Stand_Divided_We_Fall_UnityGraph_for_Unsupervised_Procedure_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Bansal_United_We_Stand_Divided_We_Fall_UnityGraph_for_Unsupervised_Procedure_WACV_2024_paper.pdf) [arXiv](http://arxiv.org/abs/2311.03550)
  `unsupervised` `unknown` `unknown` `CrossTask`
<a id="paper-2023-cvpr-workshop-leveraging-triplet-loss-unsupervised"></a>
- **Leveraging Triplet Loss for Unsupervised Action Segmentation** — Elena Belen Bueno-Benito, Biel Tura Vecino, Mariella Dimiccoli, CVPR Workshop 2023.
  [Paper](https://openaccess.thecvf.com/content/CVPR2023W/L3D-IVU/html/Bueno-Benito_Leveraging_Triplet_Loss_for_Unsupervised_Action_Segmentation_CVPRW_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2023W/L3D-IVU/papers/Bueno-Benito_Leveraging_Triplet_Loss_for_Unsupervised_Action_Segmentation_CVPRW_2023_paper.pdf) [arXiv](https://arxiv.org/abs/2304.06403)
  `unsupervised` `clustering` `unknown`
<a id="paper-2023-cvww-taec-unsupervised-aware-embedding-clustering"></a>
- **TAEC: Unsupervised Action Segmentation with Temporal-Aware Embedding and Clustering** — Wei Lin, Anna Kukleva, Horst Possegger, et al., CVWW 2023.
  [Paper](https://ceur-ws.org/Vol-3349/) [PDF](https://ceur-ws.org/Vol-3349/paper1.pdf) [arXiv](https://arxiv.org/abs/2303.05166)
  `unsupervised` `clustering` `unknown`
<a id="paper-2022-cvpr-fast-unsupervised-boundary-detection"></a>
- **Fast and Unsupervised Action Boundary Detection for Action Segmentation** — Zexing Du, Xue Wang, Guoqing Zhou, et al., CVPR 2022.
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Du_Fast_and_Unsupervised_Action_Boundary_Detection_for_Action_Segmentation_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Du_Fast_and_Unsupervised_Action_Boundary_Detection_for_Action_Segmentation_CVPR_2022_paper.pdf)
  `unsupervised` `clustering` `boundary-modeling` `IMU`
<a id="paper-2022-cvpr-unsupervised-by-joint-representation-learning"></a>
- **Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering** — Sateesh Kumar, Sanjay Haresh, Awais Ahmed, et al., CVPR 2022.
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Kumar_Unsupervised_Action_Segmentation_by_Joint_Representation_Learning_and_Online_Clustering_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Kumar_Unsupervised_Action_Segmentation_by_Joint_Representation_Learning_and_Online_Clustering_CVPR_2022_paper.pdf) [arXiv](http://arxiv.org/abs/2105.13353)
  `unsupervised` `optimal-transport` `clustering` `IMU` `Breakfast`
<a id="paper-2022-eccv-my-view-is-best-view"></a>
- **My View Is the Best View: Procedure Learning from Egocentric Videos** — Siddhant Bansal, Chetan Arora, C. V. Jawahar, ECCV 2022.
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1910_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136730656.pdf) [Code](https://sid2697.github.io/egoprocel)
  `unsupervised` `clustering` `contrastive-learning` `unknown`
<a id="paper-2021-cvpr-temporally-weighted-hierarchical-clustering-unsupervised"></a>
- **Temporally-Weighted Hierarchical Clustering for Unsupervised Action Segmentation** — Saquib Sarfraz, Naila Murray, Vivek Sharma, et al., CVPR 2021.
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Sarfraz_Temporally-Weighted_Hierarchical_Clustering_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Sarfraz_Temporally-Weighted_Hierarchical_Clustering_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.pdf) [arXiv](http://arxiv.org/abs/2103.11264)
  `unsupervised` `clustering` `unknown`
<a id="paper-2021-wacv-joint-visual-embedding-unsupervised-learning"></a>
- **Joint Visual-Temporal Embedding for Unsupervised Learning of Actions in Untrimmed Sequences** — Rosaura G. VidalMata, Walter J. Scheirer, Anna Kukleva, et al., WACV 2021.
  [Paper](https://openaccess.thecvf.com/content/WACV2021/html/VidalMata_Joint_Visual-Temporal_Embedding_for_Unsupervised_Learning_of_Actions_in_Untrimmed_WACV_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2021/papers/VidalMata_Joint_Visual-Temporal_Embedding_for_Unsupervised_Learning_of_Actions_in_Untrimmed_WACV_2021_paper.pdf)
  `unsupervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2020-cvpr-intra-inter-understanding-parsing"></a>
- **Intra- and Inter-Action Understanding via Temporal Action Parsing** — Dian Shao, Yue Zhao, Bo Dai, et al., CVPR 2020.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Shao_Intra-_and_Inter-Action_Understanding_via_Temporal_Action_Parsing_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Shao_Intra-_and_Inter-Action_Understanding_via_Temporal_Action_Parsing_CVPR_2020_paper.pdf) [arXiv](https://arxiv.org/abs/2005.10229)
  `unsupervised` `clustering` `boundary-modeling` `unknown`
<a id="paper-2019-cvpr-unsupervised-learning-classes-continuous-embedding"></a>
- **Unsupervised Learning of Action Classes With Continuous Temporal Embedding** — Anna Kukleva, Hilde Kuehne, Fadime Sener, et al., CVPR 2019.
  [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.pdf)
  `unsupervised` `unknown` `unknown` `Breakfast` `50Salads`
<a id="paper-2019-iccv-unsupervised-procedure-learning-joint-dynamic"></a>
- **Unsupervised Procedure Learning via Joint Dynamic Summarization** — Ehsan Elhamifar, Zwe Naing, ICCV 2019.
  [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.pdf)
  `unsupervised` `unknown` `multimodal`
<a id="paper-2016-cvpr-unsupervised-learning-narrated-instruction-videos"></a>
- **Unsupervised Learning From Narrated Instruction Videos** — Jean-Baptiste Alayrac, Piotr Bojanowski, Nishant Agrawal, et al., CVPR 2016.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2016/html/Alayrac_Unsupervised_Learning_From_CVPR_2016_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2016/papers/Alayrac_Unsupervised_Learning_From_CVPR_2016_paper.pdf)
  `unsupervised` `clustering` `unknown`
<a id="paper-2015-iccv-unsupervised-semantic-parsing-collections"></a>
- **Unsupervised Semantic Parsing of Video Collections** — Ozan Sener, Amir R. Zamir, Silvio Savarese, et al., ICCV 2015.
  [Paper](https://openaccess.thecvf.com/content_iccv_2015/html/Sener_Unsupervised_Semantic_Parsing_ICCV_2015_paper.html) [PDF](https://openaccess.thecvf.com/content_iccv_2015/papers/Sener_Unsupervised_Semantic_Parsing_ICCV_2015_paper.pdf)
  `unsupervised` `unknown` `unknown`

### Few-Shot and Zero-Shot

<a id="paper-2025-iccv-multi-modal-few-shot"></a>
- **Multi-Modal Few-Shot Temporal Action Segmentation** — Zijia Lu, Ehsan Elhamifar, ICCV 2025.
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_Multi-Modal_Few-Shot_Temporal_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_Multi-Modal_Few-Shot_Temporal_Action_Segmentation_ICCV_2025_paper.pdf) [Code](https://github.com/ZijiaLewisLu/ICCV2025-MMF-TAS)
  `few-shot` `Transformer` `prototype-learning` `multimodal`

### Training-Free

- _No verified paper in the current snapshot._

## Cross-index by technical route

### TCN and Multi-Stage Refinement

- [Action Segmentation Using 2D Skeleton Heatmaps and Multi-Modality Fusion](#paper-2024-icra-using-2d-skeleton-heatmaps-multi)
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](#paper-2024-neurips-onlinetas-online-baseline)
- [How Much Temporal Long-Term Context is Needed for Action Segmentation?](#paper-2023-iccv-how-much-long-term-context)
- [Streaming Video Temporal Action Segmentation in Real Time](#paper-2023-iske-streaming-real-time)
- [A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation](#paper-2022-eccv-generalized-robust-framework-timestamp-supervision)
- [Iterative Contrast-Classify for Semi-Supervised Temporal Action Segmentation](#paper-2022-aaai-iterative-contrast-classify-semi-supervised)
- [Robust Action Segmentation from Timestamp Supervision](#paper-2022-bmvc-robust-timestamp-supervision)
- [Timestamp-Supervised Action Segmentation with Graph Convolutional Networks](#paper-2022-iros-timestamp-supervised-graph-convolutional-networks)
- [Fast Weakly Supervised Action Segmentation Using Mutual Consistency](#paper-2020-eccv-fast-weakly-supervised-using-mutual)
- [TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks](#paper-2020-miccai-tecno-surgical-phase-recognition-multi)
- [Temporal Aggregate Representations for Long-Range Video Understanding](#paper-2020-eccv-aggregate-representations-long-range-understanding)
- [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](#paper-2019-cvpr-ms-tcn-multi-stage-convolutional)
- [Weakly-Supervised Action Segmentation With Iterative Soft Boundary Assignment](#paper-2018-cvpr-weakly-supervised-iterative-soft-boundary)
- [Temporal Convolutional Networks for Action Segmentation and Detection](#paper-2017-cvpr-convolutional-networks-detection)
- [Connectionist Temporal Modeling for Weakly Supervised Action Labeling](#paper-2016-eccv-connectionist-modeling-weakly-supervised-labeling)

### Transformer and Cross-Attention

- [Hierarchical Action Learning for Weakly-Supervised Action Segmentation](#paper-2026-cvpr-hierarchical-learning-weakly-supervised)
- [Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning](#paper-2026-cvpr-polyphony-diffusion-based-dual-hand)
- [Timestamp Query Transformer for Temporal Action Segmentation](#paper-2026-wacv-timestamp-query-transformer)
- [End-to-End Action Segmentation Transformer](#paper-2025-iccv-workshop-end-end-transformer)
- [Multi-Modal Few-Shot Temporal Action Segmentation](#paper-2025-iccv-multi-modal-few-shot)
- [Efficient Temporal Action Segmentation via Boundary-aware Query Voting](#paper-2024-neurips-efficient-boundary-aware-query-voting)
- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](#paper-2024-cvpr-fact-frame-cross-attention-modeling)
- [Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment](#paper-2024-wacv-permutation-aware-activity-unsupervised-frame)
- [How Much Temporal Long-Term Context is Needed for Action Segmentation?](#paper-2023-iccv-how-much-long-term-context)
- [Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation](#paper-2022-eccv-unified-fully-timestamp-supervised-sequence)
- [ASFormer: Transformer for Action Segmentation](#paper-2021-bmvc-asformer-transformer)
- [SCT: Set Constrained Temporal Transformer for Set Supervised Action Segmentation](#paper-2020-cvpr-sct-set-constrained-transformer-set)

### Diffusion Models

- [Learning Action Hierarchies via Hybrid Geometric Diffusion](#paper-2026-wacv-learning-hierarchies-hybrid-geometric-diffusion)
- [Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning](#paper-2026-cvpr-polyphony-diffusion-based-dual-hand)
- [ActFusion: a Unified Diffusion Model for Action Segmentation and Anticipation](#paper-2024-neurips-actfusion-unified-diffusion-model-anticipation)
- [Diffusion Action Segmentation](#paper-2023-iccv-diffusion)

### Optimal Transport

- [Deep Kernel Video Approximation for Unsupervised Action Segmentation](#paper-2026-icpr-deep-kernel-approximation-unsupervised)
- [CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation](#paper-2025-iccv-clot-closed-loop-optimal-transport)
- [Joint Self-Supervised Video Alignment and Action Segmentation](#paper-2025-iccv-joint-self-supervised-alignment)
- [Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment](#paper-2024-wacv-permutation-aware-activity-unsupervised-frame)
- [Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation](#paper-2024-cvpr-temporally-consistent-unbalanced-optimal-transport)
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](#paper-2022-cvpr-unsupervised-by-joint-representation-learning)

### Clustering and Prototype Learning

- [CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation](#paper-2025-iccv-clot-closed-loop-optimal-transport)
- [Hierarchical Vector Quantization for Unsupervised Action Segmentation](#paper-2025-aaai-hierarchical-vector-quantization-unsupervised)
- [Towards Open-World Human Action Segmentation Using Graph Convolutional Networks](#paper-2025-iros-towards-open-world-human-using)
- [Leveraging Triplet Loss for Unsupervised Action Segmentation](#paper-2023-cvpr-workshop-leveraging-triplet-loss-unsupervised)
- [TAEC: Unsupervised Action Segmentation with Temporal-Aware Embedding and Clustering](#paper-2023-cvww-taec-unsupervised-aware-embedding-clustering)
- [Timestamp-Supervised Action Segmentation in the Perspective of Clustering](#paper-2023-ijcai-timestamp-supervised-perspective-clustering)
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](#paper-2022-cvpr-fast-unsupervised-boundary-detection)
- [Iterative Contrast-Classify for Semi-Supervised Temporal Action Segmentation](#paper-2022-aaai-iterative-contrast-classify-semi-supervised)
- [My View Is the Best View: Procedure Learning from Egocentric Videos](#paper-2022-eccv-my-view-is-best-view)
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](#paper-2022-cvpr-unsupervised-by-joint-representation-learning)
- [Temporally-Weighted Hierarchical Clustering for Unsupervised Action Segmentation](#paper-2021-cvpr-temporally-weighted-hierarchical-clustering-unsupervised)
- [Intra- and Inter-Action Understanding via Temporal Action Parsing](#paper-2020-cvpr-intra-inter-understanding-parsing)
- [Unsupervised Learning From Narrated Instruction Videos](#paper-2016-cvpr-unsupervised-learning-narrated-instruction-videos)

### Boundary and Duration Modeling

- [Combining Boundary Supervision and Segment-Level Regularization for Fine-Grained Action Segmentation](#paper-2026-cvpr-workshop-combining-boundary-supervision-segment-level)
- [Improving Temporal Action Segmentation via Constraint-Aware Decoding](#paper-2026-icpr-improving-constraint-aware-decoding)
- [LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation](#paper-2026-cvpr-lady-lagrangian-dynamic-informed-network)
- [Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation](#paper-2026-cvpr-spectral-scalpel-amplifying-adjacent-discrepancy)
- [Pose-Aware Weakly-Supervised Action Segmentation](#paper-2025-cvpr-workshop-pose-aware-weakly-supervised)
- [Efficient Temporal Action Segmentation via Boundary-aware Query Voting](#paper-2024-neurips-efficient-boundary-aware-query-voting)
- [Efficient and Effective Weakly-Supervised Action Segmentation via Action-Transition-Aware Boundary Alignment](#paper-2024-cvpr-efficient-effective-weakly-supervised-transition)
- [OTAS: Unsupervised Boundary Detection for Object-Centric Temporal Action Segmentation](#paper-2024-wacv-otas-unsupervised-boundary-detection-object)
- [Diffusion Action Segmentation](#paper-2023-iccv-diffusion)
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](#paper-2022-cvpr-fast-unsupervised-boundary-detection)
- [Leveraging Action Affinity and Continuity for Semi-Supervised Temporal Action Segmentation](#paper-2022-eccv-leveraging-affinity-continuity-semi-supervised)
- [Robust Action Segmentation from Timestamp Supervision](#paper-2022-bmvc-robust-timestamp-supervision)
- [Turning to a Teacher for Timestamp Supervised Temporal Action Segmentation](#paper-2022-icme-turning-teacher-timestamp-supervised)
- [Uncertainty-Aware Representation Learning for Action Segmentation](#paper-2022-ijcai-uncertainty-aware-representation-learning)
- [Boundary-Aware Cascade Networks for Temporal Action Segmentation](#paper-2020-eccv-boundary-aware-cascade-networks)
- [Improving Action Segmentation via Graph-Based Temporal Reasoning](#paper-2020-cvpr-improving-graph-based-reasoning)
- [Intra- and Inter-Action Understanding via Temporal Action Parsing](#paper-2020-cvpr-intra-inter-understanding-parsing)
- [Weakly-Supervised Action Segmentation With Iterative Soft Boundary Assignment](#paper-2018-cvpr-weakly-supervised-iterative-soft-boundary)

### Structured Decoding

- [Improving Temporal Action Segmentation via Constraint-Aware Decoding](#paper-2026-icpr-improving-constraint-aware-decoding)
- [Activity Grammars for Temporal Action Segmentation](#paper-2023-neurips-activity-grammars)
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos](#paper-2023-iccv-weakly-supervised-unseen-error-detection)
- [Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation](#paper-2022-neurips-don-t-pour-cereal-into)
- [Action Shuffle Alternating Learning for Unsupervised Action Segmentation](#paper-2021-cvpr-shuffle-alternating-learning-unsupervised)
- [Anchor-Constrained Viterbi for Set-Supervised Action Segmentation](#paper-2021-cvpr-anchor-constrained-viterbi-set-supervised)
- [Fast Weakly Supervised Action Segmentation Using Mutual Consistency](#paper-2020-eccv-fast-weakly-supervised-using-mutual)
- [Set-Constrained Viterbi for Set-Supervised Action Segmentation](#paper-2020-cvpr-set-constrained-viterbi-set-supervised)
- [End-to-End Fine-Grained Action Segmentation and Recognition Using Conditional Random Field Models and Discriminative Sparse Coding](#paper-2018-wacv-end-end-fine-grained-recognition)
- [NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning](#paper-2018-cvpr-neuralnetwork-viterbi-framework-weakly-supervised)
- [Action Parsing Using Context Features](#paper-2017-dicta-parsing-using-context-features)
- [Connectionist Temporal Modeling for Weakly Supervised Action Labeling](#paper-2016-eccv-connectionist-modeling-weakly-supervised-labeling)
- [Segmental Spatiotemporal CNNs for Fine-Grained Action Segmentation](#paper-2016-eccv-segmental-spatiotemporal-cnns-fine-grained)

### Action Tokenization and VQ

- [Timestamp Query Transformer for Temporal Action Segmentation](#paper-2026-wacv-timestamp-query-transformer)
- [ActFusion: a Unified Diffusion Model for Action Segmentation and Anticipation](#paper-2024-neurips-actfusion-unified-diffusion-model-anticipation)
- [Efficient Temporal Action Segmentation via Boundary-aware Query Voting](#paper-2024-neurips-efficient-boundary-aware-query-voting)
- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](#paper-2024-cvpr-fact-frame-cross-attention-modeling)

### Vision-Language and Open Vocabulary

- _No verified paper in the current snapshot._

### Online and Streaming

- [Hierarchical Action Learning for Weakly-Supervised Action Segmentation](#paper-2026-cvpr-hierarchical-learning-weakly-supervised)
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](#paper-2024-neurips-onlinetas-online-baseline)
- [Permutation-Aware Activity Segmentation via Unsupervised Frame-To-Segment Alignment](#paper-2024-wacv-permutation-aware-activity-unsupervised-frame)
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](#paper-2024-cvpr-progress-aware-online-egocentric-procedural)
- [Streaming Video Temporal Action Segmentation in Real Time](#paper-2023-iske-streaming-real-time)

### Efficient and Long-Video Methods

- [Condensing Action Segmentation Datasets via Generative Network Inversion](#paper-2025-cvpr-condensing-datasets-generative-network-inversion)

## Cross-index by application

### General RGB Video

- _No verified paper in the current snapshot._

### Egocentric Video

- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](#paper-2024-cvpr-fact-frame-cross-attention-modeling)
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](#paper-2024-cvpr-progress-aware-online-egocentric-procedural)
- [My View Is the Best View: Procedure Learning from Egocentric Videos](#paper-2022-eccv-my-view-is-best-view)
- [Temporal Relational Modeling with Self-Supervision for Action Segmentation](#paper-2021-aaai-relational-modeling-self-supervision)
- [Improving Action Segmentation via Graph-Based Temporal Reasoning](#paper-2020-cvpr-improving-graph-based-reasoning)
- [Coupled Generative Adversarial Network for Continuous Fine-Grained Action Segmentation](#paper-2019-wacv-coupled-generative-adversarial-network-continuous)
- [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](#paper-2019-cvpr-ms-tcn-multi-stage-convolutional)

### Surgical Workflow

- [TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks](#paper-2020-miccai-tecno-surgical-phase-recognition-multi)

### Assembly and Manufacturing

- _No verified paper in the current snapshot._

### Robotics and Embodied Agents

- [M2R2: MultiModal Robotic Representation for Temporal Action Segmentation](#paper-2026-icra-m2r2-multimodal-robotic-representation)
- [Multi-Modal Graph Convolutional Network with Sinusoidal Encoding for Robust Human Action Segmentation](#paper-2025-iros-multi-modal-graph-convolutional-network)
- [Towards Open-World Human Action Segmentation Using Graph Convolutional Networks](#paper-2025-iros-towards-open-world-human-using)
- [Action Segmentation Using 2D Skeleton Heatmaps and Multi-Modality Fusion](#paper-2024-icra-using-2d-skeleton-heatmaps-multi)
- [Timestamp-Supervised Action Segmentation with Graph Convolutional Networks](#paper-2022-iros-timestamp-supervised-graph-convolutional-networks)

### Online and Streaming

- [Pose-Aware Weakly-Supervised Action Segmentation](#paper-2025-cvpr-workshop-pose-aware-weakly-supervised)
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](#paper-2024-neurips-onlinetas-online-baseline)
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](#paper-2024-cvpr-progress-aware-online-egocentric-procedural)
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos](#paper-2023-iccv-weakly-supervised-unseen-error-detection)
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](#paper-2022-cvpr-fast-unsupervised-boundary-detection)
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](#paper-2022-cvpr-unsupervised-by-joint-representation-learning)
- [Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos](#paper-2022-cvpr-weakly-supervised-online-multi-view)
- [NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning](#paper-2018-cvpr-neuralnetwork-viterbi-framework-weakly-supervised)

## Preprints / Pending Verification

<a id="paper-2026-preprint-atlas-annotation-tool-long-horizon"></a>
- **ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation** — Sergej Stanovcic, Daniel Sliwowski, Dongheui Lee, Preprint 2026.
  [PDF](https://arxiv.org/pdf/2604.26637) [arXiv](https://arxiv.org/abs/2604.26637)
  `fully-supervised` `boundary-modeling` `multimodal`
  _Status:_ arXiv 2604.26637; first submitted 2026-04-29; last updated 2026-04-29; comment=7 pages, 2 figures, 2 tables; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-adaptive-latent-trajectory-anchoring-dataset"></a>
- **Adaptive Latent Trajectory Anchoring for Action Segmentation Dataset Condensation** — Artheme Gauthier-Villar, Guodong Ding, Angela Yao, Preprint 2026.
  [PDF](https://arxiv.org/pdf/2607.09081) [arXiv](https://arxiv.org/abs/2607.09081)
  `fully-supervised` `diffusion` `dataset-condensation` `unknown` `Breakfast`
  _Publication metadata:_ ECCV 2026; `author-claimed-accepted`; `unverified-author-metadata`.
  _Status:_ arXiv 2607.09081; first submitted 2026-07-10; last updated 2026-07-10; comment=16 pages, 5 figures, accepted to ECCV 2026; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-boundary-centric-clip-budgeted-active"></a>
- **Boundary-Centric Clip-Budgeted Active Learning for Temporal Action Segmentation** — Halil Ismail Helvaci, Sen-ching Samson Cheung, Preprint 2026.
  [PDF](https://arxiv.org/pdf/2604.15173) [arXiv](https://arxiv.org/abs/2604.15173)
  `fully-supervised` `boundary-modeling` `unknown` `Breakfast` `50Salads`
  _Status:_ arXiv 2604.15173; first submitted 2026-04-16; last updated 2026-06-12; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-data-efficient-surgical-phase-small"></a>
- **Data-Efficient Surgical Phase Segmentation in Small-Incision Cataract Surgery: A Controlled Study of Vision Foundation Models** — Lincoln Spencer, Song Wang, Chen Chen, Preprint 2026.
  [PDF](https://arxiv.org/pdf/2604.10514) [arXiv](https://arxiv.org/abs/2604.10514)
  `self-supervised` `unknown` `I3D-features`
  _Status:_ arXiv 2604.10514; first submitted 2026-04-12; last updated 2026-04-12; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-ego-metas-egocentric-online-multimodal"></a>
- **Ego-METAS: Egocentric online Multimodal Energy-efficient Temporal Action Segmentation benchmark** — Maria Santos-Villafranca, Jesus Bermudez-cameo, Alejandro Perez-Yus, et al., Preprint 2026.
  [PDF](https://arxiv.org/pdf/2606.02246) [arXiv](https://arxiv.org/abs/2606.02246)
  `fully-supervised` `unknown` `multimodal` `EgoExo4D` `CMU-MMAC`
  _Status:_ arXiv 2606.02246; first submitted 2026-05-29; last updated 2026-05-29; comment=Project Page: https://maria-sanvil.github.io/Ego-METAS-website/; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-exploring-vision-language-models-open"></a>
- **Exploring Vision-Language Models for Open-Vocabulary Zero-Shot Action Segmentation** — Asim Unmesh, Kaki Ramesh, Mayank Patel, et al., Preprint 2026.
  [PDF](https://arxiv.org/pdf/2602.21406) [arXiv](https://arxiv.org/abs/2602.21406)
  `zero-shot` `unknown` `video-language`
  _Publication metadata:_ ICRA 2026; `venue-mentioned`; `unverified-author-metadata`.
  _Status:_ arXiv 2602.21406; first submitted 2026-02-24; last updated 2026-02-24; comment=ICRA 2026; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-fine-grained-renorrhaphy-robot-assisted"></a>
- **Fine-Grained Action Segmentation for Renorrhaphy in Robot-Assisted Partial Nephrectomy** — Jiaheng Dai, Huanrong Liu, Tailai Zhou, et al., Preprint 2026.
  [PDF](https://arxiv.org/pdf/2604.09051) [arXiv](https://arxiv.org/abs/2604.09051)
  `fully-supervised` `duration-modeling` `I3D-features`
  _Status:_ arXiv 2604.09051; first submitted 2026-04-10; last updated 2026-04-10; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-impact-scribe-interactive-boundary-scribbles"></a>
- **IMPACT-Scribe: Interactive Temporal Action Segmentation with Boundary Scribbles and Query Planning** — Qian Yin, Di Wen, Kunyu Peng, et al., Preprint 2026.
  [PDF](https://arxiv.org/pdf/2605.01668) [arXiv](https://arxiv.org/abs/2605.01668)
  `fully-supervised` `boundary-modeling` `unknown`
  _Status:_ arXiv 2605.01668; first submitted 2026-05-03; last updated 2026-05-03; comment=7 pages, 4 figures. Code is available at https://github.com/BanzQians/IMPACT_AS; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-learning-probabilistic-embeddings-unsupervised"></a>
- **Learning Probabilistic Embeddings for Unsupervised Action Segmentation** — Shuai Li, Duc Manh Vu, Juergen Gall, Preprint 2026.
  [PDF](https://arxiv.org/pdf/2607.05263) [arXiv](https://arxiv.org/abs/2607.05263)
  `unsupervised` `optimal-transport` `clustering` `IMU`
  _Status:_ arXiv 2607.05263; first submitted 2026-07-06; last updated 2026-07-06; comment=ECCV2026; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-point-supervised-skeleton-based-human"></a>
- **Point-Supervised Skeleton-Based Human Action Segmentation** — Hongsong Wang, Yiqin Shen, Pengbo Yan, et al., Preprint 2026.
  [PDF](https://arxiv.org/pdf/2603.06201) [arXiv](https://arxiv.org/abs/2603.06201)
  `fully-supervised` `clustering` `prototype-learning` `skeleton` `PKU-MMD`
  _Status:_ arXiv 2603.06201; first submitted 2026-03-06; last updated 2026-03-06; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2026-preprint-text-augmented-optimal-transport-unsupervised"></a>
- **Text-Augmented Action Segmentation Optimal Transport for Unsupervised Surgical Phase Recognition** — Omar Mohamed, collaborators, Preprint 2026.
  [PDF](https://arxiv.org/pdf/2602.24138) [arXiv](https://arxiv.org/abs/2602.24138)
  `unsupervised` `optimal-transport` `unknown`
  _Status:_ arXiv 2602.24138; first submitted 2026-02-27; last update 2026-02-27; no formal proceedings placement verified by 2026-07-28.
<a id="paper-2026-preprint-unsupervised-skeleton-based-hierarchical-spatiotemporal"></a>
- **Unsupervised Skeleton-Based Action Segmentation via Hierarchical Spatiotemporal Vector Quantization** — Umer Ahmed, Syed Ahmed Mahmood, Fawad Javed Fateh, et al., Preprint 2026.
  [PDF](https://arxiv.org/pdf/2604.15196) [arXiv](https://arxiv.org/abs/2604.15196)
  `timestamp-supervised` `clustering` `skeleton` `LARa`
  _Status:_ arXiv 2604.15196; first submitted 2026-04-16; last updated 2026-04-16; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-dual-stream-alignment"></a>
- **Dual-Stream Alignment for Action Segmentation** — Harshala Gammulle, Clinton Fookes, Sridha Sridharan, et al., Preprint 2025.
  [PDF](https://arxiv.org/pdf/2510.07652) [arXiv](https://arxiv.org/abs/2510.07652)
  `fully-supervised` `cross-attention` `unknown` `Breakfast` `50Salads`
  _Status:_ arXiv 2510.07652; first submitted 2025-10-09; last updated 2025-10-09; comment=Journal Submission; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-hrtr-single-stage-transformer-fine"></a>
- **HRTR: A Single-stage Transformer for Fine-grained Sub-second Action Segmentation in Stroke Rehabilitation** — Halil Ismail Helvaci, Justin Philip Huber, Jihye Bae, et al., Preprint 2025.
  [PDF](https://arxiv.org/pdf/2506.02472) [arXiv](https://arxiv.org/abs/2506.02472)
  `fully-supervised` `Transformer` `multi-stage-TCN` `IMU` `50Salads`
  _Status:_ arXiv 2506.02472; first submitted 2025-06-03; last updated 2025-06-11; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-improving-explicit-similarity-measurement"></a>
- **Improving action segmentation via explicit similarity measurement** — Kamel Aouaidjia, Wenhao Zhang, Aofan Li, et al., Preprint 2025.
  [PDF](https://arxiv.org/pdf/2502.10713) [arXiv](https://arxiv.org/abs/2502.10713)
  `unsupervised` `Transformer` `boundary-modeling` `unknown` `Breakfast` `50Salads`
  _Status:_ arXiv 2502.10713; first submitted 2025-02-15; last updated 2025-02-15; comment=13 pages, 5 figures; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-multi-stage-boundary-aware-transformer"></a>
- **Multi-Stage Boundary-Aware Transformer Network for Action Segmentation in Untrimmed Surgical Videos** — Rezowan Shuvo, M S Mekala, Eyad Elyan, Preprint 2025.
  [PDF](https://arxiv.org/pdf/2504.18756) [arXiv](https://arxiv.org/abs/2504.18756)
  `fully-supervised` `Transformer` `boundary-modeling` `unknown`
  _Status:_ arXiv 2504.18756; first submitted 2025-04-26; last updated 2025-06-10; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-text-derived-relational-graph-enhanced"></a>
- **Text-Derived Relational Graph-Enhanced Network for Skeleton-Based Action Segmentation** — Haoyu Ji, Bowen Chen, Weihong Ren, et al., Preprint 2025.
  [PDF](https://arxiv.org/pdf/2503.15126) [arXiv](https://arxiv.org/abs/2503.15126)
  `fully-supervised` `unknown` `skeleton`
  _Status:_ arXiv 2503.15126; first submitted 2025-03-19; last updated 2025-03-19; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-towards-generalizing-unseen-views"></a>
- **Towards Generalizing Temporal Action Segmentation to Unseen Views** — Emad Bahrami, Olga Zatsarynna, Gianpiero Francesca, et al., Preprint 2025.
  [PDF](https://arxiv.org/pdf/2504.02512) [arXiv](https://arxiv.org/abs/2504.02512)
  `fully-supervised` `unknown` `unknown` `Assembly101`
  _Status:_ arXiv 2504.02512; first submitted 2025-04-03; last updated 2025-04-03; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2025-preprint-vifss-view-invariant-figure-skating"></a>
- **VIFSS: View-Invariant and Figure Skating-Specific Pose Representation Learning for Temporal Action Segmentation** — Ryota Tanaka, Tomohiro Suzuki, Keisuke Fujii, Preprint 2025.
  [PDF](https://arxiv.org/pdf/2508.10281) [arXiv](https://arxiv.org/abs/2508.10281)
  `fully-supervised` `unknown` `unknown`
  _Status:_ arXiv 2508.10281; first submitted 2025-08-14; last updated 2025-08-14; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2024-preprint-2by2-weakly-supervised-learning-global"></a>
- **2by2: Weakly-Supervised Learning for Global Action Segmentation** — Elena Bueno-Benito, Mariella Dimiccoli, Preprint 2024.
  [PDF](https://arxiv.org/pdf/2412.12829) [arXiv](https://arxiv.org/abs/2412.12829)
  `weakly-supervised` `Transformer` `unknown` `Breakfast`
  _Status:_ arXiv 2412.12829; first submitted 2024-12-17; last updated 2024-12-17; comment=none; journal_ref=vol 15332, year 2024, pp 380-395. No formal conference proceedings placement has been verified.
<a id="paper-2024-preprint-study-animal-algorithms-across-supervised"></a>
- **A study of animal action segmentation algorithms across supervised, unsupervised, and semi-supervised learning paradigms** — Ari Blau, Evan S Schaffer, Neeli Mishra, et al., Preprint 2024.
  [PDF](https://arxiv.org/pdf/2407.16727) [arXiv](https://arxiv.org/abs/2407.16727)
  `semi-supervised` `TCN` `unknown`
  _Status:_ arXiv 2407.16727; first submitted 2024-07-23; last updated 2024-12-17; comment=33 pages, 15 figures; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2024-preprint-faster-diffusion"></a>
- **Faster Diffusion Action Segmentation** — Shuaibing Wang, Shunli Wang, Mingcheng Li, et al., Preprint 2024.
  [PDF](https://arxiv.org/pdf/2408.02024) [arXiv](https://arxiv.org/abs/2408.02024)
  `fully-supervised` `Transformer` `diffusion` `unknown` `Breakfast` `50Salads`
  _Status:_ arXiv 2408.02024; first submitted 2024-08-04; last updated 2024-08-04; comment=25 pages, 6 figures; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2024-preprint-friends-across-time-multi-scale"></a>
- **Friends Across Time: Multi-Scale Action Segmentation Transformer for Surgical Phase Recognition** — Bokai Zhang, Jiayuan Meng, Bin Cheng, et al., Preprint 2024.
  [PDF](https://arxiv.org/pdf/2401.11644) [arXiv](https://arxiv.org/abs/2401.11644)
  `fully-supervised` `Transformer` `cross-attention` `unknown` `Cholec80`
  _Status:_ arXiv 2401.11644; first submitted 2024-01-22; last updated 2024-01-22; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2024-preprint-language-assisted-human-part-motion"></a>
- **Language-Assisted Human Part Motion Learning for Skeleton-Based Temporal Action Segmentation** — Bowen Chen, Haoyu Ji, Zhiyong Wang, et al., Preprint 2024.
  [PDF](https://arxiv.org/pdf/2410.06353) [arXiv](https://arxiv.org/abs/2410.06353)
  `fully-supervised` `unknown` `skeleton` `PKU-MMD` `LARa`
  _Status:_ arXiv 2410.06353; first submitted 2024-10-08; last updated 2024-10-08; comment=This work has been submitted to the IEEE for possible publication; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2024-preprint-o-talc-steps-towards-combating"></a>
- **O-TALC: Steps Towards Combating Oversegmentation within Online Action Segmentation** — Matthew Kent Myers, Nick Wright, A. Stephen McGough, et al., Preprint 2024.
  [PDF](https://arxiv.org/pdf/2404.06894) [arXiv](https://arxiv.org/abs/2404.06894)
  `fully-supervised` `boundary-modeling` `unknown`
  _Publication metadata:_ TAHRI; `author-claimed-accepted`; `unverified-author-metadata`.
  _Status:_ arXiv 2404.06894; first submitted 2024-04-10; last updated 2024-04-10; comment=5 pages, 3 figures. Accepted as a short (unindexed) paper at the TAHRI conference; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-decoupled-spatio-framework-skeleton-based"></a>
- **A Decoupled Spatio-Temporal Framework for Skeleton-based Action Segmentation** — Yunheng Li, Zhongyu Li, Shanghua Gao, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2312.05830) [arXiv](https://arxiv.org/abs/2312.05830)
  `fully-supervised` `unknown` `skeleton`
  _Status:_ arXiv 2312.05830; first submitted 2023-12-10; last updated 2023-12-10; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-bit-bi-level-modeling-efficient"></a>
- **BIT: Bi-Level Temporal Modeling for Efficient Supervised Action Segmentation** — Zijia Lu, Ehsan Elhamifar, Preprint 2023.
  [PDF](https://arxiv.org/pdf/2308.14900) [arXiv](https://arxiv.org/abs/2308.14900)
  `fully-supervised` `Transformer` `cross-attention` `unknown`
  _Status:_ arXiv 2308.14900; first submitted 2023-08-28; last updated 2023-10-07; comment=9 pages, 6 figures; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-casr-refining-marginalizing-frame-levle"></a>
- **CASR: Refining Action Segmentation via Marginalizing Frame-levle Causal Relationships** — Keqing Du, Xinyu Yang, Hang Chen, Preprint 2023.
  [PDF](https://arxiv.org/pdf/2311.12401) [arXiv](https://arxiv.org/abs/2311.12401)
  `fully-supervised` `causal-model` `unknown`
  _Status:_ arXiv 2311.12401; first submitted 2023-11-21; last updated 2024-01-26; comment=We found that the paper needs to be modified in the model and all experiments must be re-run, so we request to withdraw the current version; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-dir-as-decoupling-individual-identification"></a>
- **DIR-AS: Decoupling Individual Identification and Temporal Reasoning for Action Segmentation** — Peiyao Wang, Haibin Ling, Preprint 2023.
  [PDF](https://arxiv.org/pdf/2304.02110) [arXiv](https://arxiv.org/abs/2304.02110)
  `fully-supervised` `boundary-modeling` `multi-stage-TCN` `unknown` `Breakfast` `GTEA`
  _Status:_ arXiv 2304.02110; first submitted 2023-04-04; last updated 2023-04-04; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-dpmix-mixture-depth-point-cloud"></a>
- **DPMix: Mixture of Depth and Point Cloud Video Experts for 4D Action Segmentation** — Yue Zhang, Hehe Fan, Yi Yang, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2307.16803) [arXiv](https://arxiv.org/abs/2307.16803)
  `fully-supervised` `unknown` `depth`
  _Status:_ arXiv 2307.16803; first submitted 2023-07-31; last updated 2023-07-31; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-end-end-streaming-reinforce-learning"></a>
- **End-to-End Streaming Video Temporal Action Segmentation with Reinforce Learning** — Jinrong Zhang, Wujun Wen, Shenglan Liu, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2309.15683) [arXiv](https://arxiv.org/abs/2309.15683)
  `fully-supervised` `unknown` `multimodal` `GTEA`
  _Publication metadata:_ IEEE TNNLS; `submission-only`; `unverified-author-metadata`.
  _Status:_ arXiv 2309.15683; first submitted 2023-09-27; last updated 2024-05-23; comment=submit to TNNLS; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-enhancing-transformer-backbone-egocentric"></a>
- **Enhancing Transformer Backbone for Egocentric Video Action Segmentation** — Sakib Reza, Balaji Sundareshan, Mohsen Moghaddam, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2305.11365) [arXiv](https://arxiv.org/abs/2305.11365)
  `fully-supervised` `Transformer` `unknown` `GTEA`
  _Publication metadata:_ Ego4D/EPIC Workshop 2023; `venue-mentioned`; `unverified-author-metadata`.
  _Status:_ arXiv 2305.11365; first submitted 2023-05-19; last updated 2023-05-23; comment=Joint 3rd Ego4D and 11th EPIC Workshop on Egocentric Vision at CVPR 2023; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-ms-tcrnet-multi-stage-convolutional"></a>
- **MS-TCRNet: Multi-Stage Temporal Convolutional Recurrent Networks for Action Segmentation Using Sensor-Augmented Kinematics** — Adam Goldbraikh, Omer Shubi, Or Rubin, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2303.07814) [arXiv](https://arxiv.org/abs/2303.07814)
  `fully-supervised` `TCN` `multi-stage-TCN` `IMU`
  _Publication metadata:_ Pattern Recognition; `submission-only`; `unverified-author-metadata`.
  _Status:_ arXiv 2303.07814; first submitted 2023-03-14; last updated 2024-07-12; comment=41 pages, 7 figures. Submitted to Pattern Recognition; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-prompt-enhanced-hierarchical-transformer-elevating"></a>
- **Prompt-enhanced Hierarchical Transformer Elevating Cardiopulmonary Resuscitation Instruction via Temporal Action Segmentation** — Yang Liu, Xiaoyun Zhong, Shiyao Zhai, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2308.16552) [arXiv](https://arxiv.org/abs/2308.16552)
  `fully-supervised` `Transformer` `unknown` `Breakfast` `50Salads`
  _Status:_ arXiv 2308.16552; first submitted 2023-08-31; last updated 2023-08-31; comment=Transformer for Cardiopulmonary Resuscitation; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-sfgans-self-supervised-future-generator"></a>
- **SFGANS Self-supervised Future Generator for human ActioN Segmentation** — Or Berman, Adam Goldbraikh, Shlomi Laufer, Preprint 2023.
  [PDF](https://arxiv.org/pdf/2401.00438) [arXiv](https://arxiv.org/abs/2401.00438)
  `self-supervised` `unknown` `unknown`
  _Status:_ arXiv 2401.00438; first submitted 2023-12-31; last updated 2023-12-31; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-smc-nca-semantic-guided-multi"></a>
- **SMC-NCA: Semantic-guided Multi-level Contrast for Semi-supervised Temporal Action Segmentation** — Feixiang Zhou, Zheheng Jiang, Huiyu Zhou, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2312.12347) [arXiv](https://arxiv.org/abs/2312.12347)
  `semi-supervised` `unknown` `unknown`
  _Publication metadata:_ IEEE Transactions on Multimedia; `author-claimed-accepted`; `unverified-author-metadata`.
  _Status:_ arXiv 2312.12347; first submitted 2023-12-19; last updated 2024-07-19; comment=Accepted to IEEE Transactions on Multimedia; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-sigformer-sparse-signal-guided-transformer"></a>
- **SigFormer: Sparse Signal-Guided Transformer for Multi-Modal Human Action Segmentation** — Qi Liu, Xinchen Liu, Kun Liu, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2311.17428) [arXiv](https://arxiv.org/abs/2311.17428)
  `fully-supervised` `Transformer` `cross-attention` `multimodal`
  _Status:_ arXiv 2311.17428; first submitted 2023-11-29; last updated 2024-08-26; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-synchronization-is-all-you-need"></a>
- **Synchronization is All You Need: Exocentric-to-Egocentric Transfer for Temporal Action Segmentation with Unlabeled Synchronized Video Pairs** — Camillo Quattrocchi, Antonino Furnari, Daniele Di Mauro, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2312.02638) [arXiv](https://arxiv.org/abs/2312.02638)
  `unsupervised` `unknown` `unknown` `Assembly101` `EgoExo4D`
  _Status:_ arXiv 2312.02638; first submitted 2023-12-05; last updated 2024-07-16; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2023-preprint-segment-transformer"></a>
- **Temporal Segment Transformer for Action Segmentation** — Zhichao Liu, Leshan Wang, Desen Zhou, et al., Preprint 2023.
  [PDF](https://arxiv.org/pdf/2302.13074) [arXiv](https://arxiv.org/abs/2302.13074)
  `fully-supervised` `Transformer` `unknown` `Breakfast` `50Salads`
  _Status:_ arXiv 2302.13074; first submitted 2023-02-25; last updated 2023-02-25; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-efficient-framework-few-shot-skeleton"></a>
- **An Efficient Framework for Few-shot Skeleton-based Temporal Action Segmentation** — Leiyang Xu, Qiang Wang, Xiaotian Lin, et al., Preprint 2022.
  [PDF](https://arxiv.org/pdf/2207.09925) [arXiv](https://arxiv.org/abs/2207.09925)
  `few-shot` `unknown` `skeleton`
  _Status:_ arXiv 2207.09925; first submitted 2022-07-20; last updated 2022-07-20; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-c2f-tcn-framework-semi-fully"></a>
- **C2F-TCN: A Framework for Semi and Fully Supervised Temporal Action Segmentation** — Dipika Singhania, Rahul Rahaman, Angela Yao, Preprint 2022.
  [PDF](https://arxiv.org/pdf/2212.11078) [arXiv](https://arxiv.org/abs/2212.11078)
  `semi-supervised` `clustering` `unknown`
  _Status:_ arXiv 2212.11078; first submitted 2022-12-20; last updated 2022-12-20; comment=arXiv admin note: text overlap with arXiv:2112.01402; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-cross-enhancement-transformer"></a>
- **Cross-Enhancement Transformer for Action Segmentation** — Jiahui Wang, Zhenyou Wang, Shanna Zhuang, et al., Preprint 2022.
  [PDF](https://arxiv.org/pdf/2205.09445) [arXiv](https://arxiv.org/abs/2205.09445)
  `fully-supervised` `Transformer` `TCN` `IMU` `Breakfast` `50Salads`
  _Status:_ arXiv 2205.09445; first submitted 2022-05-19; last updated 2022-05-19; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-distill-collect-semi-supervised"></a>
- **Distill and Collect for Semi-Supervised Temporal Action Segmentation** — Sovan Biswas, Anthony Rhodes, Ramesh Manuvinakurike, et al., Preprint 2022.
  [PDF](https://arxiv.org/pdf/2211.01311) [arXiv](https://arxiv.org/abs/2211.01311)
  `semi-supervised` `unknown` `IMU`
  _Status:_ arXiv 2211.01311; first submitted 2022-11-02; last updated 2022-11-03; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-do-we-really-need-convolutions"></a>
- **Do we really need temporal convolutions in action segmentation?** — Dazhao Du, Bing Su, Yu Li, et al., Preprint 2022.
  [PDF](https://arxiv.org/pdf/2205.13425) [arXiv](https://arxiv.org/abs/2205.13425)
  `fully-supervised` `Transformer` `boundary-modeling` `unknown`
  _Status:_ arXiv 2205.13425; first submitted 2022-05-26; last updated 2022-11-22; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-hand-guided-high-resolution-feature"></a>
- **Hand Guided High Resolution Feature Enhancement for Fine-Grained Atomic Action Segmentation within Complex Human Assemblies** — Matthew Kent Myers, Nick Wright, Stephen McGough, et al., Preprint 2022.
  [PDF](https://arxiv.org/pdf/2211.13694) [arXiv](https://arxiv.org/abs/2211.13694)
  `fully-supervised` `unknown` `unknown`
  _Status:_ arXiv 2211.13694; first submitted 2022-11-24; last updated 2022-11-24; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-semantic2graph-graph-based-multi-modal"></a>
- **Semantic2Graph: Graph-based Multi-modal Feature Fusion for Action Segmentation in Videos** — Junbin Zhang, Pei-Hsuan Tsai, Meng-Hsun Tsai, Preprint 2022.
  [PDF](https://arxiv.org/pdf/2209.05653) [arXiv](https://arxiv.org/abs/2209.05653)
  `fully-supervised` `Transformer` `multimodal` `50Salads` `GTEA`
  _Status:_ arXiv 2209.05653; first submitted 2022-09-12; last update 2023-03-15; no formal proceedings placement verified by 2026-07-28.
<a id="paper-2022-preprint-skeleton-based-multi-stage-spatial"></a>
- **Skeleton-Based Action Segmentation with Multi-Stage Spatial-Temporal Graph Convolutional Neural Networks** — Benjamin Filtjens, Bart Vanrumste, Peter Slaets, Preprint 2022.
  [PDF](https://arxiv.org/pdf/2202.01727) [arXiv](https://arxiv.org/abs/2202.01727)
  `fully-supervised` `TCN` `multi-stage-TCN` `skeleton`
  _Status:_ arXiv 2202.01727; first submitted 2022-02-03; last updated 2022-10-09; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-analysis-modern-techniques"></a>
- **Temporal Action Segmentation: An Analysis of Modern Techniques** — Guodong Ding, Fadime Sener, Angela Yao, Preprint 2022.
  [PDF](https://arxiv.org/pdf/2210.10352) [arXiv](https://arxiv.org/abs/2210.10352)
  `fully-supervised` `unknown` `unknown`
  _Publication metadata:_ IEEE TPAMI 2023; `venue-mentioned`; `unverified-author-metadata`.
  _Status:_ arXiv 2210.10352; first submitted 2022-10-19; last updated 2023-10-21; comment=19 pages, 9 figures, 8 tables, TPAMI 2023; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2022-preprint-transformers-weakly-supervised"></a>
- **Transformers in Action: Weakly Supervised Action Segmentation** — John Ridley, Huseyin Coskun, David Joseph Tan, et al., Preprint 2022.
  [PDF](https://arxiv.org/pdf/2201.05675) [arXiv](https://arxiv.org/abs/2201.05675)
  `weakly-supervised` `Transformer` `unknown`
  _Status:_ arXiv 2201.05675; first submitted 2022-01-14; last updated 2022-01-20; comment=Under Review; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2021-preprint-coarse-fine-multi-resolution-convolutional"></a>
- **Coarse to Fine Multi-Resolution Temporal Convolutional Network** — Dipika Singhania, Rahul Rahaman, Angela Yao, Preprint 2021.
  [PDF](https://arxiv.org/pdf/2105.10859) [arXiv](https://arxiv.org/abs/2105.10859)
  `fully-supervised` `TCN` `unknown`
  _Status:_ arXiv 2105.10859; first submitted 2021-05-23; last update 2021-05-23; no formal proceedings placement verified by 2026-07-28.
<a id="paper-2021-preprint-fifa-fast-inference-approximation"></a>
- **FIFA: Fast Inference Approximation for Action Segmentation** — Yaser Souri, Yazan Abu Farha, Fabien Despinoy, et al., Preprint 2021.
  [PDF](https://arxiv.org/pdf/2108.03894) [arXiv](https://arxiv.org/abs/2108.03894)
  `weakly-supervised` `unknown` `unknown`
  _Status:_ arXiv 2108.03894; first submitted 2021-08-09; last updated 2021-08-09; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2021-preprint-high-level-complex-activity-labels"></a>
- **Temporal Action Segmentation with High-level Complex Activity Labels** — Guodong Ding, Angela Yao, Preprint 2021.
  [PDF](https://arxiv.org/pdf/2108.06706) [arXiv](https://arxiv.org/abs/2108.06706)
  `fully-supervised` `prototype-learning` `unknown`
  _Status:_ arXiv 2108.06706; first submitted 2021-08-15; last updated 2022-12-17; comment=12 pages, 6 figures; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2021-preprint-unsupervised-instructional-videos"></a>
- **Unsupervised Action Segmentation for Instructional Videos** — AJ Piergiovanni, Anelia Angelova, Michael S. Ryoo, et al., Preprint 2021.
  [PDF](https://arxiv.org/pdf/2106.03738) [arXiv](https://arxiv.org/abs/2106.03738)
  `unsupervised` `unknown` `unknown`
  _Publication metadata:_ LUV Workshop; `venue-mentioned`; `unverified-author-metadata`.
  _Status:_ arXiv 2106.03738; first submitted 2021-06-07; last updated 2021-06-07; comment=4 page abstract for LUV workshop; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2020-preprint-hierarchical-attention-network"></a>
- **Hierarchical Attention Network for Action Segmentation** — Harshala Gammulle, Simon Denman, Sridha Sridharan, et al., Preprint 2020.
  [PDF](https://arxiv.org/pdf/2005.03209) [arXiv](https://arxiv.org/abs/2005.03209)
  `fully-supervised` `unknown` `unknown`
  _Publication metadata:_ Pattern Recognition Letters; `author-claimed-accepted`; `unverified-author-metadata`.
  _Status:_ arXiv 2005.03209; first submitted 2020-05-07; last updated 2020-05-07; comment=Published in Pattern Recognition Letters; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2020-preprint-evaluating-weakly-supervised-methods"></a>
- **On Evaluating Weakly Supervised Action Segmentation Methods** — Yaser Souri, Alexander Richard, Luca Minciullo, et al., Preprint 2020.
  [PDF](https://arxiv.org/pdf/2005.09743) [arXiv](https://arxiv.org/abs/2005.09743)
  `weakly-supervised` `unknown` `I3D-features` `Breakfast`
  _Status:_ arXiv 2005.09743; first submitted 2020-05-19; last updated 2021-10-21; comment=Technical Report; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2019-preprint-hybrid-rnn-hmm-approach-weakly"></a>
- **A Hybrid RNN-HMM Approach for Weakly Supervised Temporal Action Segmentation** — Hilde Kuehne, Alexander Richard, Juergen Gall, Preprint 2019.
  [PDF](https://arxiv.org/pdf/1906.01028) [arXiv](https://arxiv.org/abs/1906.01028)
  `weakly-supervised` `unknown` `unknown` `Breakfast`
  _Publication metadata:_ IEEE TPAMI; `submission-only`; `unverified-author-metadata`.
  _Status:_ arXiv 1906.01028; first submitted 2019-06-03; last updated 2019-06-03; comment=15 pages, preprint for IEEE TPAMI https://ieeexplore.ieee.org/document/8585084 (open access). arXiv admin note: substantial text overlap with arXiv:1703.08132; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2019-preprint-fine-grained-using-semi-supervised"></a>
- **Fine-grained Action Segmentation using the Semi-Supervised Action GAN** — Harshala Gammulle, Simon Denman, Sridha Sridharan, et al., Preprint 2019.
  [PDF](https://arxiv.org/pdf/1909.09269) [arXiv](https://arxiv.org/abs/1909.09269)
  `semi-supervised` `unknown` `unknown`
  _Publication metadata:_ Pattern Recognition; `author-claimed-accepted`; `unverified-author-metadata`.
  _Status:_ arXiv 1909.09269; first submitted 2019-09-20; last updated 2019-09-20; comment=Published in Pattern Recognition Journal; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2019-preprint-frontal-low-rank-random-tensors"></a>
- **Frontal Low-rank Random Tensors for Fine-grained Action Segmentation** — Yan Zhang, Krikamol Muandet, Qianli Ma, et al., Preprint 2019.
  [PDF](https://arxiv.org/pdf/1906.01004) [arXiv](https://arxiv.org/abs/1906.01004)
  `fully-supervised` `unknown` `unknown`
  _Status:_ arXiv 1906.01004; first submitted 2019-06-03; last updated 2020-04-06; comment=19 pages (4 pages appendix), 3 figures. Revised theories and models, new experiments; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2018-preprint-local-bilinear-pooling-fine-grained"></a>
- **Local Temporal Bilinear Pooling for Fine-grained Action Parsing** — Yan Zhang, Siyu Tang, Krikamol Muandet, et al., Preprint 2018.
  [PDF](https://arxiv.org/pdf/1812.01922) [arXiv](https://arxiv.org/abs/1812.01922)
  `fully-supervised` `TCN` `unknown`
  _Status:_ arXiv 1812.01922; first submitted 2018-12-05; last updated 2019-05-26; comment=11 pages, 2 figures. Cam.R; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2018-preprint-human-dynamic-clustering"></a>
- **Temporal Human Action Segmentation via Dynamic Clustering** — Yan Zhang, He Sun, Siyu Tang, et al., Preprint 2018.
  [PDF](https://arxiv.org/pdf/1803.05790) [arXiv](https://arxiv.org/abs/1803.05790)
  `unsupervised` `clustering` `unknown`
  _Status:_ arXiv 1803.05790; first submitted 2018-03-15; last updated 2018-03-18; comment=comparing with the 1st version, only corrected typos; journal_ref=none. No formal conference proceedings placement has been verified.
<a id="paper-2017-preprint-tricornet-hybrid-convolutional-recurrent-network"></a>
- **TricorNet: A Hybrid Temporal Convolutional and Recurrent Network for Video Action Segmentation** — Li Ding, Chenliang Xu, Preprint 2017.
  [PDF](https://arxiv.org/pdf/1705.07818) [arXiv](https://arxiv.org/abs/1705.07818)
  `fully-supervised` `TCN` `unknown`
  _Status:_ arXiv 1705.07818; first submitted 2017-05-22; last updated 2017-05-22; comment=none; journal_ref=none. No formal conference proceedings placement has been verified.

## Related-but-not-core

<a id="paper-2022-cvpr-assembly101-large-scale-multi-view"></a>
- **Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities** — Fadime Sener, Dibyadip Chatterjee, Daniel Shelepov, et al., CVPR 2022.
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.pdf) [arXiv](http://arxiv.org/abs/2203.14712)
  `fully-supervised` `unknown` `IMU` `Assembly101`
  _Why related:_ This dataset paper directly enabled or standardized temporal action/step segmentation evaluation, but its primary contribution is a benchmark rather than a core TAS method.
<a id="paper-2014-cvpr-language-actions-recovering-syntax-semantics"></a>
- **The Language of Actions: Recovering the Syntax and Semantics of Goal-Directed Human Activities** — Hilde Kuehne, Ali Arslan, Thomas Serre, CVPR 2014.
  [Paper](https://openaccess.thecvf.com/content_cvpr_2014/html/Kuehne_The_Language_of_2014_CVPR_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2014/papers/Kuehne_The_Language_of_2014_CVPR_paper.pdf)
  `fully-supervised` `structured-decoding` `unknown`
  _Why related:_ This dataset paper directly enabled or standardized temporal action/step segmentation evaluation, but its primary contribution is a benchmark rather than a core TAS method.

## Documentation

- [中文系统综述](docs/survey_zh.md)
- [历史时间线](docs/history_timeline.md)
- [任务分类体系](docs/taxonomy.md)
- [数据集与指标](docs/datasets_and_metrics.md)
- [检索方法](docs/search_methodology.md)
- [验证报告](docs/verification_report.md)

## Updating and reporting errors

完整更新：`python scripts/update_repository.py --cutoff-date 2026-07-28`。跳过 PDF：追加 `--skip-download`；联网前预演：追加 `--dry-run`。若发现遗漏、误收或失效链接，请按 [CONTRIBUTING.md](CONTRIBUTING.md) 提供标题、任务输出、实验数据集/指标和一手发表来源。

PDF 仅保存在本地 `library/pdfs/`，默认被 Git 忽略；仓库不创建远程、不上传 PDF。

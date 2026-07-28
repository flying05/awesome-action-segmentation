# Awesome Action Segmentation

一个经过一手来源核验、可重复生成的 Temporal Action Segmentation（TAS）论文与资料索引。TAS 在长视频、骨架或多模态序列上预测逐帧/逐时间步动作类别，并同时确定连续动作片段的边界。

**Data cutoff:** 2026-07-28  
**Verified conference papers:** 77  
**Preprints / pending verification:** 3  
**Related benchmark or boundary papers:** 3

## Scope and inclusion criteria

纳入的核心工作必须输出稠密动作标签或连续动作片段，并以帧准确率、MoF、Edit、segmental F1、mIoU 或动作边界指标进行评价。仅做整段动作识别、proposal、时序动作定位、时空框检测、图像/人体空间分割或无动作语义的章节切分不进入核心列表。每条正式记录至少保留一个会议proceedings、学会数字图书馆或正式论文页作为验证来源。

会议范围包括 CVPR、ICCV、NeurIPS、ICML、AAAI、IJCAI、ACM MM，以及 ECCV、WACV、BMVC；与 TAS 直接相关的 MICCAI、IROS 等工作置于扩展类别。2026 年只收录在截点前已能由正式 proceedings 确认的论文。arXiv-only 工作严格置于独立的 Pending Verification 区。

## Statistics

| View | Counts |
|---|---|
| By venue | AAAI: 1; BMVC: 2; CVPR: 36; ECCV: 8; ICCV: 14; IJCAI: 2; IROS: 1; MICCAI: 1; NeurIPS: 3; WACV: 9 |
| By year | 2026: 5; 2025: 6; 2024: 9; 2023: 6; 2022: 16; 2021: 10; 2020: 10; 2019: 5; 2018: 4; 2017: 2; 2016: 2; 2015: 1; 2014: 1 |

## Paper index by supervision

这是唯一完整主索引；后面的技术路线和应用场景索引只链接到此处，避免重复维护同一条目。

### Fully Supervised

<a id="paper-2026-cvpr-lady-lagrangian-dynamic-informed-network"></a>
- **LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation** — Haoyu Ji, Xueting Liu, Yu Gao, et al., CVPR 2026.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ji_LaDy_Lagrangian-Dynamic_Informed_Network_for_Skeleton-based_Action_Segmentation_via_Spatial-Temporal_CVPR_2026_paper.pdf)  
  `fully-supervised` `boundary-modeling` `skeleton`
<a id="paper-2026-cvpr-polyphony-diffusion-based-dual-hand"></a>
- **Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning** — Hao Zheng, Hu Wang, Tiantian Zheng, et al., CVPR 2026.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_Polyphony_Diffusion-based_Dual-Hand_Action_Segmentation_with_Alternating_Vision_Transformer_and_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_Polyphony_Diffusion-based_Dual-Hand_Action_Segmentation_with_Alternating_Vision_Transformer_and_CVPR_2026_paper.pdf)  
  `fully-supervised` `Transformer` `diffusion` `I3D-features` `Breakfast`
<a id="paper-2026-cvpr-spectral-scalpel-amplifying-adjacent-discrepancy"></a>
- **Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation** — Haoyu Ji, Bowen Chen, Zhihao Yang, et al., CVPR 2026.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.pdf)  
  `fully-supervised` `boundary-modeling` `skeleton`
<a id="paper-2025-cvpr-condensing-datasets-generative-network-inversion"></a>
- **Condensing Action Segmentation Datasets via Generative Network Inversion** — Guodong Ding, Rongyu Chen, Angela Yao, CVPR 2025.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_Condensing_Action_Segmentation_Datasets_via_Generative_Network_Inversion_CVPR_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Ding_Condensing_Action_Segmentation_Datasets_via_Generative_Network_Inversion_CVPR_2025_paper.pdf)  
  `fully-supervised` `dataset-condensation` `I3D-features` `Breakfast`
<a id="paper-2025-iccv-duoclr-dual-surrogate-contrastive-learning"></a>
- **DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation** — Haitao Tian, ICCV 2025.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_DuoCLR_Dual-Surrogate_Contrastive_Learning_for_Skeleton-based_Human_Action_Segmentation_ICCV_2025_paper.pdf)  
  `fully-supervised` `unknown` `skeleton`
<a id="paper-2024-cvpr-coherent-synthesis-incremental"></a>
- **Coherent Temporal Synthesis for Incremental Action Segmentation** — Guodong Ding, Hans Golong, Angela Yao, CVPR 2024.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Ding_Coherent_Temporal_Synthesis_for_Incremental_Action_Segmentation_CVPR_2024_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2024-cvpr-fact-frame-cross-attention-modeling"></a>
- **FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation** — Zijia Lu, Ehsan Elhamifar, CVPR 2024.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.pdf) [Code](https://github.com/ZijiaLewisLu/CVPR2024-FACT)  
  `fully-supervised` `Transformer` `cross-attention` `I3D-features`
<a id="paper-2024-cvpr-progress-aware-online-egocentric-procedural"></a>
- **Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos** — Yuhan Shen, Ehsan Elhamifar, CVPR 2024.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Shen_Progress-Aware_Online_Action_Segmentation_for_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.pdf)  
  `fully-supervised` `causal-model` `I3D-features`
<a id="paper-2024-neurips-onlinetas-online-baseline"></a>
- **OnlineTAS: An Online Baseline for Temporal Action Segmentation** — Shijie Li, Yazan Abu Farha, Juergen Gall, NeurIPS 2024.  
  [Paper](https://papers.nips.cc/paper_files/paper/2024/hash/6c6c5fccf3c8661fcae219be7ca226f7-Abstract-Conference.html) [PDF](https://papers.nips.cc/paper_files/paper/2024/file/6c6c5fccf3c8661fcae219be7ca226f7-Paper-Conference.pdf)  
  `fully-supervised` `TCN` `causal-model` `I3D-features`
<a id="paper-2023-iccv-diffusion"></a>
- **Diffusion Action Segmentation** — Daochang Liu, Qiyue Li, Anh-Dung Dinh, et al., ICCV 2023.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.pdf) [Code](https://github.com/Finspire13/DiffAct)  
  `fully-supervised` `diffusion` `boundary-modeling` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2023-iccv-contextually-refined-keypoints"></a>
- **Video Action Segmentation via Contextually Refined Temporal Keypoints** — Borui Jiang, Yang Jin, Zhentao Tan, et al., ICCV 2023.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Jiang_Video_Action_Segmentation_via_Contextually_Refined_Temporal_Keypoints_ICCV_2023_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2023-neurips-activity-grammars"></a>
- **Activity Grammars for Temporal Action Segmentation** — Dayoung Gong, Joonseok Lee, Deunsol Jung, et al., NeurIPS 2023.  
  [Paper](https://papers.nips.cc/paper_files/paper/2023/hash/ee6c4b99b4c0d3d60efd22c1ecdd9891-Abstract-Conference.html) [PDF](https://papers.nips.cc/paper_files/paper/2023/file/ee6c4b99b4c0d3d60efd22c1ecdd9891-Paper-Conference.pdf) [Code](http://cvlab.postech.ac.kr/research/KARI)  
  `fully-supervised` `structured-decoding` `I3D-features`
<a id="paper-2022-cvpr-set-supervised-learning-procedural-task"></a>
- **Set-Supervised Action Learning in Procedural Task Videos via Pairwise Order Consistency** — Zijia Lu, Ehsan Elhamifar, CVPR 2022.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lu_Set-Supervised_Action_Learning_in_Procedural_Task_Videos_via_Pairwise_Order_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lu_Set-Supervised_Action_Learning_in_Procedural_Task_Videos_via_Pairwise_Order_CVPR_2022_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features`
<a id="paper-2022-ijcai-uncertainty-aware-representation-learning"></a>
- **Uncertainty-Aware Representation Learning for Action Segmentation** — Lei Chen, Muheng Li, Yueqi Duan, et al., IJCAI 2022.  
  [Paper](https://www.ijcai.org/proceedings/2022/115) [PDF](https://www.ijcai.org/proceedings/2022/0115.pdf)  
  `fully-supervised` `uncertainty-modeling` `boundary-modeling` `I3D-features`
<a id="paper-2022-neurips-don-t-pour-cereal-into"></a>
- **Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation** — Ziwei Xu, Yogesh S. Rawat, Yongkang Wong, et al., NeurIPS 2022.  
  [Paper](https://openreview.net/forum?id=PCQyUvAmKs) [PDF](https://openreview.net/pdf?id=PCQyUvAmKs) [Code](https://diff-tl.github.io/)  
  `fully-supervised` `structured-decoding` `I3D-features`
<a id="paper-2021-bmvc-asformer-transformer"></a>
- **ASFormer: Transformer for Action Segmentation** — Fangqiu Yi, Hongyu Wen, Tingting Jiang, BMVC 2021.  
  [Paper](https://www.bmvc2021-virtualconference.com/conference/papers/paper_0578.html) [PDF](https://www.bmvc2021-virtualconference.com/assets/papers/0578.pdf) [Code](https://github.com/ChinaYi/ASFormer)  
  `fully-supervised` `Transformer` `I3D-features`
<a id="paper-2021-cvpr-anchor-constrained-viterbi-set-supervised"></a>
- **Anchor-Constrained Viterbi for Set-Supervised Action Segmentation** — Jun Li, Sinisa Todorovic, CVPR 2021.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Anchor-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Anchor-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2021_paper.pdf)  
  `fully-supervised` `structured-decoding` `I3D-features` `Breakfast`
<a id="paper-2021-cvpr-global2local-efficient-structure-search"></a>
- **Global2Local: Efficient Structure Search for Video Action Segmentation** — Shang-Hua Gao, Qi Han, Zhong-Yu Li, et al., CVPR 2021.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Gao_Global2Local_Efficient_Structure_Search_for_Video_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Gao_Global2Local_Efficient_Structure_Search_for_Video_Action_Segmentation_CVPR_2021_paper.pdf) [Code](https://github.com/Thinksky5124/G2L)  
  `fully-supervised` `unknown` `I3D-features`
<a id="paper-2021-iccv-refining-hierarchical-representations"></a>
- **Refining Action Segmentation With Hierarchical Video Representations** — Hyemin Ahn, Dongheui Lee, ICCV 2021.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Ahn_Refining_Action_Segmentation_With_Hierarchical_Video_Representations_ICCV_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Ahn_Refining_Action_Segmentation_With_Hierarchical_Video_Representations_ICCV_2021_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2020-cvpr-improving-graph-based-reasoning"></a>
- **Improving Action Segmentation via Graph-Based Temporal Reasoning** — Yifei Huang, Yusuke Sugano, Yoichi Sato, CVPR 2020.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Huang_Improving_Action_Segmentation_via_Graph-Based_Temporal_Reasoning_CVPR_2020_paper.pdf)  
  `fully-supervised` `boundary-modeling` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2020-eccv-boundary-aware-cascade-networks"></a>
- **Boundary-Aware Cascade Networks for Temporal Action Segmentation** — Zhenzhi Wang, Ziteng Gao, Limin Wang, et al., ECCV 2020.  
  [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/35_ECCV_2020_paper.php) [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123700035.pdf) [Code](https://github.com/MCG-NJU/BCN)  
  `fully-supervised` `boundary-modeling` `I3D-features`
<a id="paper-2020-eccv-aggregate-representations-long-range-understanding"></a>
- **Temporal Aggregate Representations for Long-Range Video Understanding** — Fadime Sener, Dipika Singhania, Angela Yao, ECCV 2020.  
  [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/154_ECCV_2020_paper.php) [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610154.pdf)  
  `fully-supervised` `TCN` `I3D-features`
<a id="paper-2020-miccai-tecno-surgical-phase-recognition-multi"></a>
- **TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks** — Tobias Czempiel, Magdalini Paschali, Matthias Keicher, et al., MICCAI 2020.  
  [Paper](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_33) [Code](https://github.com/tobiascz/MICCAI2020-TeCNO)  
  `fully-supervised` `TCN` `multi-stage-TCN` `I3D-features` `Cholec80`
<a id="paper-2020-wacv-mixed-domain-adaptation"></a>
- **Action Segmentation with Mixed Temporal Domain Adaptation** — Min-Hung Chen, Baopu Li, Yingze Bao, et al., WACV 2020.  
  [Paper](https://openaccess.thecvf.com/content_WACV_2020/html/Chen_Action_Segmentation_with_Mixed_Temporal_Domain_Adaptation_WACV_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_WACV_2020/papers/Chen_Action_Segmentation_with_Mixed_Temporal_Domain_Adaptation_WACV_2020_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2020-wacv-stacked-spatio-graph-convolutional-networks"></a>
- **Stacked Spatio-Temporal Graph Convolutional Networks for Action Segmentation** — Pallabi Ghosh, Yi Yao, Larry Davis, et al., WACV 2020.  
  [Paper](https://openaccess.thecvf.com/content_WACV_2020/html/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_WACV_2020/papers/Ghosh_Stacked_Spatio-Temporal_Graph_Convolutional_Networks_for_Action_Segmentation_WACV_2020_paper.pdf)  
  `fully-supervised` `unknown` `skeleton`
<a id="paper-2019-cvpr-ms-tcn-multi-stage-convolutional"></a>
- **MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation** — Yazan Abu Farha, Jurgen Gall, CVPR 2019.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.pdf) [Code](https://github.com/yabufarha/ms-tcn)  
  `fully-supervised` `TCN` `multi-stage-TCN` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2017-cvpr-convolutional-networks-detection"></a>
- **Temporal Convolutional Networks for Action Segmentation and Detection** — Colin Lea, Michael D. Flynn, Rene Vidal, et al., CVPR 2017.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2017/papers/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.pdf)  
  `fully-supervised` `duration-modeling` `TCN` `I3D-features`
<a id="paper-2014-cvpr-leveraging-hierarchical-parametric-networks-skeletal"></a>
- **Leveraging Hierarchical Parametric Networks for Skeletal Joints Based Action Segmentation and Recognition** — Di Wu, Ling Shao, CVPR 2014.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2014/html/Wu_Leveraging_Hierarchical_Parametric_2014_CVPR_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2014/papers/Wu_Leveraging_Hierarchical_Parametric_2014_CVPR_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features`

### Weakly Supervised

<a id="paper-2026-cvpr-hierarchical-learning-weakly-supervised"></a>
- **Hierarchical Action Learning for Weakly-Supervised Action Segmentation** — Junxian Huang, Ruichu Cai, Juntao Fang, et al., CVPR 2026.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Hierarchical_Action_Learning_for_Weakly-Supervised_Action_Segmentation_CVPR_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Hierarchical_Action_Learning_for_Weakly-Supervised_Action_Segmentation_CVPR_2026_paper.pdf)  
  `weakly-supervised` `Transformer` `causal-model` `I3D-features`
<a id="paper-2026-wacv-timestamp-query-transformer"></a>
- **Timestamp Query Transformer for Temporal Action Segmentation** — Tieqiao Wang, Sinisa Todorovic, WACV 2026.  
  [Paper](https://openaccess.thecvf.com/content/WACV2026/html/Wang_Timestamp_Query_Transformer_for_Temporal_Action_Segmentation_WACV_2026_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2026/papers/Wang_Timestamp_Query_Transformer_for_Temporal_Action_Segmentation_WACV_2026_paper.pdf)  
  `timestamp-supervised` `Transformer` `cross-attention` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2024-cvpr-efficient-effective-weakly-supervised-transition"></a>
- **Efficient and Effective Weakly-Supervised Action Segmentation via Action-Transition-Aware Boundary Alignment** — Angchi Xu, Wei-Shi Zheng, CVPR 2024.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Efficient_and_Effective_Weakly-Supervised_Action_Segmentation_via_Action-Transition-Aware_Boundary_Alignment_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Efficient_and_Effective_Weakly-Supervised_Action_Segmentation_via_Action-Transition-Aware_Boundary_Alignment_CVPR_2024_paper.pdf)  
  `weakly-supervised` `boundary-modeling` `I3D-features`
<a id="paper-2024-wacv-random-walks-timestamp-supervision"></a>
- **Random Walks for Temporal Action Segmentation With Timestamp Supervision** — Roy Hirsch, Regev Cohen, Tomer Golany, et al., WACV 2024.  
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Hirsch_Random_Walks_for_Temporal_Action_Segmentation_With_Timestamp_Supervision_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Hirsch_Random_Walks_for_Temporal_Action_Segmentation_With_Timestamp_Supervision_WACV_2024_paper.pdf)  
  `timestamp-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2023-iccv-weakly-supervised-unseen-error-detection"></a>
- **Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos** — Reza Ghoddoosian, Isht Dwivedi, Nakul Agarwal, et al., ICCV 2023.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.pdf)  
  `weakly-supervised` `structured-decoding` `I3D-features`
<a id="paper-2023-ijcai-timestamp-supervised-perspective-clustering"></a>
- **Timestamp-Supervised Action Segmentation in the Perspective of Clustering** — Dazhao Du, Enhan Li, Lingyu Si, et al., IJCAI 2023.  
  [Paper](https://www.ijcai.org/proceedings/2023/77) [PDF](https://www.ijcai.org/proceedings/2023/0077.pdf) [Code](https://github.com/ddz16/TSASPC)  
  `timestamp-supervised` `clustering` `I3D-features`
<a id="paper-2022-bmvc-robust-timestamp-supervision"></a>
- **Robust Action Segmentation from Timestamp Supervision** — Yaser Souri, Yazan Abu Farha, Emad Bahrami, et al., BMVC 2022.  
  [Paper](https://bmvc2022.mpi-inf.mpg.de/392/) [PDF](https://bmvc2022.mpi-inf.mpg.de/0392.pdf)  
  `timestamp-supervised` `TCN` `boundary-modeling` `I3D-features`
<a id="paper-2022-cvpr-semi-weakly-supervised-learning-complex"></a>
- **Semi-Weakly-Supervised Learning of Complex Actions From Instructional Task Videos** — Yuhan Shen, Ehsan Elhamifar, CVPR 2022.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shen_Semi-Weakly-Supervised_Learning_of_Complex_Actions_From_Instructional_Task_Videos_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Shen_Semi-Weakly-Supervised_Learning_of_Complex_Actions_From_Instructional_Task_Videos_CVPR_2022_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features`
<a id="paper-2022-cvpr-weakly-supervised-online-multi-view"></a>
- **Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos** — Reza Ghoddoosian, Isht Dwivedi, Nakul Agarwal, et al., CVPR 2022.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Ghoddoosian_Weakly-Supervised_Online_Action_Segmentation_in_Multi-View_Instructional_Videos_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Ghoddoosian_Weakly-Supervised_Online_Action_Segmentation_in_Multi-View_Instructional_Videos_CVPR_2022_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2022-eccv-generalized-robust-framework-timestamp-supervision"></a>
- **A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation** — Rahul Rahaman, Dipika Singhania, Alexandre Thiery, et al., ECCV 2022.  
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4788_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136640276.pdf) [Code](https://github.com/rahulrahaman/Timestamp-and-SkipTag)  
  `timestamp-supervised` `TCN` `uncertainty-modeling` `I3D-features`
<a id="paper-2022-eccv-unified-fully-timestamp-supervised-sequence"></a>
- **Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation** — Nadine Behrmann, S. Alireza Golestaneh, Zico Kolter, et al., ECCV 2022.  
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3672_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950052.pdf)  
  `timestamp-supervised` `Transformer` `structured-decoding` `I3D-features`
<a id="paper-2022-iros-timestamp-supervised-graph-convolutional-networks"></a>
- **Timestamp-Supervised Action Segmentation with Graph Convolutional Networks** — Hamza Khan, Sanjay Haresh, Awais Ahmed, et al., IROS 2022.  
  [Paper](https://doi.org/10.1109/IROS47612.2022.9981176) [PDF](https://arxiv.org/pdf/2206.15031)  
  `timestamp-supervised` `graphical-model` `TCN` `I3D-features`
<a id="paper-2022-wacv-hierarchical-modeling-task-recognition-weakly"></a>
- **Hierarchical Modeling for Task Recognition and Action Segmentation in Weakly-Labeled Instructional Videos** — Reza Ghoddoosian, Saif Sayed, Vassilis Athitsos, WACV 2022.  
  [Paper](https://openaccess.thecvf.com/content/WACV2022/html/Ghoddoosian_Hierarchical_Modeling_for_Task_Recognition_and_Action_Segmentation_in_Weakly-Labeled_WACV_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2022/papers/Ghoddoosian_Hierarchical_Modeling_for_Task_Recognition_and_Action_Segmentation_in_Weakly-Labeled_WACV_2022_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2022-wacv-sscap-self-supervised-co-occurrence"></a>
- **SSCAP: Self-Supervised Co-Occurrence Action Parsing for Unsupervised Temporal Action Segmentation** — Zhe Wang, Hao Chen, Xinyu Li, et al., WACV 2022.  
  [Paper](https://openaccess.thecvf.com/content/WACV2022/html/Wang_SSCAP_Self-Supervised_Co-Occurrence_Action_Parsing_for_Unsupervised_Temporal_Action_Segmentation_WACV_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2022/papers/Wang_SSCAP_Self-Supervised_Co-Occurrence_Action_Parsing_for_Unsupervised_Temporal_Action_Segmentation_WACV_2022_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2021-cvpr-learning-discriminative-prototypes-dynamic-time"></a>
- **Learning Discriminative Prototypes With Dynamic Time Warping** — Xiaobin Chang, Frederick Tung, Greg Mori, CVPR 2021.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Chang_Learning_Discriminative_Prototypes_With_Dynamic_Time_Warping_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Chang_Learning_Discriminative_Prototypes_With_Dynamic_Time_Warping_CVPR_2021_paper.pdf)  
  `weakly-supervised` `prototype-learning` `I3D-features`
<a id="paper-2021-cvpr-timestamp-supervision"></a>
- **Temporal Action Segmentation From Timestamp Supervision** — Zhe Li, Yazan Abu Farha, Jurgen Gall, CVPR 2021.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.pdf)  
  `timestamp-supervised` `unknown` `I3D-features`
<a id="paper-2021-iccv-weakly-supervised-alignment-transcript-aware"></a>
- **Weakly-Supervised Action Segmentation and Alignment via Transcript-Aware Union-of-Subspaces Learning** — Zijia Lu, Ehsan Elhamifar, ICCV 2021.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Lu_Weakly-Supervised_Action_Segmentation_and_Alignment_via_Transcript-Aware_Union-of-Subspaces_Learning_ICCV_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Lu_Weakly-Supervised_Action_Segmentation_and_Alignment_via_Transcript-Aware_Union-of-Subspaces_Learning_ICCV_2021_paper.pdf)  
  `weakly-supervised` `duration-modeling` `I3D-features`
<a id="paper-2020-cvpr-sct-set-constrained-transformer-set"></a>
- **SCT: Set Constrained Temporal Transformer for Set Supervised Action Segmentation** — Mohsen Fayyaz, Jurgen Gall, CVPR 2020.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Fayyaz_SCT_Set_Constrained_Temporal_Transformer_for_Set_Supervised_Action_Segmentation_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fayyaz_SCT_Set_Constrained_Temporal_Transformer_for_Set_Supervised_Action_Segmentation_CVPR_2020_paper.pdf)  
  `weakly-supervised` `Transformer` `I3D-features`
<a id="paper-2020-cvpr-set-constrained-viterbi-set-supervised"></a>
- **Set-Constrained Viterbi for Set-Supervised Action Segmentation** — Jun Li, Sinisa Todorovic, CVPR 2020.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Set-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Li_Set-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2020_paper.pdf)  
  `weakly-supervised` `structured-decoding` `I3D-features` `Breakfast`
<a id="paper-2020-eccv-fast-weakly-supervised-using-mutual"></a>
- **Fast Weakly Supervised Action Segmentation Using Mutual Consistency** — Yaser Souri, Mohsen Fayyaz, Luca Minciullo, et al., ECCV 2020.  
  [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1061_ECCV_2020_paper.php) [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123570664.pdf) [Code](https://github.com/yassersouri/MuCon)  
  `weakly-supervised` `TCN` `structured-decoding` `I3D-features`
<a id="paper-2019-cvpr-d3tw-discriminative-differentiable-dynamic-time"></a>
- **D3TW: Discriminative Differentiable Dynamic Time Warping for Weakly Supervised Action Alignment and Segmentation** — Chien-Yi Chang, De-An Huang, Yanan Sui, et al., CVPR 2019.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Chang_D3TW_Discriminative_Differentiable_Dynamic_Time_Warping_for_Weakly_Supervised_Action_CVPR_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Chang_D3TW_Discriminative_Differentiable_Dynamic_Time_Warping_for_Weakly_Supervised_Action_CVPR_2019_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features`
<a id="paper-2019-iccv-weakly-supervised-energy-based-learning"></a>
- **Weakly Supervised Energy-Based Learning for Action Segmentation** — Jun Li, Peng Lei, Sinisa Todorovic, ICCV 2019.  
  [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Li_Weakly_Supervised_Energy-Based_Learning_for_Action_Segmentation_ICCV_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Li_Weakly_Supervised_Energy-Based_Learning_for_Action_Segmentation_ICCV_2019_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2018-cvpr-sets-weakly-supervised-without-ordering"></a>
- **Action Sets: Weakly Supervised Action Segmentation Without Ordering Constraints** — Alexander Richard, Hilde Kuehne, Juergen Gall, CVPR 2018.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_Action_Sets_Weakly_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Richard_Action_Sets_Weakly_CVPR_2018_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features`
<a id="paper-2018-cvpr-neuralnetwork-viterbi-framework-weakly-supervised"></a>
- **NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning** — Alexander Richard, Hilde Kuehne, Ahsan Iqbal, et al., CVPR 2018.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.pdf)  
  `weakly-supervised` `structured-decoding` `I3D-features`
<a id="paper-2018-cvpr-unsupervised-learning-complex-activities"></a>
- **Unsupervised Learning and Segmentation of Complex Activities From Video** — Fadime Sener, Angela Yao, CVPR 2018.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Sener_Unsupervised_Learning_and_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Sener_Unsupervised_Learning_and_CVPR_2018_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2018-cvpr-weakly-supervised-iterative-soft-boundary"></a>
- **Weakly-Supervised Action Segmentation With Iterative Soft Boundary Assignment** — Li Ding, Chenliang Xu, CVPR 2018.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Ding_Weakly-Supervised_Action_Segmentation_CVPR_2018_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Ding_Weakly-Supervised_Action_Segmentation_CVPR_2018_paper.pdf)  
  `weakly-supervised` `boundary-modeling` `TCN` `I3D-features` `Breakfast`
<a id="paper-2017-cvpr-weakly-supervised-learning-rnn-based"></a>
- **Weakly Supervised Action Learning With RNN Based Fine-To-Coarse Modeling** — Alexander Richard, Hilde Kuehne, Juergen Gall, CVPR 2017.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Richard_Weakly_Supervised_Action_CVPR_2017_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2017/papers/Richard_Weakly_Supervised_Action_CVPR_2017_paper.pdf)  
  `weakly-supervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2016-eccv-connectionist-modeling-weakly-supervised-labeling"></a>
- **Connectionist Temporal Modeling for Weakly Supervised Action Labeling** — De-An Huang, Fei-Fei Li, Juan Carlos Niebles, ECCV 2016.  
  [Paper](https://www.ecva.net/papers/eccv_2016/papers_ECCV/html/Huang_Connectionist_Temporal_Modeling_ECCV_2016_paper.php) [PDF](https://www.ecva.net/papers/eccv_2016/papers_ECCV/papers/123560511.pdf)  
  `weakly-supervised` `TCN` `structured-decoding` `I3D-features`

### Semi-Supervised

<a id="paper-2022-aaai-iterative-contrast-classify-semi-supervised"></a>
- **Iterative Contrast-Classify for Semi-Supervised Temporal Action Segmentation** — Dipika Singhania, Rahul Rahaman, Angela Yao, AAAI 2022.  
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/20124) [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/20124/19883) [Code](https://github.com/dipika-singhania/ICC-Semi-Supervised-TAS)  
  `semi-supervised` `contrastive-learning` `clustering` `I3D-features`
<a id="paper-2022-eccv-leveraging-affinity-continuity-semi-supervised"></a>
- **Leveraging Action Affinity and Continuity for Semi-Supervised Temporal Action Segmentation** — Guodong Ding, Angela Yao, ECCV 2022.  
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3254_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950017.pdf) [Code](https://github.com/dinggd/semitas)  
  `semi-supervised` `contrastive-learning` `boundary-modeling` `I3D-features`

### Self-Supervised

<a id="paper-2025-iccv-joint-self-supervised-alignment"></a>
- **Joint Self-Supervised Video Alignment and Action Segmentation** — Ali Shah Ali, Syed Ahmed Mahmood, Mubin Saeed, et al., ICCV 2025.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ali_Joint_Self-Supervised_Video_Alignment_and_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ali_Joint_Self-Supervised_Video_Alignment_and_Action_Segmentation_ICCV_2025_paper.pdf)  
  `self-supervised` `optimal-transport` `I3D-features`
<a id="paper-2024-wacv-otas-unsupervised-boundary-detection-object"></a>
- **OTAS: Unsupervised Boundary Detection for Object-Centric Temporal Action Segmentation** — Yuerong Li, Zhengrong Xue, Huazhe Xu, WACV 2024.  
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Li_OTAS_Unsupervised_Boundary_Detection_for_Object-Centric_Temporal_Action_Segmentation_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Li_OTAS_Unsupervised_Boundary_Detection_for_Object-Centric_Temporal_Action_Segmentation_WACV_2024_paper.pdf)  
  `self-supervised` `boundary-modeling` `I3D-features`
<a id="paper-2023-iccv-lac-latent-composition-skeleton-based"></a>
- **LAC - Latent Action Composition for Skeleton-based Action Segmentation** — Di Yang, Yaohui Wang, Antitza Dantcheva, et al., ICCV 2023.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Yang_LAC_-_Latent_Action_Composition_for_Skeleton-based_Action_Segmentation_ICCV_2023_paper.pdf)  
  `self-supervised` `unknown` `skeleton`
<a id="paper-2021-cvpr-shuffle-alternating-learning-unsupervised"></a>
- **Action Shuffle Alternating Learning for Unsupervised Action Segmentation** — Jun Li, Sinisa Todorovic, CVPR 2021.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Action_Shuffle_Alternating_Learning_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Action_Shuffle_Alternating_Learning_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.pdf)  
  `self-supervised` `structured-decoding` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2020-cvpr-joint-self-supervised-domain-adaptation"></a>
- **Action Segmentation With Joint Self-Supervised Temporal Domain Adaptation** — Min-Hung Chen, Baopu Li, Yingze Bao, et al., CVPR 2020.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_Action_Segmentation_With_Joint_Self-Supervised_Temporal_Domain_Adaptation_CVPR_2020_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chen_Action_Segmentation_With_Joint_Self-Supervised_Temporal_Domain_Adaptation_CVPR_2020_paper.pdf)  
  `self-supervised` `unknown` `I3D-features` `Breakfast` `50Salads`

### Unsupervised

<a id="paper-2025-iccv-clot-closed-loop-optimal-transport"></a>
- **CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation** — Elena Bueno-Benito, Mariella Dimiccoli, ICCV 2025.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Bueno-Benito_CLOT_Closed_Loop_Optimal_Transport_for_Unsupervised_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Bueno-Benito_CLOT_Closed_Loop_Optimal_Transport_for_Unsupervised_Action_Segmentation_ICCV_2025_paper.pdf)  
  `unsupervised` `cross-attention` `optimal-transport` `I3D-features`
<a id="paper-2025-iccv-skeleton-motion-words-unsupervised-skeleton"></a>
- **Skeleton Motion Words for Unsupervised Skeleton-Based Temporal Action Segmentation** — Uzay Gökay, Federico Spurio, Dominik R. Bach, et al., ICCV 2025.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Gokay_Skeleton_Motion_Words_for_Unsupervised_Skeleton-Based_Temporal_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Gokay_Skeleton_Motion_Words_for_Unsupervised_Skeleton-Based_Temporal_Action_Segmentation_ICCV_2025_paper.pdf)  
  `unsupervised` `unknown` `skeleton`
<a id="paper-2024-cvpr-temporally-consistent-unbalanced-optimal-transport"></a>
- **Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation** — Ming Xu, Stephen Gould, CVPR 2024.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.pdf) [Code](https://github.com/mingu6/action-segmentation-ot)  
  `unsupervised` `optimal-transport` `I3D-features` `Breakfast`
<a id="paper-2024-wacv-united-we-stand-divided-we"></a>
- **United We Stand, Divided We Fall: UnityGraph for Unsupervised Procedure Learning From Videos** — Siddhant Bansal, Chetan Arora, C. V. Jawahar, WACV 2024.  
  [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Bansal_United_We_Stand_Divided_We_Fall_UnityGraph_for_Unsupervised_Procedure_WACV_2024_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2024/papers/Bansal_United_We_Stand_Divided_We_Fall_UnityGraph_for_Unsupervised_Procedure_WACV_2024_paper.pdf)  
  `unsupervised` `unknown` `I3D-features` `CrossTask`
<a id="paper-2022-cvpr-fast-unsupervised-boundary-detection"></a>
- **Fast and Unsupervised Action Boundary Detection for Action Segmentation** — Zexing Du, Xue Wang, Guoqing Zhou, et al., CVPR 2022.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Du_Fast_and_Unsupervised_Action_Boundary_Detection_for_Action_Segmentation_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Du_Fast_and_Unsupervised_Action_Boundary_Detection_for_Action_Segmentation_CVPR_2022_paper.pdf)  
  `unsupervised` `clustering` `boundary-modeling` `I3D-features`
<a id="paper-2022-cvpr-unsupervised-by-joint-representation-learning"></a>
- **Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering** — Sateesh Kumar, Sanjay Haresh, Awais Ahmed, et al., CVPR 2022.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Kumar_Unsupervised_Action_Segmentation_by_Joint_Representation_Learning_and_Online_Clustering_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Kumar_Unsupervised_Action_Segmentation_by_Joint_Representation_Learning_and_Online_Clustering_CVPR_2022_paper.pdf)  
  `unsupervised` `optimal-transport` `clustering` `I3D-features` `Breakfast`
<a id="paper-2022-eccv-my-view-is-best-view"></a>
- **My View Is the Best View: Procedure Learning from Egocentric Videos** — Siddhant Bansal, Chetan Arora, C. V. Jawahar, ECCV 2022.  
  [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1910_ECCV_2022_paper.php) [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136730656.pdf) [Code](https://sid2697.github.io/egoprocel)  
  `unsupervised` `clustering` `contrastive-learning` `I3D-features`
<a id="paper-2021-cvpr-temporally-weighted-hierarchical-clustering-unsupervised"></a>
- **Temporally-Weighted Hierarchical Clustering for Unsupervised Action Segmentation** — Saquib Sarfraz, Naila Murray, Vivek Sharma, et al., CVPR 2021.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Sarfraz_Temporally-Weighted_Hierarchical_Clustering_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Sarfraz_Temporally-Weighted_Hierarchical_Clustering_for_Unsupervised_Action_Segmentation_CVPR_2021_paper.pdf)  
  `unsupervised` `clustering` `I3D-features`
<a id="paper-2021-wacv-joint-visual-embedding-unsupervised-learning"></a>
- **Joint Visual-Temporal Embedding for Unsupervised Learning of Actions in Untrimmed Sequences** — Rosaura G. VidalMata, Walter J. Scheirer, Anna Kukleva, et al., WACV 2021.  
  [Paper](https://openaccess.thecvf.com/content/WACV2021/html/VidalMata_Joint_Visual-Temporal_Embedding_for_Unsupervised_Learning_of_Actions_in_Untrimmed_WACV_2021_paper.html) [PDF](https://openaccess.thecvf.com/content/WACV2021/papers/VidalMata_Joint_Visual-Temporal_Embedding_for_Unsupervised_Learning_of_Actions_in_Untrimmed_WACV_2021_paper.pdf)  
  `unsupervised` `unknown` `I3D-features` `Breakfast`
<a id="paper-2019-cvpr-unsupervised-learning-classes-continuous-embedding"></a>
- **Unsupervised Learning of Action Classes With Continuous Temporal Embedding** — Anna Kukleva, Hilde Kuehne, Fadime Sener, et al., CVPR 2019.  
  [Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.pdf)  
  `unsupervised` `unknown` `I3D-features` `Breakfast` `50Salads`
<a id="paper-2019-iccv-unsupervised-procedure-learning-joint-dynamic"></a>
- **Unsupervised Procedure Learning via Joint Dynamic Summarization** — Ehsan Elhamifar, Zwe Naing, ICCV 2019.  
  [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.html) [PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.pdf)  
  `unsupervised` `unknown` `video-language`
<a id="paper-2016-cvpr-unsupervised-learning-narrated-instruction-videos"></a>
- **Unsupervised Learning From Narrated Instruction Videos** — Jean-Baptiste Alayrac, Piotr Bojanowski, Nishant Agrawal, et al., CVPR 2016.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2016/html/Alayrac_Unsupervised_Learning_From_CVPR_2016_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2016/papers/Alayrac_Unsupervised_Learning_From_CVPR_2016_paper.pdf)  
  `unsupervised` `clustering` `I3D-features`
<a id="paper-2015-iccv-unsupervised-semantic-parsing-collections"></a>
- **Unsupervised Semantic Parsing of Video Collections** — Ozan Sener, Amir R. Zamir, Silvio Savarese, et al., ICCV 2015.  
  [Paper](https://openaccess.thecvf.com/content_iccv_2015/html/Sener_Unsupervised_Semantic_Parsing_ICCV_2015_paper.html) [PDF](https://openaccess.thecvf.com/content_iccv_2015/papers/Sener_Unsupervised_Semantic_Parsing_ICCV_2015_paper.pdf)  
  `unsupervised` `unknown` `I3D-features`

### Few-Shot and Zero-Shot

<a id="paper-2025-iccv-multi-modal-few-shot"></a>
- **Multi-Modal Few-Shot Temporal Action Segmentation** — Zijia Lu, Ehsan Elhamifar, ICCV 2025.  
  [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_Multi-Modal_Few-Shot_Temporal_Action_Segmentation_ICCV_2025_paper.html) [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_Multi-Modal_Few-Shot_Temporal_Action_Segmentation_ICCV_2025_paper.pdf) [Code](https://github.com/ZijiaLewisLu/ICCV2025-MMF-TAS)  
  `few-shot` `Transformer` `prototype-learning` `video-language`

### Training-Free

- _No verified paper in the current snapshot._

## Cross-index by technical route

### TCN and Multi-Stage Refinement

- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](#paper-2024-neurips-onlinetas-online-baseline)
- [A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation](#paper-2022-eccv-generalized-robust-framework-timestamp-supervision)
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
- [Multi-Modal Few-Shot Temporal Action Segmentation](#paper-2025-iccv-multi-modal-few-shot)
- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](#paper-2024-cvpr-fact-frame-cross-attention-modeling)
- [Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation](#paper-2022-eccv-unified-fully-timestamp-supervised-sequence)
- [ASFormer: Transformer for Action Segmentation](#paper-2021-bmvc-asformer-transformer)
- [SCT: Set Constrained Temporal Transformer for Set Supervised Action Segmentation](#paper-2020-cvpr-sct-set-constrained-transformer-set)

### Diffusion Models

- [Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning](#paper-2026-cvpr-polyphony-diffusion-based-dual-hand)
- [Diffusion Action Segmentation](#paper-2023-iccv-diffusion)

### Optimal Transport

- [CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation](#paper-2025-iccv-clot-closed-loop-optimal-transport)
- [Joint Self-Supervised Video Alignment and Action Segmentation](#paper-2025-iccv-joint-self-supervised-alignment)
- [Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation](#paper-2024-cvpr-temporally-consistent-unbalanced-optimal-transport)
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](#paper-2022-cvpr-unsupervised-by-joint-representation-learning)

### Clustering and Prototype Learning

- [CLOT: Closed Loop Optimal Transport for Unsupervised Action Segmentation](#paper-2025-iccv-clot-closed-loop-optimal-transport)
- [Timestamp-Supervised Action Segmentation in the Perspective of Clustering](#paper-2023-ijcai-timestamp-supervised-perspective-clustering)
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](#paper-2022-cvpr-fast-unsupervised-boundary-detection)
- [Iterative Contrast-Classify for Semi-Supervised Temporal Action Segmentation](#paper-2022-aaai-iterative-contrast-classify-semi-supervised)
- [My View Is the Best View: Procedure Learning from Egocentric Videos](#paper-2022-eccv-my-view-is-best-view)
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](#paper-2022-cvpr-unsupervised-by-joint-representation-learning)
- [Temporally-Weighted Hierarchical Clustering for Unsupervised Action Segmentation](#paper-2021-cvpr-temporally-weighted-hierarchical-clustering-unsupervised)
- [Unsupervised Learning From Narrated Instruction Videos](#paper-2016-cvpr-unsupervised-learning-narrated-instruction-videos)

### Boundary and Duration Modeling

- [LaDy: Lagrangian-Dynamic Informed Network for Skeleton-based Action Segmentation via Spatial-Temporal Modulation](#paper-2026-cvpr-lady-lagrangian-dynamic-informed-network)
- [Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation](#paper-2026-cvpr-spectral-scalpel-amplifying-adjacent-discrepancy)
- [Efficient and Effective Weakly-Supervised Action Segmentation via Action-Transition-Aware Boundary Alignment](#paper-2024-cvpr-efficient-effective-weakly-supervised-transition)
- [OTAS: Unsupervised Boundary Detection for Object-Centric Temporal Action Segmentation](#paper-2024-wacv-otas-unsupervised-boundary-detection-object)
- [Diffusion Action Segmentation](#paper-2023-iccv-diffusion)
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](#paper-2022-cvpr-fast-unsupervised-boundary-detection)
- [Leveraging Action Affinity and Continuity for Semi-Supervised Temporal Action Segmentation](#paper-2022-eccv-leveraging-affinity-continuity-semi-supervised)
- [Robust Action Segmentation from Timestamp Supervision](#paper-2022-bmvc-robust-timestamp-supervision)
- [Uncertainty-Aware Representation Learning for Action Segmentation](#paper-2022-ijcai-uncertainty-aware-representation-learning)
- [Boundary-Aware Cascade Networks for Temporal Action Segmentation](#paper-2020-eccv-boundary-aware-cascade-networks)
- [Improving Action Segmentation via Graph-Based Temporal Reasoning](#paper-2020-cvpr-improving-graph-based-reasoning)
- [Weakly-Supervised Action Segmentation With Iterative Soft Boundary Assignment](#paper-2018-cvpr-weakly-supervised-iterative-soft-boundary)

### Structured Decoding

- [Activity Grammars for Temporal Action Segmentation](#paper-2023-neurips-activity-grammars)
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos](#paper-2023-iccv-weakly-supervised-unseen-error-detection)
- [Don't Pour Cereal into Coffee: Differentiable Temporal Logic for Temporal Action Segmentation](#paper-2022-neurips-don-t-pour-cereal-into)
- [Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation](#paper-2022-eccv-unified-fully-timestamp-supervised-sequence)
- [Action Shuffle Alternating Learning for Unsupervised Action Segmentation](#paper-2021-cvpr-shuffle-alternating-learning-unsupervised)
- [Anchor-Constrained Viterbi for Set-Supervised Action Segmentation](#paper-2021-cvpr-anchor-constrained-viterbi-set-supervised)
- [Fast Weakly Supervised Action Segmentation Using Mutual Consistency](#paper-2020-eccv-fast-weakly-supervised-using-mutual)
- [Set-Constrained Viterbi for Set-Supervised Action Segmentation](#paper-2020-cvpr-set-constrained-viterbi-set-supervised)
- [NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning](#paper-2018-cvpr-neuralnetwork-viterbi-framework-weakly-supervised)
- [Connectionist Temporal Modeling for Weakly Supervised Action Labeling](#paper-2016-eccv-connectionist-modeling-weakly-supervised-labeling)

### Action Tokenization and VQ

- [Timestamp Query Transformer for Temporal Action Segmentation](#paper-2026-wacv-timestamp-query-transformer)
- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](#paper-2024-cvpr-fact-frame-cross-attention-modeling)

### Vision-Language and Open Vocabulary

- _No verified paper in the current snapshot._

### Online and Streaming

- [Hierarchical Action Learning for Weakly-Supervised Action Segmentation](#paper-2026-cvpr-hierarchical-learning-weakly-supervised)
- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](#paper-2024-neurips-onlinetas-online-baseline)
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](#paper-2024-cvpr-progress-aware-online-egocentric-procedural)

### Efficient and Long-Video Methods

- [Condensing Action Segmentation Datasets via Generative Network Inversion](#paper-2025-cvpr-condensing-datasets-generative-network-inversion)

## Cross-index by application

### General RGB Video

- _No verified paper in the current snapshot._

### Egocentric Video

- [FACT: Frame-Action Cross-Attention Temporal Modeling for Efficient Action Segmentation](#paper-2024-cvpr-fact-frame-cross-attention-modeling)
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](#paper-2024-cvpr-progress-aware-online-egocentric-procedural)
- [My View Is the Best View: Procedure Learning from Egocentric Videos](#paper-2022-eccv-my-view-is-best-view)
- [Improving Action Segmentation via Graph-Based Temporal Reasoning](#paper-2020-cvpr-improving-graph-based-reasoning)
- [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](#paper-2019-cvpr-ms-tcn-multi-stage-convolutional)

### Surgical Workflow

- [TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks](#paper-2020-miccai-tecno-surgical-phase-recognition-multi)

### Assembly and Manufacturing

- _No verified paper in the current snapshot._

### Robotics and Embodied Agents

- [Timestamp-Supervised Action Segmentation with Graph Convolutional Networks](#paper-2022-iros-timestamp-supervised-graph-convolutional-networks)

### Online and Streaming

- [OnlineTAS: An Online Baseline for Temporal Action Segmentation](#paper-2024-neurips-onlinetas-online-baseline)
- [Progress-Aware Online Action Segmentation for Egocentric Procedural Task Videos](#paper-2024-cvpr-progress-aware-online-egocentric-procedural)
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos](#paper-2023-iccv-weakly-supervised-unseen-error-detection)
- [Fast and Unsupervised Action Boundary Detection for Action Segmentation](#paper-2022-cvpr-fast-unsupervised-boundary-detection)
- [Unsupervised Action Segmentation by Joint Representation Learning and Online Clustering](#paper-2022-cvpr-unsupervised-by-joint-representation-learning)
- [Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos](#paper-2022-cvpr-weakly-supervised-online-multi-view)
- [NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning](#paper-2018-cvpr-neuralnetwork-viterbi-framework-weakly-supervised)

## Preprints / Pending Verification

<a id="paper-2026-preprint-text-augmented-optimal-transport-unsupervised"></a>
- **Text-Augmented Action Segmentation Optimal Transport for Unsupervised Surgical Phase Recognition** — Omar Mohamed, collaborators, Preprint 2026.  
  [PDF](https://arxiv.org/pdf/2602.24138) [arXiv](https://arxiv.org/abs/2602.24138)  
  `unsupervised` `optimal-transport` `I3D-features`
  _Status:_ arXiv 2602.24138; first submitted 2026-02-27; last update 2026-02-27; no formal proceedings placement verified by 2026-07-28.
<a id="paper-2022-preprint-semantic2graph-graph-based-multi-modal"></a>
- **Semantic2Graph: Graph-based Multi-modal Feature Fusion for Action Segmentation in Videos** — Junbin Zhang, Pei-Hsuan Tsai, Meng-Hsun Tsai, Preprint 2022.  
  [PDF](https://arxiv.org/pdf/2209.05653) [arXiv](https://arxiv.org/abs/2209.05653)  
  `fully-supervised` `graphical-model` `video-language`
  _Status:_ arXiv 2209.05653; first submitted 2022-09-12; last update 2023-03-15; no formal proceedings placement verified by 2026-07-28.
<a id="paper-2021-preprint-coarse-fine-multi-resolution-convolutional"></a>
- **Coarse to Fine Multi-Resolution Temporal Convolutional Network** — Dipika Singhania, Rahul Rahaman, Angela Yao, Preprint 2021.  
  [PDF](https://arxiv.org/pdf/2105.10859) [arXiv](https://arxiv.org/abs/2105.10859)  
  `fully-supervised` `TCN` `I3D-features`
  _Status:_ arXiv 2105.10859; first submitted 2021-05-23; last update 2021-05-23; no formal proceedings placement verified by 2026-07-28.

## Related-but-not-core

<a id="paper-2022-cvpr-assembly101-large-scale-multi-view"></a>
- **Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities** — Fadime Sener, Dibyadip Chatterjee, Daniel Shelepov, et al., CVPR 2022.  
  [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features` `Assembly101`
  _Why related:_ This dataset paper directly enabled or standardized temporal action/step segmentation evaluation, but its primary contribution is a benchmark rather than a core TAS method.
<a id="paper-2015-cvpr-human-hierarchical-supervoxel-consistency"></a>
- **Human Action Segmentation With Hierarchical Supervoxel Consistency** — Jiasen Lu, ran Xu, Jason J. Corso, CVPR 2015.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2015/html/Lu_Human_Action_Segmentation_2015_CVPR_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2015/papers/Lu_Human_Action_Segmentation_2015_CVPR_paper.pdf)  
  `fully-supervised` `unknown` `I3D-features`
  _Why related:_ This work segments the human/action region in video using supervoxels and actionness rather than assigning semantic action labels densely along the temporal axis.
<a id="paper-2014-cvpr-language-actions-recovering-syntax-semantics"></a>
- **The Language of Actions: Recovering the Syntax and Semantics of Goal-Directed Human Activities** — Hilde Kuehne, Ali Arslan, Thomas Serre, CVPR 2014.  
  [Paper](https://openaccess.thecvf.com/content_cvpr_2014/html/Kuehne_The_Language_of_2014_CVPR_paper.html) [PDF](https://openaccess.thecvf.com/content_cvpr_2014/papers/Kuehne_The_Language_of_2014_CVPR_paper.pdf)  
  `fully-supervised` `structured-decoding` `I3D-features`
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

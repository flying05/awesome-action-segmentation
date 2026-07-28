# 弱监督动作分割

## 任务定义与关键困难

监督信号可以是 transcript、动作集合或每段一个时间戳。核心困难不是生成任意伪标签，而是控制确认偏差、处理漏标短动作，并在跨视频动作顺序变化时保持一致。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [Hierarchical Action Learning for Weakly-Supervised Action Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Hierarchical_Action_Learning_for_Weakly-Supervised_Action_Segmentation_CVPR_2026_paper.html) — CVPR 2026; `Transformer, causal-model`
- [Timestamp Query Transformer for Temporal Action Segmentation](https://openaccess.thecvf.com/content/WACV2026/html/Wang_Timestamp_Query_Transformer_for_Temporal_Action_Segmentation_WACV_2026_paper.html) — WACV 2026; `Transformer, cross-attention, VQ-tokenization`
- [Efficient and Effective Weakly-Supervised Action Segmentation via Action-Transition-Aware Boundary Alignment](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Efficient_and_Effective_Weakly-Supervised_Action_Segmentation_via_Action-Transition-Aware_Boundary_Alignment_CVPR_2024_paper.html) — CVPR 2024; `boundary-modeling`
- [Random Walks for Temporal Action Segmentation With Timestamp Supervision](https://openaccess.thecvf.com/content/WACV2024/html/Hirsch_Random_Walks_for_Temporal_Action_Segmentation_With_Timestamp_Supervision_WACV_2024_paper.html) — WACV 2024; `unknown`
- [Timestamp-Supervised Action Segmentation in the Perspective of Clustering](https://www.ijcai.org/proceedings/2023/77) — IJCAI 2023; `clustering`
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos](https://openaccess.thecvf.com/content/ICCV2023/html/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.html) — ICCV 2023; `structured-decoding`
- [A Generalized & Robust Framework for Timestamp Supervision in Temporal Action Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4788_ECCV_2022_paper.php) — ECCV 2022; `TCN, uncertainty-modeling`
- [Hierarchical Modeling for Task Recognition and Action Segmentation in Weakly-Labeled Instructional Videos](https://openaccess.thecvf.com/content/WACV2022/html/Ghoddoosian_Hierarchical_Modeling_for_Task_Recognition_and_Action_Segmentation_in_Weakly-Labeled_WACV_2022_paper.html) — WACV 2022; `unknown`
- [Robust Action Segmentation from Timestamp Supervision](https://bmvc2022.mpi-inf.mpg.de/392/) — BMVC 2022; `TCN, boundary-modeling`
- [SSCAP: Self-Supervised Co-Occurrence Action Parsing for Unsupervised Temporal Action Segmentation](https://openaccess.thecvf.com/content/WACV2022/html/Wang_SSCAP_Self-Supervised_Co-Occurrence_Action_Parsing_for_Unsupervised_Temporal_Action_Segmentation_WACV_2022_paper.html) — WACV 2022; `unknown`
- [Semi-Weakly-Supervised Learning of Complex Actions From Instructional Task Videos](https://openaccess.thecvf.com/content/CVPR2022/html/Shen_Semi-Weakly-Supervised_Learning_of_Complex_Actions_From_Instructional_Task_Videos_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [Timestamp-Supervised Action Segmentation with Graph Convolutional Networks](https://doi.org/10.1109/IROS47612.2022.9981176) — IROS 2022; `graphical-model, TCN`
- [Unified Fully and Timestamp Supervised Temporal Action Segmentation via Sequence to Sequence Translation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3672_ECCV_2022_paper.php) — ECCV 2022; `Transformer, structured-decoding, duration-modeling`
- [Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos](https://openaccess.thecvf.com/content/CVPR2022/html/Ghoddoosian_Weakly-Supervised_Online_Action_Segmentation_in_Multi-View_Instructional_Videos_CVPR_2022_paper.html) — CVPR 2022; `unknown`
- [Learning Discriminative Prototypes With Dynamic Time Warping](https://openaccess.thecvf.com/content/CVPR2021/html/Chang_Learning_Discriminative_Prototypes_With_Dynamic_Time_Warping_CVPR_2021_paper.html) — CVPR 2021; `prototype-learning`
- [Temporal Action Segmentation From Timestamp Supervision](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.html) — CVPR 2021; `unknown`
- [Weakly-Supervised Action Segmentation and Alignment via Transcript-Aware Union-of-Subspaces Learning](https://openaccess.thecvf.com/content/ICCV2021/html/Lu_Weakly-Supervised_Action_Segmentation_and_Alignment_via_Transcript-Aware_Union-of-Subspaces_Learning_ICCV_2021_paper.html) — ICCV 2021; `duration-modeling`
- [Fast Weakly Supervised Action Segmentation Using Mutual Consistency](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1061_ECCV_2020_paper.php) — ECCV 2020; `TCN, structured-decoding`
- [SCT: Set Constrained Temporal Transformer for Set Supervised Action Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Fayyaz_SCT_Set_Constrained_Temporal_Transformer_for_Set_Supervised_Action_Segmentation_CVPR_2020_paper.html) — CVPR 2020; `Transformer`
- [Set-Constrained Viterbi for Set-Supervised Action Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Set-Constrained_Viterbi_for_Set-Supervised_Action_Segmentation_CVPR_2020_paper.html) — CVPR 2020; `structured-decoding`
- [D3TW: Discriminative Differentiable Dynamic Time Warping for Weakly Supervised Action Alignment and Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Chang_D3TW_Discriminative_Differentiable_Dynamic_Time_Warping_for_Weakly_Supervised_Action_CVPR_2019_paper.html) — CVPR 2019; `unknown`
- [Weakly Supervised Energy-Based Learning for Action Segmentation](https://openaccess.thecvf.com/content_ICCV_2019/html/Li_Weakly_Supervised_Energy-Based_Learning_for_Action_Segmentation_ICCV_2019_paper.html) — ICCV 2019; `unknown`
- [Action Sets: Weakly Supervised Action Segmentation Without Ordering Constraints](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_Action_Sets_Weakly_CVPR_2018_paper.html) — CVPR 2018; `unknown`
- [NeuralNetwork-Viterbi: A Framework for Weakly Supervised Video Learning](https://openaccess.thecvf.com/content_cvpr_2018/html/Richard_NeuralNetwork-Viterbi_A_Framework_CVPR_2018_paper.html) — CVPR 2018; `structured-decoding`
- [Unsupervised Learning and Segmentation of Complex Activities From Video](https://openaccess.thecvf.com/content_cvpr_2018/html/Sener_Unsupervised_Learning_and_CVPR_2018_paper.html) — CVPR 2018; `unknown`
- [Weakly-Supervised Action Segmentation With Iterative Soft Boundary Assignment](https://openaccess.thecvf.com/content_cvpr_2018/html/Ding_Weakly-Supervised_Action_Segmentation_CVPR_2018_paper.html) — CVPR 2018; `boundary-modeling, TCN`
- [Weakly Supervised Action Learning With RNN Based Fine-To-Coarse Modeling](https://openaccess.thecvf.com/content_cvpr_2017/html/Richard_Weakly_Supervised_Action_CVPR_2017_paper.html) — CVPR 2017; `unknown`
- [Connectionist Temporal Modeling for Weakly Supervised Action Labeling](https://www.ecva.net/papers/eccv_2016/papers_ECCV/html/Huang_Connectionist_Temporal_Modeling_ECCV_2016_paper.php) — ECCV 2016; `TCN, structured-decoding`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

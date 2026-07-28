# 动作时序分割的发展脉络、技术路线与开放问题

> 数据截点：2026-07-28。本综述只把可由正式 proceedings 或学会页面确认的会议论文当作正式工作；仅有 arXiv 的记录放在 README 的 Pending Verification 区。下文的“趋势”分为论文明确结论、跨论文归纳和待验证假设，不把后两者写成既定事实。

## 1. 任务定义

给定长度为 \(T\) 的视频或多模态时序

\[
x_{1:T}=(x_1,\ldots,x_T),
\]

TAS 预测

\[
y_{1:T},\quad y_t\in\{1,\ldots,C\},
\]

其中每个时间步都有动作类别。压缩相邻相同标签后，可写成片段序列
\(\mathcal S=\{(c_n,s_n,e_n)\}_{n=1}^{N}\)，类别为 \(c_n\)，起止时间为
\([s_n,e_n]\)，并满足相邻片段覆盖时间轴。任务同时要求“是什么”和“何时切换”，因此不同于给整段视频一个标签的 action recognition，也不同于只返回稀疏区间、允许大量背景未覆盖的 temporal action localization。

难点来自多个尺度：帧级外观在相邻动作间可能几乎相同；片段持续时间差几个数量级；同一过程的合法顺序可变；背景、重复动作和纠错动作破坏固定语法。模型若过度追随局部证据，会把一个动作切成多个碎片，即过分割；若平滑过强，又会抹掉短动作。开放类别还要求处理训练集中未出现的动作，在线系统则不能使用未来帧。

## 2. 发展阶段与继承关系

### 2.1 生成式时序模型与手工结构

早期工作把动作看作具有语法的状态序列，使用 HMM、动态规划、Viterbi 或显式 transcript 对齐。[The Language of Actions](https://openaccess.thecvf.com/content_cvpr_2014/html/Kuehne_The_Language_of_2014_CVPR_paper.html) 展示了 Breakfast 中目标导向活动的层次结构；[Connectionist Temporal Modeling](https://www.ecva.net/papers/eccv_2016/papers_ECCV/html/Huang_Connectionist_Temporal_Modeling_ECCV_2016_paper.php) 则把弱标注序列对齐与神经表示连接起来。这类方法能表达顺序和持续时间，却依赖较强结构假设，视觉表征与解码通常分离。

### 2.2 Encoder–Decoder TCN

[Temporal Convolutional Networks for Action Segmentation and Detection](https://openaccess.thecvf.com/content_cvpr_2017/html/Lea_Temporal_Convolutional_Networks_CVPR_2017_paper.html) 用一维时序卷积替代逐帧分类加独立平滑。膨胀卷积、池化与解码器扩大感受野，训练和推理均可并行。它解决了 RNN 长序列优化和手工解码的部分瓶颈，却仍可能在局部置信度波动处产生碎片。

### 2.3 Multi-Stage TCN 与迭代细化

[MS-TCN](https://openaccess.thecvf.com/content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html) 把第一阶段预测交给后续阶段反复细化，并用平滑损失压制高频标签跳变。这一范式成为多年基线。其继承关系很清楚：TCN 提供大感受野，多阶段网络把“结构化解码”近似成可学习的迭代修正。新问题是计算随阶段数增长，而且重复平滑可能牺牲短动作。

### 2.4 边界、持续时间与结构约束

[ASRF](https://openaccess.thecvf.com/content/WACV2021/html/Ishikawa_Alleviating_Over-Segmentation_Errors_by_Detecting_Action_Boundaries_WACV_2021_paper.html) 将动作分类与边界回归分支结合；[Boundary-Aware Cascade Networks](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/35_ECCV_2020_paper.php) 也显式利用边界信息。Viterbi、动态时间规整和 temporal logic 工作则把合法顺序、持续时间或逻辑关系放回解码器。它们针对过分割和不合法序列，但边界真值本身有标注歧义，过强先验也可能拒绝真实的顺序变化。

### 2.5 Transformer 与帧—动作双表示

[ASFormer](https://www.bmvc2021-virtualconference.com/conference/papers/paper_0578.html) 将局部先验嵌入高效 Transformer，避免对长视频使用无约束的全局二次注意力。[FACT](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_FACT_Frame-Action_Cross-Attention_Temporal_Modeling_for_Efficient_Action_Segmentation_CVPR_2024_paper.html) 不只在帧之间建模，还让少量动作 token 与帧表示交叉注意，从“每帧独立分类”转向帧—片段联合推理。收益是长程关系与类别级原型更直接；风险是动作 token 数、语义和边界仍受闭集标签约束。

### 2.6 扩散式动作分割

[Diffusion Action Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Diffusion_Action_Segmentation_ICCV_2023_paper.html) 把标签序列视为逐步去噪的生成对象。扩散过程能在全局上下文中修正不一致标签，而不只做一次判别预测；2026 年的层次扩散和双手分割工作继续探索结构条件。代价是多步采样、训练目标与最终 segmental 指标不完全一致，以及对短边界的噪声调度敏感。

### 2.7 弱、半监督与时间戳监督

transcript 给动作顺序而不给边界；set supervision 连顺序也省略；timestamp 通常每段只标一帧。它们都需要从不完整信号生成帧级训练目标。[Temporal Action Segmentation from Timestamp Supervision](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Temporal_Action_Segmentation_From_Timestamp_Supervision_CVPR_2021_paper.html) 依据稀疏时间戳构造伪分割；[A Generalized & Robust Framework](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4788_ECCV_2022_paper.php) 显式处理标签不确定性和漏标；[Iterative Contrast-Classify](https://ojs.aaai.org/index.php/AAAI/article/view/20124) 与 [Leveraging Action Affinity and Continuity](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3254_ECCV_2022_paper.php) 则研究少量密集标注加大量无标注视频。

低标注路线的共同瓶颈是确认偏差：初始模型更容易发现具有辨识度的中间帧，伪标签随后把这种偏好放大，导致边界偏移和短动作遗漏。若默认每段都有时间戳、每个视频包含同一动作集合或顺序近似固定，现实数据一旦违背假设，指标会陡降。

### 2.8 无监督表示、聚类与最优传输

无监督 TAS 不仅要聚类，还要让跨视频簇具有一致语义。[Unsupervised Learning and Segmentation of Complex Activities](https://openaccess.thecvf.com/content_cvpr_2018/html/Sener_Unsupervised_Learning_and_CVPR_2018_paper.html) 在判别表示与生成式顺序模型间迭代；后续连续时间嵌入、时序加权层次聚类和在线聚类加强 temporal consistency。

[ASOT](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Temporally_Consistent_Unbalanced_Optimal_Transport_for_Unsupervised_Action_Segmentation_CVPR_2024_paper.html) 用带结构先验的 Gromov–Wasserstein/非平衡最优传输联合匹配帧和动作原型。balanced OT 强迫各簇质量接近，容易扭曲真实动作时长；unbalanced OT 可吸收背景、缺失和不等时长。2025 年 [CLOT](https://openaccess.thecvf.com/content/ICCV2025/html/Bueno-Benito_CLOT_Closed_Loop_Optimal_Transport_for_Unsupervised_Action_Segmentation_ICCV_2025_paper.html) 通过帧、片段与原型间的闭环反馈继续细化。闭环也可能放大早期伪标签错误，因此不确定性和停止准则仍重要。

未知类别数是比标签置换更深的问题。Hungarian matching 只在评价时寻找预测簇与真值类的一一对应；高匹配分不证明簇具有可复用的人类语义，也无法表达一对多的层次动作。层次发现、非参数类别数估计和 discover-then-name 需要独立协议。

### 2.9 动作 token、开放词汇与具身扩展

骨架 motion words、VQ/tokenization 和动作原型把长序列压缩为离散或低秩状态，有利于层次程序建模和长视频效率。视觉语言模型进一步把原型与文本名称对齐。[Multi-Modal Few-Shot TAS](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_Multi-Modal_Few-Shot_Temporal_Action_Segmentation_ICCV_2025_paper.html) 明确区分新任务中的少样本/零样本适配。文本能提供类别语义，但对象共现或语言先验可能绕过真正的动作顺序理解。

## 3. 监督学习路线比较

TCN 的优势是线性复杂度和稳定局部归纳偏置；不足是远距离依赖需靠膨胀或多尺度间接传播。Transformer 直接建模关系，但长序列必须采用局部窗口、稀疏注意力或动作 token，否则二次复杂度不可接受。扩散模型提供全局生成式修正，却增加采样成本。boundary-aware 方法直接对症过分割，但边界损失依赖容忍窗口；duration-aware 和 structured decoding 能拒绝不合理片段，却可能把训练集流程固化。frame-action joint modeling 让片段表示反过来约束帧，如何确定动作 token 的数量和开放语义仍未解决。

因此公平比较不能只看网络名称。应固定输入特征、采样率、数据划分、背景处理和评价脚本，并说明端到端特征提取是否计入算力。大量论文使用预提取 I3D 特征；其结果不能直接等同于原始 RGB 端到端系统的总成本。

## 4. 低标注与无监督学习

- **Transcript supervision**：顺序已知，边界通过 CTC、DTW、Viterbi 或能量模型对齐；顺序变化是主要风险。
- **Timestamp supervision**：信号更局部、更强，但漏标一段会破坏“相邻时间戳之间仅含相应动作”的伪标签规则。
- **Set supervision**：允许未知顺序，搜索空间更大，容易靠数据集共现偏置取巧。
- **Semi-supervised**：要避免有标注视频与无标注视频来自不同难度分布。
- **Self-supervised / clustering**：时间邻近并不总等于语义一致，重复动作又违反单调顺序。
- **Optimal transport**：把软匹配、质量守恒和结构代价统一，但成本矩阵和正则项本身仍编码先验。
- **Prototype learning**：跨视频共享类别中心，短动作样本少时中心会被长动作主导。
- **Uncertainty modeling**：可降低错误伪标签权重，但不确定度校准需跨域验证。

## 5. 泛化与开放世界

“泛化”至少拆成 unseen task、unseen view 和 unseen action。新视角可能仍是同一类别闭集；新任务可能重组已知动作；新动作才要求类别扩展。multi-task 训练测试的是共享结构，open vocabulary 要把视觉片段映射到可扩展文本标签，zero-shot 则必须声明是否使用目标任务文本、示例或视频。discover-then-name 应分别报告无监督边界/聚类质量与名称对齐质量。test-time adaptation 还需防止视频内自训练把错误边界强化。

## 6. 特殊模态与场景

骨架 TAS 弱化背景外观，却受关节丢失、坐标系和相似微动作影响。手术工作流具有强 phase 顺序，但跨医院、术式和设备域偏移明显，临床容错也不同于厨房数据。第一视角视频有手—物交互和剧烈相机运动；装配/制造数据常有双手、多视角、返工和并行动作。RGB、音频、IMU、depth、gaze 的采样率和缺失机制不同，多模态融合必须报告传感器失效时的退化。在线/streaming 推理只能利用过去，需联合报告因果延迟、吞吐和状态缓存。

## 7. 数据集与指标

Breakfast、50Salads、GTEA 是传统三基准；Assembly101 增加规模、多视角和装配变化；COIN/CrossTask 面向大量程序任务；Cholec80 等用于手术 phase。具体规模、视角、标注粒度和来源见 [datasets_and_metrics.md](datasets_and_metrics.md)。

MoF/Frame Accuracy 统计正确帧比例，长动作主导时会掩盖短动作错误。Edit Score 先压缩连续标签再比较动作序列，强调顺序但弱化精确边界。F1@10/25/50 以不同时序 IoU 匹配片段，多余碎片成为假阳性，因而能揭示过分割。mIoU、boundary precision/recall 必须说明背景和容忍窗口。在线系统还需 latency；高效方法应报告 FLOPs、实际时间、显存和能耗。单独报告帧准确率不足以说明 TAS 已解决。

## 8. 当前开放问题

1. 长视频端到端计算与特征缓存成本。
2. 粗采样、平滑和扩散去噪中的短动作保持。
3. phase/step/原子动作之间的粒度歧义。
4. 未知动作数量与层次状态发现。
5. 伪标签确认偏差和跨视频语义对齐。
6. 新任务、新视角、新类别的分解式评估。
7. 动作发现后的语言命名与一对多语义。
8. 在线因果推理和允许延迟之间的权衡。
9. 多模态传感器选择、异步和缺失模态。
10. 动作 token 与世界模型中可干预状态的关系。
11. benchmark 饱和、预训练特征泄漏和场景偏置。
12. 大模型究竟理解程序顺序，还是利用对象/场景共现捷径。

## 9. 有证据支持的趋势与待验证假设

**论文明确提出的共同问题**：过分割、长程依赖、密集标注成本和跨视频变化反复出现在不同年代论文中；Frame Accuracy 之外的 Edit/F1 已成为主流协议。

**跨论文归纳**：技术重心从“扩大帧级感受野”转向“显式表示动作片段、边界、持续时间和原型”；监督信号从逐帧标签扩展到 transcript、timestamp、无标注视频和语言；2024–2026 的工作明显增加了最优传输、闭环细化、few-shot、骨架 token、在线和层次建模。

**仍需验证的假设**：动作 token 或视觉语言原型可能成为 TAS 与具身世界模型的接口，但现有基准尚不能证明它们形成了可组合、可干预且跨任务稳定的程序状态。更大预训练模型是否真正改善边界和顺序推理，也需要去除场景/对象捷径后的对照实验。


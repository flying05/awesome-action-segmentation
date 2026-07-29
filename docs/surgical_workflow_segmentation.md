# 手术工作流分割

## 任务定义与关键困难

手术 phase/step 序列具有强流程先验，但设备、术式与医院域偏移显著。通用 TAS 指标应与临床阶段 Jaccard、延迟和安全相关错误分开报告。

## 方法演化与比较

不同方法应在相同特征、划分、背景处理和评价脚本下比较。结构更复杂不必然意味着边界更好；要区分表征增益、解码先验和额外监督带来的收益。

## 常用数据集与指标

通用视频常用 Breakfast、50Salads、GTEA 与 Assembly101，并联合报告 Frame Accuracy、Edit、F1@10/25/50；特殊场景还应报告域内协议、延迟或临床指标。

## 代表论文索引

- [TeCNO: Surgical Phase Recognition with Multi-Stage Temporal Convolutional Networks](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_33) — MICCAI 2020; `multi-stage-TCN`

## 未解决问题

短动作保持、粒度歧义、跨视频语义对齐、伪标签确认偏差、未知类别数、新任务/新视角泛化以及真实计算成本仍需在更透明的协议下研究。

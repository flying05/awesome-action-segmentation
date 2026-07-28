# Contributing

感谢补充遗漏、纠正元数据或报告失效链接。请在提交前确认候选工作确实输出逐帧或连续片段动作标签，而不是仅做整段分类、时序定位或空间分割。

1. 在 `data/papers.yaml` 中添加或修改唯一记录。
2. 正式论文至少提供一个一手验证来源；无法核验的工作标为 `Preprint`。
3. 运行 `python scripts/generate_readme.py` 与 `python scripts/generate_docs.py`。
4. 运行 `python scripts/validate_repository.py` 和 `pytest`。

PDF 默认不进入 Git。请勿提交付费墙内容、访问令牌、Cookie 或来源不明的文件。


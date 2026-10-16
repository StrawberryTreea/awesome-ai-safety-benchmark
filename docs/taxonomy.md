# Taxonomy | 分类总览

[← 资源目录](../README.md) · **总览** · [设计依据](taxonomy-rationale.md) · [候选分类](taxonomy-proposal.md) · [验证计划](taxonomy-validation.md) · [研究附录](taxonomy-research-2026-10-16.md)

**按评测对象找资源，再看风险、机制与评测协议。** 分别记录“测谁、测什么、怎么测、依据什么判断”。

> **当前状态 · 2026-10-16**
>
> 目录使用下方的主轨、资源类型和主题导航。风险分类 `v0.1` 为 **12 个一级领域／39 个二级类型的待验证提案**，尚未用于全量目录重标。类别数与边界可随验证结果调整。

## 从这里开始

| 你想了解什么 | 阅读入口 |
| --- | --- |
| 为什么采用多轴？12／39 有什么依据？ | [设计依据与尚未解决的问题](taxonomy-rationale.md) |
| 每个候选标签怎么定义、怎么区分？ | [12 个领域与 39 个二级定义](taxonomy-proposal.md) |
| 参考了哪些标准、框架和研究？ | [来源矩阵](taxonomy-research-2026-10-16.md#source-matrix)与[完整来源注册](taxonomy-research-2026-10-16.md#references) |

<a id="tracks"></a>

## 1. 按评测对象浏览

本合集按评测对象划分主轨，再按主题导航。资源类型单独记录，不将数据集、评测框架、攻击方法和训练资源都称为独立 benchmark。

| 主轨 | 收录范围 | 典型边界 |
| --- | --- | --- |
| [🧩 LLM Safety](../README.md#llm_safety) · `llm_safety` | 回答、分类、价值判断、拒答、提示注入等模型／应用安全评测 | 多轮对话本身不足以证明包含 Agent 执行 |
| [🤖 Agent Safety](../README.md#agent_safety) · `agent_safety` | 多步行为、工具使用、环境交互、状态变化及安全约束 | 区分合成工具、LM 模拟、有状态沙箱与真实外部动作 |
| [⚖️ Guardrails & Judging](../README.md#safety_judging) · `safety_judging` | 内容、计划、下一动作和轨迹的安全判断 | 静态审查结果不能替代 Agent 的端到端安全表现 |
| [🧰 Related Resources](../README.md#related_resources) · `related_resources` | 训练数据、攻击方法、能力基线、诊断工具和套件子集 | 单列资源身份，统计时区分独立套件与组件 |

`topic` 是导航主题，不是互斥风险分类学。一个项目可能覆盖多个风险；首版选择一个主要主题，原始一级/二级维度保存在 `data/source_records.json`。后续多标签扩展应以官方来源为依据。

<a id="examples"></a>

## 2. 四个实例，读懂“测到了什么”

下表是协议阅读示例，并非本项目已完成的正式多轴标注。

| 资源 | 测量入口 | 选择与解释时要看什么 |
| --- | --- | --- |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | 动态 Agent 执行、间接提示注入 | 查看具体攻击目标、任务效用和安全指标；不能给全部任务统一贴隐私标签 |
| [R-Judge](https://github.com/Lordog/R-Judge) | 静态交互记录的风险判断 | 适合评估风险识别；需与 Agent 实际执行是否安全分别报告 |
| [WMDP](https://github.com/centerforaisafety/wmdp) | 生物、化学、网络危险知识的选择题 | 是危险知识代理测量；现实危险行动能力需要额外证据 |
| [XSTest](https://github.com/paul-rottger/xstest) | 对正常／不安全请求生成回答后判分 | 区分正常帮助、过拒和危险顺从，并报告各自分母 |

来源范围与版本见[四个资源实例](taxonomy-research-2026-10-16.md#examples)。

<details>
<summary><strong>资源类型与当前收录口径</strong></summary>

| 类型 | 含义 |
| --- | --- |
| `benchmark` | 有明确评测任务和评分目标的基准 |
| `benchmark_suite` | 组合多个任务或维度的评测套件 |
| `evaluation_dataset` | 可支持评测的数据集，不保证包含完整运行系统 |
| `training_dataset` | 主要用于训练、偏好优化或防护微调的数据 |
| `attack_method` | 攻击方法及配套实验资源 |
| `framework` | 评测、生成或防护框架，以及尚需细分的混合资源 |
| `suite_component` | 上级基准的数据子集或组成部分 |

资源类型是首批人工整理的导航判断。已对记录的网址执行页面可访问性检查，但页面响应不等于项目身份、元数据或评测协议已经核实。`listed` 表示按现有资料适合主题导航；`related` 表示补充资源；`needs_review` 表示身份、来源或范围仍需确认。这些状态均不表示已经下载或复现。

合集没有按旧本地平台的运行能力排除移动端、GUI 或具身 benchmark。旧表“暂缓”“剔除”“首轮”等建议保留在 `historical_screening`，不直接决定当前收录状态。

只统计目录条目数量，不加总不同 benchmark 的样本数。基础任务、攻击变体、行为轨迹、公开/私有测试集和训练样本不能直接相加比较。

</details>

---

**继续阅读：** [为什么这样设计 →](taxonomy-rationale.md) · [浏览候选领域 →](taxonomy-proposal.md)

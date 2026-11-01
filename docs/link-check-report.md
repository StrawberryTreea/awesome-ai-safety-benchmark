# 在线链接检查报告

检查日期：2026-11-01。

目录共有 440 个不同的原始网址，实际检查 437 个，跳过 3 个占位网址。重复出现在多个条目的网址只请求一次。

HEAD 优先；失败时用 GET 复核，仅读取最多 64 KiB 的网页文本。网络或服务器错误重试一次，完整结果保存在 [data/link_checks.json](../data/link_checks.json)。未下载数据集或论文文件。

HTTP 成功响应只说明当时的页面入口可达，不代表题名、项目身份或元数据已核实。401/403 等访问限制与 404/410 分开记录。许可证审查和 benchmark 可运行性不属于本次检查范围。

## 结果

| 状态 | 不同网址数 |
| --- | ---: |
| 可访问 | 406 |
| 正常跳转 | 27 |
| 404/410 | 2 |
| 访问受限 | 1 |
| 服务器错误 | 1 |
| 占位网址，跳过 | 3 |

最后一条检查时间：2026-11-01T10:00:00+08:00。

## 返回 404/410 的入口

已从 README、CSV 和 Excel 导航中省略这些入口，原始网址及检查证据仍保留在 JSON。条目已有可访问的替代入口，继续收录。

| 条目 | 原始网址 | HTTP | 保留的导航 |
| --- | --- | ---: | --- |
| Tensor Trust | `https://tensortrust.ai/paper%20(github.com/HumanCompatibleAI/tensor-trust)` | 404 | [项目](<https://tensortrust.ai/paper/>) · [代码](<https://github.com/HumanCompatibleAI/tensor-trust>) |
| AgentLAB | `https://tqj98.github.io/AgentLAB` | 404 | [论文](<https://arxiv.org/abs/2602.16901>) · [项目](<https://tanqiujiang.github.io/AgentLAB_main/>) · [代码](<https://github.com/TanqiuJiang/AgentLAB>) |

## 访问限制与暂时错误

| 条目 | 原始网址 | 状态 | HTTP |
| --- | --- | --- | ---: |
| CDIAL-BIAS, COLD, Cooridinate AI, CValues, Myopia_reward, One-box Tendency, Power-seeking, Self-awareness, SWSR, TOCP, TUMCC | [入口](<http://openeval.org.cn>) | 服务器错误 | 502 |
| OS-Harm | [入口](<https://huggingface.co/datasets/os-harm/os-harm>) | 访问受限 | 401 |

- OS-Harm 的 Hugging Face 入口返回 401，其 HTML 标题为 404。由于访问控制可能隐藏资源存在性，记录为受限，未确认缺失。其余项目或仓库入口保留，仓库归属问题继续列入身份核验。
- OpenEval 首页返回 502，影响 11 个历史记录。对其中已找到的项目已补充论文、仓库或数据页入口；原始聚合首页仍保留在 JSON 作为历史来源和访问证据。

## 正常跳转

导航使用最终地址，JSON 同时保留原始网址、HTTP 状态与跳转链。

| 条目 | 原始网址 | 最终地址 |
| --- | --- | --- |
| HONEST | `https://aclanthology.org/2021.naacl-main.191` | [最终入口](<https://aclanthology.org/2021.naacl-main.191/>) |
| API-Bank | `https://aclanthology.org/2023.emnlp-main.187` | [最终入口](<https://aclanthology.org/2023.emnlp-main.187/>) |
| AppWorld | `https://aclanthology.org/2024.acl-long.850` | [最终入口](<https://aclanthology.org/2024.acl-long.850/>) |
| InjecAgent | `https://aclanthology.org/2024.findings-acl.624` | [最终入口](<https://aclanthology.org/2024.findings-acl.624/>) |
| ToolSafety | `https://aclanthology.org/2025.emnlp-main.714` | [最终入口](<https://aclanthology.org/2025.emnlp-main.714/>) |
| SafeToolBench | `https://aclanthology.org/2025.findings-emnlp.958` | [最终入口](<https://aclanthology.org/2025.findings-emnlp.958/>) |
| SALAD-Bench | `https://adwardlee.github.io/salad_bench` | [最终入口](<https://adwardlee.github.io/salad_bench/>) |
| TUMCC | `https://doi.org/10.1016/j.ipm.2022.103033` | [最终入口](<https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X>) |
| MoralBench | `https://drive.google.com/drive/u/0/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7` | [最终入口](<https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7>) |
| DXPIA | `https://freyzo.github.io/deep-xpia` | [最终入口](<https://freyzo.github.io/deep-xpia/>) |
| Flames | `https://github.com/AIFlames/Flames` | [最终入口](<https://github.com/AI45Lab/Flames>) |
| MemoryGraft | `https://github.com/Jacobhhy/Agent-Memory-Poisoning` | [最终入口](<https://github.com/Jacobhhy/MemoryGraft>) |
| ToolSandbox | `https://github.com/apple/ToolSandbox` | [最终入口](<https://github.com/apple-aiml-research/ToolSandbox>) |
| SafePro | `https://github.com/eric-ai-lab/SafePro` | [最终入口](<https://github.com/UCSB-AI/SafePro>) |
| AgentDyn | `https://github.com/leolee99/AgentDyn` | [最终入口](<https://github.com/SaFo-Lab/AgentDyn>) |
| DailyDilemmas | `https://hf.co/datasets/kellycyy/daily_dilemmas` | [最终入口](<https://huggingface.co/datasets/kellycyy/daily_dilemmas>) |
| AttaQ | `https://huggingface.co/datasets/ibm/AttaQ` | [最终入口](<https://huggingface.co/datasets/ibm-research/AttaQ>) |
| ManyIH-Bench | `https://jhu-clsp.github.io/ManyIH` | [最终入口](<https://jhu-clsp.github.io/ManyIH/>) |
| OpenAI IH-Challenge | `https://openai.com/index/instruction-hierarchy-challenge` | [最终入口](<https://openai.com/index/instruction-hierarchy-challenge/>) |
| SafePro | `https://safeprobench.github.io/safepro` | [最终入口](<https://safeprobench.github.io/safepro/>) |
| WorkArena | `https://servicenow.github.io/WorkArena` | [最终入口](<https://servicenow.github.io/WorkArena/>) |
| AgentLAB | `https://tanqiujiang.github.io/AgentLAB_main` | [最终入口](<https://tanqiujiang.github.io/AgentLAB_main/>) |
| Tensor Trust | `https://tensortrust.ai/paper` | [最终入口](<https://tensortrust.ai/paper/>) |
| AgentHarm | `https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm` | [最终入口](<https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/>) |
| TOP-Bench | `https://www.semanticscholar.org/reader/f143043c62cbe142d99067328f2de1ec8b01f082` | [最终入口](<https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082>) |
| RiOSWorld | `https://yjyddq.github.io/RiOSWorld.github.io` | [最终入口](<https://yjyddq.github.io/RiOSWorld.github.io/>) |
| AgentHazard | `https://yunhao-feng.github.io/AgentHazard` | [最终入口](<https://yunhao-feng.github.io/AgentHazard/>) |

## 后续处理

继续补齐占位网址、仅有聚合首页的来源、名称与链接不一致的记录。页面访问检查与项目身份核验分别记录；论文入口可以独立收录。

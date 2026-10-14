# Awesome LLM & Agent Safety Benchmarks | LLM 与 Agent 安全 Benchmark

[English](README.md) · [简体中文](README.zh-CN.md)

| English | 中文 |
| --- | --- |
| A continuously updated collection of benchmarks, evaluation datasets and supporting resources for LLM and agent safety. | 持续收集 LLM 与 Agent 安全相关的 benchmark、评测数据和配套资源。 |
| The catalog covers model safety, agent safety and security, safety judging, guardrails, attack methods, training data and related research resources. | 内容覆盖模型安全、Agent 安全与安全防护、安全审查、护栏、攻击方法、训练数据及相关研究资源。 |
| Entries are organized by evaluation target and topic, with direct links to papers, code, datasets and project pages. | 条目按评测对象与主题导航，并提供论文、代码、数据和项目页面的直接链接。 |

## Catalog | 目录

## LLM Safety | LLM 安全

### Comprehensive safety | 综合安全

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AILuminate | Suite \| 基准套件 | 2025 | zh, en, other | [Code \| 代码](<https://github.com/mlcommons/ailuminate>) |
| Ch3Ef | Suite \| 基准套件 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2403.17830>) |
| CHiSafetyBench | Suite \| 基准套件 | 2024 | zh | [Code \| 代码](<https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench>) |
| DecodingTrust | Suite \| 基准套件 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/AI-Secure/DecodingTrust>) |
| Flames | Suite \| 基准套件 | 2023 | zh | [Code \| 代码](<https://github.com/AI45Lab/Flames>) |
| ForesightSafety Bench | Suite \| 基准套件 | 2026 | en | [Code \| 代码](<https://github.com/Beijing-AISI/ForesightSafety-Bench>) |
| JailBench | Suite \| 基准套件 | 2025 | zh | [Code \| 代码](<https://github.com/STAIR-BUPT/JailBench>) |
| LongSafety | Suite \| 基准套件 | 2025 | en | [Code \| 代码](<https://github.com/thu-coai/LongSafety>) |
| SafetyBench | Suite \| 基准套件 | 2024 | zh, en | [Code \| 代码](<https://github.com/thu-coai/SafetyBench>) |
| SALAD-Bench | Suite \| 基准套件 | 2024 | en | [Project \| 项目](<https://adwardlee.github.io/salad_bench/>) |
| SuperCLUE-Safety | Suite \| 基准套件 | 2024 | zh | [Project \| 项目](<https://www.cluebenchmarks.com/superclue_safety.html>) |
| TrustLLM | Suite \| 基准套件 | 2024 | en | [Code \| 代码](<https://github.com/HowieHwong/TrustLLM>) |
| U-SafeBench | Suite \| 基准套件 | 2025 | en | [Code \| 代码](<https://github.com/yeonjun-in/U-SafeBench>) |

### Harmful content and toxicity | 有害内容与毒性

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| BeaverTails | Eval data \| 评测数据 | 2023 | zh, en | [Project \| 项目](<https://sites.google.com/view/pku-beavertails>) |
| ChineseSafe | Eval data \| 评测数据 | 2024 | zh | [Data \| 数据](<https://huggingface.co/datasets/SUSTech/ChineseSafe>) |
| COLD | Eval data \| 评测数据 | 2022 | zh | [Code \| 代码](<https://github.com/thu-coai/COLDataset>) · [Paper \| 论文](<https://arxiv.org/abs/2201.06025>) |
| CREHate | Eval data \| 评测数据 | 2024 | en, other | [Code \| 代码](<https://github.com/nlee0212/CREHate>) |
| DICES | Eval data \| 评测数据 | 2023 | en | [Paper \| 论文](<https://arxiv.org/abs/2306.11247>) |
| Do-Not-Answer | Eval data \| 评测数据 | 2024 | zh, en | [Code \| 代码](<https://github.com/libr-ai/do-not-answer>) |
| DynaHate | Eval data \| 评测数据 | 2021 | en | [Code \| 代码](<https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset>) |
| hate_speech_offensive | Eval data \| 评测数据 | 2017 | en | [Data \| 数据](<https://huggingface.co/datasets/tdavidson/hate_speech_offensive>) |
| HateCheck | Eval data \| 评测数据 | 2021 | en | [Code \| 代码](<https://github.com/paul-rottger/hatecheck-data>) |
| Implicit Hate Corpus | Eval data \| 评测数据 | 2021 | en | [Code \| 代码](<https://github.com/SALT-NLP/implicit-hate>) |
| Measuring Hate Speech | Eval data \| 评测数据 | 2022 | en | [Data \| 数据](<https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech>) |
| moderation-api-release | Eval data \| 评测数据 | 2022 | en | [Code \| 代码](<https://github.com/openai/moderation-api-release/tree/main>) |
| Multilingual HateCheck (MHC) | Eval data \| 评测数据 | 2022 | other | [Code \| 代码](<https://github.com/rewire-online/multilingual-hatecheck>) |
| ProsocialDialog | Eval data \| 评测数据 | 2022 | en | [Code \| 代码](<https://github.com/skywalker023/prosocial-dialog>) |
| RealToxicityPrompts | Eval data \| 评测数据 | 2020 | en | [Code \| 代码](<https://github.com/allenai/real-toxicity-prompts>) |
| RTP-LX | Eval data \| 评测数据 | 2024 | zh, en, other | [Code \| 代码](<https://github.com/microsoft/RTP-LX>) |
| Safety-Prompts | Eval data \| 评测数据 | 2023 | zh | [Code \| 代码](<https://github.com/thu-coai/Safety-Prompts>) |
| SGHateCheck | Eval data \| 评测数据 | 2024 | other | [Code \| 代码](<https://github.com/Social-AI-Studio/SGHateCheck>) |
| SORRY-Bench | Eval data \| 评测数据 | 2024 | en | [Code \| 代码](<https://github.com/SORRY-Bench/sorry-bench>) |
| TOCP | Eval data \| 评测数据 | 2020 | zh | [Project \| 项目](<https://nlp.cse.ntou.edu.tw/resources/TOCP/>) · [Paper \| 论文](<https://aclanthology.org/2020.trac-1.2/>) |
| ToxiCN | Eval data \| 评测数据 | 2023 | zh | [Code \| 代码](<https://github.com/DUT-lujunyu/ToxiCN>) |
| ToxiCN MM | Eval data \| 评测数据 | 2024 | zh | [Code \| 代码](<https://github.com/DUT-lujunyu/ToxiCN_MM>) |
| ToxiGen | Eval data \| 评测数据 | 2022 | en | [Code \| 代码](<https://github.com/microsoft/ToxiGen>) |
| TUMCC | Eval data \| 评测数据 | 2020 | zh | [Code \| 代码](<https://github.com/m1-llie/TUMCC>) · [Paper \| 论文](<https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X>) |

### Jailbreaks and adversarial prompts | 越狱与对抗提示

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AdvBench | Benchmark \| 基准 | 2023 | en | [Paper \| 论文](<https://arxiv.org/abs/2307.15043>) · [Code \| 代码](<https://github.com/llm-attacks/llm-attacks>) |
| AttaQ | Benchmark \| 基准 | 2023 | en | [Data \| 数据](<https://huggingface.co/datasets/ibm-research/AttaQ>) |
| CoSafe | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/ErxinYu/CoSafe-Dataset>) |
| HarmBench | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2402.04249>) · [Code \| 代码](<https://github.com/centerforaisafety/HarmBench>) |
| In-the-Wild Jailbreak Prompts (jailbreak_llms) | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/verazuo/jailbreak_llms>) |
| JailbreakBench | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2404.01318>) · [Code \| 代码](<https://github.com/JailbreakBench/jailbreakbench>) |
| JailBreakV-28k | Benchmark \| 基准 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k>) |
| MaliciousInstruct | Benchmark \| 基准 | 2023 | en | [Code \| 代码](<https://github.com/Princeton-SysML/Jailbreak_LLM>) |
| MHJ (Multi-Turn Human Jailbreaks) | Benchmark \| 基准 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/ScaleAI/mhj>) |
| MultiBreak | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2605.01687>) |
| MultiJail | Benchmark \| 基准 | 2024 | en, other | [Data \| 数据](<https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail>) |
| PAP (Persuasive Adversarial Prompts) | Benchmark \| 基准 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/CHATS-Lab/Persuasive-Jailbreaker-Data>) |
| SafeDialBench | Benchmark \| 基准 | 2025 | zh, en | [Code \| 代码](<https://github.com/drivetosouth/SafeDialBench-Dataset>) |

### Prompt injection and instruction boundaries | 提示注入与指令边界

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| BIPIA | Benchmark \| 基准 | KDD 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2312.14197>) · [Code \| 代码](<https://github.com/microsoft/BIPIA>) |
| HackAPrompt | Benchmark \| 基准 | 2023 | 英文(含少量多语言混淆) | [Data \| 数据](<https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset>) |
| IHEval | Benchmark \| 基准 | 2025 | en | [Code \| 代码](<https://github.com/ytyz1307zzh/IHEval>) |
| Open-Prompt-Injection | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/liu00222/Open-Prompt-Injection>) |
| OpenAI IH-Challenge | Benchmark \| 基准 | 2025 | en | [Project \| 项目](<https://openai.com/index/instruction-hierarchy-challenge/>) |
| PromptInject | Benchmark \| 基准 | 2022 | en | [Code \| 代码](<https://github.com/agencyenterprise/PromptInject>) |
| Tensor Trust | Benchmark \| 基准 | 2023(arXiv)/2024(ICLR) | en | [Project \| 项目](<https://tensortrust.ai/paper/>) · [Code \| 代码](<https://github.com/HumanCompatibleAI/tensor-trust>) |

### Bias and fairness | 偏见与公平

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| BBQ | Eval data \| 评测数据 | 2021 | en | [Code \| 代码](<https://github.com/nyu-mll/BBQ>) |
| BOLD | Eval data \| 评测数据 | 2021 | en | [Code \| 代码](<https://github.com/amazon-science/bold>) |
| CDIAL-BIAS | Eval data \| 评测数据 | 2022 | zh | [Code \| 代码](<https://github.com/para-zhou/CDial-Bias>) · [Paper \| 论文](<https://arxiv.org/abs/2202.08011>) |
| HolisticBias | Eval data \| 评测数据 | 2022 | en | [Paper \| 论文](<https://arxiv.org/abs/2205.09209>) |
| HONEST | Eval data \| 评测数据 | 2021 | other | [Paper \| 论文](<https://aclanthology.org/2021.naacl-main.191/>) |
| Social Bias Frames (SBIC) | Eval data \| 评测数据 | 2020 | en | [Data \| 数据](<https://huggingface.co/datasets/allenai/social_bias_frames>) |
| SocialStigmaQA | Eval data \| 评测数据 | 2023 | en | [Data \| 数据](<https://huggingface.co/datasets/ibm-research/SocialStigmaQA>) |
| StereoSet | Eval data \| 评测数据 | 2020 | en | [Code \| 代码](<https://github.com/moinnadeem/StereoSet>) |
| SWSR | Eval data \| 评测数据 | 2021 | zh | [Code \| 代码](<https://github.com/aggiejiang/SWSR>) · [Paper \| 论文](<https://arxiv.org/abs/2108.03070>) |

### Values, ethics and cultural norms | 价值观、伦理与文化规范

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| CMoralEval | Benchmark \| 基准 | 2024 | zh | [Code \| 代码](<https://github.com/tjunlp-lab/CMoralEval>) |
| CValues | Benchmark \| 基准 | — | zh | [Code \| 代码](<https://github.com/X-PLUG/CValues>) · [Paper \| 论文](<https://arxiv.org/abs/2307.09705>) · [Data \| 数据](<https://modelscope.cn/datasets/damo/CValues-Comparison/summary>) |
| DailyDilemmas | Benchmark \| 基准 | 2024 | en | [Project \| 项目](<https://huggingface.co/datasets/kellycyy/daily_dilemmas>) |
| ETHICS | Benchmark \| 基准 | 2021 | en | [Code \| 代码](<https://github.com/hendrycks/ethics>) |
| GlobalOpinionQA | Benchmark \| 基准 | 2023 | en, other | [Data \| 数据](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>) |
| KorNAT | Benchmark \| 基准 | 2024 | other | [Data \| 数据](<https://huggingface.co/datasets/jiyounglee0523/KorNAT>) |
| MedEthicEval | Benchmark \| 基准 | 2025 | zh | [Code \| 代码](<https://github.com/X-LANCE/MedEthicEval>) |
| Moral Stories | Benchmark \| 基准 | 2021 | en | [Code \| 代码](<https://github.com/demelin/moral_stories>) |
| MoralBench | Benchmark \| 基准 | 2024 | en | [Project \| 项目](<https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7>) |
| NormAd | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/Akhila-Yerukola/NormAd>) |
| OpinionQA | Benchmark \| 基准 | 2023 | en | [Code \| 代码](<https://github.com/tatsu-lab/opinions_qa>) |
| ValueBench | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/ValueByte-AI/ValueBench>) |
| WorldValuesBench | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/Demon702/WorldValuesBench>) |

### Privacy | 隐私

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| ASQ-PHI | Benchmark \| 基准 | 2025 | en | [Code \| 代码](<https://github.com/JamesWeatherhead/asq-phi>) |
| ConfAIde | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/skywalker023/confaide/tree/main>) |
| LM_PersonalInfoLeak | Benchmark \| 基准 | 2022 | en | [Code \| 代码](<https://github.com/jeffhj/LM_PersonalInfoLeak>) |
| MultiPriv | Benchmark \| 基准 | 2025 | zh, en | [Code \| 代码](<https://github.com/CyberChangAn/MultiPriv-PII>) |
| PrivacyBench | Benchmark \| 基准 | 2025 | en | [Code \| 代码](<https://github.com/sri-ja/privacy-bench>) · [Paper \| 论文](<https://arxiv.org/abs/2512.24848>) |
| PUPA | Benchmark \| 基准 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/Columbia-NLP/PUPA>) |

### Over-refusal | 过度拒答

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| FalseReject | Benchmark \| 基准 | 2025 | en | [Data \| 数据](<https://huggingface.co/datasets/AmazonScience/FalseReject>) |
| OR-Bench | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/justincui03/or-bench>) |
| PHTest | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/umd-huang-lab/FalseRefusal>) |
| RASS / MoRBench | Benchmark \| 基准 | 2025 | other | [Code \| 代码](<https://github.com/Master-PLC/RASS>) |
| XSTest | Benchmark \| 基准 | 2023 | en | [Code \| 代码](<https://github.com/paul-rottger/xstest>) |

### Autonomy and alignment | 自主性与对齐

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| Anthropic Evals | Suite \| 基准套件 | 2022 | en | [Code \| 代码](<https://github.com/anthropics/evals>) |
| CRiskEval | Suite \| 基准套件 | 2025 | zh | [Code \| 代码](<https://github.com/tjunlp-lab/CRiskEval>) |
| Myopia_reward | Suite \| 基准套件 | 2022 | zh | [Code \| 代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper \| 论文](<https://arxiv.org/abs/2212.09251>) |
| One-box Tendency | Suite \| 基准套件 | 2022 | zh | [Code \| 代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper \| 论文](<https://arxiv.org/abs/2212.09251>) |
| Power-seeking | Suite \| 基准套件 | 2022 | zh | [Code \| 代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper \| 论文](<https://arxiv.org/abs/2212.09251>) |
| Self-awareness | Suite \| 基准套件 | 2022 | zh | [Code \| 代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper \| 论文](<https://arxiv.org/abs/2212.09251>) |

### Domain risks | 领域风险

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| CyberSecEval 1/2/3 (Purple Llama) | Benchmark \| 基准 | 2023 | en | [Code \| 代码](<https://github.com/meta-llama/PurpleLlama>) |
| FinSafetyBench | Benchmark \| 基准 | 2026 | zh, en | [Code \| 代码](<https://github.com/sustech-nlp/FinSafetyBench>) |
| MedSafetyBench | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/AI4LIFE-GROUP/med-safety-bench>) |
| SafeSci | Benchmark \| 基准 | 2026 | en | [Code \| 代码](<https://github.com/yangyangyang127/SafeSci>) |
| SciSafeEval | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2410.03769>) |
| WMDP | Benchmark \| 基准 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/cais/wmdp>) |

## Agent Safety & Security | Agent 安全

### Prompt injection and instruction boundaries | 提示注入与指令边界

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AgentDojo | Benchmark \| 基准 | NeurIPS 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2406.13352>) · [Code \| 代码](<https://github.com/ethz-spylab/agentdojo>) |
| AgentDyn | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2602.03117>) · [Code \| 代码](<https://github.com/SaFo-Lab/AgentDyn>) |
| AgentLAB | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2602.16901>) · [Project \| 项目](<https://tanqiujiang.github.io/AgentLAB_main/>) · [Code \| 代码](<https://github.com/TanqiuJiang/AgentLAB>) |
| InjecAgent | Benchmark \| 基准 | 2024（ACL Findings） | en | [Paper \| 论文](<https://aclanthology.org/2024.findings-acl.624/>) · [Code \| 代码](<https://github.com/uiuc-kang-lab/InjecAgent>) |

### General agent safety and misuse | 综合 Agent 安全与滥用

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| Agent Security Bench (ASB) | Benchmark \| 基准 | 2024/2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2410.02644>) · [Code \| 代码](<https://github.com/agiresearch/ASB>) |
| Agent-SafetyBench | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2412.14470>) · [Code \| 代码](<https://github.com/thu-coai/Agent-SafetyBench>) · [Data \| 数据](<https://huggingface.co/datasets/thu-coai/Agent-SafetyBench>) · [Project \| 项目](<https://www.semanticscholar.org/reader/7d11400eeb317ebee278f49e108226a4f8555dda>) |
| AgentHarm | Benchmark \| 基准 | ICLR 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2410.09024>) · [Data \| 数据](<https://huggingface.co/datasets/ai-safety-institute/AgentHarm>) · [Project \| 项目](<https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/>) |
| Echoes of Human Malice | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2510.14207>) |
| HAICosystem | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/XuhuiZhou/HAICosystem>) |
| OpenAgentSafety | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2507.06134>) · [Code \| 代码](<https://github.com/Open-Agent-Safety/OpenAgentSafety>) · [Data \| 数据](<https://huggingface.co/datasets/sani903/openagentsafety>) |
| SafePro | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2601.06663>) · [Code \| 代码](<https://github.com/UCSB-AI/SafePro>) · [Project \| 项目](<https://safeprobench.github.io/safepro/>) · [Data \| 数据](<https://huggingface.co/datasets/kzhou35/SafePro>) |

### Tool, API and MCP safety | 工具、API 与 MCP 安全

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| MCIP | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2505.14590>) |
| MCP Security Bench (MSB) | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2510.15994>) · [Code \| 代码](<https://github.com/dongsenzhang/MSB>) |
| MCP-TDP | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2605.24069>) |
| MCPTox | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2508.14925>) · [Code \| 代码](<https://anonymous.4open.science/r/AAAI26-7C02>) |
| RAS-EVAL | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2506.15253>) · [Code \| 代码](<https://github.com/lanzer-tree/RAS-Eval>) |
| ToolEmu | Benchmark \| 基准 | 2023/ICLR 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2309.15817>) · [Code \| 代码](<https://github.com/ryoungj/ToolEmu>) |
| ToolSword | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/Junjie-Ye/ToolSword>) |

### Privacy and memory | 隐私与记忆

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AgentDAM | Benchmark \| 基准 | 2025 | en | [Code \| 代码](<https://github.com/facebookresearch/ai-agent-privacy>) |
| AgentLeak | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2602.11510>) · [Code \| 代码](<https://github.com/Privatris/AgentLeak>) · [Data \| 数据](<https://huggingface.co/datasets/humain2/AgentLeak>) |
| PrivacyLens | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/SALT-NLP/PrivacyLens>) |

### Web, computer and mobile agents | 网页、桌面与移动 Agent

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AgentHazard | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2604.02947>) · [Code \| 代码](<https://github.com/Yunhao-Feng/AgentHazard>) · [Project \| 项目](<https://yunhao-feng.github.io/AgentHazard/>) |
| CUAHarm | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2508.00935>) · [Code \| 代码](<https://github.com/db-ol/CUAHarm>) · [Data \| 数据](<https://huggingface.co/datasets/CUAHarm/CUAHarm>) |
| MobileSafetyBench | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2410.17520>) · [Code \| 代码](<https://github.com/jylee425/mobilesafetybench>) · [Project \| 项目](<https://mobilesafetybench.github.io>) |
| RiOSWorld | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2506.00618>) · [Project \| 项目](<https://yjyddq.github.io/RiOSWorld.github.io/>) |
| SABER | Benchmark \| 基准 | 2026 | 中英混合, 英语为主 | [Paper \| 论文](<https://arxiv.org/abs/2606.01317>) · [Code \| 代码](<https://github.com/sssr-lab/saber>) |
| SafeArena | Benchmark \| 基准 | 2025 | en | [Code \| 代码](<https://github.com/McGill-NLP/safearena>) |
| ST-WebAgentBench | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2410.06703>) · [Project \| 项目](<https://sites.google.com/view/st-webagentbench/home>) · [Data \| 数据](<https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench>) · [Code \| 代码](<https://github.com/segev-shlomov/ST-WebAgentBench>) |
| WASP | Benchmark \| 基准 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2504.18575>) · [Code \| 代码](<https://github.com/facebookresearch/wasp>) |

### Embodied safety | 具身安全

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| SafeAgentBench | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2412.13178>) · [Project \| 项目](<https://safeagentbench.github.io>) · [Code \| 代码](<https://github.com/shengyin1224/SafeAgentBench>) |

## Safety Judging & Guardrails | 安全审查与护栏

### Agent trajectories and action safety | Agent 轨迹与动作安全

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| ATBench | Eval data \| 评测数据 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2604.02022>) · [Code \| 代码](<https://github.com/LiYu0524/ATbench>) · [Data \| 数据](<https://huggingface.co/datasets/AI45Research/ATBench>) |
| PhoneSafety | Eval data \| 评测数据 | 2025 | 中文为主 | [Paper \| 论文](<https://arxiv.org/abs/2605.07630>) · [Code \| 代码](<https://github.com/tangzhy/PhoneSafety>) · [Data \| 数据](<https://huggingface.co/datasets/phonesafety-anon/PhoneSafety_Data>) |
| R-Judge | Eval data \| 评测数据 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2401.10019>) · [Code \| 代码](<https://github.com/Lordog/R-Judge>) |
| SafeToolBench | Eval data \| 评测数据 | 2025 | en | [Paper \| 论文](<https://aclanthology.org/2025.findings-emnlp.958.pdf>) · [Code \| 代码](<https://github.com/BITHLP/SafeToolBench>) |
| SleightBench | Eval data \| 评测数据 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2605.16626>) · [Code \| 代码](<https://github.com/safety-research/sleight-bench>) |
| ToolSafe / TS-Bench | Eval data \| 评测数据 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2601.10156>) · [Code \| 代码](<https://github.com/MurrayTom/ToolSafe>) |
| TOP-Bench | Eval data \| 评测数据 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2512.16310>) · [Code \| 代码](<https://github.com/1Ponder/TOP-R>) · [Project \| 项目](<https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082>) |
| TraceSafe-Bench | Eval data \| 评测数据 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2604.07223>) · [Code \| 代码](<https://github.com/cycraft-corp/TraceSafe>) · [Data \| 数据](<https://huggingface.co/datasets/CyCraftAI/TraceSafe>) |
| WebGuard | Eval data \| 评测数据 | 2025 | en | [Code \| 代码](<https://github.com/OSU-NLP-Group/WebGuard>) |

### Content guardrail evaluation | 内容护栏评测

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| GuardBench | Suite \| 基准套件 | 2024 | en | [Code \| 代码](<https://github.com/AmenRa/guardbench>) |
| WildGuard (WildGuardMix/WildGuardTest) | Suite \| 基准套件 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/allenai/wildguardmix>) |

## Related Resources | 相关资源

### Training datasets | 训练数据

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| Aegis 1.0 (Nemotron Content Safety Dataset V1) | Train data \| 训练数据 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0>) |
| GuardReasoner (GuardReasonerTrain) | Train data \| 训练数据 | 2025 | en | [Data \| 数据](<https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain>) |
| HarmfulQA (RED-INSTRUCT) | Train data \| 训练数据 | 2023 | en | [Data \| 数据](<https://huggingface.co/datasets/TrustAIRLab/HarmfulQA>) |
| HH-RLHF（含Red Team Attempts） | Train data \| 训练数据 | 2022 | en | [Code \| 代码](<https://github.com/anthropics/hh-rlhf>) |
| Nemotron Content Safety Dataset V2 | Train data \| 训练数据 | 2025 | en | [Data \| 数据](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0>) |
| NVIDIA Nemotron Agentic IPI | Train data \| 训练数据 | 2026 | en | [Data \| 数据](<https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1>) |
| PKU-SafeRLHF (10K/30K) | Train data \| 训练数据 | 2023 | en | [Data \| 数据](<https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K>) |
| SafeMTData（Derail Yourself/ActorAttack配套） | Train data \| 训练数据 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/SafeMTData/SafeMTData>) |
| ToolSafety | Train data \| 训练数据 | EMNLP 2025 | en | [Paper \| 论文](<https://aclanthology.org/2025.emnlp-main.714.pdf>) · [Data \| 数据](<https://huggingface.co/datasets/jinjinyien/ToolSafety>) |
| X-Teaming Evolutionary M2S | Train data \| 训练数据 | 2025 | en | [Data \| 数据](<https://huggingface.co/datasets/hyunjun1121/X-Teaming_Evolutionary_M2S>) |
| XGuard-Train-Open-200K | Train data \| 训练数据 | 2026 | other | [Data \| 数据](<https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K>) |
| XGuard-Train（X-Teaming配套） | Train data \| 训练数据 | 2025 | en | [Data \| 数据](<https://huggingface.co/datasets/marslabucla/XGuard-Train>) |

### Attack methods | 攻击方法

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AgentPoison | Method \| 方法 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2407.12784>) · [Code \| 代码](<https://github.com/AI-secure/AgentPoison>) · [Project \| 项目](<https://billchan226.github.io/AgentPoison.html>) |
| ArtPrompt | Method \| 方法 | 2024 | en | [Code \| 代码](<https://github.com/uw-nsl/ArtPrompt>) |
| AutoDAN | Method \| 方法 | 2024 | en | [Code \| 代码](<https://github.com/SheltonLiu-N/AutoDAN>) |
| Automating Deception（FITD多轮越狱） | Method \| 方法 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2511.19517>) |
| CipherChat | Method \| 方法 | 2024 | zh, en | [Code \| 代码](<https://github.com/RobustNLP/CipherChat>) |
| CodeChameleon | Method \| 方法 | 2024 | en | [Code \| 代码](<https://github.com/huizhang-L/CodeChameleon>) |
| Crescendo | Method \| 方法 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2404.01833>) |
| Curiosity-driven Red Teaming | Method \| 方法 | 2024 | en | [Code \| 代码](<https://github.com/Improbable-AI/curiosity_redteam>) |
| DeepInception | Method \| 方法 | 2023 | en | [Code \| 代码](<https://github.com/tmlr-group/DeepInception>) |
| GPTFuzzer | Method \| 方法 | 2023 | en | [Code \| 代码](<https://github.com/hubertyoo/GPTFuzz>) |
| Latent Jailbreak | Method \| 方法 | 2023 | 英文+中文 | [Code \| 代码](<https://github.com/qiuhuachuan/latent-jailbreak>) |
| MART | Method \| 方法 | 2023 | en | [Paper \| 论文](<https://arxiv.org/abs/2311.07689>) |
| MemoryGraft | Method \| 方法 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2512.16962>) · [Code \| 代码](<https://github.com/Jacobhhy/MemoryGraft>) · [Project \| 项目](<https://www.semanticscholar.org/reader/b1d80b2eda7e175e235185bdc7df4e8233f36ef4>) |
| PsychJail | Method \| 方法 | 2026 | en | [Code \| 代码](<https://github.com/FengZeyugit/PsychJail>) |
| ReNeLLM | Method \| 方法 | 2024 | en | [Code \| 代码](<https://github.com/NJUNLP/ReNeLLM>) |

### Frameworks and mixed resources | 框架及混合资源

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| AgentDefense-Bench | Framework \| 框架 | 2025 | en | [Code \| 代码](<https://github.com/arunsanna/AgentDefense-Bench>) |
| CC-BOS | Framework \| 框架 | 2026 | zh | [Code \| 代码](<https://github.com/xaoLiu1222/cc-bos>) |
| LiveSecBench | Framework \| 框架 | 2026 | zh | [Code \| 代码](<https://github.com/ydli-ai/LiveSecBench>) |
| ORFuzz | Framework \| 框架 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2508.11222>) |
| ShieldLM | Framework \| 框架 | 2024 | zh, en | [Code \| 代码](<https://github.com/thu-coai/ShieldLM>) |
| TrustAgent | Framework \| 框架 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2402.01586>) |
| WILDTEAMING / WildJailbreak | Framework \| 框架 | 2024 | en | [Code \| 代码](<https://github.com/allenai/wildteaming>) |

### Attack challenges and data | 攻击挑战与数据

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| LLMail-Inject | Eval data \| 评测数据 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2506.09956>) · [Code \| 代码](<https://github.com/microsoft/llmail-inject-challenge>) |

### Capability baselines and environments | 能力基线与环境

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| Agent-Diff | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2602.11224>) · [Code \| 代码](<https://github.com/agent-diff-bench/agent-diff>) · [Project \| 项目](<https://www.agentdiff.dev>) · [Data \| 数据](<https://huggingface.co/datasets/hubertmarek/agent-diff-bench>) |
| API-Bank | Benchmark \| 基准 | EMNLP 2023 | en | [Paper \| 论文](<https://arxiv.org/abs/2304.08244>) |
| AppWorld | Benchmark \| 基准 | ACL 2024 | en | [Paper \| 论文](<https://aclanthology.org/2024.acl-long.850/>) · [Code \| 代码](<https://github.com/StonyBrookNLP/appworld>) · [Project \| 项目](<https://appworld.dev>) |
| BFCL | Benchmark \| 基准 | 2024/2025，持续更新至 V4 | 英语为主, 多语言函数调用场景 | [Paper \| 论文](<https://proceedings.mlr.press/v267/patil25a.html>) · [Project \| 项目](<https://gorilla.cs.berkeley.edu/leaderboard.html>) · [Data \| 数据](<https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard>) |
| SkillsBench | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2602.12670>) · [Project \| 项目](<https://www.skillsbench.ai>) · [Code \| 代码](<https://github.com/benchflow-ai/skillsbench>) |
| tau-bench | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2406.12045>) · [Code \| 代码](<https://github.com/sierra-research/tau-bench>) · [Project \| 项目](<https://www.semanticscholar.org/reader/70aa016c1f68fd5c0261f26ad20017b8307650af>) |
| TheAgentCompany | Benchmark \| 基准 | 2024/2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2412.14161>) · [Code \| 代码](<https://github.com/TheAgentCompany/TheAgentCompany>) · [Project \| 项目](<https://the-agent-company.com>) |
| TOOLATHLON | Benchmark \| 基准 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2510.25726>) · [Code \| 代码](<https://github.com/hkust-nlp/Toolathlon>) |
| ToolSandbox | Benchmark \| 基准 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2408.04682>) · [Code \| 代码](<https://github.com/apple-aiml-research/ToolSandbox>) · [Project \| 项目](<https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark>) |
| WebArena | Benchmark \| 基准 | ICLR 2024 / NeurIPS 2024 Oral 相关项目口径 | en | [Paper \| 论文](<https://arxiv.org/abs/2307.13854>) · [Code \| 代码](<https://github.com/web-arena-x/webarena>) · [Project \| 项目](<https://webarena.dev>) |
| WorkArena | Benchmark \| 基准 | ICML 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2403.07718>) · [Code \| 代码](<https://github.com/ServiceNow/workarena>) · [Project \| 项目](<https://servicenow.github.io/WorkArena/>) |

### Factuality and general trace diagnostics | 事实性与通用轨迹诊断

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| HaluEval | Eval data \| 评测数据 | 2023 | en | [Paper \| 论文](<https://arxiv.org/abs/2305.11747>) · [Code \| 代码](<https://github.com/RUCAIBox/HaluEval>) |
| RAGTruth | Eval data \| 评测数据 | 2023 | en | [Paper \| 论文](<https://arxiv.org/abs/2401.00396>) |
| SimpleQA | Eval data \| 评测数据 | 2024 | en | [Paper \| 论文](<https://arxiv.org/abs/2411.04368>) · [Code \| 代码](<https://github.com/openai/simple-evals>) |
| TraceElephant | Eval data \| 评测数据 | 2026 | en | [Paper \| 论文](<https://arxiv.org/abs/2604.22708>) · [Code \| 代码](<https://github.com/TraceElephant/TraceElephant>) · [Data \| 数据](<https://huggingface.co/datasets/TraceElephant/TraceElephant>) |
| TRAIL | Eval data \| 评测数据 | 2025 | en | [Paper \| 论文](<https://arxiv.org/abs/2505.08638>) · [Data \| 数据](<https://huggingface.co/datasets/PatronusAI/TRAIL>) |

### Domain capability benchmarks | 领域能力基准

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| CTIBench | Benchmark \| 基准 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/AI4Sec/cti-bench>) |
| CyberMetric | Benchmark \| 基准 | 2024 | en | [Code \| 代码](<https://github.com/cybermetric/CyberMetric>) |
| HealthBench | Benchmark \| 基准 | 2025 | en | [Data \| 数据](<https://huggingface.co/datasets/openai/healthbench>) |
| LawBench | Benchmark \| 基准 | 2023 | zh | [Code \| 代码](<https://github.com/open-compass/LawBench>) |
| SecEval | Benchmark \| 基准 | 2023 | en | [Code \| 代码](<https://github.com/XuanwuAI/SecEval>) |

### Components of listed suites | 已收录基准的子集

| Resource \| 条目 | Type \| 类型 | Year \| 年份 | Language \| 语言 | Links \| 链接 |
| --- | --- | --- | --- | --- |
| DecodingTrust（Privacy 子集） | Component \| 子集 | 2023 | en | [Code \| 代码](<https://github.com/AI-secure/DecodingTrust>) |
| JBB-Behaviors | Component \| 子集 | 2024 | en | [Data \| 数据](<https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors>) |

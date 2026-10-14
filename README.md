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

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AILuminate | [Code](<https://github.com/mlcommons/ailuminate>) | 2025 | zh, en, other |
| Ch3Ef | [Paper](<https://arxiv.org/abs/2403.17830>) | 2024 | en |
| CHiSafetyBench | [Code](<https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench>) | 2024 | zh |
| DecodingTrust | [Data](<https://huggingface.co/datasets/AI-Secure/DecodingTrust>) | 2024 | en |
| Flames | [Code](<https://github.com/AI45Lab/Flames>) | 2023 | zh |
| ForesightSafety Bench | [Code](<https://github.com/Beijing-AISI/ForesightSafety-Bench>) | 2026 | en |
| JailBench | [Code](<https://github.com/STAIR-BUPT/JailBench>) | 2025 | zh |
| LongSafety | [Code](<https://github.com/thu-coai/LongSafety>) | 2025 | en |
| SafetyBench | [Code](<https://github.com/thu-coai/SafetyBench>) | 2024 | zh, en |
| SALAD-Bench | [Project](<https://adwardlee.github.io/salad_bench/>) | 2024 | en |
| SuperCLUE-Safety | [Project](<https://www.cluebenchmarks.com/superclue_safety.html>) | 2024 | zh |
| TrustLLM | [Code](<https://github.com/HowieHwong/TrustLLM>) | 2024 | en |
| U-SafeBench | [Code](<https://github.com/yeonjun-in/U-SafeBench>) | 2025 | en |

### Harmful content and toxicity | 有害内容与毒性

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| BeaverTails | [Project](<https://sites.google.com/view/pku-beavertails>) | 2023 | zh, en |
| ChineseSafe | [Data](<https://huggingface.co/datasets/SUSTech/ChineseSafe>) | 2024 | zh |
| COLD | [Code](<https://github.com/thu-coai/COLDataset>) · [Paper](<https://arxiv.org/abs/2201.06025>) | 2022 | zh |
| CREHate | [Code](<https://github.com/nlee0212/CREHate>) | 2024 | en, other |
| DICES | [Paper](<https://arxiv.org/abs/2306.11247>) | 2023 | en |
| Do-Not-Answer | [Code](<https://github.com/libr-ai/do-not-answer>) | 2024 | zh, en |
| DynaHate | [Code](<https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset>) | 2021 | en |
| hate_speech_offensive | [Data](<https://huggingface.co/datasets/tdavidson/hate_speech_offensive>) | 2017 | en |
| HateCheck | [Code](<https://github.com/paul-rottger/hatecheck-data>) | 2021 | en |
| Implicit Hate Corpus | [Code](<https://github.com/SALT-NLP/implicit-hate>) | 2021 | en |
| Measuring Hate Speech | [Data](<https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech>) | 2022 | en |
| moderation-api-release | [Code](<https://github.com/openai/moderation-api-release/tree/main>) | 2022 | en |
| Multilingual HateCheck (MHC) | [Code](<https://github.com/rewire-online/multilingual-hatecheck>) | 2022 | other |
| ProsocialDialog | [Code](<https://github.com/skywalker023/prosocial-dialog>) | 2022 | en |
| RealToxicityPrompts | [Code](<https://github.com/allenai/real-toxicity-prompts>) | 2020 | en |
| RTP-LX | [Code](<https://github.com/microsoft/RTP-LX>) | 2024 | zh, en, other |
| Safety-Prompts | [Code](<https://github.com/thu-coai/Safety-Prompts>) | 2023 | zh |
| SGHateCheck | [Code](<https://github.com/Social-AI-Studio/SGHateCheck>) | 2024 | other |
| SORRY-Bench | [Code](<https://github.com/SORRY-Bench/sorry-bench>) | 2024 | en |
| TOCP | [Project](<https://nlp.cse.ntou.edu.tw/resources/TOCP/>) · [Paper](<https://aclanthology.org/2020.trac-1.2/>) | 2020 | zh |
| ToxiCN | [Code](<https://github.com/DUT-lujunyu/ToxiCN>) | 2023 | zh |
| ToxiCN MM | [Code](<https://github.com/DUT-lujunyu/ToxiCN_MM>) | 2024 | zh |
| ToxiGen | [Code](<https://github.com/microsoft/ToxiGen>) | 2022 | en |
| TUMCC | [Code](<https://github.com/m1-llie/TUMCC>) · [Paper](<https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X>) | 2020 | zh |

### Jailbreaks and adversarial prompts | 越狱与对抗提示

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AdvBench | [Paper](<https://arxiv.org/abs/2307.15043>) · [Code](<https://github.com/llm-attacks/llm-attacks>) | 2023 | en |
| AttaQ | [Data](<https://huggingface.co/datasets/ibm-research/AttaQ>) | 2023 | en |
| CoSafe | [Code](<https://github.com/ErxinYu/CoSafe-Dataset>) | 2024 | en |
| HarmBench | [Paper](<https://arxiv.org/abs/2402.04249>) · [Code](<https://github.com/centerforaisafety/HarmBench>) | 2024 | en |
| In-the-Wild Jailbreak Prompts (jailbreak_llms) | [Code](<https://github.com/verazuo/jailbreak_llms>) | 2024 | en |
| JailbreakBench | [Paper](<https://arxiv.org/abs/2404.01318>) · [Code](<https://github.com/JailbreakBench/jailbreakbench>) | 2024 | en |
| JailBreakV-28k | [Data](<https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k>) | 2024 | en |
| MaliciousInstruct | [Code](<https://github.com/Princeton-SysML/Jailbreak_LLM>) | 2023 | en |
| MHJ (Multi-Turn Human Jailbreaks) | [Data](<https://huggingface.co/datasets/ScaleAI/mhj>) | 2024 | en |
| MultiBreak | [Paper](<https://arxiv.org/abs/2605.01687>) | 2026 | en |
| MultiJail | [Data](<https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail>) | 2024 | en, other |
| PAP (Persuasive Adversarial Prompts) | [Data](<https://huggingface.co/datasets/CHATS-Lab/Persuasive-Jailbreaker-Data>) | 2024 | en |
| SafeDialBench | [Code](<https://github.com/drivetosouth/SafeDialBench-Dataset>) | 2025 | zh, en |

### Prompt injection and instruction boundaries | 提示注入与指令边界

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| BIPIA | [Paper](<https://arxiv.org/abs/2312.14197>) · [Code](<https://github.com/microsoft/BIPIA>) | KDD 2025 | en |
| HackAPrompt | [Data](<https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset>) | 2023 | 英文(含少量多语言混淆) |
| IHEval | [Code](<https://github.com/ytyz1307zzh/IHEval>) | 2025 | en |
| Open-Prompt-Injection | [Code](<https://github.com/liu00222/Open-Prompt-Injection>) | 2024 | en |
| OpenAI IH-Challenge | [Project](<https://openai.com/index/instruction-hierarchy-challenge/>) | 2025 | en |
| PromptInject | [Code](<https://github.com/agencyenterprise/PromptInject>) | 2022 | en |
| Tensor Trust | [Project](<https://tensortrust.ai/paper/>) · [Code](<https://github.com/HumanCompatibleAI/tensor-trust>) | 2023(arXiv)/2024(ICLR) | en |

### Bias and fairness | 偏见与公平

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| BBQ | [Code](<https://github.com/nyu-mll/BBQ>) | 2021 | en |
| BOLD | [Code](<https://github.com/amazon-science/bold>) | 2021 | en |
| CDIAL-BIAS | [Code](<https://github.com/para-zhou/CDial-Bias>) · [Paper](<https://arxiv.org/abs/2202.08011>) | 2022 | zh |
| HolisticBias | [Paper](<https://arxiv.org/abs/2205.09209>) | 2022 | en |
| HONEST | [Paper](<https://aclanthology.org/2021.naacl-main.191/>) | 2021 | other |
| Social Bias Frames (SBIC) | [Data](<https://huggingface.co/datasets/allenai/social_bias_frames>) | 2020 | en |
| SocialStigmaQA | [Data](<https://huggingface.co/datasets/ibm-research/SocialStigmaQA>) | 2023 | en |
| StereoSet | [Code](<https://github.com/moinnadeem/StereoSet>) | 2020 | en |
| SWSR | [Code](<https://github.com/aggiejiang/SWSR>) · [Paper](<https://arxiv.org/abs/2108.03070>) | 2021 | zh |

### Values, ethics and cultural norms | 价值观、伦理与文化规范

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| CMoralEval | [Code](<https://github.com/tjunlp-lab/CMoralEval>) | 2024 | zh |
| CValues | [Code](<https://github.com/X-PLUG/CValues>) · [Paper](<https://arxiv.org/abs/2307.09705>) · [Data](<https://modelscope.cn/datasets/damo/CValues-Comparison/summary>) | — | zh |
| DailyDilemmas | [Project](<https://huggingface.co/datasets/kellycyy/daily_dilemmas>) | 2024 | en |
| ETHICS | [Code](<https://github.com/hendrycks/ethics>) | 2021 | en |
| GlobalOpinionQA | [Data](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>) | 2023 | en, other |
| KorNAT | [Data](<https://huggingface.co/datasets/jiyounglee0523/KorNAT>) | 2024 | other |
| MedEthicEval | [Code](<https://github.com/X-LANCE/MedEthicEval>) | 2025 | zh |
| Moral Stories | [Code](<https://github.com/demelin/moral_stories>) | 2021 | en |
| MoralBench | [Project](<https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7>) | 2024 | en |
| NormAd | [Code](<https://github.com/Akhila-Yerukola/NormAd>) | 2024 | en |
| OpinionQA | [Code](<https://github.com/tatsu-lab/opinions_qa>) | 2023 | en |
| ValueBench | [Code](<https://github.com/ValueByte-AI/ValueBench>) | 2024 | en |
| WorldValuesBench | [Code](<https://github.com/Demon702/WorldValuesBench>) | 2024 | en |

### Privacy | 隐私

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| ASQ-PHI | [Code](<https://github.com/JamesWeatherhead/asq-phi>) | 2025 | en |
| ConfAIde | [Code](<https://github.com/skywalker023/confaide/tree/main>) | 2024 | en |
| LM_PersonalInfoLeak | [Code](<https://github.com/jeffhj/LM_PersonalInfoLeak>) | 2022 | en |
| MultiPriv | [Code](<https://github.com/CyberChangAn/MultiPriv-PII>) | 2025 | zh, en |
| PrivacyBench | [Code](<https://github.com/sri-ja/privacy-bench>) · [Paper](<https://arxiv.org/abs/2512.24848>) | 2025 | en |
| PUPA | [Data](<https://huggingface.co/datasets/Columbia-NLP/PUPA>) | 2024 | en |

### Over-refusal | 过度拒答

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| FalseReject | [Data](<https://huggingface.co/datasets/AmazonScience/FalseReject>) | 2025 | en |
| OR-Bench | [Code](<https://github.com/justincui03/or-bench>) | 2024 | en |
| PHTest | [Code](<https://github.com/umd-huang-lab/FalseRefusal>) | 2024 | en |
| RASS / MoRBench | [Code](<https://github.com/Master-PLC/RASS>) | 2025 | other |
| XSTest | [Code](<https://github.com/paul-rottger/xstest>) | 2023 | en |

### Autonomy and alignment | 自主性与对齐

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| Anthropic Evals | [Code](<https://github.com/anthropics/evals>) | 2022 | en |
| CRiskEval | [Code](<https://github.com/tjunlp-lab/CRiskEval>) | 2025 | zh |
| Myopia_reward | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | 2022 | zh |
| One-box Tendency | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | 2022 | zh |
| Power-seeking | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | 2022 | zh |
| Self-awareness | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | 2022 | zh |

### Domain risks | 领域风险

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| CyberSecEval 1/2/3 (Purple Llama) | [Code](<https://github.com/meta-llama/PurpleLlama>) | 2023 | en |
| FinSafetyBench | [Code](<https://github.com/sustech-nlp/FinSafetyBench>) | 2026 | zh, en |
| MedSafetyBench | [Code](<https://github.com/AI4LIFE-GROUP/med-safety-bench>) | 2024 | en |
| SafeSci | [Code](<https://github.com/yangyangyang127/SafeSci>) | 2026 | en |
| SciSafeEval | [Paper](<https://arxiv.org/abs/2410.03769>) | 2024 | en |
| WMDP | [Data](<https://huggingface.co/datasets/cais/wmdp>) | 2024 | en |

## Agent Safety & Security | Agent 安全

### Prompt injection and instruction boundaries | 提示注入与指令边界

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AgentDojo | [Paper](<https://arxiv.org/abs/2406.13352>) · [Code](<https://github.com/ethz-spylab/agentdojo>) | NeurIPS 2024 | en |
| AgentDyn | [Paper](<https://arxiv.org/abs/2602.03117>) · [Code](<https://github.com/SaFo-Lab/AgentDyn>) | 2026 | en |
| AgentLAB | [Paper](<https://arxiv.org/abs/2602.16901>) · [Project](<https://tanqiujiang.github.io/AgentLAB_main/>) · [Code](<https://github.com/TanqiuJiang/AgentLAB>) | 2025 | en |
| InjecAgent | [Paper](<https://aclanthology.org/2024.findings-acl.624/>) · [Code](<https://github.com/uiuc-kang-lab/InjecAgent>) | 2024（ACL Findings） | en |

### General agent safety and misuse | 综合 Agent 安全与滥用

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| Agent Security Bench (ASB) | [Paper](<https://arxiv.org/abs/2410.02644>) · [Code](<https://github.com/agiresearch/ASB>) | 2024/2025 | en |
| Agent-SafetyBench | [Paper](<https://arxiv.org/abs/2412.14470>) · [Code](<https://github.com/thu-coai/Agent-SafetyBench>) · [Data](<https://huggingface.co/datasets/thu-coai/Agent-SafetyBench>) · [Project](<https://www.semanticscholar.org/reader/7d11400eeb317ebee278f49e108226a4f8555dda>) | 2025 | en |
| AgentHarm | [Paper](<https://arxiv.org/abs/2410.09024>) · [Data](<https://huggingface.co/datasets/ai-safety-institute/AgentHarm>) · [Project](<https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/>) | ICLR 2025 | en |
| Echoes of Human Malice | [Paper](<https://arxiv.org/abs/2510.14207>) | 2025 | en |
| HAICosystem | [Code](<https://github.com/XuhuiZhou/HAICosystem>) | 2024 | en |
| OpenAgentSafety | [Paper](<https://arxiv.org/abs/2507.06134>) · [Code](<https://github.com/Open-Agent-Safety/OpenAgentSafety>) · [Data](<https://huggingface.co/datasets/sani903/openagentsafety>) | 2025 | en |
| SafePro | [Paper](<https://arxiv.org/abs/2601.06663>) · [Code](<https://github.com/UCSB-AI/SafePro>) · [Project](<https://safeprobench.github.io/safepro/>) · [Data](<https://huggingface.co/datasets/kzhou35/SafePro>) | 2026 | en |

### Tool, API and MCP safety | 工具、API 与 MCP 安全

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| MCIP | [Paper](<https://arxiv.org/abs/2505.14590>) | 2025 | en |
| MCP Security Bench (MSB) | [Paper](<https://arxiv.org/abs/2510.15994>) · [Code](<https://github.com/dongsenzhang/MSB>) | 2025 | en |
| MCP-TDP | [Paper](<https://arxiv.org/abs/2605.24069>) | 2026 | en |
| MCPTox | [Paper](<https://arxiv.org/abs/2508.14925>) · [Code](<https://anonymous.4open.science/r/AAAI26-7C02>) | 2025 | en |
| RAS-EVAL | [Paper](<https://arxiv.org/abs/2506.15253>) · [Code](<https://github.com/lanzer-tree/RAS-Eval>) | 2025 | en |
| ToolEmu | [Paper](<https://arxiv.org/abs/2309.15817>) · [Code](<https://github.com/ryoungj/ToolEmu>) | 2023/ICLR 2024 | en |
| ToolSword | [Code](<https://github.com/Junjie-Ye/ToolSword>) | 2024 | en |

### Privacy and memory | 隐私与记忆

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AgentDAM | [Code](<https://github.com/facebookresearch/ai-agent-privacy>) | 2025 | en |
| AgentLeak | [Paper](<https://arxiv.org/abs/2602.11510>) · [Code](<https://github.com/Privatris/AgentLeak>) · [Data](<https://huggingface.co/datasets/humain2/AgentLeak>) | 2026 | en |
| PrivacyLens | [Code](<https://github.com/SALT-NLP/PrivacyLens>) | 2024 | en |

### Web, computer and mobile agents | 网页、桌面与移动 Agent

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AgentHazard | [Paper](<https://arxiv.org/abs/2604.02947>) · [Code](<https://github.com/Yunhao-Feng/AgentHazard>) · [Project](<https://yunhao-feng.github.io/AgentHazard/>) | 2026 | en |
| CUAHarm | [Paper](<https://arxiv.org/abs/2508.00935>) · [Code](<https://github.com/db-ol/CUAHarm>) · [Data](<https://huggingface.co/datasets/CUAHarm/CUAHarm>) | 2025 | en |
| MobileSafetyBench | [Paper](<https://arxiv.org/abs/2410.17520>) · [Code](<https://github.com/jylee425/mobilesafetybench>) · [Project](<https://mobilesafetybench.github.io>) | 2024 | en |
| RiOSWorld | [Paper](<https://arxiv.org/abs/2506.00618>) · [Project](<https://yjyddq.github.io/RiOSWorld.github.io/>) | 2025 | en |
| SABER | [Paper](<https://arxiv.org/abs/2606.01317>) · [Code](<https://github.com/sssr-lab/saber>) | 2026 | 中英混合, 英语为主 |
| SafeArena | [Code](<https://github.com/McGill-NLP/safearena>) | 2025 | en |
| ST-WebAgentBench | [Paper](<https://arxiv.org/abs/2410.06703>) · [Project](<https://sites.google.com/view/st-webagentbench/home>) · [Data](<https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench>) · [Code](<https://github.com/segev-shlomov/ST-WebAgentBench>) | 2026 | en |
| WASP | [Paper](<https://arxiv.org/abs/2504.18575>) · [Code](<https://github.com/facebookresearch/wasp>) | 2025 | en |

### Embodied safety | 具身安全

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| SafeAgentBench | [Paper](<https://arxiv.org/abs/2412.13178>) · [Project](<https://safeagentbench.github.io>) · [Code](<https://github.com/shengyin1224/SafeAgentBench>) | 2024 | en |

## Safety Judging & Guardrails | 安全审查与护栏

### Agent trajectories and action safety | Agent 轨迹与动作安全

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| ATBench | [Paper](<https://arxiv.org/abs/2604.02022>) · [Code](<https://github.com/LiYu0524/ATbench>) · [Data](<https://huggingface.co/datasets/AI45Research/ATBench>) | 2026 | en |
| PhoneSafety | [Paper](<https://arxiv.org/abs/2605.07630>) · [Code](<https://github.com/tangzhy/PhoneSafety>) · [Data](<https://huggingface.co/datasets/phonesafety-anon/PhoneSafety_Data>) | 2025 | 中文为主 |
| R-Judge | [Paper](<https://arxiv.org/abs/2401.10019>) · [Code](<https://github.com/Lordog/R-Judge>) | 2024 | en |
| SafeToolBench | [Paper](<https://aclanthology.org/2025.findings-emnlp.958.pdf>) · [Code](<https://github.com/BITHLP/SafeToolBench>) | 2025 | en |
| SleightBench | [Paper](<https://arxiv.org/abs/2605.16626>) · [Code](<https://github.com/safety-research/sleight-bench>) | 2025 | en |
| ToolSafe / TS-Bench | [Paper](<https://arxiv.org/abs/2601.10156>) · [Code](<https://github.com/MurrayTom/ToolSafe>) | 2026 | en |
| TOP-Bench | [Paper](<https://arxiv.org/abs/2512.16310>) · [Code](<https://github.com/1Ponder/TOP-R>) · [Project](<https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082>) | 2026 | en |
| TraceSafe-Bench | [Paper](<https://arxiv.org/abs/2604.07223>) · [Code](<https://github.com/cycraft-corp/TraceSafe>) · [Data](<https://huggingface.co/datasets/CyCraftAI/TraceSafe>) | 2026 | en |
| WebGuard | [Code](<https://github.com/OSU-NLP-Group/WebGuard>) | 2025 | en |

### Content guardrail evaluation | 内容护栏评测

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| GuardBench | [Code](<https://github.com/AmenRa/guardbench>) | 2024 | en |
| WildGuard (WildGuardMix/WildGuardTest) | [Data](<https://huggingface.co/datasets/allenai/wildguardmix>) | 2024 | en |

## Related Resources | 相关资源

### Training datasets | 训练数据

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| Aegis 1.0 (Nemotron Content Safety Dataset V1) | [Data](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0>) | 2024 | en |
| GuardReasoner (GuardReasonerTrain) | [Data](<https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain>) | 2025 | en |
| HarmfulQA (RED-INSTRUCT) | [Data](<https://huggingface.co/datasets/TrustAIRLab/HarmfulQA>) | 2023 | en |
| HH-RLHF（含Red Team Attempts） | [Code](<https://github.com/anthropics/hh-rlhf>) | 2022 | en |
| Nemotron Content Safety Dataset V2 | [Data](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0>) | 2025 | en |
| NVIDIA Nemotron Agentic IPI | [Data](<https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1>) | 2026 | en |
| PKU-SafeRLHF (10K/30K) | [Data](<https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K>) | 2023 | en |
| SafeMTData（Derail Yourself/ActorAttack配套） | [Data](<https://huggingface.co/datasets/SafeMTData/SafeMTData>) | 2024 | en |
| ToolSafety | [Paper](<https://aclanthology.org/2025.emnlp-main.714.pdf>) · [Data](<https://huggingface.co/datasets/jinjinyien/ToolSafety>) | EMNLP 2025 | en |
| X-Teaming Evolutionary M2S | [Data](<https://huggingface.co/datasets/hyunjun1121/X-Teaming_Evolutionary_M2S>) | 2025 | en |
| XGuard-Train-Open-200K | [Data](<https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K>) | 2026 | other |
| XGuard-Train（X-Teaming配套） | [Data](<https://huggingface.co/datasets/marslabucla/XGuard-Train>) | 2025 | en |

### Attack methods | 攻击方法

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AgentPoison | [Paper](<https://arxiv.org/abs/2407.12784>) · [Code](<https://github.com/AI-secure/AgentPoison>) · [Project](<https://billchan226.github.io/AgentPoison.html>) | 2024 | en |
| ArtPrompt | [Code](<https://github.com/uw-nsl/ArtPrompt>) | 2024 | en |
| AutoDAN | [Code](<https://github.com/SheltonLiu-N/AutoDAN>) | 2024 | en |
| Automating Deception（FITD多轮越狱） | [Paper](<https://arxiv.org/abs/2511.19517>) | 2025 | en |
| CipherChat | [Code](<https://github.com/RobustNLP/CipherChat>) | 2024 | zh, en |
| CodeChameleon | [Code](<https://github.com/huizhang-L/CodeChameleon>) | 2024 | en |
| Crescendo | [Paper](<https://arxiv.org/abs/2404.01833>) | 2024 | en |
| Curiosity-driven Red Teaming | [Code](<https://github.com/Improbable-AI/curiosity_redteam>) | 2024 | en |
| DeepInception | [Code](<https://github.com/tmlr-group/DeepInception>) | 2023 | en |
| GPTFuzzer | [Code](<https://github.com/hubertyoo/GPTFuzz>) | 2023 | en |
| Latent Jailbreak | [Code](<https://github.com/qiuhuachuan/latent-jailbreak>) | 2023 | 英文+中文 |
| MART | [Paper](<https://arxiv.org/abs/2311.07689>) | 2023 | en |
| MemoryGraft | [Paper](<https://arxiv.org/abs/2512.16962>) · [Code](<https://github.com/Jacobhhy/MemoryGraft>) · [Project](<https://www.semanticscholar.org/reader/b1d80b2eda7e175e235185bdc7df4e8233f36ef4>) | 2025 | en |
| PsychJail | [Code](<https://github.com/FengZeyugit/PsychJail>) | 2026 | en |
| ReNeLLM | [Code](<https://github.com/NJUNLP/ReNeLLM>) | 2024 | en |

### Frameworks and mixed resources | 框架及混合资源

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| AgentDefense-Bench | [Code](<https://github.com/arunsanna/AgentDefense-Bench>) | 2025 | en |
| CC-BOS | [Code](<https://github.com/xaoLiu1222/cc-bos>) | 2026 | zh |
| LiveSecBench | [Code](<https://github.com/ydli-ai/LiveSecBench>) | 2026 | zh |
| ORFuzz | [Paper](<https://arxiv.org/abs/2508.11222>) | 2025 | en |
| ShieldLM | [Code](<https://github.com/thu-coai/ShieldLM>) | 2024 | zh, en |
| TrustAgent | [Paper](<https://arxiv.org/abs/2402.01586>) | 2024 | en |
| WILDTEAMING / WildJailbreak | [Code](<https://github.com/allenai/wildteaming>) | 2024 | en |

### Attack challenges and data | 攻击挑战与数据

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| LLMail-Inject | [Paper](<https://arxiv.org/abs/2506.09956>) · [Code](<https://github.com/microsoft/llmail-inject-challenge>) | 2025 | en |

### Capability baselines and environments | 能力基线与环境

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| Agent-Diff | [Paper](<https://arxiv.org/abs/2602.11224>) · [Code](<https://github.com/agent-diff-bench/agent-diff>) · [Project](<https://www.agentdiff.dev>) · [Data](<https://huggingface.co/datasets/hubertmarek/agent-diff-bench>) | 2026 | en |
| API-Bank | [Paper](<https://arxiv.org/abs/2304.08244>) | EMNLP 2023 | en |
| AppWorld | [Paper](<https://aclanthology.org/2024.acl-long.850/>) · [Code](<https://github.com/StonyBrookNLP/appworld>) · [Project](<https://appworld.dev>) | ACL 2024 | en |
| BFCL | [Paper](<https://proceedings.mlr.press/v267/patil25a.html>) · [Project](<https://gorilla.cs.berkeley.edu/leaderboard.html>) · [Data](<https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard>) | 2024/2025，持续更新至 V4 | 英语为主, 多语言函数调用场景 |
| SkillsBench | [Paper](<https://arxiv.org/abs/2602.12670>) · [Project](<https://www.skillsbench.ai>) · [Code](<https://github.com/benchflow-ai/skillsbench>) | 2026 | en |
| tau-bench | [Paper](<https://arxiv.org/abs/2406.12045>) · [Code](<https://github.com/sierra-research/tau-bench>) · [Project](<https://www.semanticscholar.org/reader/70aa016c1f68fd5c0261f26ad20017b8307650af>) | 2024 | en |
| TheAgentCompany | [Paper](<https://arxiv.org/abs/2412.14161>) · [Code](<https://github.com/TheAgentCompany/TheAgentCompany>) · [Project](<https://the-agent-company.com>) | 2024/2025 | en |
| TOOLATHLON | [Paper](<https://arxiv.org/abs/2510.25726>) · [Code](<https://github.com/hkust-nlp/Toolathlon>) | 2026 | en |
| ToolSandbox | [Paper](<https://arxiv.org/abs/2408.04682>) · [Code](<https://github.com/apple-aiml-research/ToolSandbox>) · [Project](<https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark>) | 2024 | en |
| WebArena | [Paper](<https://arxiv.org/abs/2307.13854>) · [Code](<https://github.com/web-arena-x/webarena>) · [Project](<https://webarena.dev>) | ICLR 2024 / NeurIPS 2024 Oral 相关项目口径 | en |
| WorkArena | [Paper](<https://arxiv.org/abs/2403.07718>) · [Code](<https://github.com/ServiceNow/workarena>) · [Project](<https://servicenow.github.io/WorkArena/>) | ICML 2024 | en |

### Factuality and general trace diagnostics | 事实性与通用轨迹诊断

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| HaluEval | [Paper](<https://arxiv.org/abs/2305.11747>) · [Code](<https://github.com/RUCAIBox/HaluEval>) | 2023 | en |
| RAGTruth | [Paper](<https://arxiv.org/abs/2401.00396>) | 2023 | en |
| SimpleQA | [Paper](<https://arxiv.org/abs/2411.04368>) · [Code](<https://github.com/openai/simple-evals>) | 2024 | en |
| TraceElephant | [Paper](<https://arxiv.org/abs/2604.22708>) · [Code](<https://github.com/TraceElephant/TraceElephant>) · [Data](<https://huggingface.co/datasets/TraceElephant/TraceElephant>) | 2026 | en |
| TRAIL | [Paper](<https://arxiv.org/abs/2505.08638>) · [Data](<https://huggingface.co/datasets/PatronusAI/TRAIL>) | 2025 | en |

### Domain capability benchmarks | 领域能力基准

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| CTIBench | [Data](<https://huggingface.co/datasets/AI4Sec/cti-bench>) | 2024 | en |
| CyberMetric | [Code](<https://github.com/cybermetric/CyberMetric>) | 2024 | en |
| HealthBench | [Data](<https://huggingface.co/datasets/openai/healthbench>) | 2025 | en |
| LawBench | [Code](<https://github.com/open-compass/LawBench>) | 2023 | zh |
| SecEval | [Code](<https://github.com/XuanwuAI/SecEval>) | 2023 | en |

### Components of listed suites | 已收录基准的子集

| Resource | Links | Year | Language |
| --- | --- | --- | --- |
| DecodingTrust（Privacy 子集） | [Code](<https://github.com/AI-secure/DecodingTrust>) | 2023 | en |
| JBB-Behaviors | [Data](<https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors>) | 2024 | en |

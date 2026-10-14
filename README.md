# Awesome LLM & Agent Safety Benchmarks

[English](README.md) · [简体中文](README.zh-CN.md)

A continuously updated navigation project for LLM and agent safety benchmarks, evaluation datasets and related resources. Entries are organized by evaluation target and topic.

**212 catalog entries** from 5 original source files. Updated 2026-10-14; includes 143 safety entries, 58 related resources and 11 entries pending review.

**Link check (2026-10-14):** 321 distinct URLs checked, 317 reachable or redirected, 2 missing, 1 restricted, 1 server error; 3 placeholder/misattributed URLs skipped. [Details](docs/link-check-report.md).

## Contents

- [LLM Safety](#llm-safety)
- [Agent Safety & Security](#agent-safety--security)
- [Safety Judging & Guardrails](#safety-judging--guardrails)
- [Related Resources](#related-resources)

## LLM Safety

### Comprehensive safety

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AILuminate | Suite | 2025 | zh, en, other | [Code](<https://github.com/mlcommons/ailuminate>) |
| Ch3Ef | Suite | 2024 | en | [Paper](<https://arxiv.org/abs/2403.17830>) |
| CHiSafetyBench | Suite | 2024 | zh | [Code](<https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench>) |
| DecodingTrust | Suite | 2024 | en | [Data](<https://huggingface.co/datasets/AI-Secure/DecodingTrust>) |
| Flames | Suite | 2023 | zh | [Code](<https://github.com/AI45Lab/Flames>) |
| ForesightSafety Bench | Suite | 2026 | en | [Code](<https://github.com/Beijing-AISI/ForesightSafety-Bench>) |
| JailBench | Suite | 2025 | zh | [Code](<https://github.com/STAIR-BUPT/JailBench>) |
| LongSafety | Suite | 2025 | en | [Code](<https://github.com/thu-coai/LongSafety>) |
| SafetyBench | Suite | 2024 | zh, en | [Code](<https://github.com/thu-coai/SafetyBench>) |
| SALAD-Bench | Suite | 2024 | en | [Project](<https://adwardlee.github.io/salad_bench/>) |
| SuperCLUE-Safety | Suite | 2024 | zh | [Project](<https://www.cluebenchmarks.com/superclue_safety.html>) |
| TrustLLM | Suite | 2024 | en | [Code](<https://github.com/HowieHwong/TrustLLM>) |
| U-SafeBench | Suite | 2025 | en | [Code](<https://github.com/yeonjun-in/U-SafeBench>) |

### Harmful content and toxicity

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| BeaverTails | Eval data | 2023 | zh, en | [Project](<https://sites.google.com/view/pku-beavertails>) |
| ChineseSafe | Eval data | 2024 | zh | [Data](<https://huggingface.co/datasets/SUSTech/ChineseSafe>) |
| COLD | Eval data | 2022 | zh | [Code](<https://github.com/thu-coai/COLDataset>) · [Paper](<https://arxiv.org/abs/2201.06025>) |
| CREHate | Eval data | 2024 | en, other | [Code](<https://github.com/nlee0212/CREHate>) |
| DICES | Eval data | 2023 | en | [Paper](<https://arxiv.org/abs/2306.11247>) |
| Do-Not-Answer | Eval data | 2024 | zh, en | [Code](<https://github.com/libr-ai/do-not-answer>) |
| DynaHate | Eval data | 2021 | en | [Code](<https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset>) |
| hate_speech_offensive | Eval data | 2017 | en | [Data](<https://huggingface.co/datasets/tdavidson/hate_speech_offensive>) |
| HateCheck | Eval data | 2021 | en | [Code](<https://github.com/paul-rottger/hatecheck-data>) |
| Implicit Hate Corpus | Eval data | 2021 | en | [Code](<https://github.com/SALT-NLP/implicit-hate>) |
| Measuring Hate Speech | Eval data | 2022 | en | [Data](<https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech>) |
| moderation-api-release | Eval data | 2022 | en | [Code](<https://github.com/openai/moderation-api-release/tree/main>) |
| Multilingual HateCheck (MHC) | Eval data | 2022 | other | [Code](<https://github.com/rewire-online/multilingual-hatecheck>) |
| ProsocialDialog | Eval data | 2022 | en | [Code](<https://github.com/skywalker023/prosocial-dialog>) |
| RealToxicityPrompts | Eval data | 2020 | en | [Code](<https://github.com/allenai/real-toxicity-prompts>) |
| RTP-LX | Eval data | 2024 | zh, en, other | [Code](<https://github.com/microsoft/RTP-LX>) |
| Safety-Prompts | Eval data | 2023 | zh | [Code](<https://github.com/thu-coai/Safety-Prompts>) |
| SGHateCheck | Eval data | 2024 | other | [Code](<https://github.com/Social-AI-Studio/SGHateCheck>) |
| SORRY-Bench | Eval data | 2024 | en | [Code](<https://github.com/SORRY-Bench/sorry-bench>) |
| TOCP | Eval data | 2020 | zh | [Project](<https://nlp.cse.ntou.edu.tw/resources/TOCP/>) · [Paper](<https://aclanthology.org/2020.trac-1.2/>) |
| ToxiCN | Eval data | 2023 | zh | [Code](<https://github.com/DUT-lujunyu/ToxiCN>) |
| ToxiCN MM | Eval data | 2024 | zh | [Code](<https://github.com/DUT-lujunyu/ToxiCN_MM>) |
| ToxiGen | Eval data | 2022 | en | [Code](<https://github.com/microsoft/ToxiGen>) |
| TUMCC | Eval data | 2020 | zh | [Code](<https://github.com/m1-llie/TUMCC>) · [Paper](<https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X>) |

### Jailbreaks and adversarial prompts

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AdvBench | Benchmark | 2023 | en | [Paper](<https://arxiv.org/abs/2307.15043>) · [Code](<https://github.com/llm-attacks/llm-attacks>) |
| AttaQ | Benchmark | 2023 | en | [Data](<https://huggingface.co/datasets/ibm-research/AttaQ>) |
| CoSafe | Benchmark | 2024 | en | [Code](<https://github.com/ErxinYu/CoSafe-Dataset>) |
| HarmBench | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2402.04249>) · [Code](<https://github.com/centerforaisafety/HarmBench>) |
| In-the-Wild Jailbreak Prompts (jailbreak_llms) | Benchmark | 2024 | en | [Code](<https://github.com/verazuo/jailbreak_llms>) |
| JailbreakBench | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2404.01318>) · [Code](<https://github.com/JailbreakBench/jailbreakbench>) |
| JailBreakV-28k | Benchmark | 2024 | en | [Data](<https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k>) |
| MaliciousInstruct | Benchmark | 2023 | en | [Code](<https://github.com/Princeton-SysML/Jailbreak_LLM>) |
| MHJ (Multi-Turn Human Jailbreaks) | Benchmark | 2024 | en | [Data](<https://huggingface.co/datasets/ScaleAI/mhj>) |
| MultiBreak | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2605.01687>) |
| MultiJail | Benchmark | 2024 | en, other | [Data](<https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail>) |
| PAP (Persuasive Adversarial Prompts) | Benchmark | 2024 | en | [Data](<https://huggingface.co/datasets/CHATS-Lab/Persuasive-Jailbreaker-Data>) |
| SafeDialBench | Benchmark | 2025 | zh, en | [Code](<https://github.com/drivetosouth/SafeDialBench-Dataset>) |

### Prompt injection and instruction boundaries

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| BIPIA | Benchmark | KDD 2025 | en | [Paper](<https://arxiv.org/abs/2312.14197>) · [Code](<https://github.com/microsoft/BIPIA>) |
| HackAPrompt | Benchmark | 2023 | 英文(含少量多语言混淆) | [Data](<https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset>) |
| IHEval | Benchmark | 2025 | en | [Code](<https://github.com/ytyz1307zzh/IHEval>) |
| Open-Prompt-Injection | Benchmark | 2024 | en | [Code](<https://github.com/liu00222/Open-Prompt-Injection>) |
| OpenAI IH-Challenge | Benchmark | 2025 | en | [Project](<https://openai.com/index/instruction-hierarchy-challenge/>) |
| PromptInject | Benchmark | 2022 | en | [Code](<https://github.com/agencyenterprise/PromptInject>) |
| Tensor Trust | Benchmark | 2023(arXiv)/2024(ICLR) | en | [Project](<https://tensortrust.ai/paper/>) · [Code](<https://github.com/HumanCompatibleAI/tensor-trust>) |

### Bias and fairness

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| BBQ | Eval data | 2021 | en | [Code](<https://github.com/nyu-mll/BBQ>) |
| BOLD | Eval data | 2021 | en | [Code](<https://github.com/amazon-science/bold>) |
| CDIAL-BIAS | Eval data | 2022 | zh | [Code](<https://github.com/para-zhou/CDial-Bias>) · [Paper](<https://arxiv.org/abs/2202.08011>) |
| HolisticBias | Eval data | 2022 | en | [Paper](<https://arxiv.org/abs/2205.09209>) |
| HONEST | Eval data | 2021 | other | [Paper](<https://aclanthology.org/2021.naacl-main.191/>) |
| Social Bias Frames (SBIC) | Eval data | 2020 | en | [Data](<https://huggingface.co/datasets/allenai/social_bias_frames>) |
| SocialStigmaQA | Eval data | 2023 | en | [Data](<https://huggingface.co/datasets/ibm-research/SocialStigmaQA>) |
| StereoSet | Eval data | 2020 | en | [Code](<https://github.com/moinnadeem/StereoSet>) |
| SWSR | Eval data | 2021 | zh | [Code](<https://github.com/aggiejiang/SWSR>) · [Paper](<https://arxiv.org/abs/2108.03070>) |

### Values, ethics and cultural norms

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| CMoralEval | Benchmark | 2024 | zh | [Code](<https://github.com/tjunlp-lab/CMoralEval>) |
| CValues | Benchmark | — | zh | [Code](<https://github.com/X-PLUG/CValues>) · [Paper](<https://arxiv.org/abs/2307.09705>) · [Data](<https://modelscope.cn/datasets/damo/CValues-Comparison/summary>) |
| DailyDilemmas | Benchmark | 2024 | en | [Project](<https://huggingface.co/datasets/kellycyy/daily_dilemmas>) |
| ETHICS | Benchmark | 2021 | en | [Code](<https://github.com/hendrycks/ethics>) |
| GlobalOpinionQA | Benchmark | 2023 | en, other | [Data](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>) |
| KorNAT | Benchmark | 2024 | other | [Data](<https://huggingface.co/datasets/jiyounglee0523/KorNAT>) |
| MedEthicEval | Benchmark | 2025 | zh | [Code](<https://github.com/X-LANCE/MedEthicEval>) |
| Moral Stories | Benchmark | 2021 | en | [Code](<https://github.com/demelin/moral_stories>) |
| MoralBench | Benchmark | 2024 | en | [Project](<https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7>) |
| NormAd | Benchmark | 2024 | en | [Code](<https://github.com/Akhila-Yerukola/NormAd>) |
| OpinionQA | Benchmark | 2023 | en | [Code](<https://github.com/tatsu-lab/opinions_qa>) |
| ValueBench | Benchmark | 2024 | en | [Code](<https://github.com/ValueByte-AI/ValueBench>) |
| WorldValuesBench | Benchmark | 2024 | en | [Code](<https://github.com/Demon702/WorldValuesBench>) |

### Privacy

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| ASQ-PHI | Benchmark | 2025 | en | [Code](<https://github.com/JamesWeatherhead/asq-phi>) |
| ConfAIde | Benchmark | 2024 | en | [Code](<https://github.com/skywalker023/confaide/tree/main>) |
| LM_PersonalInfoLeak | Benchmark | 2022 | en | [Code](<https://github.com/jeffhj/LM_PersonalInfoLeak>) |
| MultiPriv | Benchmark | 2025 | zh, en | [Code](<https://github.com/CyberChangAn/MultiPriv-PII>) |
| PrivacyBench | Benchmark | 2025 | en | [Code](<https://github.com/sri-ja/privacy-bench>) · [Paper](<https://arxiv.org/abs/2512.24848>) |
| PUPA | Benchmark | 2024 | en | [Data](<https://huggingface.co/datasets/Columbia-NLP/PUPA>) |

### Over-refusal

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| FalseReject | Benchmark | 2025 | en | [Data](<https://huggingface.co/datasets/AmazonScience/FalseReject>) |
| OR-Bench | Benchmark | 2024 | en | [Code](<https://github.com/justincui03/or-bench>) |
| PHTest | Benchmark | 2024 | en | [Code](<https://github.com/umd-huang-lab/FalseRefusal>) |
| RASS / MoRBench | Benchmark | 2025 | other | [Code](<https://github.com/Master-PLC/RASS>) |
| XSTest | Benchmark | 2023 | en | [Code](<https://github.com/paul-rottger/xstest>) |

### Autonomy and alignment

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| Anthropic Evals | Suite | 2022 | en | [Code](<https://github.com/anthropics/evals>) |
| CRiskEval | Suite | 2025 | zh | [Code](<https://github.com/tjunlp-lab/CRiskEval>) |
| Myopia_reward | Suite | 2022 | zh | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) |
| One-box Tendency | Suite | 2022 | zh | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) |
| Power-seeking | Suite | 2022 | zh | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) |
| Self-awareness | Suite | 2022 | zh | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) |

### Domain risks

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| CyberSecEval 1/2/3 (Purple Llama) | Benchmark | 2023 | en | [Code](<https://github.com/meta-llama/PurpleLlama>) |
| FinSafetyBench | Benchmark | 2026 | zh, en | [Code](<https://github.com/sustech-nlp/FinSafetyBench>) |
| MedSafetyBench | Benchmark | 2024 | en | [Code](<https://github.com/AI4LIFE-GROUP/med-safety-bench>) |
| SafeSci | Benchmark | 2026 | en | [Code](<https://github.com/yangyangyang127/SafeSci>) |
| SciSafeEval | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2410.03769>) |
| WMDP | Benchmark | 2024 | en | [Data](<https://huggingface.co/datasets/cais/wmdp>) |

## Agent Safety & Security

### Prompt injection and instruction boundaries

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AgentDojo | Benchmark | NeurIPS 2024 | en | [Paper](<https://arxiv.org/abs/2406.13352>) · [Code](<https://github.com/ethz-spylab/agentdojo>) |
| AgentDyn | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2602.03117>) · [Code](<https://github.com/SaFo-Lab/AgentDyn>) |
| AgentLAB | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2602.16901>) · [Project](<https://tanqiujiang.github.io/AgentLAB_main/>) · [Code](<https://github.com/TanqiuJiang/AgentLAB>) |
| InjecAgent | Benchmark | 2024（ACL Findings） | en | [Paper](<https://aclanthology.org/2024.findings-acl.624/>) · [Code](<https://github.com/uiuc-kang-lab/InjecAgent>) |

### General agent safety and misuse

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| Agent Security Bench (ASB) | Benchmark | 2024/2025 | en | [Paper](<https://arxiv.org/abs/2410.02644>) · [Code](<https://github.com/agiresearch/ASB>) |
| Agent-SafetyBench | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2412.14470>) · [Code](<https://github.com/thu-coai/Agent-SafetyBench>) · [Data](<https://huggingface.co/datasets/thu-coai/Agent-SafetyBench>) · [Project](<https://www.semanticscholar.org/reader/7d11400eeb317ebee278f49e108226a4f8555dda>) |
| AgentHarm | Benchmark | ICLR 2025 | en | [Paper](<https://arxiv.org/abs/2410.09024>) · [Data](<https://huggingface.co/datasets/ai-safety-institute/AgentHarm>) · [Project](<https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/>) |
| Echoes of Human Malice | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2510.14207>) |
| HAICosystem | Benchmark | 2024 | en | [Code](<https://github.com/XuhuiZhou/HAICosystem>) |
| OpenAgentSafety | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2507.06134>) · [Code](<https://github.com/Open-Agent-Safety/OpenAgentSafety>) · [Data](<https://huggingface.co/datasets/sani903/openagentsafety>) |
| SafePro | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2601.06663>) · [Code](<https://github.com/UCSB-AI/SafePro>) · [Project](<https://safeprobench.github.io/safepro/>) · [Data](<https://huggingface.co/datasets/kzhou35/SafePro>) |

### Tool, API and MCP safety

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| MCIP | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2505.14590>) |
| MCP Security Bench (MSB) | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2510.15994>) · [Code](<https://github.com/dongsenzhang/MSB>) |
| MCP-TDP | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2605.24069>) |
| MCPTox | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2508.14925>) · [Code](<https://anonymous.4open.science/r/AAAI26-7C02>) |
| RAS-EVAL | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2506.15253>) · [Code](<https://github.com/lanzer-tree/RAS-Eval>) |
| ToolEmu | Benchmark | 2023/ICLR 2024 | en | [Paper](<https://arxiv.org/abs/2309.15817>) · [Code](<https://github.com/ryoungj/ToolEmu>) |
| ToolSword | Benchmark | 2024 | en | [Code](<https://github.com/Junjie-Ye/ToolSword>) |

### Privacy and memory

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AgentDAM | Benchmark | 2025 | en | [Code](<https://github.com/facebookresearch/ai-agent-privacy>) |
| AgentLeak | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2602.11510>) · [Code](<https://github.com/Privatris/AgentLeak>) · [Data](<https://huggingface.co/datasets/humain2/AgentLeak>) |
| PrivacyLens | Benchmark | 2024 | en | [Code](<https://github.com/SALT-NLP/PrivacyLens>) |

### Web, computer and mobile agents

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AgentHazard | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2604.02947>) · [Code](<https://github.com/Yunhao-Feng/AgentHazard>) · [Project](<https://yunhao-feng.github.io/AgentHazard/>) |
| CUAHarm | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2508.00935>) · [Code](<https://github.com/db-ol/CUAHarm>) · [Data](<https://huggingface.co/datasets/CUAHarm/CUAHarm>) |
| MobileSafetyBench | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2410.17520>) · [Code](<https://github.com/jylee425/mobilesafetybench>) · [Project](<https://mobilesafetybench.github.io>) |
| RiOSWorld | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2506.00618>) · [Project](<https://yjyddq.github.io/RiOSWorld.github.io/>) |
| SABER | Benchmark | 2026 | 中英混合, 英语为主 | [Paper](<https://arxiv.org/abs/2606.01317>) · [Code](<https://github.com/sssr-lab/saber>) |
| SafeArena | Benchmark | 2025 | en | [Code](<https://github.com/McGill-NLP/safearena>) |
| ST-WebAgentBench | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2410.06703>) · [Project](<https://sites.google.com/view/st-webagentbench/home>) · [Data](<https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench>) · [Code](<https://github.com/segev-shlomov/ST-WebAgentBench>) |
| WASP | Benchmark | 2025 | en | [Paper](<https://arxiv.org/abs/2504.18575>) · [Code](<https://github.com/facebookresearch/wasp>) |

### Embodied safety

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| SafeAgentBench | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2412.13178>) · [Project](<https://safeagentbench.github.io>) · [Code](<https://github.com/shengyin1224/SafeAgentBench>) |

## Safety Judging & Guardrails

### Agent trajectories and action safety

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| ATBench | Eval data | 2026 | en | [Paper](<https://arxiv.org/abs/2604.02022>) · [Code](<https://github.com/LiYu0524/ATbench>) · [Data](<https://huggingface.co/datasets/AI45Research/ATBench>) |
| PhoneSafety | Eval data | 2025 | 中文为主 | [Paper](<https://arxiv.org/abs/2605.07630>) · [Code](<https://github.com/tangzhy/PhoneSafety>) · [Data](<https://huggingface.co/datasets/phonesafety-anon/PhoneSafety_Data>) |
| R-Judge | Eval data | 2024 | en | [Paper](<https://arxiv.org/abs/2401.10019>) · [Code](<https://github.com/Lordog/R-Judge>) |
| SafeToolBench | Eval data | 2025 | en | [Paper](<https://aclanthology.org/2025.findings-emnlp.958.pdf>) · [Code](<https://github.com/BITHLP/SafeToolBench>) |
| SleightBench | Eval data | 2025 | en | [Paper](<https://arxiv.org/abs/2605.16626>) · [Code](<https://github.com/safety-research/sleight-bench>) |
| ToolSafe / TS-Bench | Eval data | 2026 | en | [Paper](<https://arxiv.org/abs/2601.10156>) · [Code](<https://github.com/MurrayTom/ToolSafe>) |
| TOP-Bench | Eval data | 2026 | en | [Paper](<https://arxiv.org/abs/2512.16310>) · [Code](<https://github.com/1Ponder/TOP-R>) · [Project](<https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082>) |
| TraceSafe-Bench | Eval data | 2026 | en | [Paper](<https://arxiv.org/abs/2604.07223>) · [Code](<https://github.com/cycraft-corp/TraceSafe>) · [Data](<https://huggingface.co/datasets/CyCraftAI/TraceSafe>) |
| WebGuard | Eval data | 2025 | en | [Code](<https://github.com/OSU-NLP-Group/WebGuard>) |

### Content guardrail evaluation

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| GuardBench | Suite | 2024 | en | [Code](<https://github.com/AmenRa/guardbench>) |
| WildGuard (WildGuardMix/WildGuardTest) | Suite | 2024 | en | [Data](<https://huggingface.co/datasets/allenai/wildguardmix>) |

## Related Resources

### Training datasets

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| Aegis 1.0 (Nemotron Content Safety Dataset V1) | Train data | 2024 | en | [Data](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0>) |
| GuardReasoner (GuardReasonerTrain) | Train data | 2025 | en | [Data](<https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain>) |
| HarmfulQA (RED-INSTRUCT) | Train data | 2023 | en | [Data](<https://huggingface.co/datasets/TrustAIRLab/HarmfulQA>) |
| HH-RLHF（含Red Team Attempts） | Train data | 2022 | en | [Code](<https://github.com/anthropics/hh-rlhf>) |
| Nemotron Content Safety Dataset V2 | Train data | 2025 | en | [Data](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0>) |
| NVIDIA Nemotron Agentic IPI | Train data | 2026 | en | [Data](<https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1>) |
| PKU-SafeRLHF (10K/30K) | Train data | 2023 | en | [Data](<https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K>) |
| SafeMTData（Derail Yourself/ActorAttack配套） | Train data | 2024 | en | [Data](<https://huggingface.co/datasets/SafeMTData/SafeMTData>) |
| ToolSafety | Train data | EMNLP 2025 | en | [Paper](<https://aclanthology.org/2025.emnlp-main.714.pdf>) · [Data](<https://huggingface.co/datasets/jinjinyien/ToolSafety>) |
| X-Teaming Evolutionary M2S | Train data | 2025 | en | [Data](<https://huggingface.co/datasets/hyunjun1121/X-Teaming_Evolutionary_M2S>) |
| XGuard-Train-Open-200K | Train data | 2026 | other | [Data](<https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K>) |
| XGuard-Train（X-Teaming配套） | Train data | 2025 | en | [Data](<https://huggingface.co/datasets/marslabucla/XGuard-Train>) |

### Attack methods

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AgentPoison | Method | 2024 | en | [Paper](<https://arxiv.org/abs/2407.12784>) · [Code](<https://github.com/AI-secure/AgentPoison>) · [Project](<https://billchan226.github.io/AgentPoison.html>) |
| ArtPrompt | Method | 2024 | en | [Code](<https://github.com/uw-nsl/ArtPrompt>) |
| AutoDAN | Method | 2024 | en | [Code](<https://github.com/SheltonLiu-N/AutoDAN>) |
| Automating Deception（FITD多轮越狱） | Method | 2025 | en | [Paper](<https://arxiv.org/abs/2511.19517>) |
| CipherChat | Method | 2024 | zh, en | [Code](<https://github.com/RobustNLP/CipherChat>) |
| CodeChameleon | Method | 2024 | en | [Code](<https://github.com/huizhang-L/CodeChameleon>) |
| Crescendo | Method | 2024 | en | [Paper](<https://arxiv.org/abs/2404.01833>) |
| Curiosity-driven Red Teaming | Method | 2024 | en | [Code](<https://github.com/Improbable-AI/curiosity_redteam>) |
| DeepInception | Method | 2023 | en | [Code](<https://github.com/tmlr-group/DeepInception>) |
| GPTFuzzer | Method | 2023 | en | [Code](<https://github.com/hubertyoo/GPTFuzz>) |
| Latent Jailbreak | Method | 2023 | 英文+中文 | [Code](<https://github.com/qiuhuachuan/latent-jailbreak>) |
| MART | Method | 2023 | en | [Paper](<https://arxiv.org/abs/2311.07689>) |
| MemoryGraft | Method | 2025 | en | [Paper](<https://arxiv.org/abs/2512.16962>) · [Code](<https://github.com/Jacobhhy/MemoryGraft>) · [Project](<https://www.semanticscholar.org/reader/b1d80b2eda7e175e235185bdc7df4e8233f36ef4>) |
| PsychJail | Method | 2026 | en | [Code](<https://github.com/FengZeyugit/PsychJail>) |
| ReNeLLM | Method | 2024 | en | [Code](<https://github.com/NJUNLP/ReNeLLM>) |

### Frameworks and mixed resources

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| AgentDefense-Bench | Framework | 2025 | en | [Code](<https://github.com/arunsanna/AgentDefense-Bench>) |
| CC-BOS | Framework | 2026 | zh | [Code](<https://github.com/xaoLiu1222/cc-bos>) |
| LiveSecBench | Framework | 2026 | zh | [Code](<https://github.com/ydli-ai/LiveSecBench>) |
| ORFuzz | Framework | 2025 | en | [Paper](<https://arxiv.org/abs/2508.11222>) |
| ShieldLM | Framework | 2024 | zh, en | [Code](<https://github.com/thu-coai/ShieldLM>) |
| TrustAgent | Framework | 2024 | en | [Paper](<https://arxiv.org/abs/2402.01586>) |
| WILDTEAMING / WildJailbreak | Framework | 2024 | en | [Code](<https://github.com/allenai/wildteaming>) |

### Attack challenges and data

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| LLMail-Inject | Eval data | 2025 | en | [Paper](<https://arxiv.org/abs/2506.09956>) · [Code](<https://github.com/microsoft/llmail-inject-challenge>) |

### Capability baselines and environments

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| Agent-Diff | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2602.11224>) · [Code](<https://github.com/agent-diff-bench/agent-diff>) · [Project](<https://www.agentdiff.dev>) · [Data](<https://huggingface.co/datasets/hubertmarek/agent-diff-bench>) |
| API-Bank | Benchmark | EMNLP 2023 | en | [Paper](<https://arxiv.org/abs/2304.08244>) |
| AppWorld | Benchmark | ACL 2024 | en | [Paper](<https://aclanthology.org/2024.acl-long.850/>) · [Code](<https://github.com/StonyBrookNLP/appworld>) · [Project](<https://appworld.dev>) |
| BFCL | Benchmark | 2024/2025，持续更新至 V4 | 英语为主, 多语言函数调用场景 | [Paper](<https://proceedings.mlr.press/v267/patil25a.html>) · [Project](<https://gorilla.cs.berkeley.edu/leaderboard.html>) · [Data](<https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard>) |
| SkillsBench | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2602.12670>) · [Project](<https://www.skillsbench.ai>) · [Code](<https://github.com/benchflow-ai/skillsbench>) |
| tau-bench | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2406.12045>) · [Code](<https://github.com/sierra-research/tau-bench>) · [Project](<https://www.semanticscholar.org/reader/70aa016c1f68fd5c0261f26ad20017b8307650af>) |
| TheAgentCompany | Benchmark | 2024/2025 | en | [Paper](<https://arxiv.org/abs/2412.14161>) · [Code](<https://github.com/TheAgentCompany/TheAgentCompany>) · [Project](<https://the-agent-company.com>) |
| TOOLATHLON | Benchmark | 2026 | en | [Paper](<https://arxiv.org/abs/2510.25726>) · [Code](<https://github.com/hkust-nlp/Toolathlon>) |
| ToolSandbox | Benchmark | 2024 | en | [Paper](<https://arxiv.org/abs/2408.04682>) · [Code](<https://github.com/apple-aiml-research/ToolSandbox>) · [Project](<https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark>) |
| WebArena | Benchmark | ICLR 2024 / NeurIPS 2024 Oral 相关项目口径 | en | [Paper](<https://arxiv.org/abs/2307.13854>) · [Code](<https://github.com/web-arena-x/webarena>) · [Project](<https://webarena.dev>) |
| WorkArena | Benchmark | ICML 2024 | en | [Paper](<https://arxiv.org/abs/2403.07718>) · [Code](<https://github.com/ServiceNow/workarena>) · [Project](<https://servicenow.github.io/WorkArena/>) |

### Factuality and general trace diagnostics

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| HaluEval | Eval data | 2023 | en | [Paper](<https://arxiv.org/abs/2305.11747>) · [Code](<https://github.com/RUCAIBox/HaluEval>) |
| RAGTruth | Eval data | 2023 | en | [Paper](<https://arxiv.org/abs/2401.00396>) |
| SimpleQA | Eval data | 2024 | en | [Paper](<https://arxiv.org/abs/2411.04368>) · [Code](<https://github.com/openai/simple-evals>) |
| TraceElephant | Eval data | 2026 | en | [Paper](<https://arxiv.org/abs/2604.22708>) · [Code](<https://github.com/TraceElephant/TraceElephant>) · [Data](<https://huggingface.co/datasets/TraceElephant/TraceElephant>) |
| TRAIL | Eval data | 2025 | en | [Paper](<https://arxiv.org/abs/2505.08638>) · [Data](<https://huggingface.co/datasets/PatronusAI/TRAIL>) |

### Domain capability benchmarks

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| CTIBench | Benchmark | 2024 | en | [Data](<https://huggingface.co/datasets/AI4Sec/cti-bench>) |
| CyberMetric | Benchmark | 2024 | en | [Code](<https://github.com/cybermetric/CyberMetric>) |
| HealthBench | Benchmark | 2025 | en | [Data](<https://huggingface.co/datasets/openai/healthbench>) |
| LawBench | Benchmark | 2023 | zh | [Code](<https://github.com/open-compass/LawBench>) |
| SecEval | Benchmark | 2023 | en | [Code](<https://github.com/XuanwuAI/SecEval>) |

### Components of listed suites

| Resource | Type | Year reported | Language reported | Links |
| --- | --- | --- | --- | --- |
| DecodingTrust（Privacy 子集） | Component | 2023 | en | [Code](<https://github.com/AI-secure/DecodingTrust>) |
| JBB-Behaviors | Component | 2024 | en | [Data](<https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors>) |

## Maintenance

Add or update records in `data/benchmarks.json`, then run:

```powershell
python scripts/check_links.py
python scripts/apply_link_checks.py
python scripts/build_readme.py
python scripts/validate.py
```

See [contribution criteria](CONTRIBUTING.md), [taxonomy](docs/taxonomy.md), [schema](docs/schema.md) and [import report](docs/import-report.md). Unresolved identity or scope questions remain in the private maintenance data under `.local/`; source snapshots containing local paths and collector information are excluded via `.gitignore`.

# Awesome LLM & Agent Safety Benchmarks | LLM 与 Agent 安全 Benchmark

[English](README.md) · [简体中文](README.zh-CN.md)

| English | 中文 |
| --- | --- |
| A continuously updated collection of benchmarks, evaluation datasets and supporting resources for LLM and agent safety. | 持续收集 LLM 与 Agent 安全相关的 benchmark、评测数据和配套资源。 |
| The catalog covers model safety, agent safety and security, safety judging, guardrails, attack methods, training data and related research resources. | 内容覆盖模型安全、Agent 安全与安全防护、安全审查、护栏、攻击方法、训练数据及相关研究资源。 |
| Entries are organized by evaluation target and topic, with direct links to papers, code, datasets and project pages. | 条目按评测对象与主题导航，并提供论文、代码、数据和项目页面的直接链接。 |

## Catalog | 目录

## LLM Safety | LLM 安全

| Topic | Resource | Links | Type | Year | Language |
| --- | --- | --- | --- | --- | --- |
| Jailbreaks and adversarial prompts | AdvBench | [Paper](<https://arxiv.org/abs/2307.15043>) · [Code](<https://github.com/llm-attacks/llm-attacks>) | Benchmark | 2023 | en |
| Comprehensive safety | AILuminate | [Code](<https://github.com/mlcommons/ailuminate>) | Suite | 2025 | zh, en, other |
| Autonomy and alignment | Anthropic Evals | [Code](<https://github.com/anthropics/evals>) | Suite | 2022 | en |
| Privacy | ASQ-PHI | [Code](<https://github.com/JamesWeatherhead/asq-phi>) | Benchmark | 2025 | en |
| Jailbreaks and adversarial prompts | AttaQ | [Data](<https://huggingface.co/datasets/ibm-research/AttaQ>) | Benchmark | 2023 | en |
| Bias and fairness | BBQ | [Code](<https://github.com/nyu-mll/BBQ>) | Eval data | 2021 | en |
| Harmful content and toxicity | BeaverTails | [Project](<https://sites.google.com/view/pku-beavertails>) | Eval data | 2023 | zh, en |
| Prompt injection and instruction boundaries | BIPIA | [Paper](<https://arxiv.org/abs/2312.14197>) · [Code](<https://github.com/microsoft/BIPIA>) | Benchmark | KDD 2025 | en |
| Bias and fairness | BOLD | [Code](<https://github.com/amazon-science/bold>) | Eval data | 2021 | en |
| Bias and fairness | CDIAL-BIAS | [Code](<https://github.com/para-zhou/CDial-Bias>) · [Paper](<https://arxiv.org/abs/2202.08011>) | Eval data | 2022 | zh |
| Comprehensive safety | Ch3Ef | [Paper](<https://arxiv.org/abs/2403.17830>) | Suite | 2024 | en |
| Harmful content and toxicity | ChineseSafe | [Data](<https://huggingface.co/datasets/SUSTech/ChineseSafe>) | Eval data | 2024 | zh |
| Comprehensive safety | CHiSafetyBench | [Code](<https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench>) | Suite | 2024 | zh |
| Values, ethics and cultural norms | CMoralEval | [Code](<https://github.com/tjunlp-lab/CMoralEval>) | Benchmark | 2024 | zh |
| Harmful content and toxicity | COLD | [Code](<https://github.com/thu-coai/COLDataset>) · [Paper](<https://arxiv.org/abs/2201.06025>) | Eval data | 2022 | zh |
| Privacy | ConfAIde | [Code](<https://github.com/skywalker023/confaide/tree/main>) | Benchmark | 2024 | en |
| Jailbreaks and adversarial prompts | CoSafe | [Code](<https://github.com/ErxinYu/CoSafe-Dataset>) | Benchmark | 2024 | en |
| Harmful content and toxicity | CREHate | [Code](<https://github.com/nlee0212/CREHate>) | Eval data | 2024 | en, other |
| Autonomy and alignment | CRiskEval | [Code](<https://github.com/tjunlp-lab/CRiskEval>) | Suite | 2025 | zh |
| Values, ethics and cultural norms | CValues | [Code](<https://github.com/X-PLUG/CValues>) · [Paper](<https://arxiv.org/abs/2307.09705>) · [Data](<https://modelscope.cn/datasets/damo/CValues-Comparison/summary>) | Benchmark | — | zh |
| Domain risks | CyberSecEval 1/2/3 (Purple Llama) | [Code](<https://github.com/meta-llama/PurpleLlama>) | Benchmark | 2023 | en |
| Values, ethics and cultural norms | DailyDilemmas | [Project](<https://huggingface.co/datasets/kellycyy/daily_dilemmas>) | Benchmark | 2024 | en |
| Comprehensive safety | DecodingTrust | [Data](<https://huggingface.co/datasets/AI-Secure/DecodingTrust>) | Suite | 2024 | en |
| Harmful content and toxicity | DICES | [Paper](<https://arxiv.org/abs/2306.11247>) | Eval data | 2023 | en |
| Harmful content and toxicity | Do-Not-Answer | [Code](<https://github.com/libr-ai/do-not-answer>) | Eval data | 2024 | zh, en |
| Harmful content and toxicity | DynaHate | [Code](<https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset>) | Eval data | 2021 | en |
| Values, ethics and cultural norms | ETHICS | [Code](<https://github.com/hendrycks/ethics>) | Benchmark | 2021 | en |
| Over-refusal | FalseReject | [Data](<https://huggingface.co/datasets/AmazonScience/FalseReject>) | Benchmark | 2025 | en |
| Domain risks | FinSafetyBench | [Code](<https://github.com/sustech-nlp/FinSafetyBench>) | Benchmark | 2026 | zh, en |
| Comprehensive safety | Flames | [Code](<https://github.com/AI45Lab/Flames>) | Suite | 2023 | zh |
| Comprehensive safety | ForesightSafety Bench | [Code](<https://github.com/Beijing-AISI/ForesightSafety-Bench>) | Suite | 2026 | en |
| Values, ethics and cultural norms | GlobalOpinionQA | [Data](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>) | Benchmark | 2023 | en, other |
| Prompt injection and instruction boundaries | HackAPrompt | [Data](<https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset>) | Benchmark | 2023 | 英文(含少量多语言混淆) |
| Jailbreaks and adversarial prompts | HarmBench | [Paper](<https://arxiv.org/abs/2402.04249>) · [Code](<https://github.com/centerforaisafety/HarmBench>) | Benchmark | 2024 | en |
| Harmful content and toxicity | hate_speech_offensive | [Data](<https://huggingface.co/datasets/tdavidson/hate_speech_offensive>) | Eval data | 2017 | en |
| Harmful content and toxicity | HateCheck | [Code](<https://github.com/paul-rottger/hatecheck-data>) | Eval data | 2021 | en |
| Bias and fairness | HolisticBias | [Paper](<https://arxiv.org/abs/2205.09209>) | Eval data | 2022 | en |
| Bias and fairness | HONEST | [Paper](<https://aclanthology.org/2021.naacl-main.191/>) | Eval data | 2021 | other |
| Prompt injection and instruction boundaries | IHEval | [Code](<https://github.com/ytyz1307zzh/IHEval>) | Benchmark | 2025 | en |
| Harmful content and toxicity | Implicit Hate Corpus | [Code](<https://github.com/SALT-NLP/implicit-hate>) | Eval data | 2021 | en |
| Jailbreaks and adversarial prompts | In-the-Wild Jailbreak Prompts (jailbreak_llms) | [Code](<https://github.com/verazuo/jailbreak_llms>) | Benchmark | 2024 | en |
| Comprehensive safety | JailBench | [Code](<https://github.com/STAIR-BUPT/JailBench>) | Suite | 2025 | zh |
| Jailbreaks and adversarial prompts | JailbreakBench | [Paper](<https://arxiv.org/abs/2404.01318>) · [Code](<https://github.com/JailbreakBench/jailbreakbench>) | Benchmark | 2024 | en |
| Jailbreaks and adversarial prompts | JailBreakV-28k | [Data](<https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k>) | Benchmark | 2024 | en |
| Values, ethics and cultural norms | KorNAT | [Data](<https://huggingface.co/datasets/jiyounglee0523/KorNAT>) | Benchmark | 2024 | other |
| Privacy | LM_PersonalInfoLeak | [Code](<https://github.com/jeffhj/LM_PersonalInfoLeak>) | Benchmark | 2022 | en |
| Comprehensive safety | LongSafety | [Code](<https://github.com/thu-coai/LongSafety>) | Suite | 2025 | en |
| Jailbreaks and adversarial prompts | MaliciousInstruct | [Code](<https://github.com/Princeton-SysML/Jailbreak_LLM>) | Benchmark | 2023 | en |
| Harmful content and toxicity | Measuring Hate Speech | [Data](<https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech>) | Eval data | 2022 | en |
| Values, ethics and cultural norms | MedEthicEval | [Code](<https://github.com/X-LANCE/MedEthicEval>) | Benchmark | 2025 | zh |
| Domain risks | MedSafetyBench | [Code](<https://github.com/AI4LIFE-GROUP/med-safety-bench>) | Benchmark | 2024 | en |
| Jailbreaks and adversarial prompts | MHJ (Multi-Turn Human Jailbreaks) | [Data](<https://huggingface.co/datasets/ScaleAI/mhj>) | Benchmark | 2024 | en |
| Harmful content and toxicity | moderation-api-release | [Code](<https://github.com/openai/moderation-api-release/tree/main>) | Eval data | 2022 | en |
| Values, ethics and cultural norms | Moral Stories | [Code](<https://github.com/demelin/moral_stories>) | Benchmark | 2021 | en |
| Values, ethics and cultural norms | MoralBench | [Project](<https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7>) | Benchmark | 2024 | en |
| Jailbreaks and adversarial prompts | MultiBreak | [Paper](<https://arxiv.org/abs/2605.01687>) | Benchmark | 2026 | en |
| Jailbreaks and adversarial prompts | MultiJail | [Data](<https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail>) | Benchmark | 2024 | en, other |
| Harmful content and toxicity | Multilingual HateCheck (MHC) | [Code](<https://github.com/rewire-online/multilingual-hatecheck>) | Eval data | 2022 | other |
| Privacy | MultiPriv | [Code](<https://github.com/CyberChangAn/MultiPriv-PII>) | Benchmark | 2025 | zh, en |
| Autonomy and alignment | Myopia_reward | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | Suite | 2022 | zh |
| Values, ethics and cultural norms | NormAd | [Code](<https://github.com/Akhila-Yerukola/NormAd>) | Benchmark | 2024 | en |
| Autonomy and alignment | One-box Tendency | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | Suite | 2022 | zh |
| Prompt injection and instruction boundaries | Open-Prompt-Injection | [Code](<https://github.com/liu00222/Open-Prompt-Injection>) | Benchmark | 2024 | en |
| Prompt injection and instruction boundaries | OpenAI IH-Challenge | [Project](<https://openai.com/index/instruction-hierarchy-challenge/>) | Benchmark | 2025 | en |
| Values, ethics and cultural norms | OpinionQA | [Code](<https://github.com/tatsu-lab/opinions_qa>) | Benchmark | 2023 | en |
| Over-refusal | OR-Bench | [Code](<https://github.com/justincui03/or-bench>) | Benchmark | 2024 | en |
| Jailbreaks and adversarial prompts | PAP (Persuasive Adversarial Prompts) | [Data](<https://huggingface.co/datasets/CHATS-Lab/Persuasive-Jailbreaker-Data>) | Benchmark | 2024 | en |
| Over-refusal | PHTest | [Code](<https://github.com/umd-huang-lab/FalseRefusal>) | Benchmark | 2024 | en |
| Autonomy and alignment | Power-seeking | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | Suite | 2022 | zh |
| Privacy | PrivacyBench | [Code](<https://github.com/sri-ja/privacy-bench>) · [Paper](<https://arxiv.org/abs/2512.24848>) | Benchmark | 2025 | en |
| Prompt injection and instruction boundaries | PromptInject | [Code](<https://github.com/agencyenterprise/PromptInject>) | Benchmark | 2022 | en |
| Harmful content and toxicity | ProsocialDialog | [Code](<https://github.com/skywalker023/prosocial-dialog>) | Eval data | 2022 | en |
| Privacy | PUPA | [Data](<https://huggingface.co/datasets/Columbia-NLP/PUPA>) | Benchmark | 2024 | en |
| Over-refusal | RASS / MoRBench | [Code](<https://github.com/Master-PLC/RASS>) | Benchmark | 2025 | other |
| Harmful content and toxicity | RealToxicityPrompts | [Code](<https://github.com/allenai/real-toxicity-prompts>) | Eval data | 2020 | en |
| Harmful content and toxicity | RTP-LX | [Code](<https://github.com/microsoft/RTP-LX>) | Eval data | 2024 | zh, en, other |
| Jailbreaks and adversarial prompts | SafeDialBench | [Code](<https://github.com/drivetosouth/SafeDialBench-Dataset>) | Benchmark | 2025 | zh, en |
| Domain risks | SafeSci | [Code](<https://github.com/yangyangyang127/SafeSci>) | Benchmark | 2026 | en |
| Harmful content and toxicity | Safety-Prompts | [Code](<https://github.com/thu-coai/Safety-Prompts>) | Eval data | 2023 | zh |
| Comprehensive safety | SafetyBench | [Code](<https://github.com/thu-coai/SafetyBench>) | Suite | 2024 | zh, en |
| Comprehensive safety | SALAD-Bench | [Project](<https://adwardlee.github.io/salad_bench/>) | Suite | 2024 | en |
| Domain risks | SciSafeEval | [Paper](<https://arxiv.org/abs/2410.03769>) | Benchmark | 2024 | en |
| Autonomy and alignment | Self-awareness | [Code](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [Paper](<https://arxiv.org/abs/2212.09251>) | Suite | 2022 | zh |
| Harmful content and toxicity | SGHateCheck | [Code](<https://github.com/Social-AI-Studio/SGHateCheck>) | Eval data | 2024 | other |
| Bias and fairness | Social Bias Frames (SBIC) | [Data](<https://huggingface.co/datasets/allenai/social_bias_frames>) | Eval data | 2020 | en |
| Bias and fairness | SocialStigmaQA | [Data](<https://huggingface.co/datasets/ibm-research/SocialStigmaQA>) | Eval data | 2023 | en |
| Harmful content and toxicity | SORRY-Bench | [Code](<https://github.com/SORRY-Bench/sorry-bench>) | Eval data | 2024 | en |
| Bias and fairness | StereoSet | [Code](<https://github.com/moinnadeem/StereoSet>) | Eval data | 2020 | en |
| Comprehensive safety | SuperCLUE-Safety | [Project](<https://www.cluebenchmarks.com/superclue_safety.html>) | Suite | 2024 | zh |
| Bias and fairness | SWSR | [Code](<https://github.com/aggiejiang/SWSR>) · [Paper](<https://arxiv.org/abs/2108.03070>) | Eval data | 2021 | zh |
| Prompt injection and instruction boundaries | Tensor Trust | [Project](<https://tensortrust.ai/paper/>) · [Code](<https://github.com/HumanCompatibleAI/tensor-trust>) | Benchmark | 2023(arXiv)/2024(ICLR) | en |
| Harmful content and toxicity | TOCP | [Project](<https://nlp.cse.ntou.edu.tw/resources/TOCP/>) · [Paper](<https://aclanthology.org/2020.trac-1.2/>) | Eval data | 2020 | zh |
| Harmful content and toxicity | ToxiCN | [Code](<https://github.com/DUT-lujunyu/ToxiCN>) | Eval data | 2023 | zh |
| Harmful content and toxicity | ToxiCN MM | [Code](<https://github.com/DUT-lujunyu/ToxiCN_MM>) | Eval data | 2024 | zh |
| Harmful content and toxicity | ToxiGen | [Code](<https://github.com/microsoft/ToxiGen>) | Eval data | 2022 | en |
| Comprehensive safety | TrustLLM | [Code](<https://github.com/HowieHwong/TrustLLM>) | Suite | 2024 | en |
| Harmful content and toxicity | TUMCC | [Code](<https://github.com/m1-llie/TUMCC>) · [Paper](<https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X>) | Eval data | 2020 | zh |
| Comprehensive safety | U-SafeBench | [Code](<https://github.com/yeonjun-in/U-SafeBench>) | Suite | 2025 | en |
| Values, ethics and cultural norms | ValueBench | [Code](<https://github.com/ValueByte-AI/ValueBench>) | Benchmark | 2024 | en |
| Domain risks | WMDP | [Data](<https://huggingface.co/datasets/cais/wmdp>) | Benchmark | 2024 | en |
| Values, ethics and cultural norms | WorldValuesBench | [Code](<https://github.com/Demon702/WorldValuesBench>) | Benchmark | 2024 | en |
| Over-refusal | XSTest | [Code](<https://github.com/paul-rottger/xstest>) | Benchmark | 2023 | en |

## Agent Safety & Security | Agent 安全

| Topic | Resource | Links | Type | Year | Language |
| --- | --- | --- | --- | --- | --- |
| General agent safety and misuse | Agent Security Bench (ASB) | [Paper](<https://arxiv.org/abs/2410.02644>) · [Code](<https://github.com/agiresearch/ASB>) | Benchmark | 2024/2025 | en |
| General agent safety and misuse | Agent-SafetyBench | [Paper](<https://arxiv.org/abs/2412.14470>) · [Code](<https://github.com/thu-coai/Agent-SafetyBench>) · [Data](<https://huggingface.co/datasets/thu-coai/Agent-SafetyBench>) · [Project](<https://www.semanticscholar.org/reader/7d11400eeb317ebee278f49e108226a4f8555dda>) | Benchmark | 2025 | en |
| Privacy and memory | AgentDAM | [Code](<https://github.com/facebookresearch/ai-agent-privacy>) | Benchmark | 2025 | en |
| Prompt injection and instruction boundaries | AgentDojo | [Paper](<https://arxiv.org/abs/2406.13352>) · [Code](<https://github.com/ethz-spylab/agentdojo>) | Benchmark | NeurIPS 2024 | en |
| Prompt injection and instruction boundaries | AgentDyn | [Paper](<https://arxiv.org/abs/2602.03117>) · [Code](<https://github.com/SaFo-Lab/AgentDyn>) | Benchmark | 2026 | en |
| General agent safety and misuse | AgentHarm | [Paper](<https://arxiv.org/abs/2410.09024>) · [Data](<https://huggingface.co/datasets/ai-safety-institute/AgentHarm>) · [Project](<https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/>) | Benchmark | ICLR 2025 | en |
| Web, computer and mobile agents | AgentHazard | [Paper](<https://arxiv.org/abs/2604.02947>) · [Code](<https://github.com/Yunhao-Feng/AgentHazard>) · [Project](<https://yunhao-feng.github.io/AgentHazard/>) | Benchmark | 2026 | en |
| Prompt injection and instruction boundaries | AgentLAB | [Paper](<https://arxiv.org/abs/2602.16901>) · [Project](<https://tanqiujiang.github.io/AgentLAB_main/>) · [Code](<https://github.com/TanqiuJiang/AgentLAB>) | Benchmark | 2025 | en |
| Privacy and memory | AgentLeak | [Paper](<https://arxiv.org/abs/2602.11510>) · [Code](<https://github.com/Privatris/AgentLeak>) · [Data](<https://huggingface.co/datasets/humain2/AgentLeak>) | Benchmark | 2026 | en |
| Web, computer and mobile agents | CUAHarm | [Paper](<https://arxiv.org/abs/2508.00935>) · [Code](<https://github.com/db-ol/CUAHarm>) · [Data](<https://huggingface.co/datasets/CUAHarm/CUAHarm>) | Benchmark | 2025 | en |
| General agent safety and misuse | Echoes of Human Malice | [Paper](<https://arxiv.org/abs/2510.14207>) | Benchmark | 2025 | en |
| General agent safety and misuse | HAICosystem | [Code](<https://github.com/XuhuiZhou/HAICosystem>) | Benchmark | 2024 | en |
| Prompt injection and instruction boundaries | InjecAgent | [Paper](<https://aclanthology.org/2024.findings-acl.624/>) · [Code](<https://github.com/uiuc-kang-lab/InjecAgent>) | Benchmark | 2024（ACL Findings） | en |
| Tool, API and MCP safety | MCIP | [Paper](<https://arxiv.org/abs/2505.14590>) | Benchmark | 2025 | en |
| Tool, API and MCP safety | MCP Security Bench (MSB) | [Paper](<https://arxiv.org/abs/2510.15994>) · [Code](<https://github.com/dongsenzhang/MSB>) | Benchmark | 2025 | en |
| Tool, API and MCP safety | MCP-TDP | [Paper](<https://arxiv.org/abs/2605.24069>) | Benchmark | 2026 | en |
| Tool, API and MCP safety | MCPTox | [Paper](<https://arxiv.org/abs/2508.14925>) · [Code](<https://anonymous.4open.science/r/AAAI26-7C02>) | Benchmark | 2025 | en |
| Web, computer and mobile agents | MobileSafetyBench | [Paper](<https://arxiv.org/abs/2410.17520>) · [Code](<https://github.com/jylee425/mobilesafetybench>) · [Project](<https://mobilesafetybench.github.io>) | Benchmark | 2024 | en |
| General agent safety and misuse | OpenAgentSafety | [Paper](<https://arxiv.org/abs/2507.06134>) · [Code](<https://github.com/Open-Agent-Safety/OpenAgentSafety>) · [Data](<https://huggingface.co/datasets/sani903/openagentsafety>) | Benchmark | 2025 | en |
| Privacy and memory | PrivacyLens | [Code](<https://github.com/SALT-NLP/PrivacyLens>) | Benchmark | 2024 | en |
| Tool, API and MCP safety | RAS-EVAL | [Paper](<https://arxiv.org/abs/2506.15253>) · [Code](<https://github.com/lanzer-tree/RAS-Eval>) | Benchmark | 2025 | en |
| Web, computer and mobile agents | RiOSWorld | [Paper](<https://arxiv.org/abs/2506.00618>) · [Project](<https://yjyddq.github.io/RiOSWorld.github.io/>) | Benchmark | 2025 | en |
| Web, computer and mobile agents | SABER | [Paper](<https://arxiv.org/abs/2606.01317>) · [Code](<https://github.com/sssr-lab/saber>) | Benchmark | 2026 | 中英混合, 英语为主 |
| Embodied safety | SafeAgentBench | [Paper](<https://arxiv.org/abs/2412.13178>) · [Project](<https://safeagentbench.github.io>) · [Code](<https://github.com/shengyin1224/SafeAgentBench>) | Benchmark | 2024 | en |
| Web, computer and mobile agents | SafeArena | [Code](<https://github.com/McGill-NLP/safearena>) | Benchmark | 2025 | en |
| General agent safety and misuse | SafePro | [Paper](<https://arxiv.org/abs/2601.06663>) · [Code](<https://github.com/UCSB-AI/SafePro>) · [Project](<https://safeprobench.github.io/safepro/>) · [Data](<https://huggingface.co/datasets/kzhou35/SafePro>) | Benchmark | 2026 | en |
| Web, computer and mobile agents | ST-WebAgentBench | [Paper](<https://arxiv.org/abs/2410.06703>) · [Project](<https://sites.google.com/view/st-webagentbench/home>) · [Data](<https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench>) · [Code](<https://github.com/segev-shlomov/ST-WebAgentBench>) | Benchmark | 2026 | en |
| Tool, API and MCP safety | ToolEmu | [Paper](<https://arxiv.org/abs/2309.15817>) · [Code](<https://github.com/ryoungj/ToolEmu>) | Benchmark | 2023/ICLR 2024 | en |
| Tool, API and MCP safety | ToolSword | [Code](<https://github.com/Junjie-Ye/ToolSword>) | Benchmark | 2024 | en |
| Web, computer and mobile agents | WASP | [Paper](<https://arxiv.org/abs/2504.18575>) · [Code](<https://github.com/facebookresearch/wasp>) | Benchmark | 2025 | en |

## Safety Judging & Guardrails | 安全审查与护栏

| Topic | Resource | Links | Type | Year | Language |
| --- | --- | --- | --- | --- | --- |
| Agent trajectories and action safety | ATBench | [Paper](<https://arxiv.org/abs/2604.02022>) · [Code](<https://github.com/LiYu0524/ATbench>) · [Data](<https://huggingface.co/datasets/AI45Research/ATBench>) | Eval data | 2026 | en |
| Content guardrail evaluation | GuardBench | [Code](<https://github.com/AmenRa/guardbench>) | Suite | 2024 | en |
| Agent trajectories and action safety | PhoneSafety | [Paper](<https://arxiv.org/abs/2605.07630>) · [Code](<https://github.com/tangzhy/PhoneSafety>) · [Data](<https://huggingface.co/datasets/phonesafety-anon/PhoneSafety_Data>) | Eval data | 2025 | 中文为主 |
| Agent trajectories and action safety | R-Judge | [Paper](<https://arxiv.org/abs/2401.10019>) · [Code](<https://github.com/Lordog/R-Judge>) | Eval data | 2024 | en |
| Agent trajectories and action safety | SafeToolBench | [Paper](<https://aclanthology.org/2025.findings-emnlp.958.pdf>) · [Code](<https://github.com/BITHLP/SafeToolBench>) | Eval data | 2025 | en |
| Agent trajectories and action safety | SleightBench | [Paper](<https://arxiv.org/abs/2605.16626>) · [Code](<https://github.com/safety-research/sleight-bench>) | Eval data | 2025 | en |
| Agent trajectories and action safety | ToolSafe / TS-Bench | [Paper](<https://arxiv.org/abs/2601.10156>) · [Code](<https://github.com/MurrayTom/ToolSafe>) | Eval data | 2026 | en |
| Agent trajectories and action safety | TOP-Bench | [Paper](<https://arxiv.org/abs/2512.16310>) · [Code](<https://github.com/1Ponder/TOP-R>) · [Project](<https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082>) | Eval data | 2026 | en |
| Agent trajectories and action safety | TraceSafe-Bench | [Paper](<https://arxiv.org/abs/2604.07223>) · [Code](<https://github.com/cycraft-corp/TraceSafe>) · [Data](<https://huggingface.co/datasets/CyCraftAI/TraceSafe>) | Eval data | 2026 | en |
| Agent trajectories and action safety | WebGuard | [Code](<https://github.com/OSU-NLP-Group/WebGuard>) | Eval data | 2025 | en |
| Content guardrail evaluation | WildGuard (WildGuardMix/WildGuardTest) | [Data](<https://huggingface.co/datasets/allenai/wildguardmix>) | Suite | 2024 | en |

## Related Resources | 相关资源

| Topic | Resource | Links | Type | Year | Language |
| --- | --- | --- | --- | --- | --- |
| Training datasets | Aegis 1.0 (Nemotron Content Safety Dataset V1) | [Data](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0>) | Train data | 2024 | en |
| Capability baselines and environments | Agent-Diff | [Paper](<https://arxiv.org/abs/2602.11224>) · [Code](<https://github.com/agent-diff-bench/agent-diff>) · [Project](<https://www.agentdiff.dev>) · [Data](<https://huggingface.co/datasets/hubertmarek/agent-diff-bench>) | Benchmark | 2026 | en |
| Frameworks and mixed resources | AgentDefense-Bench | [Code](<https://github.com/arunsanna/AgentDefense-Bench>) | Framework | 2025 | en |
| Attack methods | AgentPoison | [Paper](<https://arxiv.org/abs/2407.12784>) · [Code](<https://github.com/AI-secure/AgentPoison>) · [Project](<https://billchan226.github.io/AgentPoison.html>) | Method | 2024 | en |
| Capability baselines and environments | API-Bank | [Paper](<https://arxiv.org/abs/2304.08244>) | Benchmark | EMNLP 2023 | en |
| Capability baselines and environments | AppWorld | [Paper](<https://aclanthology.org/2024.acl-long.850/>) · [Code](<https://github.com/StonyBrookNLP/appworld>) · [Project](<https://appworld.dev>) | Benchmark | ACL 2024 | en |
| Attack methods | ArtPrompt | [Code](<https://github.com/uw-nsl/ArtPrompt>) | Method | 2024 | en |
| Attack methods | AutoDAN | [Code](<https://github.com/SheltonLiu-N/AutoDAN>) | Method | 2024 | en |
| Attack methods | Automating Deception（FITD多轮越狱） | [Paper](<https://arxiv.org/abs/2511.19517>) | Method | 2025 | en |
| Capability baselines and environments | BFCL | [Paper](<https://proceedings.mlr.press/v267/patil25a.html>) · [Project](<https://gorilla.cs.berkeley.edu/leaderboard.html>) · [Data](<https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard>) | Benchmark | 2024/2025，持续更新至 V4 | 英语为主, 多语言函数调用场景 |
| Frameworks and mixed resources | CC-BOS | [Code](<https://github.com/xaoLiu1222/cc-bos>) | Framework | 2026 | zh |
| Attack methods | CipherChat | [Code](<https://github.com/RobustNLP/CipherChat>) | Method | 2024 | zh, en |
| Attack methods | CodeChameleon | [Code](<https://github.com/huizhang-L/CodeChameleon>) | Method | 2024 | en |
| Attack methods | Crescendo | [Paper](<https://arxiv.org/abs/2404.01833>) | Method | 2024 | en |
| Domain capability benchmarks | CTIBench | [Data](<https://huggingface.co/datasets/AI4Sec/cti-bench>) | Benchmark | 2024 | en |
| Attack methods | Curiosity-driven Red Teaming | [Code](<https://github.com/Improbable-AI/curiosity_redteam>) | Method | 2024 | en |
| Domain capability benchmarks | CyberMetric | [Code](<https://github.com/cybermetric/CyberMetric>) | Benchmark | 2024 | en |
| Components of listed suites | DecodingTrust（Privacy 子集） | [Code](<https://github.com/AI-secure/DecodingTrust>) | Component | 2023 | en |
| Attack methods | DeepInception | [Code](<https://github.com/tmlr-group/DeepInception>) | Method | 2023 | en |
| Attack methods | GPTFuzzer | [Code](<https://github.com/hubertyoo/GPTFuzz>) | Method | 2023 | en |
| Training datasets | GuardReasoner (GuardReasonerTrain) | [Data](<https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain>) | Train data | 2025 | en |
| Factuality and general trace diagnostics | HaluEval | [Paper](<https://arxiv.org/abs/2305.11747>) · [Code](<https://github.com/RUCAIBox/HaluEval>) | Eval data | 2023 | en |
| Training datasets | HarmfulQA (RED-INSTRUCT) | [Data](<https://huggingface.co/datasets/TrustAIRLab/HarmfulQA>) | Train data | 2023 | en |
| Domain capability benchmarks | HealthBench | [Data](<https://huggingface.co/datasets/openai/healthbench>) | Benchmark | 2025 | en |
| Training datasets | HH-RLHF（含Red Team Attempts） | [Code](<https://github.com/anthropics/hh-rlhf>) | Train data | 2022 | en |
| Components of listed suites | JBB-Behaviors | [Data](<https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors>) | Component | 2024 | en |
| Attack methods | Latent Jailbreak | [Code](<https://github.com/qiuhuachuan/latent-jailbreak>) | Method | 2023 | 英文+中文 |
| Domain capability benchmarks | LawBench | [Code](<https://github.com/open-compass/LawBench>) | Benchmark | 2023 | zh |
| Frameworks and mixed resources | LiveSecBench | [Code](<https://github.com/ydli-ai/LiveSecBench>) | Framework | 2026 | zh |
| Attack challenges and data | LLMail-Inject | [Paper](<https://arxiv.org/abs/2506.09956>) · [Code](<https://github.com/microsoft/llmail-inject-challenge>) | Eval data | 2025 | en |
| Attack methods | MART | [Paper](<https://arxiv.org/abs/2311.07689>) | Method | 2023 | en |
| Attack methods | MemoryGraft | [Paper](<https://arxiv.org/abs/2512.16962>) · [Code](<https://github.com/Jacobhhy/MemoryGraft>) · [Project](<https://www.semanticscholar.org/reader/b1d80b2eda7e175e235185bdc7df4e8233f36ef4>) | Method | 2025 | en |
| Training datasets | Nemotron Content Safety Dataset V2 | [Data](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0>) | Train data | 2025 | en |
| Training datasets | NVIDIA Nemotron Agentic IPI | [Data](<https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1>) | Train data | 2026 | en |
| Frameworks and mixed resources | ORFuzz | [Paper](<https://arxiv.org/abs/2508.11222>) | Framework | 2025 | en |
| Training datasets | PKU-SafeRLHF (10K/30K) | [Data](<https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K>) | Train data | 2023 | en |
| Attack methods | PsychJail | [Code](<https://github.com/FengZeyugit/PsychJail>) | Method | 2026 | en |
| Factuality and general trace diagnostics | RAGTruth | [Paper](<https://arxiv.org/abs/2401.00396>) | Eval data | 2023 | en |
| Attack methods | ReNeLLM | [Code](<https://github.com/NJUNLP/ReNeLLM>) | Method | 2024 | en |
| Training datasets | SafeMTData（Derail Yourself/ActorAttack配套） | [Data](<https://huggingface.co/datasets/SafeMTData/SafeMTData>) | Train data | 2024 | en |
| Domain capability benchmarks | SecEval | [Code](<https://github.com/XuanwuAI/SecEval>) | Benchmark | 2023 | en |
| Frameworks and mixed resources | ShieldLM | [Code](<https://github.com/thu-coai/ShieldLM>) | Framework | 2024 | zh, en |
| Factuality and general trace diagnostics | SimpleQA | [Paper](<https://arxiv.org/abs/2411.04368>) · [Code](<https://github.com/openai/simple-evals>) | Eval data | 2024 | en |
| Capability baselines and environments | SkillsBench | [Paper](<https://arxiv.org/abs/2602.12670>) · [Project](<https://www.skillsbench.ai>) · [Code](<https://github.com/benchflow-ai/skillsbench>) | Benchmark | 2026 | en |
| Capability baselines and environments | tau-bench | [Paper](<https://arxiv.org/abs/2406.12045>) · [Code](<https://github.com/sierra-research/tau-bench>) · [Project](<https://www.semanticscholar.org/reader/70aa016c1f68fd5c0261f26ad20017b8307650af>) | Benchmark | 2024 | en |
| Capability baselines and environments | TheAgentCompany | [Paper](<https://arxiv.org/abs/2412.14161>) · [Code](<https://github.com/TheAgentCompany/TheAgentCompany>) · [Project](<https://the-agent-company.com>) | Benchmark | 2024/2025 | en |
| Capability baselines and environments | TOOLATHLON | [Paper](<https://arxiv.org/abs/2510.25726>) · [Code](<https://github.com/hkust-nlp/Toolathlon>) | Benchmark | 2026 | en |
| Training datasets | ToolSafety | [Paper](<https://aclanthology.org/2025.emnlp-main.714.pdf>) · [Data](<https://huggingface.co/datasets/jinjinyien/ToolSafety>) | Train data | EMNLP 2025 | en |
| Capability baselines and environments | ToolSandbox | [Paper](<https://arxiv.org/abs/2408.04682>) · [Code](<https://github.com/apple-aiml-research/ToolSandbox>) · [Project](<https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark>) | Benchmark | 2024 | en |
| Factuality and general trace diagnostics | TraceElephant | [Paper](<https://arxiv.org/abs/2604.22708>) · [Code](<https://github.com/TraceElephant/TraceElephant>) · [Data](<https://huggingface.co/datasets/TraceElephant/TraceElephant>) | Eval data | 2026 | en |
| Factuality and general trace diagnostics | TRAIL | [Paper](<https://arxiv.org/abs/2505.08638>) · [Data](<https://huggingface.co/datasets/PatronusAI/TRAIL>) | Eval data | 2025 | en |
| Frameworks and mixed resources | TrustAgent | [Paper](<https://arxiv.org/abs/2402.01586>) | Framework | 2024 | en |
| Capability baselines and environments | WebArena | [Paper](<https://arxiv.org/abs/2307.13854>) · [Code](<https://github.com/web-arena-x/webarena>) · [Project](<https://webarena.dev>) | Benchmark | ICLR 2024 / NeurIPS 2024 Oral 相关项目口径 | en |
| Frameworks and mixed resources | WILDTEAMING / WildJailbreak | [Code](<https://github.com/allenai/wildteaming>) | Framework | 2024 | en |
| Capability baselines and environments | WorkArena | [Paper](<https://arxiv.org/abs/2403.07718>) · [Code](<https://github.com/ServiceNow/workarena>) · [Project](<https://servicenow.github.io/WorkArena/>) | Benchmark | ICML 2024 | en |
| Training datasets | X-Teaming Evolutionary M2S | [Data](<https://huggingface.co/datasets/hyunjun1121/X-Teaming_Evolutionary_M2S>) | Train data | 2025 | en |
| Training datasets | XGuard-Train-Open-200K | [Data](<https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K>) | Train data | 2026 | other |
| Training datasets | XGuard-Train（X-Teaming配套） | [Data](<https://huggingface.co/datasets/marslabucla/XGuard-Train>) | Train data | 2025 | en |

# Awesome LLM & Agent Safety Benchmarks

[English](README.md) · [简体中文](README.zh-CN.md)

本项目持续收集 LLM 与 Agent 安全相关 benchmark、评测数据和配套资源，按评测对象与主题整理。

更新日期 2026-10-14：从 5 份原始来源中整理出 **212 个目录条目**，其中安全收录 143 项、相关资源 58 项、待核验 11 项。

**链接检查（2026-10-14）：**检查 321 个不同网址，317 个可访问或正常跳转、2 个返回 404/410、1 个访问受限、1 个服务器错误；另跳过 3 个占位或误归属网址。详见[检查报告](docs/link-check-report.md)。

## 目录

- [LLM 安全](#llm-安全)
- [Agent 安全](#agent-安全)
- [安全审查与护栏](#安全审查与护栏)
- [相关资源](#相关资源)

## LLM 安全

### 综合安全

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AILuminate | — | 基准套件 | 2025 | zh, en, other | [代码](<https://github.com/mlcommons/ailuminate>) |
| Ch3Ef | HHH（helpful/honest/harmless）对齐12域46任务 | 基准套件 | 2024 | en | [论文](<https://arxiv.org/abs/2403.17830>) |
| CHiSafetyBench | 风险识别与拒绝 | 基准套件 | 2024 | zh | [代码](<https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench>) |
| DecodingTrust | 训练数据泄露 | 基准套件 | 2024 | en | [数据](<https://huggingface.co/datasets/AI-Secure/DecodingTrust>) |
| Flames | 中文价值对齐（安全、公平、道德、数据保护、合法性） | 基准套件 | 2023 | zh | [代码](<https://github.com/AI45Lab/Flames>) |
| ForesightSafety Bench | — | 基准套件 | 2026 | en | [代码](<https://github.com/Beijing-AISI/ForesightSafety-Bench>) |
| JailBench | — | 基准套件 | 2025 | zh | [代码](<https://github.com/STAIR-BUPT/JailBench>) |
| LongSafety | 长上下文开放任务安全 | 基准套件 | 2025 | en | [代码](<https://github.com/thu-coai/LongSafety>) |
| SafetyBench | — | 基准套件 | 2024 | zh, en | [代码](<https://github.com/thu-coai/SafetyBench>) |
| SALAD-Bench | — | 基准套件 | 2024 | en | [项目](<https://adwardlee.github.io/salad_bench/>) |
| SuperCLUE-Safety | — | 基准套件 | 2024 | zh | [项目](<https://www.cluebenchmarks.com/superclue_safety.html>) |
| TrustLLM | 可信性六维综合评测（真实性/安全/公平/鲁棒/隐私/机器伦理） | 基准套件 | 2024 | en | [代码](<https://github.com/HowieHwong/TrustLLM>) |
| U-SafeBench | 用户特定安全标准评测 | 基准套件 | 2025 | en | [代码](<https://github.com/yeonjun-in/U-SafeBench>) |

### 有害内容与毒性

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| BeaverTails | — | 评测数据 | 2023 | zh, en | [项目](<https://sites.google.com/view/pku-beavertails>) |
| ChineseSafe | 政治敏感/色情/暴恐/变体谐音规避（4大类10小类） | 评测数据 | 2024 | zh | [数据](<https://huggingface.co/datasets/SUSTech/ChineseSafe>) |
| COLD | 伤害类型8：攻击性与有害表达风险 | 评测数据 | 2022 | zh | [代码](<https://github.com/thu-coai/COLDataset>) · [论文](<https://arxiv.org/abs/2201.06025>) |
| CREHate | 仇恨言论（跨文化标注差异） | 评测数据 | 2024 | en, other | [代码](<https://github.com/nlee0212/CREHate>) |
| DICES | 带评分者人口统计多样性的对话安全标注 | 评测数据 | 2023 | en | [论文](<https://arxiv.org/abs/2306.11247>) |
| Do-Not-Answer | — | 评测数据 | 2024 | zh, en | [代码](<https://github.com/libr-ai/do-not-answer>) |
| DynaHate | 仇恨言论（对抗动态生成） | 评测数据 | 2021 | en | [代码](<https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset>) |
| hate_speech_offensive | 仇恨言论 | 评测数据 | 2017 | en | [数据](<https://huggingface.co/datasets/tdavidson/hate_speech_offensive>) |
| HateCheck | 仇恨言论功能性诊断测试（29项功能） | 评测数据 | 2021 | en | [代码](<https://github.com/paul-rottger/hatecheck-data>) |
| Implicit Hate Corpus | 仇恨言论（隐性仇恨） | 评测数据 | 2021 | en | [代码](<https://github.com/SALT-NLP/implicit-hate>) |
| Measuring Hate Speech | 仇恨言论（连续hate score） | 评测数据 | 2022 | en | [数据](<https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech>) |
| moderation-api-release | — | 评测数据 | 2022 | en | [代码](<https://github.com/openai/moderation-api-release/tree/main>) |
| Multilingual HateCheck (MHC) | 仇恨言论（多语言功能性测试） | 评测数据 | 2022 | other | [代码](<https://github.com/rewire-online/multilingual-hatecheck>) |
| ProsocialDialog | 亲社会回应/社会规范引导（rules-of-thought） | 评测数据 | 2022 | en | [代码](<https://github.com/skywalker023/prosocial-dialog>) |
| RealToxicityPrompts | 自然网页语料的毒性触发补全 | 评测数据 | 2020 | en | [代码](<https://github.com/allenai/real-toxicity-prompts>) |
| RTP-LX | — | 评测数据 | 2024 | zh, en, other | [代码](<https://github.com/microsoft/RTP-LX>) |
| Safety-Prompts | 7类典型安全场景+6类指令攻击 | 评测数据 | 2023 | zh | [代码](<https://github.com/thu-coai/Safety-Prompts>) |
| SGHateCheck | 仇恨言论（新加坡低资源语言功能性测试） | 评测数据 | 2024 | other | [代码](<https://github.com/Social-AI-Studio/SGHateCheck>) |
| SORRY-Bench | — | 评测数据 | 2024 | en | [代码](<https://github.com/SORRY-Bench/sorry-bench>) |
| TOCP | 伤害类型8：攻击性与有害表达风险 | 评测数据 | 2020 | zh | [项目](<https://nlp.cse.ntou.edu.tw/resources/TOCP/>) · [论文](<https://aclanthology.org/2020.trac-1.2/>) |
| ToxiCN | 仇恨言论/毒性（中文细粒度） | 评测数据 | 2023 | zh | [代码](<https://github.com/DUT-lujunyu/ToxiCN>) |
| ToxiCN MM | 有害迷因（多模态中文） | 评测数据 | 2024 | zh | [代码](<https://github.com/DUT-lujunyu/ToxiCN_MM>) |
| ToxiGen | 仇恨言论（13个少数群体隐性毒性） | 评测数据 | 2022 | en | [代码](<https://github.com/microsoft/ToxiGen>) |
| TUMCC | — | 评测数据 | 2020 | zh | [代码](<https://github.com/m1-llie/TUMCC>) · [论文](<https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X>) |

### 越狱与对抗提示

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AdvBench | 有害请求与越狱 | 基准 | 2023 | en | [论文](<https://arxiv.org/abs/2307.15043>) · [代码](<https://github.com/llm-attacks/llm-attacks>) |
| AttaQ | 对抗性问题有害响应倾向 | 基准 | 2023 | en | [数据](<https://huggingface.co/datasets/ibm-research/AttaQ>) |
| CoSafe | 多轮对话指代消解安全攻击 | 基准 | 2024 | en | [代码](<https://github.com/ErxinYu/CoSafe-Dataset>) |
| HarmBench | 有害行为与越狱 | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2402.04249>) · [代码](<https://github.com/centerforaisafety/HarmBench>) |
| In-the-Wild Jailbreak Prompts (jailbreak_llms) | 野外真实越狱提示库 | 基准 | 2024 | en | [代码](<https://github.com/verazuo/jailbreak_llms>) |
| JailbreakBench | 越狱攻击与拒绝 | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2404.01318>) · [代码](<https://github.com/JailbreakBench/jailbreakbench>) |
| JailBreakV-28k | Jailbreak攻击 | 基准 | 2024 | en | [数据](<https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k>) |
| MaliciousInstruct | 越狱攻击/恶意指令 | 基准 | 2023 | en | [代码](<https://github.com/Princeton-SysML/Jailbreak_LLM>) |
| MHJ (Multi-Turn Human Jailbreaks) | 人类红队真实多轮越狱 | 基准 | 2024 | en | [数据](<https://huggingface.co/datasets/ScaleAI/mhj>) |
| MultiBreak | 大规模多样化多轮越狱 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2605.01687>) |
| MultiJail | 多语言越狱 | 基准 | 2024 | en, other | [数据](<https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail>) |
| PAP (Persuasive Adversarial Prompts) | 说服式越狱 | 基准 | 2024 | en | [数据](<https://huggingface.co/datasets/CHATS-Lab/Persuasive-Jailbreaker-Data>) |
| SafeDialBench | 多轮越狱对话细粒度安全评测 | 基准 | 2025 | zh, en | [代码](<https://github.com/drivetosouth/SafeDialBench-Dataset>) |

### 提示注入与指令边界

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| BIPIA | 间接提示注入 | 基准 | KDD 2025 | en | [论文](<https://arxiv.org/abs/2312.14197>) · [代码](<https://github.com/microsoft/BIPIA>) |
| HackAPrompt | 提示攻击与越狱 | 基准 | 2023 | 英文(含少量多语言混淆) | [数据](<https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset>) |
| IHEval | Instruction hierarchy | 基准 | 2025 | en | [代码](<https://github.com/ytyz1307zzh/IHEval>) |
| Open-Prompt-Injection | Prompt injection | 基准 | 2024 | en | [代码](<https://github.com/liu00222/Open-Prompt-Injection>) |
| OpenAI IH-Challenge | 指令优先级与提示注入 | 基准 | 2025 | en | [项目](<https://openai.com/index/instruction-hierarchy-challenge/>) |
| PromptInject | Prompt injection | 基准 | 2022 | en | [代码](<https://github.com/agencyenterprise/PromptInject>) |
| Tensor Trust | 直接提示注入与防御 | 基准 | 2023(arXiv)/2024(ICLR) | en | [项目](<https://tensortrust.ai/paper/>) · [代码](<https://github.com/HumanCompatibleAI/tensor-trust>) |

### 偏见与公平

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| BBQ | 群体公平与偏见风险（社会偏见问答） | 评测数据 | 2021 | en | [代码](<https://github.com/nyu-mll/BBQ>) |
| BOLD | 群体公平与偏见风险（开放生成公平性，5域43群体） | 评测数据 | 2021 | en | [代码](<https://github.com/amazon-science/bold>) |
| CDIAL-BIAS | 伤害类型7：群体公平与偏见风险 | 评测数据 | 2022 | zh | [代码](<https://github.com/para-zhou/CDial-Bias>) · [论文](<https://arxiv.org/abs/2202.08011>) |
| HolisticBias | 群体公平与偏见风险（细粒度身份描述词，13个人口学轴） | 评测数据 | 2022 | en | [论文](<https://arxiv.org/abs/2205.09209>) |
| HONEST | 群体公平与偏见风险（hurtful句子补全） | 评测数据 | 2021 | other | [论文](<https://aclanthology.org/2021.naacl-main.191/>) |
| Social Bias Frames (SBIC) | 结构性偏见与冒犯（group-offense框架） | 评测数据 | 2020 | en | [数据](<https://huggingface.co/datasets/allenai/social_bias_frames>) |
| SocialStigmaQA | 社会污名偏见放大（93个美国污名身份） | 评测数据 | 2023 | en | [数据](<https://huggingface.co/datasets/ibm-research/SocialStigmaQA>) |
| StereoSet | 刻板印象/反刻板印象/无关注续写选择 | 评测数据 | 2020 | en | [代码](<https://github.com/moinnadeem/StereoSet>) |
| SWSR | 伤害类型7：群体公平与偏见风险 | 评测数据 | 2021 | zh | [代码](<https://github.com/aggiejiang/SWSR>) · [论文](<https://arxiv.org/abs/2108.03070>) |

### 价值观、伦理与文化规范

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| CMoralEval | 价值观 | 基准 | 2024 | zh | [代码](<https://github.com/tjunlp-lab/CMoralEval>) |
| CValues | — | 基准 | — | zh | [代码](<https://github.com/X-PLUG/CValues>) · [论文](<https://arxiv.org/abs/2307.09705>) · [数据](<https://modelscope.cn/datasets/damo/CValues-Comparison/summary>) |
| DailyDilemmas | 价值观 | 基准 | 2024 | en | [项目](<https://huggingface.co/datasets/kellycyy/daily_dilemmas>) |
| ETHICS | 机器伦理/道德判断（正义、义务、美德、常识、功利主义） | 基准 | 2021 | en | [代码](<https://github.com/hendrycks/ethics>) |
| GlobalOpinionQA | 价值观对齐（跨国全球观点代表性） | 基准 | 2023 | en, other | [数据](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>) |
| KorNAT | 价值观 | 基准 | 2024 | other | [数据](<https://huggingface.co/datasets/jiyounglee0523/KorNAT>) |
| MedEthicEval | 价值观 | 基准 | 2025 | zh | [代码](<https://github.com/X-LANCE/MedEthicEval>) |
| Moral Stories | 价值观/社会规范情境推理（规范-意图-情境-行动-后果） | 基准 | 2021 | en | [代码](<https://github.com/demelin/moral_stories>) |
| MoralBench | 价值观 | 基准 | 2024 | en | [项目](<https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7>) |
| NormAd | 价值观对齐（文化规范适应力，75国） | 基准 | 2024 | en | [代码](<https://github.com/Akhila-Yerukola/NormAd>) |
| OpinionQA | 价值观对齐（人类观点分布：23个粗粒度+40个细粒度议题，60个美国人口群体） | 基准 | 2023 | en | [代码](<https://github.com/tatsu-lab/opinions_qa>) |
| ValueBench | 价值取向探测（44个心理测量量表/453个价值维度） | 基准 | 2024 | en | [代码](<https://github.com/ValueByte-AI/ValueBench>) |
| WorldValuesBench | 价值观 | 基准 | 2024 | en | [代码](<https://github.com/Demon702/WorldValuesBench>) |

### 隐私

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| ASQ-PHI | PII泄露 | 基准 | 2025 | en | [代码](<https://github.com/JamesWeatherhead/asq-phi>) |
| ConfAIde | 训练数据泄露 | 基准 | 2024 | en | [代码](<https://github.com/skywalker023/confaide/tree/main>) |
| LM_PersonalInfoLeak | PII泄露 | 基准 | 2022 | en | [代码](<https://github.com/jeffhj/LM_PersonalInfoLeak>) |
| MultiPriv | PII泄露 | 基准 | 2025 | zh, en | [代码](<https://github.com/CyberChangAn/MultiPriv-PII>) |
| PrivacyBench | 训练数据泄露 | 基准 | 2025 | en | [代码](<https://github.com/sri-ja/privacy-bench>) · [论文](<https://arxiv.org/abs/2512.24848>) |
| PUPA | PII泄露 | 基准 | 2024 | en | [数据](<https://huggingface.co/datasets/Columbia-NLP/PUPA>) |

### 过度拒答

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| FalseReject | 过度拒答校准（伪有害但实际无害查询） | 基准 | 2025 | en | [数据](<https://huggingface.co/datasets/AmazonScience/FalseReject>) |
| OR-Bench | 过度拒答校准 | 基准 | 2024 | en | [代码](<https://github.com/justincui03/or-bench>) |
| PHTest | 过度拒答校准（伪有害提示自动生成） | 基准 | 2024 | en | [代码](<https://github.com/umd-huang-lab/FalseRefusal>) |
| RASS / MoRBench | 过度拒答校准（安全决策边界模糊提示） | 基准 | 2025 | other | [代码](<https://github.com/Master-PLC/RASS>) |
| XSTest | 过度拒答校准 | 基准 | 2023 | en | [代码](<https://github.com/paul-rottger/xstest>) |

### 自主性与对齐

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| Anthropic Evals | — | 基准套件 | 2022 | en | [代码](<https://github.com/anthropics/evals>) |
| CRiskEval | — | 基准套件 | 2025 | zh | [代码](<https://github.com/tjunlp-lab/CRiskEval>) |
| Myopia_reward | — | 基准套件 | 2022 | zh | [代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [论文](<https://arxiv.org/abs/2212.09251>) |
| One-box Tendency | — | 基准套件 | 2022 | zh | [代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [论文](<https://arxiv.org/abs/2212.09251>) |
| Power-seeking | — | 基准套件 | 2022 | zh | [代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [论文](<https://arxiv.org/abs/2212.09251>) |
| Self-awareness | — | 基准套件 | 2022 | zh | [代码](<https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals>) · [论文](<https://arxiv.org/abs/2212.09251>) |

### 领域风险

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| CyberSecEval 1/2/3 (Purple Llama) | 不安全代码/网络攻击协助/提示注入（v3含视觉注入与自主网络攻击） | 基准 | 2023 | en | [代码](<https://github.com/meta-llama/PurpleLlama>) |
| FinSafetyBench | 金融安全（金融犯罪+职业伦理违规，14细分类别） | 基准 | 2026 | zh, en | [代码](<https://github.com/sustech-nlp/FinSafetyBench>) |
| MedSafetyBench | 医疗安全（有害医疗请求应答） | 基准 | 2024 | en | [代码](<https://github.com/AI4LIFE-GROUP/med-safety-bench>) |
| SafeSci | — | 基准 | 2026 | en | [代码](<https://github.com/yangyangyang127/SafeSci>) |
| SciSafeEval | 科学语言安全对齐（文本/分子/蛋白/基因组） | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2410.03769>) |
| WMDP | 生物/化学/网络危险知识测量 | 基准 | 2024 | en | [数据](<https://huggingface.co/datasets/cais/wmdp>) |

## Agent 安全

### 提示注入与指令边界

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AgentDojo | 任务覆盖四类真实应用场景：Workspace：邮件、日历、云盘任务，例如统计日程、总结邮件、发送信息；Slack：读取网页/文件、发 Slack 消息、邀请成员… | 基准 | NeurIPS 2024 | en | [论文](<https://arxiv.org/abs/2406.13352>) · [代码](<https://github.com/ethz-spylab/agentdojo>) |
| AgentDyn | 在开放式动态任务中插入有用但潜在恶意的第三方指令，测试 agent 是否能完成任务同时抵御注入。 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2602.03117>) · [代码](<https://github.com/SaFo-Lab/AgentDyn>) |
| AgentLAB | 测试长程任务中 intent hijacking、tool chaining、task injection、objective drifting、memory … | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2602.16901>) · [项目](<https://tanqiujiang.github.io/AgentLAB_main/>) · [代码](<https://github.com/TanqiuJiang/AgentLAB>) |
| InjecAgent | 测试任务是：用户先提出一个正常请求，Agent 需要调用某个工具读取外部内容；外部内容中被植入攻击者指令，诱导 Agent 调用其他工具执行有害行为。攻击分两大… | 基准 | 2024（ACL Findings） | en | [论文](<https://aclanthology.org/2024.findings-acl.624/>) · [代码](<https://github.com/uiuc-kang-lab/InjecAgent>) |

### 综合 Agent 安全与滥用

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| Agent Security Bench (ASB) | 任务分为两类：一类是正常任务，例如系统管理员 Agent “识别并修补过期软件漏洞”、学术搜索 Agent 检索和总结论文、金融分析 Agent 做投资分析等；… | 基准 | 2024/2025 | en | [论文](<https://arxiv.org/abs/2410.02644>) · [代码](<https://github.com/agiresearch/ASB>) |
| Agent-SafetyBench | 测试任务覆盖 8 类风险：敏感信息泄露、财产损失、传播不安全/虚假信息、造成物理伤害、违法/伦理违规、破坏可用性、生成/传播有害或脆弱代码、产生不安全/虚假内容… | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2412.14470>) · [代码](<https://github.com/thu-coai/Agent-SafetyBench>) · [数据](<https://huggingface.co/datasets/thu-coai/Agent-SafetyBench>) · [项目](<https://www.semanticscholar.org/reader/7d11400eeb317ebee278f49e108226a4f8555dda>) |
| AgentHarm | 测试任务是显式恶意的 agentic misuse 请求，覆盖 Fraud、Cybercrime、Self-harm、Harassment、Sexual、Cop… | 基准 | ICLR 2025 | en | [论文](<https://arxiv.org/abs/2410.09024>) · [数据](<https://huggingface.co/datasets/ai-safety-institute/AgentHarm>) · [项目](<https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/>) |
| Echoes of Human Malice | 多轮网络骚扰智能体攻击 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2510.14207>) |
| HAICosystem | 人机交互伦理安全沙盒 | 基准 | 2024 | en | [代码](<https://github.com/XuhuiZhou/HAICosystem>) |
| OpenAgentSafety | 评测 agent 使用浏览器、代码、文件系统、bash、消息平台等真实工具时的安全风险。 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2507.06134>) · [代码](<https://github.com/Open-Agent-Safety/OpenAgentSafety>) · [数据](<https://huggingface.co/datasets/sani903/openagentsafety>) |
| SafePro | 评测专业工作场景中 agent 是否执行不安全专业行为，例如误导性金融/法律/医疗/工程操作或危险文件/代码处理。 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2601.06663>) · [代码](<https://github.com/UCSB-AI/SafePro>) · [项目](<https://safeprobench.github.io/safepro/>) · [数据](<https://huggingface.co/datasets/kzhou35/SafePro>) |

### 工具、API 与 MCP 安全

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| MCIP | MCP工具调用安全 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2505.14590>) |
| MCP Security Bench (MSB) | 覆盖 MCP 规划、工具调用、响应处理等阶段的攻击，如工具名碰撞、描述注入、越界参数、错误升级、检索注入等。 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2510.15994>) · [代码](<https://github.com/dongsenzhang/MSB>) |
| MCP-TDP | 工具描述/手册投毒 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2605.24069>) |
| MCPTox | 测试任务是：用户提出一个正常请求，Agent 接入包含正常工具和被投毒工具描述的 MCP 工具列表；攻击者在某个恶意工具的 description 中嵌入规则，… | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2508.14925>) · [代码](<https://anonymous.4open.science/r/AAAI26-7C02>) |
| RAS-EVAL | 把正常任务转化为攻击任务，测试 agent 在真实或模拟工具环境中是否保持鲁棒、安全和任务完成能力。 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2506.15253>) · [代码](<https://github.com/lanzer-tree/RAS-Eval>) |
| ToolEmu | 任务关注 instruction underspecification，即用户请求本身是善意的，但存在关键信息缺失或歧义，如果 Agent 不澄清就直接执行，可… | 基准 | 2023/ICLR 2024 | en | [论文](<https://arxiv.org/abs/2309.15817>) · [代码](<https://github.com/ryoungj/ToolEmu>) |
| ToolSword | 工具学习全流程安全（输入/执行/输出三阶段六场景） | 基准 | 2024 | en | [代码](<https://github.com/Junjie-Ye/ToolSword>) |

### 隐私与记忆

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AgentDAM | 智能体隐私最小化/隐私泄露 | 基准 | 2025 | en | [代码](<https://github.com/facebookresearch/ai-agent-privacy>) |
| AgentLeak | 评测多 agent 系统中隐私信息是否通过内部消息、共享记忆、工具参数等通道泄露。 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2602.11510>) · [代码](<https://github.com/Privatris/AgentLeak>) · [数据](<https://huggingface.co/datasets/humain2/AgentLeak>) |
| PrivacyLens | 情境化隐私规范/PII泄露（智能体行动） | 基准 | 2024 | en | [代码](<https://github.com/SALT-NLP/PrivacyLens>) |

### 网页、桌面与移动 Agent

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AgentHazard | 将有害目标拆成局部看似合理的步骤，测试 agent 是否能在多轮工具使用中识别并中止累计风险。 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2604.02947>) · [代码](<https://github.com/Yunhao-Feng/AgentHazard>) · [项目](<https://yunhao-feng.github.io/AgentHazard/>) |
| CUAHarm | 测试 computer-use agent 是否会完成禁用防火墙、泄露机密、发起 DoS、安装后门等误用目标。 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2508.00935>) · [代码](<https://github.com/db-ol/CUAHarm>) · [数据](<https://huggingface.co/datasets/CUAHarm/CUAHarm>) |
| MobileSafetyBench | 移动设备操作安全 / 间接提示注入 | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2410.17520>) · [代码](<https://github.com/jylee425/mobilesafetybench>) · [项目](<https://mobilesafetybench.github.io>) |
| RiOSWorld | 真实 GUI 高风险操作 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2506.00618>) · [项目](<https://yjyddq.github.io/RiOSWorld.github.io/>) |
| SABER | 评测编码 agent 在项目工作区中面对恶意环境内容、风险自选择、上下文警告时是否执行有害命令或传播风险。 | 基准 | 2026 | 中英混合, 英语为主 | [论文](<https://arxiv.org/abs/2606.01317>) · [代码](<https://github.com/sssr-lab/saber>) |
| SafeArena | 网页智能体恶意任务多轮执行 | 基准 | 2025 | en | [代码](<https://github.com/McGill-NLP/safearena>) |
| ST-WebAgentBench | 在企业 Web 工作流中测试 agent 是否既完成任务又遵守安全可信策略，例如权限、隐私、合规和风险约束。 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2410.06703>) · [项目](<https://sites.google.com/view/st-webagentbench/home>) · [数据](<https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench>) · [代码](<https://github.com/segev-shlomov/ST-WebAgentBench>) |
| WASP | 测试网页中的恶意内容是否能劫持 Web agent，使其偏离用户目标并执行攻击者目标。 | 基准 | 2025 | en | [论文](<https://arxiv.org/abs/2504.18575>) · [代码](<https://github.com/facebookresearch/wasp>) |

### 具身安全

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| SafeAgentBench | 具身任务规划与物理安全 | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2412.13178>) · [项目](<https://safeagentbench.github.io>) · [代码](<https://github.com/shengyin1224/SafeAgentBench>) |

## 安全审查与护栏

### Agent 轨迹与动作安全

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| ATBench | 完整轨迹安全判断与风险归因 | 评测数据 | 2026 | en | [论文](<https://arxiv.org/abs/2604.02022>) · [代码](<https://github.com/LiYu0524/ATbench>) · [数据](<https://huggingface.co/datasets/AI45Research/ATBench>) |
| PhoneSafety | 手机关键决策下一动作安全 | 评测数据 | 2025 | 中文为主 | [论文](<https://arxiv.org/abs/2605.07630>) · [代码](<https://github.com/tangzhy/PhoneSafety>) · [数据](<https://huggingface.co/datasets/phonesafety-anon/PhoneSafety_Data>) |
| R-Judge | 既有 Agent 轨迹风险识别 | 评测数据 | 2024 | en | [论文](<https://arxiv.org/abs/2401.10019>) · [代码](<https://github.com/Lordog/R-Judge>) |
| SafeToolBench | 执行前风险识别 | 评测数据 | 2025 | en | [论文](<https://aclanthology.org/2025.findings-emnlp.958.pdf>) · [代码](<https://github.com/BITHLP/SafeToolBench>) |
| SleightBench | 恶意编码轨迹监控与规避检测 | 评测数据 | 2025 | en | [论文](<https://arxiv.org/abs/2605.16626>) · [代码](<https://github.com/safety-research/sleight-bench>) |
| ToolSafe / TS-Bench | 候选工具调用安全分类 | 评测数据 | 2026 | en | [论文](<https://arxiv.org/abs/2601.10156>) · [代码](<https://github.com/MurrayTom/ToolSafe>) |
| TOP-Bench | 跨工具组合推断导致的隐私泄露 | 评测数据 | 2026 | en | [论文](<https://arxiv.org/abs/2512.16310>) · [代码](<https://github.com/1Ponder/TOP-R>) · [项目](<https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082>) |
| TraceSafe-Bench | 多步工具轨迹风险检测 | 评测数据 | 2026 | en | [论文](<https://arxiv.org/abs/2604.07223>) · [代码](<https://github.com/cycraft-corp/TraceSafe>) · [数据](<https://huggingface.co/datasets/CyCraftAI/TraceSafe>) |
| WebGuard | 网页操作风险分级护栏 | 评测数据 | 2025 | en | [代码](<https://github.com/OSU-NLP-Group/WebGuard>) |

### 内容护栏评测

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| GuardBench | 护栏模型评测（统一聚合40个安全评测数据集） | 基准套件 | 2024 | en | [代码](<https://github.com/AmenRa/guardbench>) |
| WildGuard (WildGuardMix/WildGuardTest) | 护栏审核（用户意图识别/回复有害性判定/拒答检测，13风险类） | 基准套件 | 2024 | en | [数据](<https://huggingface.co/datasets/allenai/wildguardmix>) |

## 相关资源

### 训练数据

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| Aegis 1.0 (Nemotron Content Safety Dataset V1) | 护栏审核（13类关键风险内容安全分类） | 训练数据 | 2024 | en | [数据](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0>) |
| GuardReasoner (GuardReasonerTrain) | 护栏审核（推理型安全防护，3类护栏任务/13个基准） | 训练数据 | 2025 | en | [数据](<https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain>) |
| HarmfulQA (RED-INSTRUCT) | 有害问答红队（直接+越狱提问，10主题） | 训练数据 | 2023 | en | [数据](<https://huggingface.co/datasets/TrustAIRLab/HarmfulQA>) |
| HH-RLHF（含Red Team Attempts） | 无害性偏好数据+人工红队对话 | 训练数据 | 2022 | en | [代码](<https://github.com/anthropics/hh-rlhf>) |
| Nemotron Content Safety Dataset V2 | — | 训练数据 | 2025 | en | [数据](<https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0>) |
| NVIDIA Nemotron Agentic IPI | 工具返回中的间接提示注入 | 训练数据 | 2026 | en | [数据](<https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1>) |
| PKU-SafeRLHF (10K/30K) | 安全偏好标注（红队提示+细粒度安全标签） | 训练数据 | 2023 | en | [数据](<https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K>) |
| SafeMTData（Derail Yourself/ActorAttack配套） | 自然分布偏移多轮攻击 | 训练数据 | 2024 | en | [数据](<https://huggingface.co/datasets/SafeMTData/SafeMTData>) |
| ToolSafety | 安全工具调用数据与微调 | 训练数据 | EMNLP 2025 | en | [论文](<https://aclanthology.org/2025.emnlp-main.714.pdf>) · [数据](<https://huggingface.co/datasets/jinjinyien/ToolSafety>) |
| X-Teaming Evolutionary M2S | 多轮到单轮越狱模板自动发现 | 训练数据 | 2025 | en | [数据](<https://huggingface.co/datasets/hyunjun1121/X-Teaming_Evolutionary_M2S>) |
| XGuard-Train-Open-200K | 护栏审核训练数据（9大风险维度/28细分类别，多语言） | 训练数据 | 2026 | other | [数据](<https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K>) |
| XGuard-Train（X-Teaming配套） | 多智能体自适应多轮越狱训练集 | 训练数据 | 2025 | en | [数据](<https://huggingface.co/datasets/marslabucla/XGuard-Train>) |

### 攻击方法

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AgentPoison | 向Agent的外部知识库或memory中注入恶意数据，并通过优化触发器提高投毒内容的检索概率，评估RAG poisoning攻击对Agent行为和输出的影响 | 方法 | 2024 | en | [论文](<https://arxiv.org/abs/2407.12784>) · [代码](<https://github.com/AI-secure/AgentPoison>) · [项目](<https://billchan226.github.io/AgentPoison.html>) |
| ArtPrompt | ASCII艺术编码越狱 | 方法 | 2024 | en | [代码](<https://github.com/uw-nsl/ArtPrompt>) |
| AutoDAN | 隐蔽越狱提示生成 | 方法 | 2024 | en | [代码](<https://github.com/SheltonLiu-N/AutoDAN>) |
| Automating Deception（FITD多轮越狱） | 登门槛效应（Foot-in-the-Door）心理操纵多轮越狱 | 方法 | 2025 | en | [论文](<https://arxiv.org/abs/2511.19517>) |
| CipherChat | 密码编码越狱 | 方法 | 2024 | zh, en | [代码](<https://github.com/RobustNLP/CipherChat>) |
| CodeChameleon | 个性化加密越狱 | 方法 | 2024 | en | [代码](<https://github.com/huizhang-L/CodeChameleon>) |
| Crescendo | 渐进式对话升级越狱 | 方法 | 2024 | en | [论文](<https://arxiv.org/abs/2404.01833>) |
| Curiosity-driven Red Teaming | 好奇心驱动自动红队 | 方法 | 2024 | en | [代码](<https://github.com/Improbable-AI/curiosity_redteam>) |
| DeepInception | 场景嵌套越狱 | 方法 | 2023 | en | [代码](<https://github.com/tmlr-group/DeepInception>) |
| GPTFuzzer | 越狱模板变异模糊测试 | 方法 | 2023 | en | [代码](<https://github.com/hubertyoo/GPTFuzz>) |
| Latent Jailbreak | 隐式/潜在越狱 | 方法 | 2023 | 英文+中文 | [代码](<https://github.com/qiuhuachuan/latent-jailbreak>) |
| MART | 多轮自动红队攻防迭代 | 方法 | 2023 | en | [论文](<https://arxiv.org/abs/2311.07689>) |
| MemoryGraft | 经验检索投毒与持久行为漂移 | 方法 | 2025 | en | [论文](<https://arxiv.org/abs/2512.16962>) · [代码](<https://github.com/Jacobhhy/MemoryGraft>) · [项目](<https://www.semanticscholar.org/reader/b1d80b2eda7e175e235185bdc7df4e8233f36ef4>) |
| PsychJail | 社会心理学说服策略多轮红队 | 方法 | 2026 | en | [代码](<https://github.com/FengZeyugit/PsychJail>) |
| ReNeLLM | 嵌套提示越狱（提示改写+56种场景嵌套） | 方法 | 2024 | en | [代码](<https://github.com/NJUNLP/ReNeLLM>) |

### 框架及混合资源

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| AgentDefense-Bench | MCP 请求检测与阻断 | 框架 | 2025 | en | [代码](<https://github.com/arunsanna/AgentDefense-Bench>) |
| CC-BOS | — | 框架 | 2026 | zh | [代码](<https://github.com/xaoLiu1222/cc-bos>) |
| LiveSecBench | — | 框架 | 2026 | zh | [代码](<https://github.com/ydli-ai/LiveSecBench>) |
| ORFuzz | 过度拒答校准（演化模糊测试） | 框架 | 2025 | en | [论文](<https://arxiv.org/abs/2508.11222>) |
| ShieldLM | 护栏审核（中英双语安全检测，safe/unsafe/controversial三分类） | 框架 | 2024 | zh, en | [代码](<https://github.com/thu-coai/ShieldLM>) |
| TrustAgent | 智能体规划安全宪法 | 框架 | 2024 | en | [论文](<https://arxiv.org/abs/2402.01586>) |
| WILDTEAMING / WildJailbreak | 越狱策略挖掘与对抗安全训练 | 框架 | 2024 | en | [代码](<https://github.com/allenai/wildteaming>) |

### 攻击挑战与数据

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| LLMail-Inject | 邮件场景间接提示注入 | 评测数据 | 2025 | en | [论文](<https://arxiv.org/abs/2506.09956>) · [代码](<https://github.com/microsoft/llmail-inject-challenge>) |

### 能力基线与环境

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| Agent-Diff | 工作流状态差分与任务完成 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2602.11224>) · [代码](<https://github.com/agent-diff-bench/agent-diff>) · [项目](<https://www.agentdiff.dev>) · [数据](<https://huggingface.co/datasets/hubertmarek/agent-diff-bench>) |
| API-Bank | API 理解、检索、调用与回答 | 基准 | EMNLP 2023 | en | [论文](<https://arxiv.org/abs/2304.08244>) |
| AppWorld | 跨应用任务完成与代码执行能力 | 基准 | ACL 2024 | en | [论文](<https://aclanthology.org/2024.acl-long.850/>) · [代码](<https://github.com/StonyBrookNLP/appworld>) · [项目](<https://appworld.dev>) |
| BFCL | 函数选择、参数生成与多步调用 | 基准 | 2024/2025，持续更新至 V4 | 英语为主, 多语言函数调用场景 | [论文](<https://proceedings.mlr.press/v267/patil25a.html>) · [项目](<https://gorilla.cs.berkeley.edu/leaderboard.html>) · [数据](<https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard>) |
| SkillsBench | Skill 使用与能力增益 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2602.12670>) · [项目](<https://www.skillsbench.ai>) · [代码](<https://github.com/benchflow-ai/skillsbench>) |
| tau-bench | 规则遵循、任务完成与稳定性 | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2406.12045>) · [代码](<https://github.com/sierra-research/tau-bench>) · [项目](<https://www.semanticscholar.org/reader/70aa016c1f68fd5c0261f26ad20017b8307650af>) |
| TheAgentCompany | 办公、编码和协作任务完成 | 基准 | 2024/2025 | en | [论文](<https://arxiv.org/abs/2412.14161>) · [代码](<https://github.com/TheAgentCompany/TheAgentCompany>) · [项目](<https://the-agent-company.com>) |
| TOOLATHLON | 多工具任务完成与效率 | 基准 | 2026 | en | [论文](<https://arxiv.org/abs/2510.25726>) · [代码](<https://github.com/hkust-nlp/Toolathlon>) |
| ToolSandbox | 多轮有状态工具调用能力 | 基准 | 2024 | en | [论文](<https://arxiv.org/abs/2408.04682>) · [代码](<https://github.com/apple-aiml-research/ToolSandbox>) · [项目](<https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark>) |
| WebArena | 网页导航与任务完成 | 基准 | ICLR 2024 / NeurIPS 2024 Oral 相关项目口径 | en | [论文](<https://arxiv.org/abs/2307.13854>) · [代码](<https://github.com/web-arena-x/webarena>) · [项目](<https://webarena.dev>) |
| WorkArena | ServiceNow 任务完成 | 基准 | ICML 2024 | en | [论文](<https://arxiv.org/abs/2403.07718>) · [代码](<https://github.com/ServiceNow/workarena>) · [项目](<https://servicenow.github.io/WorkArena/>) |

### 事实性与通用轨迹诊断

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| HaluEval | 幻觉识别与生成 | 评测数据 | 2023 | en | [论文](<https://arxiv.org/abs/2305.11747>) · [代码](<https://github.com/RUCAIBox/HaluEval>) |
| RAGTruth | 幻觉与事实一致性 | 评测数据 | 2023 | en | [论文](<https://arxiv.org/abs/2401.00396>) |
| SimpleQA | 事实问答准确性 | 评测数据 | 2024 | en | [论文](<https://arxiv.org/abs/2411.04368>) · [代码](<https://github.com/openai/simple-evals>) |
| TraceElephant | 责任组件与关键失败步骤定位 | 评测数据 | 2026 | en | [论文](<https://arxiv.org/abs/2604.22708>) · [代码](<https://github.com/TraceElephant/TraceElephant>) · [数据](<https://huggingface.co/datasets/TraceElephant/TraceElephant>) |
| TRAIL | 错误分类与 trace span 定位 | 评测数据 | 2025 | en | [论文](<https://arxiv.org/abs/2505.08638>) · [数据](<https://huggingface.co/datasets/PatronusAI/TRAIL>) |

### 领域能力基准

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| CTIBench | 网络威胁情报CTI任务（MCQ/根因映射/归因/ATT&CK提取） | 基准 | 2024 | en | [数据](<https://huggingface.co/datasets/AI4Sec/cti-bench>) |
| CyberMetric | 网络安全知识（基于NIST框架/RAG生成） | 基准 | 2024 | en | [代码](<https://github.com/cybermetric/CyberMetric>) |
| HealthBench | 医疗安全（急诊转诊/不安全响应/情境理解等） | 基准 | 2025 | en | [数据](<https://huggingface.co/datasets/openai/healthbench>) |
| LawBench | 法律安全（法条/罪名/刑期预测、犯罪金额计算等20任务） | 基准 | 2023 | zh | [代码](<https://github.com/open-compass/LawBench>) |
| SecEval | 网络安全知识（系统/Web/渗透/漏洞/密码学等9子领域） | 基准 | 2023 | en | [代码](<https://github.com/XuanwuAI/SecEval>) |

### 已收录基准的子集

| 条目 | 评测重点（原表摘要） | 类型 | 原表年份 | 原表语言 | 链接 |
| --- | --- | --- | --- | --- | --- |
| DecodingTrust（Privacy 子集） | PII泄露 | 子集 | 2023 | en | [代码](<https://github.com/AI-secure/DecodingTrust>) |
| JBB-Behaviors | Jailbreak攻击 | 子集 | 2024 | en | [数据](<https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors>) |

## 维护

在 `data/benchmarks.json` 中增量添加或更新条目，然后运行：

```powershell
python scripts/check_links.py
python scripts/apply_link_checks.py
python scripts/build_readme.py
python scripts/validate.py
```

详见[贡献说明](CONTRIBUTING.md)、[分类口径](docs/taxonomy.md)、[字段说明](docs/schema.md)和[导入报告](docs/import-report.md)。身份或主题范围待核验事项保留在 `.local/` 的后台维护数据中；包含本机路径、收集人信息的原始快照也保留在已忽略的 `.local/` 中。

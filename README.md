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

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AILuminate</td><td><span title="—">—</span></td><td>2025</td><td>zh, en, other</td><td><a href="https://github.com/mlcommons/ailuminate">Code</a></td></tr>
<tr><td>Ch3Ef</td><td><span title="HHH（helpful/honest/harmless）对齐12域46任务">HHH（helpful/honest/harmless）对齐12域46任务</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2403.17830">Paper</a></td></tr>
<tr><td>CHiSafetyBench</td><td><span title="风险识别与拒绝">风险识别与拒绝</span></td><td>2024</td><td>zh</td><td><a href="https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench">Code</a></td></tr>
<tr><td>DecodingTrust</td><td><span title="训练数据泄露">训练数据泄露</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/AI-Secure/DecodingTrust">Data</a></td></tr>
<tr><td>Flames</td><td><span title="中文价值对齐（安全、公平、道德、数据保护、合法性）">中文价值对齐（安全、公平、道德、数据保护、合法性）</span></td><td>2023</td><td>zh</td><td><a href="https://github.com/AI45Lab/Flames">Code</a></td></tr>
<tr><td>ForesightSafety Bench</td><td><span title="—">—</span></td><td>2026</td><td>en</td><td><a href="https://github.com/Beijing-AISI/ForesightSafety-Bench">Code</a></td></tr>
<tr><td>JailBench</td><td><span title="—">—</span></td><td>2025</td><td>zh</td><td><a href="https://github.com/STAIR-BUPT/JailBench">Code</a></td></tr>
<tr><td>LongSafety</td><td><span title="长上下文开放任务安全">长上下文开放任务安全</span></td><td>2025</td><td>en</td><td><a href="https://github.com/thu-coai/LongSafety">Code</a></td></tr>
<tr><td>SafetyBench</td><td><span title="—">—</span></td><td>2024</td><td>zh, en</td><td><a href="https://github.com/thu-coai/SafetyBench">Code</a></td></tr>
<tr><td>SALAD-Bench</td><td><span title="—">—</span></td><td>2024</td><td>en</td><td><a href="https://adwardlee.github.io/salad_bench/">Project</a></td></tr>
<tr><td>SuperCLUE-Safety</td><td><span title="—">—</span></td><td>2024</td><td>zh</td><td><a href="https://www.cluebenchmarks.com/superclue_safety.html">Project</a></td></tr>
<tr><td>TrustLLM</td><td><span title="可信性六维综合评测（真实性/安全/公平/鲁棒/隐私/机器伦理）">可信性六维综合评测（真实性/安全/公平/鲁棒/隐私/机器伦理）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/HowieHwong/TrustLLM">Code</a></td></tr>
<tr><td>U-SafeBench</td><td><span title="用户特定安全标准评测">用户特定安全标准评测</span></td><td>2025</td><td>en</td><td><a href="https://github.com/yeonjun-in/U-SafeBench">Code</a></td></tr>
</tbody>
</table>

### Harmful content and toxicity | 有害内容与毒性

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>BeaverTails</td><td><span title="—">—</span></td><td>2023</td><td>zh, en</td><td><a href="https://sites.google.com/view/pku-beavertails">Project</a></td></tr>
<tr><td>ChineseSafe</td><td><span title="政治敏感/色情/暴恐/变体谐音规避（4大类10小类）">政治敏感/色情/暴恐/变体谐音规避（4大类10小类）</span></td><td>2024</td><td>zh</td><td><a href="https://huggingface.co/datasets/SUSTech/ChineseSafe">Data</a></td></tr>
<tr><td>COLD</td><td><span title="伤害类型8：攻击性与有害表达风险">伤害类型8：攻击性与有害表达风险</span></td><td>2022</td><td>zh</td><td><a href="https://github.com/thu-coai/COLDataset">Code</a><br><a href="https://arxiv.org/abs/2201.06025">Paper</a></td></tr>
<tr><td>CREHate</td><td><span title="仇恨言论（跨文化标注差异）">仇恨言论（跨文化标注差异）</span></td><td>2024</td><td>en, other</td><td><a href="https://github.com/nlee0212/CREHate">Code</a></td></tr>
<tr><td>DICES</td><td><span title="带评分者人口统计多样性的对话安全标注">带评分者人口统计多样性的对话安全标注</span></td><td>2023</td><td>en</td><td><a href="https://arxiv.org/abs/2306.11247">Paper</a></td></tr>
<tr><td>Do-Not-Answer</td><td><span title="—">—</span></td><td>2024</td><td>zh, en</td><td><a href="https://github.com/libr-ai/do-not-answer">Code</a></td></tr>
<tr><td>DynaHate</td><td><span title="仇恨言论（对抗动态生成）">仇恨言论（对抗动态生成）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset">Code</a></td></tr>
<tr><td>hate_speech_offensive</td><td><span title="仇恨言论">仇恨言论</span></td><td>2017</td><td>en</td><td><a href="https://huggingface.co/datasets/tdavidson/hate_speech_offensive">Data</a></td></tr>
<tr><td>HateCheck</td><td><span title="仇恨言论功能性诊断测试（29项功能）">仇恨言论功能性诊断测试（29项功能）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/paul-rottger/hatecheck-data">Code</a></td></tr>
<tr><td>Implicit Hate Corpus</td><td><span title="仇恨言论（隐性仇恨）">仇恨言论（隐性仇恨）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/SALT-NLP/implicit-hate">Code</a></td></tr>
<tr><td>Measuring Hate Speech</td><td><span title="仇恨言论（连续hate score）">仇恨言论（连续hate score）</span></td><td>2022</td><td>en</td><td><a href="https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech">Data</a></td></tr>
<tr><td>moderation-api-release</td><td><span title="—">—</span></td><td>2022</td><td>en</td><td><a href="https://github.com/openai/moderation-api-release/tree/main">Code</a></td></tr>
<tr><td>Multilingual HateCheck (MHC)</td><td><span title="仇恨言论（多语言功能性测试）">仇恨言论（多语言功能性测试）</span></td><td>2022</td><td>other</td><td><a href="https://github.com/rewire-online/multilingual-hatecheck">Code</a></td></tr>
<tr><td>ProsocialDialog</td><td><span title="亲社会回应/社会规范引导（rules-of-thought）">亲社会回应/社会规范引导（rules-of-thought）</span></td><td>2022</td><td>en</td><td><a href="https://github.com/skywalker023/prosocial-dialog">Code</a></td></tr>
<tr><td>RealToxicityPrompts</td><td><span title="自然网页语料的毒性触发补全">自然网页语料的毒性触发补全</span></td><td>2020</td><td>en</td><td><a href="https://github.com/allenai/real-toxicity-prompts">Code</a></td></tr>
<tr><td>RTP-LX</td><td><span title="—">—</span></td><td>2024</td><td>zh, en, other</td><td><a href="https://github.com/microsoft/RTP-LX">Code</a></td></tr>
<tr><td>Safety-Prompts</td><td><span title="7类典型安全场景+6类指令攻击">7类典型安全场景+6类指令攻击</span></td><td>2023</td><td>zh</td><td><a href="https://github.com/thu-coai/Safety-Prompts">Code</a></td></tr>
<tr><td>SGHateCheck</td><td><span title="仇恨言论（新加坡低资源语言功能性测试）">仇恨言论（新加坡低资源语言功能性测试）</span></td><td>2024</td><td>other</td><td><a href="https://github.com/Social-AI-Studio/SGHateCheck">Code</a></td></tr>
<tr><td>SORRY-Bench</td><td><span title="—">—</span></td><td>2024</td><td>en</td><td><a href="https://github.com/SORRY-Bench/sorry-bench">Code</a></td></tr>
<tr><td>TOCP</td><td><span title="伤害类型8：攻击性与有害表达风险">伤害类型8：攻击性与有害表达风险</span></td><td>2020</td><td>zh</td><td><a href="https://nlp.cse.ntou.edu.tw/resources/TOCP/">Project</a><br><a href="https://aclanthology.org/2020.trac-1.2/">Paper</a></td></tr>
<tr><td>ToxiCN</td><td><span title="仇恨言论/毒性（中文细粒度）">仇恨言论/毒性（中文细粒度）</span></td><td>2023</td><td>zh</td><td><a href="https://github.com/DUT-lujunyu/ToxiCN">Code</a></td></tr>
<tr><td>ToxiCN MM</td><td><span title="有害迷因（多模态中文）">有害迷因（多模态中文）</span></td><td>2024</td><td>zh</td><td><a href="https://github.com/DUT-lujunyu/ToxiCN_MM">Code</a></td></tr>
<tr><td>ToxiGen</td><td><span title="仇恨言论（13个少数群体隐性毒性）">仇恨言论（13个少数群体隐性毒性）</span></td><td>2022</td><td>en</td><td><a href="https://github.com/microsoft/ToxiGen">Code</a></td></tr>
<tr><td>TUMCC</td><td><span title="—">—</span></td><td>2020</td><td>zh</td><td><a href="https://github.com/m1-llie/TUMCC">Code</a><br><a href="https://linkinghub.elsevier.com/retrieve/pii/S030645732200142X">Paper</a></td></tr>
</tbody>
</table>

### Jailbreaks and adversarial prompts | 越狱与对抗提示

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AdvBench</td><td><span title="有害请求与越狱">有害请求与越狱</span></td><td>2023</td><td>en</td><td><a href="https://arxiv.org/abs/2307.15043">Paper</a><br><a href="https://github.com/llm-attacks/llm-attacks">Code</a></td></tr>
<tr><td>AttaQ</td><td><span title="对抗性问题有害响应倾向">对抗性问题有害响应倾向</span></td><td>2023</td><td>en</td><td><a href="https://huggingface.co/datasets/ibm-research/AttaQ">Data</a></td></tr>
<tr><td>CoSafe</td><td><span title="多轮对话指代消解安全攻击">多轮对话指代消解安全攻击</span></td><td>2024</td><td>en</td><td><a href="https://github.com/ErxinYu/CoSafe-Dataset">Code</a></td></tr>
<tr><td>HarmBench</td><td><span title="有害行为与越狱">有害行为与越狱</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2402.04249">Paper</a><br><a href="https://github.com/centerforaisafety/HarmBench">Code</a></td></tr>
<tr><td>In-the-Wild Jailbreak Prompts (jailbreak_llms)</td><td><span title="野外真实越狱提示库">野外真实越狱提示库</span></td><td>2024</td><td>en</td><td><a href="https://github.com/verazuo/jailbreak_llms">Code</a></td></tr>
<tr><td>JailbreakBench</td><td><span title="越狱攻击与拒绝">越狱攻击与拒绝</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2404.01318">Paper</a><br><a href="https://github.com/JailbreakBench/jailbreakbench">Code</a></td></tr>
<tr><td>JailBreakV-28k</td><td><span title="Jailbreak攻击">Jailbreak攻击</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k">Data</a></td></tr>
<tr><td>MaliciousInstruct</td><td><span title="越狱攻击/恶意指令">越狱攻击/恶意指令</span></td><td>2023</td><td>en</td><td><a href="https://github.com/Princeton-SysML/Jailbreak_LLM">Code</a></td></tr>
<tr><td>MHJ (Multi-Turn Human Jailbreaks)</td><td><span title="人类红队真实多轮越狱">人类红队真实多轮越狱</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/ScaleAI/mhj">Data</a></td></tr>
<tr><td>MultiBreak</td><td><span title="大规模多样化多轮越狱">大规模多样化多轮越狱</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2605.01687">Paper</a></td></tr>
<tr><td>MultiJail</td><td><span title="多语言越狱">多语言越狱</span></td><td>2024</td><td>en, other</td><td><a href="https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail">Data</a></td></tr>
<tr><td>PAP (Persuasive Adversarial Prompts)</td><td><span title="说服式越狱">说服式越狱</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/CHATS-Lab/Persuasive-Jailbreaker-Data">Data</a></td></tr>
<tr><td>SafeDialBench</td><td><span title="多轮越狱对话细粒度安全评测">多轮越狱对话细粒度安全评测</span></td><td>2025</td><td>zh, en</td><td><a href="https://github.com/drivetosouth/SafeDialBench-Dataset">Code</a></td></tr>
</tbody>
</table>

### Prompt injection and instruction boundaries | 提示注入与指令边界

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>BIPIA</td><td><span title="间接提示注入">间接提示注入</span></td><td>KDD 2025</td><td>en</td><td><a href="https://arxiv.org/abs/2312.14197">Paper</a><br><a href="https://github.com/microsoft/BIPIA">Code</a></td></tr>
<tr><td>HackAPrompt</td><td><span title="提示攻击与越狱">提示攻击与越狱</span></td><td>2023</td><td>英文(含少量多语言混淆)</td><td><a href="https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset">Data</a></td></tr>
<tr><td>IHEval</td><td><span title="Instruction hierarchy">Instruction hierarchy</span></td><td>2025</td><td>en</td><td><a href="https://github.com/ytyz1307zzh/IHEval">Code</a></td></tr>
<tr><td>Open-Prompt-Injection</td><td><span title="Prompt injection">Prompt injection</span></td><td>2024</td><td>en</td><td><a href="https://github.com/liu00222/Open-Prompt-Injection">Code</a></td></tr>
<tr><td>OpenAI IH-Challenge</td><td><span title="指令优先级与提示注入">指令优先级与提示注入</span></td><td>2025</td><td>en</td><td><a href="https://openai.com/index/instruction-hierarchy-challenge/">Project</a></td></tr>
<tr><td>PromptInject</td><td><span title="Prompt injection">Prompt injection</span></td><td>2022</td><td>en</td><td><a href="https://github.com/agencyenterprise/PromptInject">Code</a></td></tr>
<tr><td>Tensor Trust</td><td><span title="直接提示注入与防御">直接提示注入与防御</span></td><td>2023(arXiv)/2024(ICLR)</td><td>en</td><td><a href="https://tensortrust.ai/paper/">Project</a><br><a href="https://github.com/HumanCompatibleAI/tensor-trust">Code</a></td></tr>
</tbody>
</table>

### Bias and fairness | 偏见与公平

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>BBQ</td><td><span title="群体公平与偏见风险（社会偏见问答）">群体公平与偏见风险（社会偏见问答）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/nyu-mll/BBQ">Code</a></td></tr>
<tr><td>BOLD</td><td><span title="群体公平与偏见风险（开放生成公平性，5域43群体）">群体公平与偏见风险（开放生成公平性，5域43群体）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/amazon-science/bold">Code</a></td></tr>
<tr><td>CDIAL-BIAS</td><td><span title="伤害类型7：群体公平与偏见风险">伤害类型7：群体公平与偏见风险</span></td><td>2022</td><td>zh</td><td><a href="https://github.com/para-zhou/CDial-Bias">Code</a><br><a href="https://arxiv.org/abs/2202.08011">Paper</a></td></tr>
<tr><td>HolisticBias</td><td><span title="群体公平与偏见风险（细粒度身份描述词，13个人口学轴）">群体公平与偏见风险（细粒度身份描述词，13个人口学轴）</span></td><td>2022</td><td>en</td><td><a href="https://arxiv.org/abs/2205.09209">Paper</a></td></tr>
<tr><td>HONEST</td><td><span title="群体公平与偏见风险（hurtful句子补全）">群体公平与偏见风险（hurtful句子补全）</span></td><td>2021</td><td>other</td><td><a href="https://aclanthology.org/2021.naacl-main.191/">Paper</a></td></tr>
<tr><td>Social Bias Frames (SBIC)</td><td><span title="结构性偏见与冒犯（group-offense框架）">结构性偏见与冒犯（group-offense框架）</span></td><td>2020</td><td>en</td><td><a href="https://huggingface.co/datasets/allenai/social_bias_frames">Data</a></td></tr>
<tr><td>SocialStigmaQA</td><td><span title="社会污名偏见放大（93个美国污名身份）">社会污名偏见放大（93个美国污名身份）</span></td><td>2023</td><td>en</td><td><a href="https://huggingface.co/datasets/ibm-research/SocialStigmaQA">Data</a></td></tr>
<tr><td>StereoSet</td><td><span title="刻板印象/反刻板印象/无关注续写选择">刻板印象/反刻板印象/无关注续写选择</span></td><td>2020</td><td>en</td><td><a href="https://github.com/moinnadeem/StereoSet">Code</a></td></tr>
<tr><td>SWSR</td><td><span title="伤害类型7：群体公平与偏见风险">伤害类型7：群体公平与偏见风险</span></td><td>2021</td><td>zh</td><td><a href="https://github.com/aggiejiang/SWSR">Code</a><br><a href="https://arxiv.org/abs/2108.03070">Paper</a></td></tr>
</tbody>
</table>

### Values, ethics and cultural norms | 价值观、伦理与文化规范

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>CMoralEval</td><td><span title="价值观">价值观</span></td><td>2024</td><td>zh</td><td><a href="https://github.com/tjunlp-lab/CMoralEval">Code</a></td></tr>
<tr><td>CValues</td><td><span title="—">—</span></td><td>None</td><td>zh</td><td><a href="https://github.com/X-PLUG/CValues">Code</a><br><a href="https://arxiv.org/abs/2307.09705">Paper</a><br><a href="https://modelscope.cn/datasets/damo/CValues-Comparison/summary">Data</a></td></tr>
<tr><td>DailyDilemmas</td><td><span title="价值观">价值观</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/kellycyy/daily_dilemmas">Project</a></td></tr>
<tr><td>ETHICS</td><td><span title="机器伦理/道德判断（正义、义务、美德、常识、功利主义）">机器伦理/道德判断（正义、义务、美德、常识、功利主义）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/hendrycks/ethics">Code</a></td></tr>
<tr><td>GlobalOpinionQA</td><td><span title="价值观对齐（跨国全球观点代表性）">价值观对齐（跨国全球观点代表性）</span></td><td>2023</td><td>en, other</td><td><a href="https://huggingface.co/datasets/Anthropic/llm_global_opinions">Data</a></td></tr>
<tr><td>KorNAT</td><td><span title="价值观">价值观</span></td><td>2024</td><td>other</td><td><a href="https://huggingface.co/datasets/jiyounglee0523/KorNAT">Data</a></td></tr>
<tr><td>MedEthicEval</td><td><span title="价值观">价值观</span></td><td>2025</td><td>zh</td><td><a href="https://github.com/X-LANCE/MedEthicEval">Code</a></td></tr>
<tr><td>Moral Stories</td><td><span title="价值观/社会规范情境推理（规范-意图-情境-行动-后果）">价值观/社会规范情境推理（规范-意图-情境-行动-后果）</span></td><td>2021</td><td>en</td><td><a href="https://github.com/demelin/moral_stories">Code</a></td></tr>
<tr><td>MoralBench</td><td><span title="价值观">价值观</span></td><td>2024</td><td>en</td><td><a href="https://drive.google.com/drive/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7">Project</a></td></tr>
<tr><td>NormAd</td><td><span title="价值观对齐（文化规范适应力，75国）">价值观对齐（文化规范适应力，75国）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/Akhila-Yerukola/NormAd">Code</a></td></tr>
<tr><td>OpinionQA</td><td><span title="价值观对齐（人类观点分布：23个粗粒度+40个细粒度议题，60个美国人口群体）">价值观对齐（人类观点分布：23个粗粒度+40个细粒度议题，60个美国人口群体）</span></td><td>2023</td><td>en</td><td><a href="https://github.com/tatsu-lab/opinions_qa">Code</a></td></tr>
<tr><td>ValueBench</td><td><span title="价值取向探测（44个心理测量量表/453个价值维度）">价值取向探测（44个心理测量量表/453个价值维度）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/ValueByte-AI/ValueBench">Code</a></td></tr>
<tr><td>WorldValuesBench</td><td><span title="价值观">价值观</span></td><td>2024</td><td>en</td><td><a href="https://github.com/Demon702/WorldValuesBench">Code</a></td></tr>
</tbody>
</table>

### Privacy | 隐私

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>ASQ-PHI</td><td><span title="PII泄露">PII泄露</span></td><td>2025</td><td>en</td><td><a href="https://github.com/JamesWeatherhead/asq-phi">Code</a></td></tr>
<tr><td>ConfAIde</td><td><span title="训练数据泄露">训练数据泄露</span></td><td>2024</td><td>en</td><td><a href="https://github.com/skywalker023/confaide/tree/main">Code</a></td></tr>
<tr><td>LM_PersonalInfoLeak</td><td><span title="PII泄露">PII泄露</span></td><td>2022</td><td>en</td><td><a href="https://github.com/jeffhj/LM_PersonalInfoLeak">Code</a></td></tr>
<tr><td>MultiPriv</td><td><span title="PII泄露">PII泄露</span></td><td>2025</td><td>zh, en</td><td><a href="https://github.com/CyberChangAn/MultiPriv-PII">Code</a></td></tr>
<tr><td>PrivacyBench</td><td><span title="训练数据泄露">训练数据泄露</span></td><td>2025</td><td>en</td><td><a href="https://github.com/sri-ja/privacy-bench">Code</a><br><a href="https://arxiv.org/abs/2512.24848">Paper</a></td></tr>
<tr><td>PUPA</td><td><span title="PII泄露">PII泄露</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/Columbia-NLP/PUPA">Data</a></td></tr>
</tbody>
</table>

### Over-refusal | 过度拒答

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>FalseReject</td><td><span title="过度拒答校准（伪有害但实际无害查询）">过度拒答校准（伪有害但实际无害查询）</span></td><td>2025</td><td>en</td><td><a href="https://huggingface.co/datasets/AmazonScience/FalseReject">Data</a></td></tr>
<tr><td>OR-Bench</td><td><span title="过度拒答校准">过度拒答校准</span></td><td>2024</td><td>en</td><td><a href="https://github.com/justincui03/or-bench">Code</a></td></tr>
<tr><td>PHTest</td><td><span title="过度拒答校准（伪有害提示自动生成）">过度拒答校准（伪有害提示自动生成）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/umd-huang-lab/FalseRefusal">Code</a></td></tr>
<tr><td>RASS / MoRBench</td><td><span title="过度拒答校准（安全决策边界模糊提示）">过度拒答校准（安全决策边界模糊提示）</span></td><td>2025</td><td>other</td><td><a href="https://github.com/Master-PLC/RASS">Code</a></td></tr>
<tr><td>XSTest</td><td><span title="过度拒答校准">过度拒答校准</span></td><td>2023</td><td>en</td><td><a href="https://github.com/paul-rottger/xstest">Code</a></td></tr>
</tbody>
</table>

### Autonomy and alignment | 自主性与对齐

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>Anthropic Evals</td><td><span title="—">—</span></td><td>2022</td><td>en</td><td><a href="https://github.com/anthropics/evals">Code</a></td></tr>
<tr><td>CRiskEval</td><td><span title="—">—</span></td><td>2025</td><td>zh</td><td><a href="https://github.com/tjunlp-lab/CRiskEval">Code</a></td></tr>
<tr><td>Myopia_reward</td><td><span title="—">—</span></td><td>2022</td><td>zh</td><td><a href="https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals">Code</a><br><a href="https://arxiv.org/abs/2212.09251">Paper</a></td></tr>
<tr><td>One-box Tendency</td><td><span title="—">—</span></td><td>2022</td><td>zh</td><td><a href="https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals">Code</a><br><a href="https://arxiv.org/abs/2212.09251">Paper</a></td></tr>
<tr><td>Power-seeking</td><td><span title="—">—</span></td><td>2022</td><td>zh</td><td><a href="https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals">Code</a><br><a href="https://arxiv.org/abs/2212.09251">Paper</a></td></tr>
<tr><td>Self-awareness</td><td><span title="—">—</span></td><td>2022</td><td>zh</td><td><a href="https://github.com/anthropics/evals/tree/main/advanced-ai-risk/human_generated_evals">Code</a><br><a href="https://arxiv.org/abs/2212.09251">Paper</a></td></tr>
</tbody>
</table>

### Domain risks | 领域风险

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>CyberSecEval 1/2/3 (Purple Llama)</td><td><span title="不安全代码/网络攻击协助/提示注入（v3含视觉注入与自主网络攻击）">不安全代码/网络攻击协助/提示注入（v3含视觉注入与自主网络攻击）</span></td><td>2023</td><td>en</td><td><a href="https://github.com/meta-llama/PurpleLlama">Code</a></td></tr>
<tr><td>FinSafetyBench</td><td><span title="金融安全（金融犯罪+职业伦理违规，14细分类别）">金融安全（金融犯罪+职业伦理违规，14细分类别）</span></td><td>2026</td><td>zh, en</td><td><a href="https://github.com/sustech-nlp/FinSafetyBench">Code</a></td></tr>
<tr><td>MedSafetyBench</td><td><span title="医疗安全（有害医疗请求应答）">医疗安全（有害医疗请求应答）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/AI4LIFE-GROUP/med-safety-bench">Code</a></td></tr>
<tr><td>SafeSci</td><td><span title="—">—</span></td><td>2026</td><td>en</td><td><a href="https://github.com/yangyangyang127/SafeSci">Code</a></td></tr>
<tr><td>SciSafeEval</td><td><span title="科学语言安全对齐（文本/分子/蛋白/基因组）">科学语言安全对齐（文本/分子/蛋白/基因组）</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2410.03769">Paper</a></td></tr>
<tr><td>WMDP</td><td><span title="生物/化学/网络危险知识测量">生物/化学/网络危险知识测量</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/cais/wmdp">Data</a></td></tr>
</tbody>
</table>

## Agent Safety & Security | Agent 安全

### Prompt injection and instruction boundaries | 提示注入与指令边界

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AgentDojo</td><td><span title="任务覆盖四类真实应用场景：Workspace：邮件、日历、云盘任务，例如统计日程、总结邮件、发送信息；Slack：读取网页/文件、发 Slack 消息、邀请成员；Travel：搜索并预订航班、酒店、餐厅、租车；Banking：转账、支付账单、总结银行流水等。攻击任务则是通过工具返回的不可信内容注入恶意指令，例如泄露邮件、发送 2FA 验证码、发送钓鱼链接、预订最贵酒店、把钱转到攻击者账户等。">任务覆盖四类真实应用场景：Workspace：邮件、日历、云盘任务，例如统计日程、总结邮件、发送信息；Slack：读取网页/文件、发 Slack 消息、邀请成员…</span></td><td>NeurIPS 2024</td><td>en</td><td><a href="https://arxiv.org/abs/2406.13352">Paper</a><br><a href="https://github.com/ethz-spylab/agentdojo">Code</a></td></tr>
<tr><td>AgentDyn</td><td><span title="在开放式动态任务中插入有用但潜在恶意的第三方指令，测试 agent 是否能完成任务同时抵御注入。">在开放式动态任务中插入有用但潜在恶意的第三方指令，测试 agent 是否能完成任务同时抵御注入。</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2602.03117">Paper</a><br><a href="https://github.com/SaFo-Lab/AgentDyn">Code</a></td></tr>
<tr><td>AgentLAB</td><td><span title="测试长程任务中 intent hijacking、tool chaining、task injection、objective drifting、memory poisoning 等自适应攻击。">测试长程任务中 intent hijacking、tool chaining、task injection、objective drifting、memory…</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2602.16901">Paper</a><br><a href="https://tanqiujiang.github.io/AgentLAB_main/">Project</a><br><a href="https://github.com/TanqiuJiang/AgentLAB">Code</a></td></tr>
<tr><td>InjecAgent</td><td><span title="测试任务是：用户先提出一个正常请求，Agent 需要调用某个工具读取外部内容；外部内容中被植入攻击者指令，诱导 Agent 调用其他工具执行有害行为。攻击分两大类：Direct Harm Attack 和 Data Stealing Attack。Direct Harm 包括金融伤害、物理伤害、数据安全破坏等，例如转账、开门、移动私人文件；Data Stealing 包括金融数据、医疗/物理相关数据、搜索历史等隐私外泄，例如读取支付方式、医疗记录、搜索历史并发送给攻击者邮箱。">测试任务是：用户先提出一个正常请求，Agent 需要调用某个工具读取外部内容；外部内容中被植入攻击者指令，诱导 Agent 调用其他工具执行有害行为。攻击分两大…</span></td><td>2024（ACL Findings）</td><td>en</td><td><a href="https://aclanthology.org/2024.findings-acl.624/">Paper</a><br><a href="https://github.com/uiuc-kang-lab/InjecAgent">Code</a></td></tr>
</tbody>
</table>

### General agent safety and misuse | 综合 Agent 安全与滥用

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>Agent Security Bench (ASB)</td><td><span title="任务分为两类：一类是正常任务，例如系统管理员 Agent “识别并修补过期软件漏洞”、学术搜索 Agent 检索和总结论文、金融分析 Agent 做投资分析等；另一类是攻击任务，例如诱导 Agent 调用攻击工具删除客户数据库、导出财务数据、执行错误投资/医疗/法律/自动驾驶等高风险操作。攻击方式包括 Direct Prompt Injection、Indirect Prompt Injection、Memory Poisoning、Plan-of-Thought Backdoor、Mixed Attack。">任务分为两类：一类是正常任务，例如系统管理员 Agent “识别并修补过期软件漏洞”、学术搜索 Agent 检索和总结论文、金融分析 Agent 做投资分析等；…</span></td><td>2024/2025</td><td>en</td><td><a href="https://arxiv.org/abs/2410.02644">Paper</a><br><a href="https://github.com/agiresearch/ASB">Code</a></td></tr>
<tr><td>Agent-SafetyBench</td><td><span title="测试任务覆盖 8 类风险：敏感信息泄露、财产损失、传播不安全/虚假信息、造成物理伤害、违法/伦理违规、破坏可用性、生成/传播有害或脆弱代码、产生不安全/虚假内容。任务不只是问模型“能不能拒答”，而是让 Agent 在邮件、网页、银行、家庭助手、文件、代码、日程、网络等环境中调用工具，观察其是否会因错误工具调用、忽视约束、过度信任工具结果等行为造成风险。">测试任务覆盖 8 类风险：敏感信息泄露、财产损失、传播不安全/虚假信息、造成物理伤害、违法/伦理违规、破坏可用性、生成/传播有害或脆弱代码、产生不安全/虚假内容…</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2412.14470">Paper</a><br><a href="https://github.com/thu-coai/Agent-SafetyBench">Code</a><br><a href="https://huggingface.co/datasets/thu-coai/Agent-SafetyBench">Data</a><br><a href="https://www.semanticscholar.org/reader/7d11400eeb317ebee278f49e108226a4f8555dda">Project</a></td></tr>
<tr><td>AgentHarm</td><td><span title="测试任务是显式恶意的 agentic misuse 请求，覆盖 Fraud、Cybercrime、Self-harm、Harassment、Sexual、Copyright、Drugs、Disinformation、Hate、Violence、Terrorism 11 类。任务通常要求 Agent 执行多步工具调用，并且存在调用顺序依赖：后续工具调用需要利用前一步返回的信息。论文强调这些任务是“digitally realizable behaviors”，但不包含真实姓名、地址、地点等敏感现实信息。">测试任务是显式恶意的 agentic misuse 请求，覆盖 Fraud、Cybercrime、Self-harm、Harassment、Sexual、Cop…</span></td><td>ICLR 2025</td><td>en</td><td><a href="https://arxiv.org/abs/2410.09024">Paper</a><br><a href="https://huggingface.co/datasets/ai-safety-institute/AgentHarm">Data</a><br><a href="https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/">Project</a></td></tr>
<tr><td>Echoes of Human Malice</td><td><span title="多轮网络骚扰智能体攻击">多轮网络骚扰智能体攻击</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2510.14207">Paper</a></td></tr>
<tr><td>HAICosystem</td><td><span title="人机交互伦理安全沙盒">人机交互伦理安全沙盒</span></td><td>2024</td><td>en</td><td><a href="https://github.com/XuhuiZhou/HAICosystem">Code</a></td></tr>
<tr><td>OpenAgentSafety</td><td><span title="评测 agent 使用浏览器、代码、文件系统、bash、消息平台等真实工具时的安全风险。">评测 agent 使用浏览器、代码、文件系统、bash、消息平台等真实工具时的安全风险。</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2507.06134">Paper</a><br><a href="https://github.com/Open-Agent-Safety/OpenAgentSafety">Code</a><br><a href="https://huggingface.co/datasets/sani903/openagentsafety">Data</a></td></tr>
<tr><td>SafePro</td><td><span title="评测专业工作场景中 agent 是否执行不安全专业行为，例如误导性金融/法律/医疗/工程操作或危险文件/代码处理。">评测专业工作场景中 agent 是否执行不安全专业行为，例如误导性金融/法律/医疗/工程操作或危险文件/代码处理。</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2601.06663">Paper</a><br><a href="https://github.com/UCSB-AI/SafePro">Code</a><br><a href="https://safeprobench.github.io/safepro/">Project</a><br><a href="https://huggingface.co/datasets/kzhou35/SafePro">Data</a></td></tr>
</tbody>
</table>

### Tool, API and MCP safety | 工具、API 与 MCP 安全

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>MCIP</td><td><span title="MCP工具调用安全">MCP工具调用安全</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2505.14590">Paper</a></td></tr>
<tr><td>MCP Security Bench (MSB)</td><td><span title="覆盖 MCP 规划、工具调用、响应处理等阶段的攻击，如工具名碰撞、描述注入、越界参数、错误升级、检索注入等。">覆盖 MCP 规划、工具调用、响应处理等阶段的攻击，如工具名碰撞、描述注入、越界参数、错误升级、检索注入等。</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2510.15994">Paper</a><br><a href="https://github.com/dongsenzhang/MSB">Code</a></td></tr>
<tr><td>MCP-TDP</td><td><span title="工具描述/手册投毒">工具描述/手册投毒</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2605.24069">Paper</a></td></tr>
<tr><td>MCPTox</td><td><span title="测试任务是：用户提出一个正常请求，Agent 接入包含正常工具和被投毒工具描述的 MCP 工具列表；攻击者在某个恶意工具的 description 中嵌入规则，诱导 Agent 在完成正常任务时调用另一个“合法高权限工具”执行恶意动作。攻击范式包括三类：Explicit Trigger - Function Hijacking、Implicit Trigger - Function Hijacking、Implicit Trigger - Parameter Tampering。例子包括在执行文件操作前读取 SSH 私钥、发送邮件时偷偷篡改收件人为攻击者邮箱等。">测试任务是：用户提出一个正常请求，Agent 接入包含正常工具和被投毒工具描述的 MCP 工具列表；攻击者在某个恶意工具的 description 中嵌入规则，…</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2508.14925">Paper</a><br><a href="https://anonymous.4open.science/r/AAAI26-7C02">Code</a></td></tr>
<tr><td>RAS-EVAL</td><td><span title="把正常任务转化为攻击任务，测试 agent 在真实或模拟工具环境中是否保持鲁棒、安全和任务完成能力。">把正常任务转化为攻击任务，测试 agent 在真实或模拟工具环境中是否保持鲁棒、安全和任务完成能力。</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2506.15253">Paper</a><br><a href="https://github.com/lanzer-tree/RAS-Eval">Code</a></td></tr>
<tr><td>ToolEmu</td><td><span title="任务关注 instruction underspecification，即用户请求本身是善意的，但存在关键信息缺失或歧义，如果 Agent 不澄清就直接执行，可能造成风险。例如：删除文件释放空间、支付账单、授予门锁权限、分享机密笔记、控制交通灯、操控室内机器人等。风险类型包括 隐私泄露、财务损失、执行错误/低效、物理伤害与安全隐患、声誉损害、计算机安全破坏、法律合规违规、数据丢失/损坏、其他风险">任务关注 instruction underspecification，即用户请求本身是善意的，但存在关键信息缺失或歧义，如果 Agent 不澄清就直接执行，可…</span></td><td>2023/ICLR 2024</td><td>en</td><td><a href="https://arxiv.org/abs/2309.15817">Paper</a><br><a href="https://github.com/ryoungj/ToolEmu">Code</a></td></tr>
<tr><td>ToolSword</td><td><span title="工具学习全流程安全（输入/执行/输出三阶段六场景）">工具学习全流程安全（输入/执行/输出三阶段六场景）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/Junjie-Ye/ToolSword">Code</a></td></tr>
</tbody>
</table>

### Privacy and memory | 隐私与记忆

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AgentDAM</td><td><span title="智能体隐私最小化/隐私泄露">智能体隐私最小化/隐私泄露</span></td><td>2025</td><td>en</td><td><a href="https://github.com/facebookresearch/ai-agent-privacy">Code</a></td></tr>
<tr><td>AgentLeak</td><td><span title="评测多 agent 系统中隐私信息是否通过内部消息、共享记忆、工具参数等通道泄露。">评测多 agent 系统中隐私信息是否通过内部消息、共享记忆、工具参数等通道泄露。</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2602.11510">Paper</a><br><a href="https://github.com/Privatris/AgentLeak">Code</a><br><a href="https://huggingface.co/datasets/humain2/AgentLeak">Data</a></td></tr>
<tr><td>PrivacyLens</td><td><span title="情境化隐私规范/PII泄露（智能体行动）">情境化隐私规范/PII泄露（智能体行动）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/SALT-NLP/PrivacyLens">Code</a></td></tr>
</tbody>
</table>

### Web, computer and mobile agents | 网页、桌面与移动 Agent

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AgentHazard</td><td><span title="将有害目标拆成局部看似合理的步骤，测试 agent 是否能在多轮工具使用中识别并中止累计风险。">将有害目标拆成局部看似合理的步骤，测试 agent 是否能在多轮工具使用中识别并中止累计风险。</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2604.02947">Paper</a><br><a href="https://github.com/Yunhao-Feng/AgentHazard">Code</a><br><a href="https://yunhao-feng.github.io/AgentHazard/">Project</a></td></tr>
<tr><td>CUAHarm</td><td><span title="测试 computer-use agent 是否会完成禁用防火墙、泄露机密、发起 DoS、安装后门等误用目标。">测试 computer-use agent 是否会完成禁用防火墙、泄露机密、发起 DoS、安装后门等误用目标。</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2508.00935">Paper</a><br><a href="https://github.com/db-ol/CUAHarm">Code</a><br><a href="https://huggingface.co/datasets/CUAHarm/CUAHarm">Data</a></td></tr>
<tr><td>MobileSafetyBench</td><td><span title="移动设备操作安全 / 间接提示注入">移动设备操作安全 / 间接提示注入</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2410.17520">Paper</a><br><a href="https://github.com/jylee425/mobilesafetybench">Code</a><br><a href="https://mobilesafetybench.github.io">Project</a></td></tr>
<tr><td>RiOSWorld</td><td><span title="真实 GUI 高风险操作">真实 GUI 高风险操作</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2506.00618">Paper</a><br><a href="https://yjyddq.github.io/RiOSWorld.github.io/">Project</a></td></tr>
<tr><td>SABER</td><td><span title="评测编码 agent 在项目工作区中面对恶意环境内容、风险自选择、上下文警告时是否执行有害命令或传播风险。">评测编码 agent 在项目工作区中面对恶意环境内容、风险自选择、上下文警告时是否执行有害命令或传播风险。</span></td><td>2026</td><td>中英混合, 英语为主</td><td><a href="https://arxiv.org/abs/2606.01317">Paper</a><br><a href="https://github.com/sssr-lab/saber">Code</a></td></tr>
<tr><td>SafeArena</td><td><span title="网页智能体恶意任务多轮执行">网页智能体恶意任务多轮执行</span></td><td>2025</td><td>en</td><td><a href="https://github.com/McGill-NLP/safearena">Code</a></td></tr>
<tr><td>ST-WebAgentBench</td><td><span title="在企业 Web 工作流中测试 agent 是否既完成任务又遵守安全可信策略，例如权限、隐私、合规和风险约束。">在企业 Web 工作流中测试 agent 是否既完成任务又遵守安全可信策略，例如权限、隐私、合规和风险约束。</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2410.06703">Paper</a><br><a href="https://sites.google.com/view/st-webagentbench/home">Project</a><br><a href="https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench">Data</a><br><a href="https://github.com/segev-shlomov/ST-WebAgentBench">Code</a></td></tr>
<tr><td>WASP</td><td><span title="测试网页中的恶意内容是否能劫持 Web agent，使其偏离用户目标并执行攻击者目标。">测试网页中的恶意内容是否能劫持 Web agent，使其偏离用户目标并执行攻击者目标。</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2504.18575">Paper</a><br><a href="https://github.com/facebookresearch/wasp">Code</a></td></tr>
</tbody>
</table>

### Embodied safety | 具身安全

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>SafeAgentBench</td><td><span title="具身任务规划与物理安全">具身任务规划与物理安全</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2412.13178">Paper</a><br><a href="https://safeagentbench.github.io">Project</a><br><a href="https://github.com/shengyin1224/SafeAgentBench">Code</a></td></tr>
</tbody>
</table>

## Safety Judging & Guardrails | 安全审查与护栏

### Agent trajectories and action safety | Agent 轨迹与动作安全

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>ATBench</td><td><span title="完整轨迹安全判断与风险归因">完整轨迹安全判断与风险归因</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2604.02022">Paper</a><br><a href="https://github.com/LiYu0524/ATbench">Code</a><br><a href="https://huggingface.co/datasets/AI45Research/ATBench">Data</a></td></tr>
<tr><td>PhoneSafety</td><td><span title="手机关键决策下一动作安全">手机关键决策下一动作安全</span></td><td>2025</td><td>中文为主</td><td><a href="https://arxiv.org/abs/2605.07630">Paper</a><br><a href="https://github.com/tangzhy/PhoneSafety">Code</a><br><a href="https://huggingface.co/datasets/phonesafety-anon/PhoneSafety_Data">Data</a></td></tr>
<tr><td>R-Judge</td><td><span title="既有 Agent 轨迹风险识别">既有 Agent 轨迹风险识别</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2401.10019">Paper</a><br><a href="https://github.com/Lordog/R-Judge">Code</a></td></tr>
<tr><td>SafeToolBench</td><td><span title="执行前风险识别">执行前风险识别</span></td><td>2025</td><td>en</td><td><a href="https://aclanthology.org/2025.findings-emnlp.958.pdf">Paper</a><br><a href="https://github.com/BITHLP/SafeToolBench">Code</a></td></tr>
<tr><td>SleightBench</td><td><span title="恶意编码轨迹监控与规避检测">恶意编码轨迹监控与规避检测</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2605.16626">Paper</a><br><a href="https://github.com/safety-research/sleight-bench">Code</a></td></tr>
<tr><td>ToolSafe / TS-Bench</td><td><span title="候选工具调用安全分类">候选工具调用安全分类</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2601.10156">Paper</a><br><a href="https://github.com/MurrayTom/ToolSafe">Code</a></td></tr>
<tr><td>TOP-Bench</td><td><span title="跨工具组合推断导致的隐私泄露">跨工具组合推断导致的隐私泄露</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2512.16310">Paper</a><br><a href="https://github.com/1Ponder/TOP-R">Code</a><br><a href="https://www.semanticscholar.org/paper/f143043c62cbe142d99067328f2de1ec8b01f082">Project</a></td></tr>
<tr><td>TraceSafe-Bench</td><td><span title="多步工具轨迹风险检测">多步工具轨迹风险检测</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2604.07223">Paper</a><br><a href="https://github.com/cycraft-corp/TraceSafe">Code</a><br><a href="https://huggingface.co/datasets/CyCraftAI/TraceSafe">Data</a></td></tr>
<tr><td>WebGuard</td><td><span title="网页操作风险分级护栏">网页操作风险分级护栏</span></td><td>2025</td><td>en</td><td><a href="https://github.com/OSU-NLP-Group/WebGuard">Code</a></td></tr>
</tbody>
</table>

### Content guardrail evaluation | 内容护栏评测

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>GuardBench</td><td><span title="护栏模型评测（统一聚合40个安全评测数据集）">护栏模型评测（统一聚合40个安全评测数据集）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/AmenRa/guardbench">Code</a></td></tr>
<tr><td>WildGuard (WildGuardMix/WildGuardTest)</td><td><span title="护栏审核（用户意图识别/回复有害性判定/拒答检测，13风险类）">护栏审核（用户意图识别/回复有害性判定/拒答检测，13风险类）</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/allenai/wildguardmix">Data</a></td></tr>
</tbody>
</table>

## Related Resources | 相关资源

### Training datasets | 训练数据

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>Aegis 1.0 (Nemotron Content Safety Dataset V1)</td><td><span title="护栏审核（13类关键风险内容安全分类）">护栏审核（13类关键风险内容安全分类）</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0">Data</a></td></tr>
<tr><td>GuardReasoner (GuardReasonerTrain)</td><td><span title="护栏审核（推理型安全防护，3类护栏任务/13个基准）">护栏审核（推理型安全防护，3类护栏任务/13个基准）</span></td><td>2025</td><td>en</td><td><a href="https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain">Data</a></td></tr>
<tr><td>HarmfulQA (RED-INSTRUCT)</td><td><span title="有害问答红队（直接+越狱提问，10主题）">有害问答红队（直接+越狱提问，10主题）</span></td><td>2023</td><td>en</td><td><a href="https://huggingface.co/datasets/TrustAIRLab/HarmfulQA">Data</a></td></tr>
<tr><td>HH-RLHF（含Red Team Attempts）</td><td><span title="无害性偏好数据+人工红队对话">无害性偏好数据+人工红队对话</span></td><td>2022</td><td>en</td><td><a href="https://github.com/anthropics/hh-rlhf">Code</a></td></tr>
<tr><td>Nemotron Content Safety Dataset V2</td><td><span title="—">—</span></td><td>2025</td><td>en</td><td><a href="https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0">Data</a></td></tr>
<tr><td>NVIDIA Nemotron Agentic IPI</td><td><span title="工具返回中的间接提示注入">工具返回中的间接提示注入</span></td><td>2026</td><td>en</td><td><a href="https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1">Data</a></td></tr>
<tr><td>PKU-SafeRLHF (10K/30K)</td><td><span title="安全偏好标注（红队提示+细粒度安全标签）">安全偏好标注（红队提示+细粒度安全标签）</span></td><td>2023</td><td>en</td><td><a href="https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K">Data</a></td></tr>
<tr><td>SafeMTData（Derail Yourself/ActorAttack配套）</td><td><span title="自然分布偏移多轮攻击">自然分布偏移多轮攻击</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/SafeMTData/SafeMTData">Data</a></td></tr>
<tr><td>ToolSafety</td><td><span title="安全工具调用数据与微调">安全工具调用数据与微调</span></td><td>EMNLP 2025</td><td>en</td><td><a href="https://aclanthology.org/2025.emnlp-main.714.pdf">Paper</a><br><a href="https://huggingface.co/datasets/jinjinyien/ToolSafety">Data</a></td></tr>
<tr><td>X-Teaming Evolutionary M2S</td><td><span title="多轮到单轮越狱模板自动发现">多轮到单轮越狱模板自动发现</span></td><td>2025</td><td>en</td><td><a href="https://huggingface.co/datasets/hyunjun1121/X-Teaming_Evolutionary_M2S">Data</a></td></tr>
<tr><td>XGuard-Train-Open-200K</td><td><span title="护栏审核训练数据（9大风险维度/28细分类别，多语言）">护栏审核训练数据（9大风险维度/28细分类别，多语言）</span></td><td>2026</td><td>other</td><td><a href="https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K">Data</a></td></tr>
<tr><td>XGuard-Train（X-Teaming配套）</td><td><span title="多智能体自适应多轮越狱训练集">多智能体自适应多轮越狱训练集</span></td><td>2025</td><td>en</td><td><a href="https://huggingface.co/datasets/marslabucla/XGuard-Train">Data</a></td></tr>
</tbody>
</table>

### Attack methods | 攻击方法

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AgentPoison</td><td><span title="向Agent的外部知识库或memory中注入恶意数据，并通过优化触发器提高投毒内容的检索概率，评估RAG poisoning攻击对Agent行为和输出的影响">向Agent的外部知识库或memory中注入恶意数据，并通过优化触发器提高投毒内容的检索概率，评估RAG poisoning攻击对Agent行为和输出的影响</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2407.12784">Paper</a><br><a href="https://github.com/AI-secure/AgentPoison">Code</a><br><a href="https://billchan226.github.io/AgentPoison.html">Project</a></td></tr>
<tr><td>ArtPrompt</td><td><span title="ASCII艺术编码越狱">ASCII艺术编码越狱</span></td><td>2024</td><td>en</td><td><a href="https://github.com/uw-nsl/ArtPrompt">Code</a></td></tr>
<tr><td>AutoDAN</td><td><span title="隐蔽越狱提示生成">隐蔽越狱提示生成</span></td><td>2024</td><td>en</td><td><a href="https://github.com/SheltonLiu-N/AutoDAN">Code</a></td></tr>
<tr><td>Automating Deception（FITD多轮越狱）</td><td><span title="登门槛效应（Foot-in-the-Door）心理操纵多轮越狱">登门槛效应（Foot-in-the-Door）心理操纵多轮越狱</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2511.19517">Paper</a></td></tr>
<tr><td>CipherChat</td><td><span title="密码编码越狱">密码编码越狱</span></td><td>2024</td><td>zh, en</td><td><a href="https://github.com/RobustNLP/CipherChat">Code</a></td></tr>
<tr><td>CodeChameleon</td><td><span title="个性化加密越狱">个性化加密越狱</span></td><td>2024</td><td>en</td><td><a href="https://github.com/huizhang-L/CodeChameleon">Code</a></td></tr>
<tr><td>Crescendo</td><td><span title="渐进式对话升级越狱">渐进式对话升级越狱</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2404.01833">Paper</a></td></tr>
<tr><td>Curiosity-driven Red Teaming</td><td><span title="好奇心驱动自动红队">好奇心驱动自动红队</span></td><td>2024</td><td>en</td><td><a href="https://github.com/Improbable-AI/curiosity_redteam">Code</a></td></tr>
<tr><td>DeepInception</td><td><span title="场景嵌套越狱">场景嵌套越狱</span></td><td>2023</td><td>en</td><td><a href="https://github.com/tmlr-group/DeepInception">Code</a></td></tr>
<tr><td>GPTFuzzer</td><td><span title="越狱模板变异模糊测试">越狱模板变异模糊测试</span></td><td>2023</td><td>en</td><td><a href="https://github.com/hubertyoo/GPTFuzz">Code</a></td></tr>
<tr><td>Latent Jailbreak</td><td><span title="隐式/潜在越狱">隐式/潜在越狱</span></td><td>2023</td><td>英文+中文</td><td><a href="https://github.com/qiuhuachuan/latent-jailbreak">Code</a></td></tr>
<tr><td>MART</td><td><span title="多轮自动红队攻防迭代">多轮自动红队攻防迭代</span></td><td>2023</td><td>en</td><td><a href="https://arxiv.org/abs/2311.07689">Paper</a></td></tr>
<tr><td>MemoryGraft</td><td><span title="经验检索投毒与持久行为漂移">经验检索投毒与持久行为漂移</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2512.16962">Paper</a><br><a href="https://github.com/Jacobhhy/MemoryGraft">Code</a><br><a href="https://www.semanticscholar.org/reader/b1d80b2eda7e175e235185bdc7df4e8233f36ef4">Project</a></td></tr>
<tr><td>PsychJail</td><td><span title="社会心理学说服策略多轮红队">社会心理学说服策略多轮红队</span></td><td>2026</td><td>en</td><td><a href="https://github.com/FengZeyugit/PsychJail">Code</a></td></tr>
<tr><td>ReNeLLM</td><td><span title="嵌套提示越狱（提示改写+56种场景嵌套）">嵌套提示越狱（提示改写+56种场景嵌套）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/NJUNLP/ReNeLLM">Code</a></td></tr>
</tbody>
</table>

### Frameworks and mixed resources | 框架及混合资源

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>AgentDefense-Bench</td><td><span title="MCP 请求检测与阻断">MCP 请求检测与阻断</span></td><td>2025</td><td>en</td><td><a href="https://github.com/arunsanna/AgentDefense-Bench">Code</a></td></tr>
<tr><td>CC-BOS</td><td><span title="—">—</span></td><td>2026</td><td>zh</td><td><a href="https://github.com/xaoLiu1222/cc-bos">Code</a></td></tr>
<tr><td>LiveSecBench</td><td><span title="—">—</span></td><td>2026</td><td>zh</td><td><a href="https://github.com/ydli-ai/LiveSecBench">Code</a></td></tr>
<tr><td>ORFuzz</td><td><span title="过度拒答校准（演化模糊测试）">过度拒答校准（演化模糊测试）</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2508.11222">Paper</a></td></tr>
<tr><td>ShieldLM</td><td><span title="护栏审核（中英双语安全检测，safe/unsafe/controversial三分类）">护栏审核（中英双语安全检测，safe/unsafe/controversial三分类）</span></td><td>2024</td><td>zh, en</td><td><a href="https://github.com/thu-coai/ShieldLM">Code</a></td></tr>
<tr><td>TrustAgent</td><td><span title="智能体规划安全宪法">智能体规划安全宪法</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2402.01586">Paper</a></td></tr>
<tr><td>WILDTEAMING / WildJailbreak</td><td><span title="越狱策略挖掘与对抗安全训练">越狱策略挖掘与对抗安全训练</span></td><td>2024</td><td>en</td><td><a href="https://github.com/allenai/wildteaming">Code</a></td></tr>
</tbody>
</table>

### Attack challenges and data | 攻击挑战与数据

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>LLMail-Inject</td><td><span title="邮件场景间接提示注入">邮件场景间接提示注入</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2506.09956">Paper</a><br><a href="https://github.com/microsoft/llmail-inject-challenge">Code</a></td></tr>
</tbody>
</table>

### Capability baselines and environments | 能力基线与环境

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>Agent-Diff</td><td><span title="工作流状态差分与任务完成">工作流状态差分与任务完成</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2602.11224">Paper</a><br><a href="https://github.com/agent-diff-bench/agent-diff">Code</a><br><a href="https://www.agentdiff.dev">Project</a><br><a href="https://huggingface.co/datasets/hubertmarek/agent-diff-bench">Data</a></td></tr>
<tr><td>API-Bank</td><td><span title="API 理解、检索、调用与回答">API 理解、检索、调用与回答</span></td><td>EMNLP 2023</td><td>en</td><td><a href="https://arxiv.org/abs/2304.08244">Paper</a></td></tr>
<tr><td>AppWorld</td><td><span title="跨应用任务完成与代码执行能力">跨应用任务完成与代码执行能力</span></td><td>ACL 2024</td><td>en</td><td><a href="https://aclanthology.org/2024.acl-long.850/">Paper</a><br><a href="https://github.com/StonyBrookNLP/appworld">Code</a><br><a href="https://appworld.dev">Project</a></td></tr>
<tr><td>BFCL</td><td><span title="函数选择、参数生成与多步调用">函数选择、参数生成与多步调用</span></td><td>2024/2025，持续更新至 V4</td><td>英语为主, 多语言函数调用场景</td><td><a href="https://proceedings.mlr.press/v267/patil25a.html">Paper</a><br><a href="https://gorilla.cs.berkeley.edu/leaderboard.html">Project</a><br><a href="https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard">Data</a></td></tr>
<tr><td>SkillsBench</td><td><span title="Skill 使用与能力增益">Skill 使用与能力增益</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2602.12670">Paper</a><br><a href="https://www.skillsbench.ai">Project</a><br><a href="https://github.com/benchflow-ai/skillsbench">Code</a></td></tr>
<tr><td>tau-bench</td><td><span title="规则遵循、任务完成与稳定性">规则遵循、任务完成与稳定性</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2406.12045">Paper</a><br><a href="https://github.com/sierra-research/tau-bench">Code</a><br><a href="https://www.semanticscholar.org/reader/70aa016c1f68fd5c0261f26ad20017b8307650af">Project</a></td></tr>
<tr><td>TheAgentCompany</td><td><span title="办公、编码和协作任务完成">办公、编码和协作任务完成</span></td><td>2024/2025</td><td>en</td><td><a href="https://arxiv.org/abs/2412.14161">Paper</a><br><a href="https://github.com/TheAgentCompany/TheAgentCompany">Code</a><br><a href="https://the-agent-company.com">Project</a></td></tr>
<tr><td>TOOLATHLON</td><td><span title="多工具任务完成与效率">多工具任务完成与效率</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2510.25726">Paper</a><br><a href="https://github.com/hkust-nlp/Toolathlon">Code</a></td></tr>
<tr><td>ToolSandbox</td><td><span title="多轮有状态工具调用能力">多轮有状态工具调用能力</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2408.04682">Paper</a><br><a href="https://github.com/apple-aiml-research/ToolSandbox">Code</a><br><a href="https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark">Project</a></td></tr>
<tr><td>WebArena</td><td><span title="网页导航与任务完成">网页导航与任务完成</span></td><td>ICLR 2024 / NeurIPS 2024 Oral 相关项目口径</td><td>en</td><td><a href="https://arxiv.org/abs/2307.13854">Paper</a><br><a href="https://github.com/web-arena-x/webarena">Code</a><br><a href="https://webarena.dev">Project</a></td></tr>
<tr><td>WorkArena</td><td><span title="ServiceNow 任务完成">ServiceNow 任务完成</span></td><td>ICML 2024</td><td>en</td><td><a href="https://arxiv.org/abs/2403.07718">Paper</a><br><a href="https://github.com/ServiceNow/workarena">Code</a><br><a href="https://servicenow.github.io/WorkArena/">Project</a></td></tr>
</tbody>
</table>

### Factuality and general trace diagnostics | 事实性与通用轨迹诊断

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>HaluEval</td><td><span title="幻觉识别与生成">幻觉识别与生成</span></td><td>2023</td><td>en</td><td><a href="https://arxiv.org/abs/2305.11747">Paper</a><br><a href="https://github.com/RUCAIBox/HaluEval">Code</a></td></tr>
<tr><td>RAGTruth</td><td><span title="幻觉与事实一致性">幻觉与事实一致性</span></td><td>2023</td><td>en</td><td><a href="https://arxiv.org/abs/2401.00396">Paper</a></td></tr>
<tr><td>SimpleQA</td><td><span title="事实问答准确性">事实问答准确性</span></td><td>2024</td><td>en</td><td><a href="https://arxiv.org/abs/2411.04368">Paper</a><br><a href="https://github.com/openai/simple-evals">Code</a></td></tr>
<tr><td>TraceElephant</td><td><span title="责任组件与关键失败步骤定位">责任组件与关键失败步骤定位</span></td><td>2026</td><td>en</td><td><a href="https://arxiv.org/abs/2604.22708">Paper</a><br><a href="https://github.com/TraceElephant/TraceElephant">Code</a><br><a href="https://huggingface.co/datasets/TraceElephant/TraceElephant">Data</a></td></tr>
<tr><td>TRAIL</td><td><span title="错误分类与 trace span 定位">错误分类与 trace span 定位</span></td><td>2025</td><td>en</td><td><a href="https://arxiv.org/abs/2505.08638">Paper</a><br><a href="https://huggingface.co/datasets/PatronusAI/TRAIL">Data</a></td></tr>
</tbody>
</table>

### Domain capability benchmarks | 领域能力基准

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>CTIBench</td><td><span title="网络威胁情报CTI任务（MCQ/根因映射/归因/ATT&amp;CK提取）">网络威胁情报CTI任务（MCQ/根因映射/归因/ATT&amp;CK提取）</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/AI4Sec/cti-bench">Data</a></td></tr>
<tr><td>CyberMetric</td><td><span title="网络安全知识（基于NIST框架/RAG生成）">网络安全知识（基于NIST框架/RAG生成）</span></td><td>2024</td><td>en</td><td><a href="https://github.com/cybermetric/CyberMetric">Code</a></td></tr>
<tr><td>HealthBench</td><td><span title="医疗安全（急诊转诊/不安全响应/情境理解等）">医疗安全（急诊转诊/不安全响应/情境理解等）</span></td><td>2025</td><td>en</td><td><a href="https://huggingface.co/datasets/openai/healthbench">Data</a></td></tr>
<tr><td>LawBench</td><td><span title="法律安全（法条/罪名/刑期预测、犯罪金额计算等20任务）">法律安全（法条/罪名/刑期预测、犯罪金额计算等20任务）</span></td><td>2023</td><td>zh</td><td><a href="https://github.com/open-compass/LawBench">Code</a></td></tr>
<tr><td>SecEval</td><td><span title="网络安全知识（系统/Web/渗透/漏洞/密码学等9子领域）">网络安全知识（系统/Web/渗透/漏洞/密码学等9子领域）</span></td><td>2023</td><td>en</td><td><a href="https://github.com/XuanwuAI/SecEval">Code</a></td></tr>
</tbody>
</table>

### Components of listed suites | 已收录基准的子集

<table width="100%">
<colgroup>
  <col width="18%">
  <col width="46%">
  <col width="10%">
  <col width="10%">
  <col width="16%">
</colgroup>
<thead>
<tr><th width="18%">Resource</th><th width="46%">Description</th><th width="10%">Year</th><th width="10%">Language</th><th width="16%">Links</th></tr>
</thead>
<tbody>
<tr><td>DecodingTrust（Privacy 子集）</td><td><span title="PII泄露">PII泄露</span></td><td>2023</td><td>en</td><td><a href="https://github.com/AI-secure/DecodingTrust">Code</a></td></tr>
<tr><td>JBB-Behaviors</td><td><span title="Jailbreak攻击">Jailbreak攻击</span></td><td>2024</td><td>en</td><td><a href="https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors">Data</a></td></tr>
</tbody>
</table>

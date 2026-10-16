# Contributing

Contributions should help readers choose an evaluation for a concrete LLM or agent safety question.

## Add or update a resource

1. Search the JSON catalog for the name, aliases, paper and repository. Update an existing record when appropriate. Add a parent relationship for a component rather than counting it as a new independent suite.
2. Add primary evidence: an official paper, code repository, dataset page or project site. Preserve the source URL and the claim it supports. An aggregator homepage alone is insufficient for the main navigation.
3. Classify the evaluation target and resource type using [the taxonomy](docs/taxonomy.md). Training data, attack methods and generic capability benchmarks belong under related resources.
4. Add concise English and Chinese descriptions for public entries. Record language, split, version, scale, metrics and environment descriptions when supplied by the source. Keep missing metadata null. This collection provides access links; license review and runnable implementations are not inclusion requirements.
5. Check that the linked resource page is reachable, record the date and distinguish redirects, missing pages and restricted access. Link checks concern the page; other metadata retains its source attribution.
6. Edit `data/benchmarks.json`, then regenerate and validate:

```powershell
python scripts/build_readme.py
python scripts/validate.py
python scripts/build_readme.py --check
```

Check all recorded resource links and refresh the generated pages:

```powershell
python scripts/check_links.py
python scripts/apply_link_checks.py
python scripts/build_readme.py
python scripts/validate.py
```

The checker uses HEAD requests with a bounded HTML/text fallback. It does not fetch dataset files, clone repositories or download paper PDFs. Access restrictions and network errors remain distinct from confirmed missing pages.

The catalog and generator require Python 3.10+. Importing historical XLSX files additionally requires `openpyxl`.

`scripts/curate.py` rebuilds the **initial import** from the historical snapshots and explicit decisions in `data/curation.json`. Do not run it over later manually curated catalog changes unless you have incorporated those changes into the import inputs. Routine additions use the canonical JSON and README generator.

## Evidence and scope

Distinguish agent tool-call selection, synthetic tool execution, LM-emulated tools, stateful sandboxes and effects on external systems. Identify static action/trajectory judging separately from agent execution. Record both safety and utility metrics where the source reports them.

Historical screening conclusions refer to the earlier evaluator and its environment. They are evidence to consider, not instructions governing this collection. A GUI safety benchmark can be relevant even when the maintainer cannot run its environment locally.

Do not include collector names, local machine paths, raw attack examples, credentials or original private workbooks in contributions. Public provenance uses source IDs, worksheet names and row/cell references.

<a id="taxonomy-feedback"></a>

## Improve the taxonomy | 改进分类

The [candidate risk taxonomy](docs/taxonomy-proposal.md) is under validation. See the [design rationale](docs/taxonomy-rationale.md) and [validation roadmap](docs/taxonomy-validation.md) before proposing changes. Current catalog navigation continues to use evaluation tracks and topics.

建议提交可裁决的具体问题：

1. **对象与版本：** 标签 ID、资源／任务组件及版本。
2. **证据定位：** 官方 URL、来源版本、章节／任务 ID 和简短证据摘要。内部材料注明未公开，保留原文权限。
3. **边界问题：** 当前定义为何不适用？与哪个近邻标签混淆？风险、机制、场景或协议是否混在一起？
4. **修改建议：** 合并、拆分、改名或移轴，以及对现有映射的影响。附一个正例和一个近邻反例的概述。

维护者修改候选标签时，编辑 `docs/taxonomy-proposal-v0.1.json`，同步记录 `docs/taxonomy-validation.md` 的变更理由，再运行上方生成与检查命令。`docs/taxonomy-proposal.md` 由 JSON 自动生成。公开贡献只引用可公开的来源定位；详细证据缓存保留在维护者本地。

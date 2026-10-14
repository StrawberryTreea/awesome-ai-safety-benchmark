# Data schema and maintenance

`data/benchmarks.json` is the canonical catalog. Both READMEs, CSV exports and summary statistics are generated from it. The unresolved-review data is retained in `data/review_queue.csv` and the private `.local/review_queue.md` maintenance artifact; it is not published as a GitHub page. The initial import used five supplied XLSX files; future additions can use new source records with primary evidence.

| Field | Meaning |
| --- | --- |
| `id` | Stable ASCII identifier; retain it when a display name changes |
| `name`, `aliases` | Canonical display name and source name variants |
| `track`, `topic`, `resource_type` | Evaluation target, navigation topic and resource identity |
| `catalog_status` | `listed`, `related` or `needs_review`; separate from verification |
| `description_zh` | Short source-derived description, null when missing |
| `year` | Parsed source year only when unambiguous; null for multiple years |
| `languages` | Normalized unambiguous language labels; unusual source labels retained |
| `reported_metadata` | Original values with source IDs, cells and alternative expressions |
| `links` | All URLs, resource type, quality flag and supporting source references |
| `verification` | Import date, latest link check date and checks performed |
| `issues`, `curation_note_zh` | Machine-readable issue flags and the curation rationale |
| `parent_id`, `parent_name` | Parent suite for a component; null for standalone resources |
| `source_refs` | Every supporting source record, including duplicated screening views |
| `historical_screening` | Historical platform decisions, retained as source material |

`reported_metadata` stores `year`, `languages`, `size`, `tasks`, `environment`, `execution`, `execution_notes`, `evaluation`, `metrics`, `availability`, `maturity` and `multi_turn`. Each value includes `value`, `source_ref`, `field`, `cell` and `alternatives`. `metadata_variant_fields` denotes different source expressions; these may reflect versions or verbosity rather than factual contradictions.

For overlapping rows, the initial import selects a nonempty field from the v2 core verification table, v2 final screening table, v2 detailed screening, original Agent collection, original LLM collection and earlier rescreening, in that order. Within a sheet, earlier row numbers take precedence. All alternatives remain available. This is source precedence, not external confirmation.

URL normalization removes trailing slashes and normalizes arXiv HTML/PDF/version links to abstract IDs; raw URL forms remain in source records. Original URLs remain in the catalog, with live redirect targets recorded separately. Navigation uses an observed reachable redirect target and prefers reachable links of each resource type. Confirmed missing pages and placeholders are omitted from the navigation; restricted pages remain explicitly labeled.

Each link's `access` field records `status`, `checked_at`, `http_status`, `final_url`, redirect chain and diagnostic evidence. `data/link_checks.json` preserves the unique-URL audit and attempts; `docs/link-check-report.md` summarizes it. Statuses distinguish `accessible`, `redirected`, `not_found`, `restricted`, `login_required`, `network_error`, `server_error`, `http_error` and explicitly skipped placeholders. A page check does not update source-reported benchmark metadata.

This is a collection of access links. License review, dataset downloads and benchmark reproduction are outside the maintenance scope and are not inclusion gates.

`data/source_records.json` preserves nonprivate source fields and coordinates. `data/sources.json` records workbook filenames, SHA-256 hashes and sheet counts. Source references have the form `source_id:sheet:row`. Absolute input paths, collector names, examples and full cell snapshots remain local under `.local/` or in the original workbooks.

## Future additions

1. Add a source description to `data/sources.json`, using a new ID and the available primary evidence. Set its `named_rows` to the number of corresponding source records. A new web source can use `filename` as its short title and a `url` field; it does not need a workbook hash or worksheet inventory.
2. Add one or more provenance records to `data/source_records.json` with a stable `record_id`, `source_id`, `sheet` (e.g. `web`), `row` (sequence number), `name`, `fields`, `cells` and `hyperlinks`. For web evidence, record claim URLs in `fields` and leave `cells` empty.
3. Add or update the catalog entry, preserving field provenance. Unsupported metadata stays null. Use an existing navigation topic or extend the generator's documented topic mapping.
4. Run the README generator, validator and generated-file check. Use `data/review_queue.csv` or the private `.local/review_queue.md` artifact for unresolved identity or scope questions.

Before live checking, imported records have `verification.status=imported_unverified`, `last_link_check=null` and `link_access_checked=false`. After checking actual links, the status becomes `links_checked`, the actual check date is recorded and the per-link outcomes remain available. Entries containing only skipped links have `status=link_sources_pending`, no check date and `link_access_checked=false`. The import date is **not** a link check date.

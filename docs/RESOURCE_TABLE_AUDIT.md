# Topic-Grouped Resource Table Audit

[Home](../README.md) · [Resource policy](RESOURCE_POLICY.md) · [Book order](READING_GUIDE.md)

Baseline: `4f44edffa977a6cbaa2924963707e45a31d64b50`. This correction restores resource tables while retaining the guided README architecture. It does not change the syllabus, prerequisite graph, book order or project contracts.

## Presentation contract

Each resource library follows its README topics. Every group has one recommended route, an explicit sequence for different required concepts, bounded choices where genuine overlap exists, and implementation references. Resource roles are local to that group. Other complements are clearly as-needed; paid/advanced resources do not block completion.

Five consistent columns keep the table scannable: **Resource · Provider · Language**, **Resource Type**, **Role in this group**, **Topic / subtopic**, **Study only**. Full bounds, access, scope limits and verification notes remain expandable. A video in a playlist is labelled **Single Video (part of playlist)**. No timestamps or unverifiable playlist lesson numbers were invented.

## All-Level coverage

| Level | Topic tables / direct step links | Bounded alternative groups | Required complementary additions | Resources retained |
|---|---|---|---|---|
| [L00](../00-Orientation/resources.md) | 5 / 5 | 2 | 0 | 19 |
| [L01](../01-Python-FastAPI/resources.md) | 6 / 6 | 2 | 1 | 19 |
| [L02](../02-Mathematics-ML/resources.md) | 6 / 6 | 2 | 0 | 15 |
| [L03](../03-Deep-Learning-Foundation-Models/resources.md) | 6 / 6 | 1 | 1 | 14 |
| [L04](../04-LLM-Applications-Prompts/resources.md) | 6 / 6 | 1 | 0 | 19 |
| [L05](../05-Evaluation/resources.md) | 6 / 6 | 1 | 0 | 13 |
| [L06](../06-Application-State/resources.md) | 6 / 6 | 2 | 0 | 11 |
| [L07](../07-Embeddings-Semantic-Search/resources.md) | 6 / 6 | 2 | 1 | 20 |
| [L08](../08-RAG-Systems/resources.md) | 6 / 6 | 2 | 0 | 17 |
| [L09](../09-Context-Memory/resources.md) | 6 / 6 | 2 | 0 | 12 |
| [L10](../10-Concurrency-Streaming-Jobs/resources.md) | 6 / 6 | 1 | 1 | 13 |
| [L11](../11-Security-Responsible-AI/resources.md) | 6 / 6 | 2 | 0 | 17 |
| [L12](../12-Tools-Agents/resources.md) | 6 / 6 | 2 | 0 | 18 |
| [L13](../13-MCP-Enterprise-Integration/resources.md) | 6 / 6 | 3 | 1 | 14 |
| [L14](../14-LLMOps-Deployment/resources.md) | 6 / 6 | 3 | 0 | 15 |
| [L15](../15-Model-Selection-Optimization/resources.md) | 6 / 6 | 1 | 0 | 19 |
| [L16](../16-Capstone-Career/resources.md) | 6 / 6 | 0 | 0 | 26 |
| [L17](../17-Fine-Tuning-Advanced-Serving/resources.md) | 6 / 6 | 0 | 0 | 14 |
| [L18](../18-Supporting-Frontend/resources.md) | 6 / 6 | 1 | 0 | 12 |

Zero alternative groups means no fully justified substitution was established; it is not a missing recommendation. Those groups still have a required default route and optional complementary explanations. Partial overlaps are not promoted to complete alternatives.

## Representative checks

- **L01:** routing and validation have separate course choices; dependency injection **THEN lifespan** are different required concepts. Python exception lessons support testing prerequisites but do not replace pytest.
- **L09:** context selection, JIT retrieval, memory and compaction remain separate units. A memory video cannot replace the context-rot experiment; Anthropic reading is narrowed to each decision.
- **L13:** server/tool construction and resource/prompt primitives have explicit complementary SDK work. Client and authorization sources belong to their own groups.
- **L14:** Docker, CI, versioning, tracing, deployment and recovery have distinct tables. A deployment video is not an alternative to every operations topic.

## Preservation and checks

All 153 catalog resources and all existing per-Level/topic mappings remain. The catalog itself is byte-for-byte unchanged. Every verified direct-lesson URL, access term, original broad selection, language label and scope limit remains in source notes; active topic choices are separately recorded in `RESOURCE_GROUPS.json`.

`resource_table_baseline.json` locks the previous book guides, reading ledger, curriculum/catalog and all 19 details pages against unintended edits. Existing preservation checks still protect the syllabus, 84 exercises, eight milestones and learner progress. READMEs retain their assigned reading, primary routes, tasks and gates; the old generic “Alternative” shortcut is replaced by the direct topic-group link.

Run `python scripts/audit_level_content.py`, `python scripts/validate.py` and `python -m unittest discover -s tests -v`. Checks cover all 19 topic-group counts, table shape, source IDs, typed roles, bounded alternatives, required complements, book consistency, isolated regeneration and internal anchors. Mechanical checks cannot prove instructional interchangeability or usability; representative rendered tables and source scopes are reviewed separately. The existing dated URL evidence remains historical reachability verification, not a claim of new full video playback.

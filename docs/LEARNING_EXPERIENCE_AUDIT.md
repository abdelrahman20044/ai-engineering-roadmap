# Learning Experience Refactor Audit

[Home](../README.md) · [Resource preservation](RESOURCE_AUDIT.md) · [Reading order](READING_GUIDE.md)

Date: 16 October 2026. Baseline: `b788161947af8381f2a385a258d80197bddc7b4a`. Scope: information architecture and learning guidance in the existing repository. Six tiers, 19 Levels, syllabus coverage, prerequisites and practical contracts are preserved.

## Acceptance criteria

- Every README exposes its next action before the numbered steps and uses zero resource/reference tables.
- Every topic connects concepts, bounded reading, one Primary resource, practice and an observable completion check.
- Every library retains its assigned resource IDs and now distinguishes format, selection role, assigned portion, scope and limits.
- Diagnostics, full scope, mistakes and self-check answers remain accessible in `details.md`.
- The book ledger owns new reading; all step IDs and generated guides agree. Review references introduce no new mandatory chapter restart.
- Preserved catalog records and topic research, 84 assessed exercises, prerequisites, gates, ITI mappings, eight milestone files and learner progress are mechanically compared with the baseline.

The “next action within 30 seconds” goal is addressed through position and explicit wording; no timed usability study is claimed. A learner still decides how much background review is needed.

## All 19 Levels

| Level | Ordered steps | Retained resources | README tables | Book ownership / generated pages |
|---|---|---|---|---|
| [L00](../00-Orientation/README.md) | 5 | 19 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L01](../01-Python-FastAPI/README.md) | 6 | 19 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L02](../02-Mathematics-ML/README.md) | 6 | 15 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L03](../03-Deep-Learning-Foundation-Models/README.md) | 6 | 14 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L04](../04-LLM-Applications-Prompts/README.md) | 6 | 19 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L05](../05-Evaluation/README.md) | 6 | 13 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L06](../06-Application-State/README.md) | 6 | 11 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L07](../07-Embeddings-Semantic-Search/README.md) | 6 | 20 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L08](../08-RAG-Systems/README.md) | 6 | 17 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L09](../09-Context-Memory/README.md) | 6 | 12 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L10](../10-Concurrency-Streaming-Jobs/README.md) | 6 | 13 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L11](../11-Security-Responsible-AI/README.md) | 6 | 17 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L12](../12-Tools-Agents/README.md) | 6 | 18 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L13](../13-MCP-Enterprise-Integration/README.md) | 6 | 14 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L14](../14-LLMOps-Deployment/README.md) | 6 | 15 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L15](../15-Model-Selection-Optimization/README.md) | 6 | 19 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L16](../16-Capstone-Career/README.md) | 6 | 26 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L17](../17-Fine-Tuning-Advanced-Serving/README.md) | 6 | 14 | 0 | Ledger IDs checked; one first-use owner per entry |
| [L18](../18-Supporting-Frontend/README.md) | 6 | 12 | 0 | Ledger IDs checked; one first-use owner per entry |

All Levels preserve Arabic/Egyptian and English choices. Arabic translated text and prerequisite-only coverage remain explicitly labelled; advanced gaps are not disguised as verified Arabic video courses. Unverified playlist lesson identifiers are disclosed. No full 10–20-hour course is required merely because its URL is listed.

## Representative before/after comparison

The comparison uses the actual baseline files, not a reconstructed example. README table counts below measure Markdown table blocks; the complete technical scope was moved into support pages rather than discarded.

| Level | Before | After | Effect |
|---|---|---|---|
| [L01](../01-Python-FastAPI/README.md) | 10 README table blocks; parallel topic/resource/book instructions | 0 README tables; 6 ordered steps plus library/details links | Routes → dependencies → Python typing/contracts → cleanup → tests. A learner can transfer Express experience without a full beginner course. |
| [L09](../09-Context-Memory/README.md) | 10 README table blocks; parallel topic/resource/book instructions | 0 README tables; 6 ordered steps plus library/details links | Context rot → selection → JIT retrieval → memory → compaction → sub-agent decision. Anthropic sections are selected step by step; prior C5 is review. |
| [L14](../14-LLMOps-Deployment/README.md) | 10 README table blocks; parallel topic/resource/book instructions | 0 README tables; 6 ordered steps plus library/details links | Containers → CI → release manifest → tracing → deployment → recovery. F12 is assigned once; later steps apply it instead of restarting the chapter. |

The resource libraries deliberately remain comprehensive. Their repeated resource cards are reference entries, not extra required learning steps. Book sections link one master ledger instead of carrying independent reading assignments in three places. Repeated use of an article or documentation page is limited to the named section or API needed by the next task.

## Verification and limits

`python scripts/audit_level_content.py` performs the all-Level consistency, preservation and Markdown-fragment audit, including isolated re-render comparison. `python scripts/validate.py` and the existing tooling tests check the prerequisite graph, tracker, source coverage, synthetic data and reader links.

Source outlines and supplied book text were consulted for section boundaries. In particular F5 provider/RAG/concurrency portions and F11 unit/integration/behavioral/E2E portions were separated using the actual text. Full source chapters and research associations remain in the chapter map/catalog. No book PDFs are distributed. The existing dated external catalog check is retained; HTTP reachability and course outlines do not amount to complete video playback or paid assessment verification.

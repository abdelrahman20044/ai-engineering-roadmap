# M09 — Context Engineering, Memory, and Conversations

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M08](../m08-rag/README.md) |
| Personal effort | 14–22 focused hours; not official ITI hours |
| Project milestone | [S4](../../project/milestones/s4.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Budget instructions, evidence, selected journals, history, and memory. |
| O2 | Manage memory provenance, correction, deletion, and summarization loss. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N04 | Prompt / Context Engineering & Structured Outputs | 24 |
| N19 | RAG Systems Engineering | 24 |
| N22 | Agentic AI & Multi-Agent Orchestration | 36 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | Anthropic: context selection/retrieval and long-horizon sections. |
| 2 | C5 pp. 218–219; C6 Memory pp. 300–304; C10 Enhance Context p.450. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M09-E1 | Write a context contract with source priorities and a token budget. | Show how each input is selected, bounded, and truncated. |
| M09-E2 | Compare focused evidence against longer distractor-heavy context. | Use the same tasks and measure effects rather than assuming more context helps. |
| M09-E3 | Add journal CRUD and connect a user-selected entry to source passages. | Clearly separate source claims, journal facts, and assistant suggestions. |
| M09-E4 | Store explicit memory items with owner, source, date, edit, and delete. | Do not infer permanent personality traits automatically; changes affect active context. |
| M09-E5 | Trial compaction on a long synthetic conversation. | Compare required facts before/after and retain source links and covered message ranges; JIT tools arrive in M12. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Context contract, journal workflow, and editable memory schema; Focused-context and optional compaction experiments |
| Pass condition | Explain what entered context and why. Deletion is respected and stale summaries are not silently treated as facts. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M09 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Uneditable automatic memory |
| Sub-agents before a working bounded single-agent design |

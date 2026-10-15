# L09 · Context Engineering, Memory, and Conversations

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 3 · Grounded Retrieval and Context | 14–22 h | 3/5 | P1 | [L08](../08-RAG-Systems/README.md) |

**Outcome:** Budget instructions, evidence, selected journals, history, and memory. Manage memory provenance, correction, deletion, and summarization loss.

**Unlocks:** [L12](../12-Tools-Agents/README.md), [L16](../16-Capstone-Career/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Context budgets and context rot | Anthropic context engineering; C5 pp.218–219; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 1](resources.md#practice-and-evidence) |
| Selection and just-in-time retrieval | Anthropic context selection sections; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 2](resources.md#practice-and-evidence) |
| Structured memory with provenance | C6 pp.300–304; C10 p.450; [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html) | [Practice 3](resources.md#practice-and-evidence) |
| Compaction and retained facts | Anthropic long-horizon sections; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 4](resources.md#practice-and-evidence) |
| Sub-agent decision boundary | Anthropic sub-agent section; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 5](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N04** — Prompt / Context Engineering & Structured Outputs.
- **N19** — RAG Systems Engineering.
- **N22** — Agentic AI & Multi-Agent Orchestration.

| ITI topic IDs | Interpretation |
| --- | --- |
| N04, N19, N22 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L09-E1 | Write a context contract with source priorities and a token budget. | Show how each input is selected, bounded, and truncated. |
| L09-E2 | Compare focused evidence against longer distractor-heavy context. | Use the same tasks and measure effects rather than assuming more context helps. |
| L09-E3 | Add journal CRUD and connect a user-selected entry to source passages. | Clearly separate source claims, journal facts, and assistant suggestions. |
| L09-E4 | Store explicit memory items with owner, source, date, edit, and delete. | Do not infer permanent personality traits automatically; changes affect active context. |
| L09-E5 | Trial compaction on a long synthetic conversation. | Compare required facts before/after and retain source links and covered message ranges; JIT tools arrive in L12. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S4](../project/milestones/s4.md) | Context contract, journal workflow, and editable memory schema; Focused-context and optional compaction experiments | Explain what entered context and why. Deletion is respected and stale summaries are not silently treated as facts. |

## Postpone

| Outside this level |
| --- |
| Uneditable automatic memory |
| Sub-agents before a working bounded single-agent design |

## Record completion

```bash
python scripts/progress.py set L09 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L08](../08-RAG-Systems/README.md) · Next numbered Level: [L10](../10-Concurrency-Streaming-Jobs/README.md). Follow the prerequisite table if branches differ.

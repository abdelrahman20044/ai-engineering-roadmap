# L08 · RAG Systems, Citations, and Retrieval Improvement

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 3 · Grounded Retrieval and Context | 18–28 h | 3/5 | P1 | [L05](../05-Evaluation/README.md), [L07](../07-Embeddings-Semantic-Search/README.md) |

**Outcome:** Build retrieval → context → generation with verifiable citations. Diagnose failures and justify hybrid search or reranking through comparison.

**Unlocks:** [L09](../09-Context-Memory/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md), [L16](../16-Capstone-Career/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Retrieve-then-generate baseline | G4 pp.94–100; F5 RAG; [pgvector search and indexing](https://github.com/pgvector/pgvector) | [Practice 1](resources.md#practice-and-evidence) |
| Citation correctness and abstention | C4 evaluation; F11 PDF519–527; [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | [Practice 2](resources.md#practice-and-evidence) |
| Hybrid retrieval and reranking | C6 pp.267–272; [pgvector search and indexing](https://github.com/pgvector/pgvector) | [Practice 3](resources.md#practice-and-evidence) |
| Recall and ranking metrics | C6 pp.253–274; [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N17** — Embeddings, Vector DBs & Semantic Search.
- **N19** — RAG Systems Engineering.
- **N20** — AI Evaluation, Safety & Responsible AI.

| ITI topic IDs | Interpretation |
| --- | --- |
| N17, N19, N20 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L08-E1 | Generate an evidence whitelist, validate references, and display server-provided source/page/snippet. | Reject invented IDs and review whether cited passages actually support claims. |
| L08-E2 | Measure hit@5 and recall@5 using evidence labels; run generation with oracle context. | Distinguish parsing, retrieval, and generation failures. |
| L08-E3 | Compare lexical and dense retrieval; trial one hybrid/RRF or reranker approach if justified. | Keep the same dataset and report quality, latency, and cost differences. |
| L08-E4 | Change one chunking or top-k setting at a time. | Save fixed settings and negative results rather than presenting only wins. |
| L08-E5 | Test no-answer, contradictory sources, and an existing but irrelevant citation. | The system does not invent support; similarity is not interpreted as answer confidence. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | Measured RAG MVP and citation contract tests; Before/after report and failure taxonomy | Explain five failures using evidence. References both exist and support the answer under review. Report thresholds as your project targets, not official ITI standards. |

## Postpone

| Outside this level |
| --- |
| Agentic retrieval before a measured baseline |
| Fine-tuning as a parser repair strategy |

## Record completion

```bash
python scripts/progress.py set L08 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L07](../07-Embeddings-Semantic-Search/README.md) · Next numbered Level: [L09](../09-Context-Memory/README.md). Follow the prerequisite table if branches differ.

# M08 — RAG Systems, Citations, and Retrieval Improvement

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M05](../m05-evaluation/README.md), [M07](../m07-ingestion-embeddings/README.md) |
| Personal effort | 18–28 focused hours; not official ITI hours |
| Project milestone | [S3](../../project/milestones/s3.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Build retrieval → context → generation with verifiable citations. |
| O2 | Diagnose failures and justify hybrid search or reranking through comparison. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N17 | Embeddings, Vector DBs & Semantic Search | 18 |
| N19 | RAG Systems Engineering | 24 |
| N20 | AI Evaluation, Safety & Responsible AI | 12 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | G4 printed pp. 94–100: improvements and coding explanation. |
| 2 | F5 RAG and F11 PDF 519–527 retrieval integration. |
| 3 | C6 pp. 253–274, especially pp. 267–272; C4 component evaluation. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M08-E1 | Generate an evidence whitelist, validate references, and display server-provided source/page/snippet. | Reject invented IDs and review whether cited passages actually support claims. |
| M08-E2 | Measure hit@5 and recall@5 using evidence labels; run generation with oracle context. | Distinguish parsing, retrieval, and generation failures. |
| M08-E3 | Compare lexical and dense retrieval; trial one hybrid/RRF or reranker approach if justified. | Keep the same dataset and report quality, latency, and cost differences. |
| M08-E4 | Change one chunking or top-k setting at a time. | Save fixed settings and negative results rather than presenting only wins. |
| M08-E5 | Test no-answer, contradictory sources, and an existing but irrelevant citation. | The system does not invent support; similarity is not interpreted as answer confidence. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Measured RAG MVP and citation contract tests; Before/after report and failure taxonomy |
| Pass condition | Explain five failures using evidence. References both exist and support the answer under review. Report thresholds as your project targets, not official ITI standards. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M08 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Agentic retrieval before a measured baseline |
| Fine-tuning as a parser repair strategy |

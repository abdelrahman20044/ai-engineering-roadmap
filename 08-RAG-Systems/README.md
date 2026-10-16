# L08 · RAG Systems, Citations, and Retrieval Improvement

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 3 · Grounded Retrieval and Context | 18–28 h | 3/5 | P1 | [L05](../05-Evaluation/README.md), [L07](../07-Embeddings-Semantic-Search/README.md) |

**Unlocks:** [L09](../09-Context-Memory/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md), [L16](../16-Capstone-Career/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Build retrieval → context → generation with verifiable citations. Diagnose failures and justify hybrid search or reranking through comparison. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| L05 readiness | A labeled query set and separate component metrics exist. |
| L07 readiness | Each returned chunk has valid owner/source/page metadata. |
| Prompt readiness | A model adapter returns validated structured fields. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] RAG orchestration: Ship /ask with passages, source IDs and a defined no-evidence response.
- [ ] Citation correctness: Inject fabricated source IDs and unrelated real sources; catch both failure types.
- [ ] Ranking evaluation: Compute a tiny ranking example manually and match the implementation.
- [ ] Hybrid search: Compare lexical-only, vector-only and hybrid on identical owner-filtered queries.
- [ ] Reranking and query changes: Add reranking only if evidence ranking improves enough to justify extra latency.
- [ ] Answer reliability and ablations: Freeze a baseline, change one factor, report quality/citation/latency plus three failed cases.

## Recommended learning path

Measured exact retrieval → cited generation → no-evidence tests → hybrid/reranking experiments only for observed ranking failures.

| Pass | Work to do | Stop condition |
| --- | --- | --- |
| 1 · Orient | Use the assigned book/article focus and one Arabic or English explanation for each unfamiliar topic. | Explain the mechanism in your own words. |
| 2 · Implement | Work through the numbered topic outputs below; integrate them into the assessed exercises. | The specified behavior is reproducible in your own code. |
| 3 · Verify | Run the failure cases, self-check and milestone acceptance contract. | Evidence and remaining limitations are recorded. |

The resource library contains alternatives and optional depth. The effort estimate covers a selected path plus implementation, not watching every listed course. Choose Arabic teaching when it speeds understanding, then consult the English API reference for exact behavior.

## What you learn and exactly where

Each numbered row is a learning unit. **Arabic teaching**, **machine-translated Arabic text**, **English videos**, and **English documentation** are labeled separately. A missing verified Arabic resource is stated explicitly; a loosely related video is not presented as full coverage.

| Topic and required subtopics | Arabic route | English route | Build or verify |
| --- | --- | --- | --- |
| **L08-T01 · RAG orchestration**<br>Question → retrieve → assemble context → generate → validate → cite | [mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU) (AR video)<br>[RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) (AR machine-translated text) | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Ship /ask with passages, source IDs and a defined no-evidence response. |
| **L08-T02 · Citation correctness**<br>Allowed IDs; source resolution; page display; claim support | [mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU) (AR video)<br>**Scope:** Grounded-answer implementation; citation-support evaluation is additional work. | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN)<br>[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Inject fabricated source IDs and unrelated real sources; catch both failure types. |
| **L08-T03 · Ranking evaluation**<br>Recall@k; MRR/NDCG; relevant-document versus relevant-chunk labels | [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) (AR machine-translated text)<br>**Scope:** RAG overview only; use the IR evaluator for metric definitions. | [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) (EN)<br>[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Compute a tiny ranking example manually and match the implementation. |
| **L08-T04 · Hybrid search**<br>Lexical + dense; candidate union; reciprocal rank fusion; filters | [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE) (AR video) | [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) (EN video + labs) | Compare lexical-only, vector-only and hybrid on identical owner-filtered queries. |
| **L08-T05 · Reranking and query changes**<br>Cross-encoder; candidate count; query rewrite; multilingual checks | **Arabic gap:** no directly matching resource verified; use the English route. | [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) (EN video + labs) | Add reranking only if evidence ranking improves enough to justify extra latency. |
| **L08-T06 · Answer reliability and ablations**<br>Abstention; conflicting sources; context-only checks; retriever/generator failures | [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Freeze a baseline, change one factor, report quality/citation/latency plus three failed cases. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L08-T01 | G4 pp.94–100; F5 RAG | [pgvector README](https://github.com/pgvector/pgvector) (EN) |
| L08-T02 | F11 PDF519–527; C4 correctness criteria | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) (EN)<br>[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L08-T03 | C6 pp.253–274; evaluation formulas from IR evaluator docs | [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) (EN) |
| L08-T04 | C6 pp.267–272, read improvements selectively | [PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html) (EN)<br>[pgvector README](https://github.com/pgvector/pgvector) (EN) |
| L08-T05 | C6 pp.267–272 | [Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) (EN)<br>[Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) (EN) |
| L08-T06 | C3/C4 applied evaluation; F11 retrieval tests | [Ragas evaluation documentation](https://docs.ragas.io/en/stable/) (EN)<br>[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N17 · Embeddings, Vector DBs & Semantic Search | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N19 · RAG Systems Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N20 · AI Evaluation, Safety & Responsible AI | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L08-E1 | Generate an evidence whitelist, validate references, and display server-provided source/page/snippet. | Reject invented IDs and review whether cited passages actually support claims. |
| L08-E2 | Measure hit@5 and recall@5 using evidence labels; run generation with oracle context. | Distinguish parsing, retrieval, and generation failures. |
| L08-E3 | Compare lexical and dense retrieval; trial one hybrid/RRF or reranker approach if justified. | Keep the same dataset and report quality, latency, and cost differences. |
| L08-E4 | Change one chunking or top-k setting at a time. | Save fixed settings and negative results rather than presenting only wins. |
| L08-E5 | Test no-answer, contradictory sources, and an existing but irrelevant citation. | The system does not invent support; similarity is not interpreted as answer confidence. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| A citation string equals evidence | Resolve source IDs, inspect source content and assess support for the actual claim. |
| Hybrid search always improves | Use the same query set and compare recall/ranking/cost; retain a simpler baseline if better. |
| Reranking the entire corpus | Retrieve candidates first; rerank a bounded list and measure the latency increase. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What does Recall@k tell you?
2. Why RRF?
3. What must abstention test?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | How much of the labeled relevant evidence appears among the first k results; define relevance granularity. |
| 2 | It combines ranked lists without assuming their numeric scores are calibrated to each other. |
| 3 | No evidence, irrelevant evidence and conflicting evidence; the response should expose uncertainty rather than invent support. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | Measured RAG MVP and citation contract tests; Before/after report and failure taxonomy | Explain five failures using evidence. References both exist and support the answer under review. Report thresholds as your project targets, not official ITI standards. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Explain five failures using evidence. References both exist and support the answer under review. Report thresholds as your project targets, not official ITI standards.

## Postpone until justified

- Agentic retrieval before a measured baseline
- Fine-tuning as a parser repair strategy

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L08 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L07](../07-Embeddings-Semantic-Search/README.md) · Next numbered Level: [L09](../09-Context-Memory/README.md)

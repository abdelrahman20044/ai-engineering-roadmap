# Technical Details · L08

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **L05 readiness:** A labeled query set and separate component metrics exist.
- **L07 readiness:** Each returned chunk has valid owner/source/page metadata.
- **Prompt readiness:** A model adapter returns validated structured fields.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **RAG orchestration:** Question → retrieve → assemble context → generate → validate → cite.
- **Citation correctness:** Allowed IDs; source resolution; page display; claim support.
- **Ranking evaluation:** Recall@k; MRR/NDCG; relevant-document versus relevant-chunk labels.
- **Hybrid search:** Lexical + dense; candidate union; reciprocal rank fusion; filters.
- **Reranking and query changes:** Cross-encoder; candidate count; query rewrite; multilingual checks.
- **Answer reliability and ablations:** Abstention; conflicting sources; context-only checks; retriever/generator failures.

## Common mistakes and debugging

### A citation string equals evidence

Resolve source IDs, inspect source content and assess support for the actual claim.

### Hybrid search always improves

Use the same query set and compare recall/ranking/cost; retain a simpler baseline if better.

### Reranking the entire corpus

Retrieve candidates first; rerank a bounded list and measure the latency increase.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. What does Recall@k tell you?
2. Why RRF?
3. What must abstention test?

<details>
<summary>Answer guide</summary>

**What does Recall@k tell you?**

How much of the labeled relevant evidence appears among the first k results; define relevance granularity.

**Why RRF?**

It combines ranked lists without assuming their numeric scores are calibrated to each other.

**What must abstention test?**

No evidence, irrelevant evidence and conflicting evidence; the response should expose uncertainty rather than invent support.

</details>

## ITI provenance and industry extensions

- **N17:** Embeddings, Vector DBs & Semantic Search — official published module title.
- **N19:** RAG Systems Engineering — official published module title.
- **N20:** AI Evaluation, Safety & Responsible AI — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Ship /ask with passages, source IDs and a defined no-evidence response.
- [ ] Inject fabricated source IDs and unrelated real sources; catch both failure types.
- [ ] Compute a tiny ranking example manually and match the implementation.
- [ ] Compare lexical-only, vector-only and hybrid on identical owner-filtered queries.
- [ ] Add reranking only if evidence ranking improves enough to justify extra latency.
- [ ] Freeze a baseline, change one factor, report quality/citation/latency plus three failed cases.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

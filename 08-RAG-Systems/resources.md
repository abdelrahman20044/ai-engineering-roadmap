# Resource Library · L08 — RAG Systems, Citations, and Retrieval Improvement

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

## Topic navigation

1. [RAG orchestration](#unit-01)
2. [Citation correctness](#unit-02)
3. [Ranking evaluation](#unit-03)
4. [Hybrid search](#unit-04)
5. [Reranking and query changes](#unit-05)
6. [Answer reliability and ablations](#unit-06)

<a id="unit-01"></a>

## 1. RAG orchestration

[Return to README Step 1](README.md#1-rag-orchestration)

**Topic/subtopics:** Question → retrieve → assemble context → generate → validate → cite.

**Required sequence (default route):** the assigned book slices [B24 · G4](../docs/READING_GUIDE.md#b24), [B25 · F5](../docs/READING_GUIDE.md#b25) **THEN** `ar-mini-17`. Stop each source at the stated portion.

**Choose ONE explanation for retrieve-then-generate architecture:** default `ar-mini-17` **OR** `ar-gen-rag`. This translated lesson does not replace the integrated implementation and citation tests. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `pgvector`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-rag-orchestration) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B24 · G4](../docs/READING_GUIDE.md#b24)<br>Andrea De Mauro · EN | Book Section | Complementary | RAG orchestration | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b24) |
| [B25 · F5](../docs/READING_GUIDE.md#b25)<br>Alireza Parandeh · EN | Book Section | Complementary | RAG orchestration | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b25) |
| `ar-mini-17` · [mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | Augmented Answers in a working RAG backend. | The linked video only; not its playlist. |
| `ar-gen-rag` · [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Alternative | Retrieval architecture and grounding. | Only the linked translated lesson: Retrieval architecture and grounding.… [bounds](#unit-01-ar-gen-rag) |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | Advanced RAG Pipeline orientation; RAG Triad of metrics for baseline… [bounds](#unit-01-dla-rag) |
| `pgvector` · [pgvector README](https://github.com/pgvector/pgvector)<br>pgvector maintainers · EN | Official repository / implementation guide | Reference | Exact search, filtered approximate search, HNSW/IVFFlat… | Consult the relevant example for Exact search, filtered approximate… [bounds](#unit-01-pgvector) |
| `ir-labs` · [Hugging Face semantic search lesson](https://huggingface.co/learn/llm-course/chapter5/6)<br>Hugging Face · EN notebook lesson | Practical notebook lesson | Complementary (as needed) | Build a semantic search experiment with embeddings. | One matching lab/notebook for the stated topic; do not complete the whole platform. |
| `rag-paper` · [Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401)<br>Lewis et al. · EN research paper | Research paper | Optional Advanced | Original RAG architecture and retrieval/generation… | Problem statement and architecture/results relevant to this topic;… [bounds](#unit-01-rag-paper) |
| `mini-code` · [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)<br>Abu Bakr Soliman · AR explanations / Python code | Course repository / lesson index | Optional Advanced | Match each lesson to its tutorial branch; compare… | Only the branch corresponding to this topic’s named mini-RAG lesson.… [bounds](#unit-01-mini-code) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-mini-17"></a>

**`ar-mini-17` — selected portion:** Only the linked “Augmented Answers” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-gen-rag"></a>

**`ar-gen-rag` — selected portion:** Only the linked translated lesson: Retrieval architecture and grounding. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Substitute only for retrieve-then-generate architecture. This translated lesson does not replace the integrated implementation and citation tests.

<a id="unit-01-dla-rag"></a>

**`dla-rag` — selected portion:** Advanced RAG Pipeline orientation; RAG Triad of metrics for baseline review. Sentence-window/auto-merging only after a measured failure.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-pgvector"></a>

**`pgvector` — selected portion:** Consult the relevant example for Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-01-ir-labs"></a>

**`ir-labs` — selected portion:** One matching lab/notebook for the stated topic; do not complete the whole platform.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-rag-paper"></a>

**`rag-paper` — selected portion:** Problem statement and architecture/results relevant to this topic; optional depth, not paper-wide implementation homework.

**Relationship:** Optional depth/purchase; does not block the completion gate.

<a id="unit-01-mini-code"></a>

**`mini-code` — selected portion:** Only the branch corresponding to this topic’s named mini-RAG lesson. Inspect after writing your own implementation.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-02"></a>

## 2. Citation correctness

[Return to README Step 2](README.md#2-citation-correctness)

**Topic/subtopics:** Allowed IDs; source resolution; page display; claim support.

**Required sequence:** the assigned book slice [B26 · F11](../docs/READING_GUIDE.md#b26) **THEN** `promptfoo`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `pytest`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-citation-correctness) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B26 · F11](../docs/READING_GUIDE.md#b26)<br>Alireza Parandeh · EN | Book Section | Complementary | Citation correctness | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b26) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Primary | Deterministic checks, model judges and eval assertions. | The assertion type matching Citation correctness; start with deterministic… [bounds](#unit-02-promptfoo) |
| `ar-mini-17` · [mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Augmented Answers in a working RAG backend. | The linked video only; not its playlist. |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | Advanced RAG Pipeline orientation; RAG Triad of metrics for baseline… [bounds](#unit-02-dla-rag) |
| `pytest` · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)<br>pytest · EN | Documentation / tutorial | Reference | Fixtures, scope, teardown and dependency isolation. | Consult the relevant example for Fixtures, scope, teardown and dependency… [bounds](#unit-02-pytest) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-promptfoo"></a>

**`promptfoo` — selected portion:** The assertion type matching Citation correctness; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mini-17"></a>

**`ar-mini-17` — selected portion:** Only the linked “Augmented Answers” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Grounded-answer implementation; citation-support evaluation is additional work.

<a id="unit-02-dla-rag"></a>

**`dla-rag` — selected portion:** Advanced RAG Pipeline orientation; RAG Triad of metrics for baseline review. Sentence-window/auto-merging only after a measured failure.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-pytest"></a>

**`pytest` — selected portion:** Consult the relevant example for Fixtures, scope, teardown and dependency isolation. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Ranking evaluation

[Return to README Step 3](README.md#3-ranking-evaluation)

**Topic/subtopics:** Recall@k; MRR/NDCG; relevant-document versus relevant-chunk labels.

**Required sequence:** the assigned book slice [B27 · C6](../docs/READING_GUIDE.md#b27) **THEN** `st-eval`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-ranking-evaluation) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B20 · C6](../docs/READING_GUIDE.md#b20)<br>Chip Huyen · EN | Book Section | Reference | Ranking evaluation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b20) |
| [B27 · C6](../docs/READING_GUIDE.md#b27)<br>Chip Huyen · EN | Book Section | Complementary | Ranking evaluation | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b27) |
| `st-eval` · [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html)<br>Sentence Transformers · EN | Documentation / tutorial | Primary | MRR, NDCG, accuracy, precision/recall and MAP; select the… | InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and… [bounds](#unit-03-st-eval) |
| `ar-gen-rag` · [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Retrieval architecture and grounding. | Only the linked translated lesson: Retrieval architecture and grounding.… [bounds](#unit-03-ar-gen-rag) |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt… [bounds](#unit-03-dla-rag) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-st-eval"></a>

**`st-eval` — selected portion:** InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-gen-rag"></a>

**`ar-gen-rag` — selected portion:** Only the linked translated lesson: Retrieval architecture and grounding. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: RAG overview only; use the IR evaluator for metric definitions.

<a id="unit-03-dla-rag"></a>

**`dla-rag` — selected portion:** RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt metrics to your own rubric.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-04"></a>

## 4. Hybrid search

[Return to README Step 4](README.md#4-hybrid-search)

**Topic/subtopics:** Lexical + dense; candidate union; reciprocal rank fusion; filters.

**Required sequence:** `pgvector`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `fts`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-hybrid-search) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B27 · C6](../docs/READING_GUIDE.md#b27)<br>Chip Huyen · EN | Book Section | Reference | Hybrid search | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b27) |
| `pgvector` · [pgvector README](https://github.com/pgvector/pgvector)<br>pgvector maintainers · EN | Official repository / implementation guide | Primary | Exact search, filtered approximate search, HNSW/IVFFlat… | Consult the Lexical + dense; candidate union; reciprocal rank fusion;… [bounds](#unit-04-pgvector) |
| `ar-mini-21` · [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | The way to PgVector in a working RAG backend. | The linked video only; not its playlist. |
| `dla-retrieval` · [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai)<br>DeepLearning.AI · Chroma · EN video + labs | Short Course + notebooks | Complementary (as needed) | Query expansion, reranking and retrieval failure analysis. | Pitfalls of retrieval—when simple vector search fails. SQL hybrid… [bounds](#unit-04-dla-retrieval) |
| `fts` · [PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html)<br>PostgreSQL · EN | Documentation / tutorial | Reference | tsvector, tsquery and ranking for a lexical baseline. | Consult the relevant example for tsvector, tsquery and ranking for a… [bounds](#unit-04-fts) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-pgvector"></a>

**`pgvector` — selected portion:** Consult the Lexical + dense; candidate union; reciprocal rank fusion; filters sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-mini-21"></a>

**`ar-mini-21` — selected portion:** Only the linked “The way to PgVector” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-dla-retrieval"></a>

**`dla-retrieval` — selected portion:** Pitfalls of retrieval—when simple vector search fails. SQL hybrid implementation still uses pgvector/PostgreSQL.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-fts"></a>

**`fts` — selected portion:** Consult the relevant example for tsvector, tsquery and ranking for a lexical baseline. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Reranking and query changes

[Return to README Step 5](README.md#5-reranking-and-query-changes)

**Topic/subtopics:** Cross-encoder; candidate count; query rewrite; multilingual checks.

**Required sequence (default route):** `st-rerank`. Stop each source at the stated portion.

**Choose ONE explanation for cross-encoder reranking:** default `st-rerank` **OR** `dla-retrieval`. Query expansion is a different experiment; do not treat it as another name for reranking. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `e5`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-reranking-and-query-changes) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B27 · C6](../docs/READING_GUIDE.md#b27)<br>Chip Huyen · EN | Book Section | Reference | Reranking and query changes | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b27) |
| `st-rerank` · [Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)<br>Sentence Transformers · EN | Documentation / tutorial | Primary | Bi-encoder candidate retrieval followed by cross-encoder… | Consult the Cross-encoder; candidate count; query rewrite; multilingual… [bounds](#unit-05-st-rerank) |
| `dla-retrieval` · [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai)<br>DeepLearning.AI · Chroma · EN video + labs | Short Course + notebooks | Alternative | Query expansion, reranking and retrieval failure analysis. | Cross-encoder re-ranking. Query Expansion is a separate complementary experiment. |
| `e5` · [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small)<br>intfloat · model authors · EN | Model card + usage examples | Reference | Supported languages, query/passage prefixes, examples and… | Consult the relevant example for Supported languages, query/passage… [bounds](#unit-05-e5) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-st-rerank"></a>

**`st-rerank` — selected portion:** Consult the Cross-encoder; candidate count; query rewrite; multilingual checks sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-05-dla-retrieval"></a>

**`dla-retrieval` — selected portion:** Cross-encoder re-ranking. Query Expansion is a separate complementary experiment.

**Relationship:** Substitute only for cross-encoder reranking. Query expansion is a different experiment; do not treat it as another name for reranking.

<a id="unit-05-e5"></a>

**`e5` — selected portion:** Consult the relevant example for Supported languages, query/passage prefixes, examples and model limitations. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Answer reliability and ablations

[Return to README Step 6](README.md#6-answer-reliability-and-ablations)

**Topic/subtopics:** Abstention; conflicting sources; context-only checks; retriever/generator failures.

**Required sequence:** `ragas`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-answer-reliability-and-ablations) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B15 · C3](../docs/READING_GUIDE.md#b15)<br>Chip Huyen · EN | Book Section | Reference | Answer reliability and ablations | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b15) |
| [B16 · C4](../docs/READING_GUIDE.md#b16)<br>Chip Huyen · EN | Book Section | Reference | Answer reliability and ablations | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b16) |
| [B17 · F11](../docs/READING_GUIDE.md#b17)<br>Alireza Parandeh · EN | Book Section | Reference | Answer reliability and ablations | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b17) |
| `ragas` · [Ragas evaluation documentation](https://docs.ragas.io/en/stable/)<br>Ragas · EN | Documentation / evaluation tutorials | Primary | Reference/context/answer metrics and experiment workflow;… | Consult the Abstention; conflicting sources; context-only checks;… [bounds](#unit-06-ragas) |
| `ar-gen-responsible` · [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Fairness, reliability and accountable use. | Only the linked translated lesson: Fairness, reliability and accountable… [bounds](#unit-06-ar-gen-responsible) |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt… [bounds](#unit-06-dla-rag) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-06-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-ragas"></a>

**`ragas` — selected portion:** Consult the Abstention; conflicting sources; context-only checks; retriever/generator failures sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-gen-responsible"></a>

**`ar-gen-responsible` — selected portion:** Only the linked translated lesson: Fairness, reliability and accountable use. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-dla-rag"></a>

**`dla-rag` — selected portion:** RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt metrics to your own rubric.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-mini-17"></a>

<details>
<summary>ar-mini-17 · mini-RAG · Augmented Answers — access, scope and verification</summary>

[mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Augmented Answers in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** RAG orchestration; Citation correctness.
- **Retained broad selection notes (lookup only):** Only the linked “Augmented Answers” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-gen-rag"></a>

<details>
<summary>ar-gen-rag · RAG and vector databases · Arabic — access, scope and verification</summary>

[RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Retrieval architecture and grounding.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** RAG orchestration; Ranking evaluation.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about RAG orchestration. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-dla-rag"></a>

<details>
<summary>dla-rag · Building and Evaluating Advanced RAG — access, scope and verification</summary>

[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) · DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks

- **Resource Type:** Short Course + notebooks.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Catalog scope:** Advanced retrieval and structured evaluation experiments.
- **Scope/version limits:** Framework-specific lab; reimplement one comparison using your existing retrieval interface.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** RAG orchestration; Citation correctness; Ranking evaluation; Answer reliability and ablations.
- **Retained broad selection notes (lookup only):** “Advanced RAG Pipeline”, “Sentence-window retrieval” and “Auto-merging retrieval”: choose one improvement only after identifying a failure.

</details>

<a id="r-pgvector"></a>

<details>
<summary>pgvector · pgvector README — access, scope and verification</summary>

[pgvector README](https://github.com/pgvector/pgvector) · pgvector maintainers · EN

- **Resource Type:** Official repository / implementation guide.
- **Access:** Free.
- **Catalog scope:** Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** RAG orchestration; Hybrid search.
- **Retained broad selection notes (lookup only):** Consult the Lexical + dense; candidate union; reciprocal rank fusion; filters sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-promptfoo"></a>

<details>
<summary>promptfoo · Assertions and metrics — access, scope and verification</summary>

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) · Promptfoo · EN

- **Resource Type:** Documentation: assertions reference.
- **Access:** Free.
- **Catalog scope:** Deterministic checks, model judges and eval assertions.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Citation correctness; Answer reliability and ablations.
- **Retained broad selection notes (lookup only):** The assertion type matching Citation correctness; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

</details>

<a id="r-pytest"></a>

<details>
<summary>pytest · pytest fixtures — access, scope and verification</summary>

[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · pytest · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Fixtures, scope, teardown and dependency isolation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Citation correctness.
- **Retained broad selection notes (lookup only):** Consult the Allowed IDs; source resolution; page display; claim support sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-st-eval"></a>

<details>
<summary>st-eval · InformationRetrievalEvaluator — access, scope and verification</summary>

[InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) · Sentence Transformers · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Ranking evaluation.
- **Retained broad selection notes (lookup only):** InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.

</details>

<a id="r-ar-mini-21"></a>

<details>
<summary>ar-mini-21 · mini-RAG · The way to PgVector — access, scope and verification</summary>

[mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** The way to PgVector in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Hybrid search.
- **Retained broad selection notes (lookup only):** Only the linked “The way to PgVector” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-dla-retrieval"></a>

<details>
<summary>dla-retrieval · Advanced Retrieval for AI with Chroma — access, scope and verification</summary>

[Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) · DeepLearning.AI · Chroma · EN video + labs

- **Resource Type:** Short Course + notebooks.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Catalog scope:** Query expansion, reranking and retrieval failure analysis.
- **Scope/version limits:** Chroma is a lab alternative; no database migration is required.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Hybrid search; Reranking and query changes.
- **Retained broad selection notes (lookup only):** “Query Expansion” and “Cross-encoder re-ranking”; embedding adaptors are optional advanced.

</details>

<a id="r-fts"></a>

<details>
<summary>fts · PostgreSQL text search controls — access, scope and verification</summary>

[PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html) · PostgreSQL · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** tsvector, tsquery and ranking for a lexical baseline.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Hybrid search.
- **Retained broad selection notes (lookup only):** Consult the Lexical + dense; candidate union; reciprocal rank fusion; filters sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-st-rerank"></a>

<details>
<summary>st-rerank · Retrieve and rerank — access, scope and verification</summary>

[Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) · Sentence Transformers · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Bi-encoder candidate retrieval followed by cross-encoder reranking.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Reranking and query changes.
- **Retained broad selection notes (lookup only):** Consult the Cross-encoder; candidate count; query rewrite; multilingual checks sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-e5"></a>

<details>
<summary>e5 · Multilingual E5 model card — access, scope and verification</summary>

[Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) · intfloat · model authors · EN

- **Resource Type:** Model card + usage examples.
- **Access:** Free.
- **Catalog scope:** Supported languages, query/passage prefixes, examples and model limitations.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Reranking and query changes.
- **Retained broad selection notes (lookup only):** Consult the Cross-encoder; candidate count; query rewrite; multilingual checks sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-responsible"></a>

<details>
<summary>ar-gen-responsible · Responsible generative AI · Arabic — access, scope and verification</summary>

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Fairness, reliability and accountable use.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Answer reliability and ablations.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Answer reliability and ablations. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-ragas"></a>

<details>
<summary>ragas · Ragas evaluation documentation — access, scope and verification</summary>

[Ragas evaluation documentation](https://docs.ragas.io/en/stable/) · Ragas · EN

- **Resource Type:** Documentation / evaluation tutorials.
- **Access:** Free.
- **Catalog scope:** Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Answer reliability and ablations.
- **Retained broad selection notes (lookup only):** Consult the Abstention; conflicting sources; context-only checks; retriever/generator failures sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ir-labs"></a>

<details>
<summary>ir-labs · Hugging Face semantic search lesson — access, scope and verification</summary>

[Hugging Face semantic search lesson](https://huggingface.co/learn/llm-course/chapter5/6) · Hugging Face · EN notebook lesson

- **Resource Type:** Practical notebook lesson.
- **Access:** Free.
- **Catalog scope:** Build a semantic search experiment with embeddings.
- **Scope/version limits:** Adapt the corpus and verify ranking locally; no claim of external grading.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Chapter 5 “Semantic search with FAISS”: the embedding/query notebook. Reuse the concept with your corpus; switching from pgvector is not required.

</details>

<a id="r-rag-paper"></a>

<details>
<summary>rag-paper · Retrieval-Augmented Generation paper — access, scope and verification</summary>

[Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401) · Lewis et al. · EN research paper

- **Resource Type:** Research paper.
- **Access:** Free.
- **Catalog scope:** Original RAG architecture and retrieval/generation distinction.
- **Scope/version limits:** Modern application-level RAG need not reproduce the training architecture.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Original RAG architecture and retrieval/generation distinction. Optional lookup; implement only the portion that addresses the named gap.

</details>

<a id="r-mini-code"></a>

<details>
<summary>mini-code · mini-RAG lesson index and source branches — access, scope and verification</summary>

[mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag) · Abu Bakr Soliman · AR explanations / Python code

- **Resource Type:** Course repository / lesson index.
- **Access:** Free.
- **Catalog scope:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers.
- **Scope/version limits:** Educational reference, not a security or correctness certification.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. Optional lookup; implement only the portion that addresses the named gap.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

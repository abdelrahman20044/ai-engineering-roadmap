# Resource Library · L08 — RAG Systems, Citations, and Retrieval Improvement

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

## Book references

Assigned reading is authoritative in [the master order for L08](../docs/READING_GUIDE.md#l08). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B24 · G4](../docs/READING_GUIDE.md#b24), [B25 · F5](../docs/READING_GUIDE.md#b25), [B26 · F11](../docs/READING_GUIDE.md#b26), [B27 · C6](../docs/READING_GUIDE.md#b27).

**Previously covered / lookup only:** [B15 · C3](../docs/READING_GUIDE.md#b15), [B16 · C4](../docs/READING_GUIDE.md#b16), [B17 · F11](../docs/READING_GUIDE.md#b17), [B19 · G4](../docs/READING_GUIDE.md#b19), [B20 · C6](../docs/READING_GUIDE.md#b20), [B21 · F5](../docs/READING_GUIDE.md#b21). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-mini-17"></a>

### mini-RAG · Augmented Answers

[mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Primary. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** RAG orchestration; Citation correctness.
- **Assigned portion:** Only the linked “Augmented Answers” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Augmented Answers in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Grounded-answer implementation; citation-support evaluation is additional work.

<a id="r-ar-gen-rag"></a>

### RAG and vector databases · Arabic

[RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** RAG orchestration; Ranking evaluation.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about RAG orchestration. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Retrieval architecture and grounding.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

**Arabic scope note:** RAG overview only; use the IR evaluator for metric definitions.

<a id="r-ar-mini-21"></a>

### mini-RAG · The way to PgVector

[mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Hybrid search.
- **Assigned portion:** Only the linked “The way to PgVector” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** The way to PgVector in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

<a id="r-ar-gen-responsible"></a>

### Responsible generative AI · Arabic

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Answer reliability and ablations.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Answer reliability and ablations. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Fairness, reliability and accountable use.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-dla-rag"></a>

### Building and Evaluating Advanced RAG

[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)

- **Resource Type:** Short video course + notebooks.
- **Role:** Alternative. **Language:** EN video + notebooks. **By:** DeepLearning.AI · LlamaIndex/TruEra.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** RAG orchestration; Citation correctness; Ranking evaluation; Answer reliability and ablations.
- **Assigned portion:** “Advanced RAG Pipeline”, “Sentence-window retrieval” and “Auto-merging retrieval”: choose one improvement only after identifying a failure.
- **Scope:** Advanced retrieval and structured evaluation experiments.
- **Limit:** Framework-specific lab; reimplement one comparison using your existing retrieval interface.

<a id="r-dla-retrieval"></a>

### Advanced Retrieval for AI with Chroma

[Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai)

- **Resource Type:** Short video course + notebooks.
- **Role:** Alternative. **Language:** EN video + labs. **By:** DeepLearning.AI · Chroma.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** Hybrid search; Reranking and query changes.
- **Assigned portion:** “Query Expansion” and “Cross-encoder re-ranking”; embedding adaptors are optional advanced.
- **Scope:** Query expansion, reranking and retrieval failure analysis.
- **Limit:** Chroma is a lab alternative; no database migration is required.

## Slides, notebooks and repositories

<a id="r-mini-code"></a>

### mini-RAG lesson index and source branches

[mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)

- **Resource Type:** Course repository / lesson index.
- **Role:** Reference. **Language:** AR explanations / Python code. **By:** Abu Bakr Soliman.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers.
- **Limit:** Educational reference, not a security or correctness certification.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

<a id="r-ir-labs"></a>

### Hugging Face semantic search lesson

[Hugging Face semantic search lesson](https://huggingface.co/learn/llm-course/chapter5/6)

- **Resource Type:** Practical notebook lesson.
- **Role:** Alternative. **Language:** EN notebook lesson. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Chapter 5 “Semantic search with FAISS”: the embedding/query notebook. Reuse the concept with your corpus; switching from pgvector is not required.
- **Scope:** Build a semantic search experiment with embeddings.
- **Limit:** Adapt the corpus and verify ranking locally; no claim of external grading.

## Official documentation and engineering articles

<a id="r-pgvector"></a>

### pgvector README

[pgvector README](https://github.com/pgvector/pgvector)

- **Resource Type:** Official repository / implementation guide.
- **Role:** Primary. **Language:** EN. **By:** pgvector maintainers.
- **Access:** Free.
- **Use for:** RAG orchestration; Hybrid search.
- **Assigned portion:** Consult the Lexical + dense; candidate union; reciprocal rank fusion; filters sections/examples only. Do not read the entire documentation site.
- **Scope:** Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-promptfoo"></a>

### Assertions and metrics

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

- **Resource Type:** Documentation: assertions reference.
- **Role:** Primary. **Language:** EN. **By:** Promptfoo.
- **Access:** Free.
- **Use for:** Citation correctness; Answer reliability and ablations.
- **Assigned portion:** The assertion type matching Citation correctness; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.
- **Scope:** Deterministic checks, model judges and eval assertions.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pytest"></a>

### pytest fixtures

[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** pytest.
- **Access:** Free.
- **Use for:** Citation correctness.
- **Assigned portion:** Consult the Allowed IDs; source resolution; page display; claim support sections/examples only. Do not read the entire documentation site.
- **Scope:** Fixtures, scope, teardown and dependency isolation.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-st-eval"></a>

### InformationRetrievalEvaluator

[InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Sentence Transformers.
- **Access:** Free.
- **Use for:** Ranking evaluation.
- **Assigned portion:** InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.
- **Scope:** MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-fts"></a>

### PostgreSQL text search controls

[PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** PostgreSQL.
- **Access:** Free.
- **Use for:** Hybrid search.
- **Assigned portion:** Consult the Lexical + dense; candidate union; reciprocal rank fusion; filters sections/examples only. Do not read the entire documentation site.
- **Scope:** tsvector, tsquery and ranking for a lexical baseline.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-st-rerank"></a>

### Retrieve and rerank

[Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Sentence Transformers.
- **Access:** Free.
- **Use for:** Reranking and query changes.
- **Assigned portion:** Consult the Cross-encoder; candidate count; query rewrite; multilingual checks sections/examples only. Do not read the entire documentation site.
- **Scope:** Bi-encoder candidate retrieval followed by cross-encoder reranking.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-e5"></a>

### Multilingual E5 model card

[Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small)

- **Resource Type:** Model card + usage examples.
- **Role:** Reference. **Language:** EN. **By:** intfloat · model authors.
- **Access:** Free.
- **Use for:** Reranking and query changes.
- **Assigned portion:** Consult the Cross-encoder; candidate count; query rewrite; multilingual checks sections/examples only. Do not read the entire documentation site.
- **Scope:** Supported languages, query/passage prefixes, examples and model limitations.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ragas"></a>

### Ragas evaluation documentation

[Ragas evaluation documentation](https://docs.ragas.io/en/stable/)

- **Resource Type:** Documentation / evaluation tutorials.
- **Role:** Primary. **Language:** EN. **By:** Ragas.
- **Access:** Free.
- **Use for:** Answer reliability and ablations.
- **Assigned portion:** Consult the Abstention; conflicting sources; context-only checks; retriever/generator failures sections/examples only. Do not read the entire documentation site.
- **Scope:** Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

<a id="r-rag-paper"></a>

### Retrieval-Augmented Generation paper

[Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401)

- **Resource Type:** Research paper.
- **Role:** Optional Advanced. **Language:** EN research paper. **By:** Lewis et al..
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Original RAG architecture and retrieval/generation distinction. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Original RAG architecture and retrieval/generation distinction.
- **Limit:** Modern application-level RAG need not reproduce the training architecture.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

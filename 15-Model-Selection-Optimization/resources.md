# Resource Library · L15 — Model Selection, Cost, Latency, and User Feedback

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** Arabic lifecycle and deployment material provides context. Dedicated Arabic instruction for controlled model selection, tail latency and cache isolation was not verified; use C4/C9/C10 and the English engineering material.

## Book references

Assigned reading is authoritative in [the master order for L15](../docs/READING_GUIDE.md#l15). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B40 · C4](../docs/READING_GUIDE.md#b40), [B42 · C9](../docs/READING_GUIDE.md#b42), [B41 · F10](../docs/READING_GUIDE.md#b41), [B43 · C10](../docs/READING_GUIDE.md#b43).

**Previously covered / lookup only:** [B16 · C4](../docs/READING_GUIDE.md#b16), [B39a · C10](../docs/READING_GUIDE.md#b39a). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-gen-intro"></a>

### Introduction to generative AI · Arabic

[Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Model selection for the product.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Model selection for the product. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Application versus foundation model and basic capabilities.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

**Arabic scope note:** Model/application orientation; controlled selection is taught by C4 and English evaluation resources.

<a id="r-ar-gen-lifecycle"></a>

### Generative AI lifecycle · Arabic

[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Latency and throughput; Feedback and monitoring loop.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Latency and throughput. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Evaluation, versioning and operational stages.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

**Arabic scope note:** Lifecycle orientation; tail-latency measurement uses C9/Locust.

<a id="r-ar-mini-19"></a>

### mini-RAG · Ollama Local LLM Server

[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Cost accounting.
- **Assigned portion:** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Ollama Local LLM Server in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Local model-serving context; cost accounting uses C4/C9 and measured usage.

<a id="r-ar-mini-20"></a>

### mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic

[mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Safe caching.
- **Assigned portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Database ownership context only; cache-key/invalidation design is an industry extension.

<a id="r-ar-agent-context"></a>

### Context engineering · Arabic

[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Measured optimization.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Measured optimization. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Selecting and organizing information for agents.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-ux"></a>

### AI user experience · Arabic

[AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Feedback and monitoring loop.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Feedback and monitoring loop. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Communicating limitations, feedback and human control.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-fsdl-foundation"></a>

### LLM Foundations

[LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/)

- **Resource Type:** Single lecture video + slides.
- **Role:** Alternative. **Language:** EN video + slides. **By:** Full Stack Deep Learning.
- **Access:** Free.
- **Use for:** Model selection for the product.
- **Assigned portion:** Only the linked “LLM Foundations” lecture; not the complete LLM Bootcamp. Use the parts relevant to Model selection for the product. Exact timestamps are not assigned.
- **Scope:** Language-model capabilities and application boundaries.
- **Limit:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.

<a id="r-dla-retrieval"></a>

### Advanced Retrieval for AI with Chroma

[Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai)

- **Resource Type:** Short video course + notebooks.
- **Role:** Alternative. **Language:** EN video + labs. **By:** DeepLearning.AI · Chroma.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** Measured optimization.
- **Assigned portion:** Only the lesson matching the measured retrieval bottleneck; no full-course repeat.
- **Scope:** Query expansion, reranking and retrieval failure analysis.
- **Limit:** Chroma is a lab alternative; no database migration is required.

<a id="r-fsdl-ux"></a>

### UX for Language User Interfaces

[UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/)

- **Resource Type:** Single lecture video + slides.
- **Role:** Primary. **Language:** EN video + slides. **By:** Full Stack Deep Learning.
- **Access:** Free.
- **Use for:** Feedback and monitoring loop.
- **Assigned portion:** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Feedback and monitoring loop. Exact timestamps are not assigned.
- **Scope:** Uncertainty, interaction design and feedback.
- **Limit:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.

<a id="r-dla-rag"></a>

### Building and Evaluating Advanced RAG

[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)

- **Resource Type:** Short video course + notebooks.
- **Role:** Alternative. **Language:** EN video + notebooks. **By:** DeepLearning.AI · LlamaIndex/TruEra.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Evaluation review for the optimization comparison; do not repeat the entire short course.
- **Scope:** Advanced retrieval and structured evaluation experiments.
- **Limit:** Framework-specific lab; reimplement one comparison using your existing retrieval interface.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Official documentation and engineering articles

<a id="r-promptfoo"></a>

### Assertions and metrics

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

- **Resource Type:** Documentation: assertions reference.
- **Role:** Reference. **Language:** EN. **By:** Promptfoo.
- **Access:** Free.
- **Use for:** Model selection for the product.
- **Assigned portion:** The assertion type matching Model selection for the product; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.
- **Scope:** Deterministic checks, model judges and eval assertions.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-e5"></a>

### Multilingual E5 model card

[Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small)

- **Resource Type:** Model card + usage examples.
- **Role:** Reference. **Language:** EN. **By:** intfloat · model authors.
- **Access:** Free.
- **Use for:** Model selection for the product.
- **Assigned portion:** Consult the Language; task quality; license; privacy; context; availability sections/examples only. Do not read the entire documentation site.
- **Scope:** Supported languages, query/passage prefixes, examples and model limitations.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-locust"></a>

### Locust quickstart

[Locust quickstart](https://docs.locust.io/en/stable/quickstart.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Locust.
- **Access:** Free.
- **Use for:** Latency and throughput; Measured optimization.
- **Assigned portion:** Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets sections/examples only. Do not read the entire documentation site.
- **Scope:** Concurrent user scenarios and latency/throughput measurement.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-otel"></a>

### Python instrumentation

[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** OpenTelemetry.
- **Access:** Free.
- **Use for:** Latency and throughput; Cost accounting; Feedback and monitoring loop.
- **Assigned portion:** Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets sections/examples only. Do not read the entire documentation site.
- **Scope:** Spans, attributes, context and exporting telemetry.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-hf-token"></a>

### Tokenizers

[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Cost accounting.
- **Assigned portion:** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.
- **Scope:** Subword tokenization and language-dependent token counts.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-authz"></a>

### Authorization cheat sheet

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** OWASP.
- **Access:** Free.
- **Use for:** Safe caching.
- **Assigned portion:** Consult the Cache key; tenant boundary; source/version invalidation; expiry sections/examples only. Do not read the entire documentation site.
- **Scope:** Deny-by-default object authorization and least privilege.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-sqlasync"></a>

### SQLAlchemy asyncio

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** SQLAlchemy.
- **Access:** Free.
- **Use for:** Safe caching.
- **Assigned portion:** Consult the Cache key; tenant boundary; source/version invalidation; expiry sections/examples only. Do not read the entire documentation site.
- **Scope:** One session per concurrent task; explicit database I/O.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pgvector"></a>

### pgvector README

[pgvector README](https://github.com/pgvector/pgvector)

- **Resource Type:** Official repository / implementation guide.
- **Role:** Primary. **Language:** EN. **By:** pgvector maintainers.
- **Access:** Free.
- **Use for:** Measured optimization.
- **Assigned portion:** Read pgvector’s Querying, Indexing, Filtering and Hybrid Search sections relevant to a measured retrieval bottleneck. Test one change; provider caching/backpressure are separate techniques from F10, not pgvector features.
- **Scope:** Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

<a id="r-sre-slos"></a>

### Implementing SLOs

[Implementing SLOs](https://sre.google/workbook/implementing-slos/)

- **Resource Type:** Worked book chapter (free online).
- **Role:** Optional Advanced. **Language:** EN worked chapter. **By:** Google SRE.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Availability/latency indicators, objectives and error budgets. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Availability/latency indicators, objectives and error budgets.
- **Limit:** Use modest application-level targets; do not copy enterprise numbers.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

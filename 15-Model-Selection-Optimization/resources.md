# Resource Library · L15 — Model Selection, Cost, Latency, and User Feedback

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Arabic lifecycle and deployment material provides context. Dedicated Arabic instruction for controlled model selection, tail latency and cache isolation was not verified; use C4/C9/C10 and the English engineering material.

## Topic navigation

1. [Model selection for the product](#unit-01)
2. [Latency and throughput](#unit-02)
3. [Cost accounting](#unit-03)
4. [Safe caching](#unit-04)
5. [Measured optimization](#unit-05)
6. [Feedback and monitoring loop](#unit-06)

<a id="unit-01"></a>

## 1. Model selection for the product

[Return to README Step 1](README.md#1-model-selection-for-the-product)

**Topic/subtopics:** Language; task quality; license; privacy; context; availability.

**Required sequence:** the assigned book slice [B40 · C4](../docs/READING_GUIDE.md#b40). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `promptfoo`, `e5`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-model-selection-for-the-product) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B40 · C4](../docs/READING_GUIDE.md#b40)<br>Chip Huyen · EN | Book Section | Primary | Model selection for the product | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b40) |
| `ar-gen-intro` · [Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Application versus foundation model and basic capabilities. | Only the linked translated lesson: Application versus foundation model and… [bounds](#unit-01-ar-gen-intro) |
| `fsdl-foundation` · [LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Complementary (as needed) | Language-model capabilities and application boundaries. | Topic bounds; lesson IDs not verified — [details](#unit-01-fsdl-foundation) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-01-promptfoo) |
| `e5` · [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small)<br>intfloat · model authors · EN | Model card + usage examples | Reference | Supported languages, query/passage prefixes, examples and… | Consult the relevant example for Supported languages, query/passage… [bounds](#unit-01-e5) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-gen-intro"></a>

**`ar-gen-intro` — selected portion:** Only the linked translated lesson: Application versus foundation model and basic capabilities. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Model/application orientation; controlled selection is taught by C4 and English evaluation resources.

<a id="unit-01-fsdl-foundation"></a>

**`fsdl-foundation` — selected portion:** Only the linked lesson on Language-model capabilities and application boundaries. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-01-e5"></a>

**`e5` — selected portion:** Consult the relevant example for Supported languages, query/passage prefixes, examples and model limitations. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-02"></a>

## 2. Latency and throughput

[Return to README Step 2](README.md#2-latency-and-throughput)

**Topic/subtopics:** TTFT; end-to-end p50/p95; concurrency; stage budgets.

**Required sequence:** the assigned book slice [B42 · C9](../docs/READING_GUIDE.md#b42) **THEN** `locust`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `otel`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-latency-and-throughput) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B42 · C9](../docs/READING_GUIDE.md#b42)<br>Chip Huyen · EN | Book Section | Complementary | Latency and throughput | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b42) |
| `locust` · [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html)<br>Locust · EN | Documentation / tutorial | Primary | Concurrent user scenarios and latency/throughput… | Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets… [bounds](#unit-02-locust) |
| `ar-gen-lifecycle` · [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation, versioning and operational stages. | Only the linked translated lesson: Evaluation, versioning and operational… [bounds](#unit-02-ar-gen-lifecycle) |
| `otel` · [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)<br>OpenTelemetry · EN | Documentation / tutorial | Reference | Spans, attributes, context and exporting telemetry. | Consult the relevant example for Spans, attributes, context and exporting… [bounds](#unit-02-otel) |
| `sre-slos` · [Implementing SLOs](https://sre.google/workbook/implementing-slos/)<br>Google SRE · EN worked chapter | Worked book chapter (free online) | Optional Advanced | Availability/latency indicators, objectives and error… | Consult the relevant example for Availability/latency indicators,… [bounds](#unit-02-sre-slos) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-locust"></a>

**`locust` — selected portion:** Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-gen-lifecycle"></a>

**`ar-gen-lifecycle` — selected portion:** Only the linked translated lesson: Evaluation, versioning and operational stages. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Lifecycle orientation; tail-latency measurement uses C9/Locust.

<a id="unit-02-otel"></a>

**`otel` — selected portion:** Consult the relevant example for Spans, attributes, context and exporting telemetry. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-02-sre-slos"></a>

**`sre-slos` — selected portion:** Consult the relevant example for Availability/latency indicators, objectives and error budgets. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-03"></a>

## 3. Cost accounting

[Return to README Step 3](README.md#3-cost-accounting)

**Topic/subtopics:** Input/output tokens; retries; embeddings; reranking; local hardware assumptions.

**Required sequence:** review only [B42 · C9](../docs/READING_GUIDE.md#b42) for this task. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `otel`, `hf-token`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-cost-accounting) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B42 · C9](../docs/READING_GUIDE.md#b42)<br>Chip Huyen · EN | Book Section | Primary | Cost accounting | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b42) |
| `ar-mini-19` · [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Ollama Local LLM Server in a working RAG backend. | The linked video only; not its playlist. |
| `otel` · [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)<br>OpenTelemetry · EN | Documentation / tutorial | Reference | Spans, attributes, context and exporting telemetry. | Consult the relevant example for Spans, attributes, context and exporting… [bounds](#unit-03-otel) |
| `hf-token` · [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)<br>Hugging Face · EN | Documentation / tutorial | Reference | Subword tokenization and language-dependent token counts. | Chapter 6 introduction to tokenization; selected tokenizer/model example… [bounds](#unit-03-hf-token) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-ar-mini-19"></a>

**`ar-mini-19` — selected portion:** Only the linked “Ollama Local LLM Server” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Local model-serving context; cost accounting uses C4/C9 and measured usage.

<a id="unit-03-otel"></a>

**`otel` — selected portion:** Consult the relevant example for Spans, attributes, context and exporting telemetry. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-03-hf-token"></a>

**`hf-token` — selected portion:** Chapter 6 introduction to tokenization; selected tokenizer/model example only. Reuse for token counting, not a course restart.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Safe caching

[Return to README Step 4](README.md#4-safe-caching)

**Topic/subtopics:** Cache key; tenant boundary; source/version invalidation; expiry.

**Required sequence:** the assigned book slice [B41 · F10](../docs/READING_GUIDE.md#b41). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `authz`, `sqlasync`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-safe-caching) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B41 · F10](../docs/READING_GUIDE.md#b41)<br>Alireza Parandeh · EN | Book Section | Primary | Safe caching | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b41) |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `authz` · [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Reference | Deny-by-default object authorization and least privilege. | Consult the relevant example for Deny-by-default object authorization and… [bounds](#unit-04-authz) |
| `sqlasync` · [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)<br>SQLAlchemy · EN | Documentation / tutorial | Reference | One session per concurrent task; explicit database I/O. | Consult the relevant example for One session per concurrent task; explicit… [bounds](#unit-04-sqlasync) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Database ownership context only; cache-key/invalidation design is an industry extension.

<a id="unit-04-authz"></a>

**`authz` — selected portion:** Consult the relevant example for Deny-by-default object authorization and least privilege. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-04-sqlasync"></a>

**`sqlasync` — selected portion:** Consult the relevant example for One session per concurrent task; explicit database I/O. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Measured optimization

[Return to README Step 5](README.md#5-measured-optimization)

**Topic/subtopics:** Prompt/context reduction; search tuning; caching; queue/backpressure.

**Required sequence:** `pgvector`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `locust`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-measured-optimization) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B41 · F10](../docs/READING_GUIDE.md#b41)<br>Alireza Parandeh · EN | Book Section | Reference | Measured optimization | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b41) |
| `pgvector` · [pgvector README](https://github.com/pgvector/pgvector)<br>pgvector maintainers · EN | Official repository / implementation guide | Primary | Exact search, filtered approximate search, HNSW/IVFFlat… | Read pgvector’s Querying, Indexing, Filtering and Hybrid Search sections… [bounds](#unit-05-pgvector) |
| `ar-agent-context` · [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Selecting and organizing information for agents. | Only the linked translated lesson: Selecting and organizing information… [bounds](#unit-05-ar-agent-context) |
| `dla-retrieval` · [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai)<br>DeepLearning.AI · Chroma · EN video + labs | Short Course + notebooks | Complementary (as needed) | Query expansion, reranking and retrieval failure analysis. | Choose Query Expansion, Cross-encoder re-ranking or Embedding adaptors… [bounds](#unit-05-dla-retrieval) |
| `locust` · [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html)<br>Locust · EN | Documentation / tutorial | Reference | Concurrent user scenarios and latency/throughput… | Consult the relevant example for Concurrent user scenarios and… [bounds](#unit-05-locust) |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Optional Advanced | Advanced retrieval and structured evaluation experiments. | Advanced RAG Pipeline orientation; RAG Triad of metrics for baseline… [bounds](#unit-05-dla-rag) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-pgvector"></a>

**`pgvector` — selected portion:** Read pgvector’s Querying, Indexing, Filtering and Hybrid Search sections relevant to a measured retrieval bottleneck. Test one change; provider caching/backpressure are separate techniques from F10, not pgvector features.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-agent-context"></a>

**`ar-agent-context` — selected portion:** Only the linked translated lesson: Selecting and organizing information for agents. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-dla-retrieval"></a>

**`dla-retrieval` — selected portion:** Choose Query Expansion, Cross-encoder re-ranking or Embedding adaptors only for the measured failure; run one experiment.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-locust"></a>

**`locust` — selected portion:** Consult the relevant example for Concurrent user scenarios and latency/throughput measurement. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-dla-rag"></a>

**`dla-rag` — selected portion:** Advanced RAG Pipeline orientation; RAG Triad of metrics for baseline review. Sentence-window/auto-merging only after a measured failure.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-06"></a>

## 6. Feedback and monitoring loop

[Return to README Step 6](README.md#6-feedback-and-monitoring-loop)

**Topic/subtopics:** Consent; ratings; corrections; failure review; feedback bias.

**Required sequence (default route):** the assigned book slice [B43 · C10](../docs/READING_GUIDE.md#b43) **THEN** `fsdl-ux`. Stop each source at the stated portion.

**Choose ONE explanation for user-facing feedback design:** default `fsdl-ux` **OR** `ar-gen-ux`. Monitoring instrumentation and feedback-quality checks remain separate required work. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `otel`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-feedback-and-monitoring-loop) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B43 · C10](../docs/READING_GUIDE.md#b43)<br>Chip Huyen · EN | Book Section | Complementary | Feedback and monitoring loop | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b43) |
| `fsdl-ux` · [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Primary | Uncertainty, interaction design and feedback. | Only the linked “UX for Language User Interfaces” lecture; not the… [bounds](#unit-06-fsdl-ux) |
| `ar-gen-ux` · [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Alternative | Communicating limitations, feedback and human control. | Only the linked translated lesson: Communicating limitations, feedback and… [bounds](#unit-06-ar-gen-ux) |
| `ar-gen-lifecycle` · [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation, versioning and operational stages. | Only the linked translated lesson: Evaluation, versioning and operational… [bounds](#unit-06-ar-gen-lifecycle) |
| `otel` · [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)<br>OpenTelemetry · EN | Documentation / tutorial | Reference | Spans, attributes, context and exporting telemetry. | Consult the relevant example for Spans, attributes, context and exporting… [bounds](#unit-06-otel) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-fsdl-ux"></a>

**`fsdl-ux` — selected portion:** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Feedback and monitoring loop. Exact timestamps are not assigned.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-gen-ux"></a>

**`ar-gen-ux` — selected portion:** Only the linked translated lesson: Communicating limitations, feedback and human control. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Substitute only for user-facing feedback design. Monitoring instrumentation and feedback-quality checks remain separate required work.

<a id="unit-06-ar-gen-lifecycle"></a>

**`ar-gen-lifecycle` — selected portion:** Only the linked translated lesson: Evaluation, versioning and operational stages. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-otel"></a>

**`otel` — selected portion:** Consult the relevant example for Spans, attributes, context and exporting telemetry. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-gen-intro"></a>

<details>
<summary>ar-gen-intro · Introduction to generative AI · Arabic — access, scope and verification</summary>

[Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Application versus foundation model and basic capabilities.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Model selection for the product.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Model selection for the product. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-fsdl-foundation"></a>

<details>
<summary>fsdl-foundation · LLM Foundations — access, scope and verification</summary>

[LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Language-model capabilities and application boundaries.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Model selection for the product.
- **Retained broad selection notes (lookup only):** Only the linked “LLM Foundations” lecture; not the complete LLM Bootcamp. Use the parts relevant to Model selection for the product. Exact timestamps are not assigned.

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
- **Retained Level-wide topic association:** Model selection for the product.
- **Retained broad selection notes (lookup only):** The assertion type matching Model selection for the product; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

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
- **Retained Level-wide topic association:** Model selection for the product.
- **Retained broad selection notes (lookup only):** Consult the Language; task quality; license; privacy; context; availability sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-lifecycle"></a>

<details>
<summary>ar-gen-lifecycle · Generative AI lifecycle · Arabic — access, scope and verification</summary>

[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Evaluation, versioning and operational stages.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Latency and throughput; Feedback and monitoring loop.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Latency and throughput. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-locust"></a>

<details>
<summary>locust · Locust quickstart — access, scope and verification</summary>

[Locust quickstart](https://docs.locust.io/en/stable/quickstart.html) · Locust · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Concurrent user scenarios and latency/throughput measurement.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Latency and throughput; Measured optimization.
- **Retained broad selection notes (lookup only):** Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-otel"></a>

<details>
<summary>otel · Python instrumentation — access, scope and verification</summary>

[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) · OpenTelemetry · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Spans, attributes, context and exporting telemetry.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Latency and throughput; Cost accounting; Feedback and monitoring loop.
- **Retained broad selection notes (lookup only):** Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-19"></a>

<details>
<summary>ar-mini-19 · mini-RAG · Ollama Local LLM Server — access, scope and verification</summary>

[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Ollama Local LLM Server in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Cost accounting.
- **Retained broad selection notes (lookup only):** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-hf-token"></a>

<details>
<summary>hf-token · Tokenizers — access, scope and verification</summary>

[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) · Hugging Face · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Subword tokenization and language-dependent token counts.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Cost accounting.
- **Retained broad selection notes (lookup only):** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.

</details>

<a id="r-ar-mini-20"></a>

<details>
<summary>ar-mini-20 · mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic — access, scope and verification</summary>

[mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Safe caching.
- **Retained broad selection notes (lookup only):** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-authz"></a>

<details>
<summary>authz · Authorization cheat sheet — access, scope and verification</summary>

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · OWASP · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Deny-by-default object authorization and least privilege.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Safe caching.
- **Retained broad selection notes (lookup only):** Consult the Cache key; tenant boundary; source/version invalidation; expiry sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-sqlasync"></a>

<details>
<summary>sqlasync · SQLAlchemy asyncio — access, scope and verification</summary>

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** One session per concurrent task; explicit database I/O.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Safe caching.
- **Retained broad selection notes (lookup only):** Consult the Cache key; tenant boundary; source/version invalidation; expiry sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-agent-context"></a>

<details>
<summary>ar-agent-context · Context engineering · Arabic — access, scope and verification</summary>

[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Selecting and organizing information for agents.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Measured optimization.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Measured optimization. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Measured optimization.
- **Retained broad selection notes (lookup only):** Only the lesson matching the measured retrieval bottleneck; no full-course repeat.

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
- **Retained Level-wide topic association:** Measured optimization.
- **Retained broad selection notes (lookup only):** Read pgvector’s Querying, Indexing, Filtering and Hybrid Search sections relevant to a measured retrieval bottleneck. Test one change; provider caching/backpressure are separate techniques from F10, not pgvector features.

</details>

<a id="r-ar-gen-ux"></a>

<details>
<summary>ar-gen-ux · AI user experience · Arabic — access, scope and verification</summary>

[AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Communicating limitations, feedback and human control.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Feedback and monitoring loop.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Feedback and monitoring loop. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-fsdl-ux"></a>

<details>
<summary>fsdl-ux · UX for Language User Interfaces — access, scope and verification</summary>

[UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Uncertainty, interaction design and feedback.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Feedback and monitoring loop.
- **Retained broad selection notes (lookup only):** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Feedback and monitoring loop. Exact timestamps are not assigned.

</details>

<a id="r-sre-slos"></a>

<details>
<summary>sre-slos · Implementing SLOs — access, scope and verification</summary>

[Implementing SLOs](https://sre.google/workbook/implementing-slos/) · Google SRE · EN worked chapter

- **Resource Type:** Worked book chapter (free online).
- **Access:** Free.
- **Catalog scope:** Availability/latency indicators, objectives and error budgets.
- **Scope/version limits:** Use modest application-level targets; do not copy enterprise numbers.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Availability/latency indicators, objectives and error budgets. Optional lookup; implement only the portion that addresses the named gap.

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
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Evaluation review for the optimization comparison; do not repeat the entire short course.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

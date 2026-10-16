# Resource Library · L15 — Model Selection, Cost, Latency, and User Feedback

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

C4 model selection → comparable runs → C9 metrics → one bottleneck experiment → C10 feedback loop. Keep quality gates active during optimization.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Arabic lifecycle and deployment material provides context. Dedicated Arabic instruction for controlled model selection, tail latency and cache isolation was not verified; use C4/C9/C10 and the English engineering material.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md) | Microsoft<br>AR machine-translated text<br>Free | L15-T01 · Model selection for the product | Application versus foundation model and basic capabilities. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) | Microsoft<br>AR machine-translated text<br>Free | L15-T02 · Latency and throughput; L15-T06 · Feedback and monitoring loop | Evaluation, versioning and operational stages. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L15-T03 · Cost accounting | Ollama Local LLM Server in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L15-T04 · Safe caching | From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) | Microsoft<br>AR machine-translated text<br>Free | L15-T05 · Measured optimization | Selecting and organizing information for agents. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L15-T06 · Feedback and monitoring loop | Communicating limitations, feedback and human control. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L15-T01 · Model selection for the product | Language-model capabilities and application boundaries. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) | DeepLearning.AI · Chroma<br>EN video + labs<br>Limited-time free access advertised; account/terms may change | L15-T05 · Measured optimization | Query expansion, reranking and retrieval failure analysis. **Boundary:** Chroma is a lab alternative; no database migration is required. |
| [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L15-T06 · Feedback and monitoring loop | Uncertainty, interaction design and feedback. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | DeepLearning.AI · LlamaIndex/TruEra<br>EN video + notebooks<br>Limited-time free access advertised; account/terms may change | Optional support for this Level’s assessed exercises | Advanced retrieval and structured evaluation experiments. **Boundary:** Framework-specific lab; reimplement one comparison using your existing retrieval interface. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| C4 Model Selection pp.179–200 and Cost and Latency pp.177–178. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F10 PDF429–476 selectively; C9 Performance Metrics pp.412–418. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C10 Feedback Design pp.480–489 and limitations pp.490–491. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L15-T01 | Compare two feasible models on the same queries and configuration table. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L15-T02 | Measure cold/warm runs and concurrency with a fixed workload; show bottleneck spans. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L15-T03 | Report cost/request using explicit dated assumptions and a hard experiment budget. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L15-T04 | Test similar questions from two users and deleted sources before enabling a cache. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L15-T05 | Change one bottleneck factor and retain before/after quality, latency and cost results. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L15-T06 | Capture optional feedback, triage three cases and propose a measured follow-up experiment. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L15-T01 · Model selection for the product | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) | intfloat · model authors<br>EN<br>Free | L15-T01 · Model selection for the product | Supported languages, query/passage prefixes, examples and model limitations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html) | Locust<br>EN<br>Free | L15-T02 · Latency and throughput; L15-T05 · Measured optimization | Concurrent user scenarios and latency/throughput measurement. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | OpenTelemetry<br>EN<br>Free | L15-T02 · Latency and throughput; L15-T03 · Cost accounting; L15-T06 · Feedback and monitoring loop | Spans, attributes, context and exporting telemetry. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) | Hugging Face<br>EN<br>Free | L15-T03 · Cost accounting | Subword tokenization and language-dependent token counts. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP<br>EN<br>Free | L15-T04 · Safe caching | Deny-by-default object authorization and least privilege. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | SQLAlchemy<br>EN<br>Free | L15-T04 · Safe caching | One session per concurrent task; explicit database I/O. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [pgvector README](https://github.com/pgvector/pgvector) | pgvector maintainers<br>EN<br>Free | L15-T05 · Measured optimization | Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Implementing SLOs](https://sre.google/workbook/implementing-slos/) | Google SRE<br>EN worked chapter<br>Free | Optional support for this Level’s assessed exercises | Availability/latency indicators, objectives and error budgets. **Boundary:** Use modest application-level targets; do not copy enterprise numbers. |

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

# Resource Library · L08 — RAG Systems, Citations, and Retrieval Improvement

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Measured exact retrieval → cited generation → no-evidence tests → hybrid/reranking experiments only for observed ranking failures.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L08-T01 · RAG orchestration; L08-T02 · Citation correctness | Augmented Answers in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) | Microsoft<br>AR machine-translated text<br>Free | L08-T01 · RAG orchestration; L08-T03 · Ranking evaluation | Retrieval architecture and grounding. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L08-T04 · Hybrid search | The way to PgVector in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) | Microsoft<br>AR machine-translated text<br>Free | L08-T06 · Answer reliability and ablations | Fairness, reliability and accountable use. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | DeepLearning.AI · LlamaIndex/TruEra<br>EN video + notebooks<br>Limited-time free access advertised; account/terms may change | L08-T01 · RAG orchestration; L08-T02 · Citation correctness; L08-T03 · Ranking evaluation; L08-T06 · Answer reliability and ablations | Advanced retrieval and structured evaluation experiments. **Boundary:** Framework-specific lab; reimplement one comparison using your existing retrieval interface. |
| [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) | DeepLearning.AI · Chroma<br>EN video + labs<br>Limited-time free access advertised; account/terms may change | L08-T04 · Hybrid search; L08-T05 · Reranking and query changes | Query expansion, reranking and retrieval failure analysis. **Boundary:** Chroma is a lab alternative; no database migration is required. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag) | Abu Bakr Soliman<br>AR explanations / Python code<br>Free | Optional support for this Level’s assessed exercises | Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. **Boundary:** Educational reference, not a security or correctness certification. |

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| G4 printed pp.94–100: improvements and coding explanation. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F5 RAG and F11 PDF519–527 retrieval integration. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C6 pp.253–274, especially pp.267–272; C4 component evaluation. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Hugging Face semantic search lesson](https://huggingface.co/learn/llm-course/chapter5/6) | Hugging Face<br>EN notebook lesson<br>Free | Optional support for this Level’s assessed exercises | Build a semantic search experiment with embeddings. **Boundary:** Adapt the corpus and verify ranking locally; no claim of external grading. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L08-T01 | Ship /ask with passages, source IDs and a defined no-evidence response. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L08-T02 | Inject fabricated source IDs and unrelated real sources; catch both failure types. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L08-T03 | Compute a tiny ranking example manually and match the implementation. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L08-T04 | Compare lexical-only, vector-only and hybrid on identical owner-filtered queries. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L08-T05 | Add reranking only if evidence ranking improves enough to justify extra latency. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L08-T06 | Freeze a baseline, change one factor, report quality/citation/latency plus three failed cases. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [pgvector README](https://github.com/pgvector/pgvector) | pgvector maintainers<br>EN<br>Free | L08-T01 · RAG orchestration; L08-T04 · Hybrid search | Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L08-T02 · Citation correctness; L08-T06 · Answer reliability and ablations | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | pytest<br>EN<br>Free | L08-T02 · Citation correctness | Fixtures, scope, teardown and dependency isolation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) | Sentence Transformers<br>EN<br>Free | L08-T03 · Ranking evaluation | MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html) | PostgreSQL<br>EN<br>Free | L08-T04 · Hybrid search | tsvector, tsquery and ranking for a lexical baseline. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | Sentence Transformers<br>EN<br>Free | L08-T05 · Reranking and query changes | Bi-encoder candidate retrieval followed by cross-encoder reranking. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) | intfloat · model authors<br>EN<br>Free | L08-T05 · Reranking and query changes | Supported languages, query/passage prefixes, examples and model limitations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ragas evaluation documentation](https://docs.ragas.io/en/stable/) | Ragas<br>EN<br>Free | L08-T06 · Answer reliability and ablations | Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401) | Lewis et al.<br>EN research paper<br>Free | Optional support for this Level’s assessed exercises | Original RAG architecture and retrieval/generation distinction. **Boundary:** Modern application-level RAG need not reproduce the training architecture. |

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

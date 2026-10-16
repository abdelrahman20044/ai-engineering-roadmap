# Resource Library · L07 — RAG Document Preparation, Embeddings, and Semantic Search

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

G4/C6 retrieval basics → mini-RAG processing/search lessons → pgvector exact search → a labeled bilingual retrieval set. Keep page provenance before optimizing.

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
| [mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T01 · Parsing and extraction quality | Uploading a File in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T01 · Parsing and extraction quality; L07-T02 · Chunk design and metadata | File Processing in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T02 · Chunk design and metadata; L07-T06 · Repeatable ingestion lifecycle | Data Pipeline Enhancements in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Semantic Search](https://www.youtube.com/watch?v=V3swQKokJW8) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T03 · Embeddings and multilingual behavior; L07-T05 · Filtering and lexical baseline | Semantic Search in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Search applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/08-building-search-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L07-T03 · Embeddings and multilingual behavior | Embeddings and semantic retrieval. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Vector DB Factory](https://www.youtube.com/watch?v=JtS9UkvF_10) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T04 · Vector persistence and exact search | Vector DB Factory in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T04 · Vector persistence and exact search; L07-T05 · Filtering and lexical baseline | The way to PgVector in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L07-T06 · Repeatable ingestion lifecycle | From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | DeepLearning.AI · LlamaIndex/TruEra<br>EN video + notebooks<br>Limited-time free access advertised; account/terms may change | L07-T01 · Parsing and extraction quality; L07-T02 · Chunk design and metadata | Advanced retrieval and structured evaluation experiments. **Boundary:** Framework-specific lab; reimplement one comparison using your existing retrieval interface. |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Hugging Face<br>EN course + videos + quizzes<br>Free | L07-T03 · Embeddings and multilingual behavior | Transformer families, tokenization and using pretrained models. **Boundary:** Read targeted sections; training an LLM is optional. |
| [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) | DeepLearning.AI · Chroma<br>EN video + labs<br>Limited-time free access advertised; account/terms may change | L07-T05 · Filtering and lexical baseline | Query expansion, reranking and retrieval failure analysis. **Boundary:** Chroma is a lab alternative; no database migration is required. |

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
| G4 printed pp.74–82; C6 pp.257–266: retrieval foundations. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F5 PDF212–239: document ingestion/RAG; C8 pp.396–402: processing principles adapted to the corpus. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| pgvector official documentation: exact search and filtering first; ANN later if measured need exists. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Hugging Face semantic search lesson](https://huggingface.co/learn/llm-course/chapter5/6) | Hugging Face<br>EN notebook lesson<br>Free | Optional support for this Level’s assessed exercises | Build a semantic search experiment with embeddings. **Boundary:** Adapt the corpus and verify ranking locally; no claim of external grading. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L07-T01 | Extract three pages and manually compare text/order/page numbers with the originals. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L07-T02 | Compare two chunk policies and retain exact source offsets or page references. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L07-T03 | Embed Arabic and English queries with the documented prefixes and inspect top results. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L07-T04 | Run exact top-k queries in SQL and verify against a small in-memory baseline. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L07-T05 | Compare keyword and vector retrieval; test tenant isolation before returning chunks. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L07-T06 | Ingest the same document twice, change its version, delete it, and assert no stale duplicates. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html) | PyMuPDF<br>EN<br>Free | L07-T01 · Parsing and extraction quality; L07-T02 · Chunk design and metadata | Document extraction for RAG; check license and extraction quality for your use. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) | Sentence Transformers<br>EN<br>Free | L07-T03 · Embeddings and multilingual behavior | Encode documents/queries and score retrieval. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) | intfloat · model authors<br>EN<br>Free | L07-T03 · Embeddings and multilingual behavior | Supported languages, query/passage prefixes, examples and model limitations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [pgvector README](https://github.com/pgvector/pgvector) | pgvector maintainers<br>EN<br>Free | L07-T04 · Vector persistence and exact search; L07-T05 · Filtering and lexical baseline | Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html) | PostgreSQL<br>EN<br>Free | L07-T05 · Filtering and lexical baseline | tsvector, tsquery and ranking for a lexical baseline. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) | SQLAlchemy<br>EN<br>Free | L07-T06 · Repeatable ingestion lifecycle | Mapped classes, relationships, selects and unit of work. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

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

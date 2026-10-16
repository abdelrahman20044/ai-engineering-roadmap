# Resource Library · L07 — RAG Document Preparation, Embeddings, and Semantic Search

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

1. [Parsing and extraction quality](#unit-01)
2. [Chunk design and metadata](#unit-02)
3. [Embeddings and multilingual behavior](#unit-03)
4. [Vector persistence and exact search](#unit-04)
5. [Filtering and lexical baseline](#unit-05)
6. [Repeatable ingestion lifecycle](#unit-06)

<a id="unit-01"></a>

## 1. Parsing and extraction quality

[Return to README Step 1](README.md#1-parsing-and-extraction-quality)

**Topic/subtopics:** Text PDF; page order; tables; scanned PDF limitations; extraction checks.

**Required sequence:** the assigned book slices [B21 · F5](../docs/READING_GUIDE.md#b21), [B22 · C8](../docs/READING_GUIDE.md#b22) **THEN** `pymupdf`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-parsing-and-extraction-quality) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B21 · F5](../docs/READING_GUIDE.md#b21)<br>Alireza Parandeh · EN | Book Section | Complementary | Parsing and extraction quality | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b21) |
| [B22 · C8](../docs/READING_GUIDE.md#b22)<br>Chip Huyen · EN | Book Section | Complementary | Parsing and extraction quality | [Skim: exact assigned slice](../docs/READING_GUIDE.md#b22) |
| `pymupdf` · [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html)<br>PyMuPDF · EN | Documentation / tutorial | Primary | Document extraction for RAG; check license and extraction… | Consult the Text PDF; page order; tables; scanned PDF limitations;… [bounds](#unit-01-pymupdf) |
| `ar-mini-7` · [mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Uploading a File in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-8` · [mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | File Processing in a working RAG backend. | The linked video only; not its playlist. |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | Advanced RAG Pipeline orientation only; Sentence-window retrieval design… [bounds](#unit-01-dla-rag) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-pymupdf"></a>

**`pymupdf` — selected portion:** Consult the Text PDF; page order; tables; scanned PDF limitations; extraction checks sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-mini-7"></a>

**`ar-mini-7` — selected portion:** Only the linked “Uploading a File” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-ar-mini-8"></a>

**`ar-mini-8` — selected portion:** Only the linked “File Processing” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-dla-rag"></a>

**`dla-rag` — selected portion:** Advanced RAG Pipeline orientation only; Sentence-window retrieval design comparison is optional. Do not build auto-merging yet.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-02"></a>

## 2. Chunk design and metadata

[Return to README Step 2](README.md#2-chunk-design-and-metadata)

**Topic/subtopics:** Size; overlap; headings; stable IDs; source/page/version.

**Required sequence:** the assigned book slice [B19 · G4](../docs/READING_GUIDE.md#b19) **THEN** `ar-mini-8`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `pymupdf`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-chunk-design-and-metadata) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B19 · G4](../docs/READING_GUIDE.md#b19)<br>Andrea De Mauro · EN | Book Section | Complementary | Chunk design and metadata | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b19) |
| [B21 · F5](../docs/READING_GUIDE.md#b21)<br>Alireza Parandeh · EN | Book Section | Reference | Chunk design and metadata | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b21) |
| `ar-mini-8` · [mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | File Processing in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-12` · [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Data Pipeline Enhancements in a working RAG backend. | The linked video only; not its playlist. |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | Advanced RAG Pipeline orientation only; Sentence-window retrieval design… [bounds](#unit-02-dla-rag) |
| `pymupdf` · [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html)<br>PyMuPDF · EN | Documentation / tutorial | Reference | Document extraction for RAG; check license and extraction… | Consult the relevant example for Document extraction for RAG; check… [bounds](#unit-02-pymupdf) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-ar-mini-8"></a>

**`ar-mini-8` — selected portion:** Only the linked “File Processing” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mini-12"></a>

**`ar-mini-12` — selected portion:** Only the linked “Data Pipeline Enhancements” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-dla-rag"></a>

**`dla-rag` — selected portion:** Advanced RAG Pipeline orientation only; Sentence-window retrieval design comparison is optional. Do not build auto-merging yet.

**Relationship:** Different or partially overlapping concepts; as-needed support, not a substitute for the required route.

<a id="unit-02-pymupdf"></a>

**`pymupdf` — selected portion:** Consult the relevant example for Document extraction for RAG; check license and extraction quality for your use. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Embeddings and multilingual behavior

[Return to README Step 3](README.md#3-embeddings-and-multilingual-behavior)

**Topic/subtopics:** Bi-encoders; query/document encoding; model card; prefixes; dimensions.

**Required sequence (default route):** the assigned book slice [B20 · C6](../docs/READING_GUIDE.md#b20) **THEN** `st-search`. Stop each source at the stated portion.

**Choose ONE explanation for embeddings-based semantic-search intuition:** default `st-search` **OR** `ar-mini-16`. The multilingual comparison and model-specific prefix/tokenization rules remain required. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `e5`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-embeddings-and-multilingual-behavior) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B20 · C6](../docs/READING_GUIDE.md#b20)<br>Chip Huyen · EN | Book Section | Complementary | Embeddings and multilingual behavior | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b20) |
| [B23 · C3](../docs/READING_GUIDE.md#b23)<br>Chip Huyen · EN | Book Section | Reference | Embeddings and multilingual behavior | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b23) |
| `st-search` · [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)<br>Sentence Transformers · EN | Documentation / tutorial | Primary | Encode documents/queries and score retrieval. | Consult the Bi-encoders; query/document encoding; model card; prefixes;… [bounds](#unit-03-st-search) |
| `ar-mini-16` · [mini-RAG · Semantic Search](https://www.youtube.com/watch?v=V3swQKokJW8)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Alternative | Semantic Search in a working RAG backend. | The linked video only; not its playlist. |
| `ar-gen-search` · [Search applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/08-building-search-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Embeddings and semantic retrieval. | Only the linked translated lesson: Embeddings and semantic retrieval.… [bounds](#unit-03-ar-gen-search) |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Complementary (as needed) | Transformer families, tokenization and using pretrained… | Chapter 2 tokenizer/model basics for retrieval inputs; no training curriculum. |
| `e5` · [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small)<br>intfloat · model authors · EN | Model card + usage examples | Reference | Supported languages, query/passage prefixes, examples and… | Consult the relevant example for Supported languages, query/passage… [bounds](#unit-03-e5) |
| `ir-labs` · [Hugging Face semantic search lesson](https://huggingface.co/learn/llm-course/chapter5/6)<br>Hugging Face · EN notebook lesson | Practical notebook lesson | Complementary (as needed) | Build a semantic search experiment with embeddings. | One matching lab/notebook for the stated topic; do not complete the whole platform. |
| `rag-paper` · [Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401)<br>Lewis et al. · EN research paper | Research paper | Optional Advanced | Original RAG architecture and retrieval/generation… | Problem statement and architecture/results relevant to this topic;… [bounds](#unit-03-rag-paper) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-st-search"></a>

**`st-search` — selected portion:** Consult the Bi-encoders; query/document encoding; model card; prefixes; dimensions sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-mini-16"></a>

**`ar-mini-16` — selected portion:** Only the linked “Semantic Search” lesson. Not the full mini-RAG playlist.

**Relationship:** Substitute only for embeddings-based semantic-search intuition. The multilingual comparison and model-specific prefix/tokenization rules remain required.

<a id="unit-03-ar-gen-search"></a>

**`ar-gen-search` — selected portion:** Only the linked translated lesson: Embeddings and semantic retrieval. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-hf-llm"></a>

**`hf-llm` — selected portion:** Chapter 2 tokenizer/model basics for retrieval inputs; no training curriculum.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-e5"></a>

**`e5` — selected portion:** Consult the relevant example for Supported languages, query/passage prefixes, examples and model limitations. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-03-ir-labs"></a>

**`ir-labs` — selected portion:** One matching lab/notebook for the stated topic; do not complete the whole platform.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-rag-paper"></a>

**`rag-paper` — selected portion:** Problem statement and architecture/results relevant to this topic; optional depth, not paper-wide implementation homework.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-04"></a>

## 4. Vector persistence and exact search

[Return to README Step 4](README.md#4-vector-persistence-and-exact-search)

**Topic/subtopics:** pgvector types; distance operators; deterministic test corpus.

**Required sequence (default route):** `ar-mini-21`. Stop each source at the stated portion.

**Choose ONE explanation for storing/querying vectors in PostgreSQL:** default `ar-mini-21` **OR** `pgvector`. Use the same pgvector schema and exact-search tests in either route. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-vector-persistence-and-exact-search) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B21 · F5](../docs/READING_GUIDE.md#b21)<br>Alireza Parandeh · EN | Book Section | Reference | Vector persistence and exact search | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b21) |
| `ar-mini-21` · [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | The way to PgVector in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-15` · [mini-RAG · Vector DB Factory](https://www.youtube.com/watch?v=JtS9UkvF_10)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Vector DB Factory in a working RAG backend. | The linked video only; not its playlist. |
| `pgvector` · [pgvector README](https://github.com/pgvector/pgvector)<br>pgvector maintainers · EN | Official repository / implementation guide | Alternative | Exact search, filtered approximate search, HNSW/IVFFlat… | Consult the relevant example for Exact search, filtered approximate… [bounds](#unit-04-pgvector) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-ar-mini-21"></a>

**`ar-mini-21` — selected portion:** Only the linked “The way to PgVector” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-mini-15"></a>

**`ar-mini-15` — selected portion:** Only the linked “Vector DB Factory” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-pgvector"></a>

**`pgvector` — selected portion:** Consult the relevant example for Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Substitute only for storing/querying vectors in PostgreSQL. Use the same pgvector schema and exact-search tests in either route.

</details>

<a id="unit-05"></a>

## 5. Filtering and lexical baseline

[Return to README Step 5](README.md#5-filtering-and-lexical-baseline)

**Topic/subtopics:** Owner/document predicates; full-text search; language configuration.

**Required sequence:** `fts` **THEN** `pgvector` (a different required capability). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-filtering-and-lexical-baseline) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B20 · C6](../docs/READING_GUIDE.md#b20)<br>Chip Huyen · EN | Book Section | Reference | Filtering and lexical baseline | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b20) |
| `fts` · [PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html)<br>PostgreSQL · EN | Documentation / tutorial | Primary | tsvector, tsquery and ranking for a lexical baseline. | Consult the Owner/document predicates; full-text search; language… [bounds](#unit-05-fts) |
| `ar-mini-16` · [mini-RAG · Semantic Search](https://www.youtube.com/watch?v=V3swQKokJW8)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Semantic Search in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-21` · [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | The way to PgVector in a working RAG backend. | The linked video only; not its playlist. |
| `dla-retrieval` · [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai)<br>DeepLearning.AI · Chroma · EN video + labs | Short Course + notebooks | Complementary (as needed) | Query expansion, reranking and retrieval failure analysis. | Overview of embeddings-based retrieval; Pitfalls of retrieval—when simple… [bounds](#unit-05-dla-retrieval) |
| `pgvector` · [pgvector README](https://github.com/pgvector/pgvector)<br>pgvector maintainers · EN | Official repository / implementation guide | Complementary (required) | Exact search, filtered approximate search, HNSW/IVFFlat… | Consult the relevant example for Exact search, filtered approximate… [bounds](#unit-05-pgvector) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-fts"></a>

**`fts` — selected portion:** Consult the Owner/document predicates; full-text search; language configuration sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-16"></a>

**`ar-mini-16` — selected portion:** Only the linked “Semantic Search” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Semantic/vector-search teaching; lexical/hybrid details use PostgreSQL docs.

<a id="unit-05-ar-mini-21"></a>

**`ar-mini-21` — selected portion:** Only the linked “The way to PgVector” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Semantic/vector-search teaching; lexical/hybrid details use PostgreSQL docs.

<a id="unit-05-dla-retrieval"></a>

**`dla-retrieval` — selected portion:** Overview of embeddings-based retrieval; Pitfalls of retrieval—when simple vector search fails. This is background, not SQL full-text syntax.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-pgvector"></a>

**`pgvector` — selected portion:** Consult the relevant example for Exact search, filtered approximate search, HNSW/IVFFlat and SQL hybrid examples. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Required after the primary: a distinct capability, not a replacement.

</details>

<a id="unit-06"></a>

## 6. Repeatable ingestion lifecycle

[Return to README Step 6](README.md#6-repeatable-ingestion-lifecycle)

**Topic/subtopics:** Content hash; versions; retries; delete/re-index; stale vectors.

**Required sequence:** `sqlalchemy`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-repeatable-ingestion-lifecycle) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B21 · F5](../docs/READING_GUIDE.md#b21)<br>Alireza Parandeh · EN | Book Section | Reference | Repeatable ingestion lifecycle | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b21) |
| [B22 · C8](../docs/READING_GUIDE.md#b22)<br>Chip Huyen · EN | Book Section | Reference | Repeatable ingestion lifecycle | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b22) |
| `sqlalchemy` · [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)<br>SQLAlchemy · EN | Documentation / tutorial | Primary | Mapped classes, relationships, selects and unit of work. | Review SQLAlchemy transaction/session examples only. Design source hashes,… [bounds](#unit-06-sqlalchemy) |
| `ar-mini-12` · [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Data Pipeline Enhancements in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `mini-code` · [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)<br>Abu Bakr Soliman · AR explanations / Python code | Course repository / lesson index | Optional Advanced | Match each lesson to its tutorial branch; compare… | Only the branch corresponding to this topic’s named mini-RAG lesson.… [bounds](#unit-06-mini-code) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-sqlalchemy"></a>

**`sqlalchemy` — selected portion:** Review SQLAlchemy transaction/session examples only. Design source hashes, ingestion versions and retry state in your application; these AI lifecycle decisions are your exercise.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-mini-12"></a>

**`ar-mini-12` — selected portion:** Only the linked “Data Pipeline Enhancements” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-mini-code"></a>

**`mini-code` — selected portion:** Only the branch corresponding to this topic’s named mini-RAG lesson. Inspect after writing your own implementation.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-mini-7"></a>

<details>
<summary>ar-mini-7 · mini-RAG · Uploading a File — access, scope and verification</summary>

[mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Uploading a File in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Parsing and extraction quality.
- **Retained broad selection notes (lookup only):** Only the linked “Uploading a File” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-mini-8"></a>

<details>
<summary>ar-mini-8 · mini-RAG · File Processing — access, scope and verification</summary>

[mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** File Processing in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Parsing and extraction quality; Chunk design and metadata.
- **Retained broad selection notes (lookup only):** Only the linked “File Processing” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-pymupdf"></a>

<details>
<summary>pymupdf · PyMuPDF RAG extraction — access, scope and verification</summary>

[PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html) · PyMuPDF · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Document extraction for RAG; check license and extraction quality for your use.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Parsing and extraction quality; Chunk design and metadata.
- **Retained broad selection notes (lookup only):** Consult the Text PDF; page order; tables; scanned PDF limitations; extraction checks sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Parsing and extraction quality; Chunk design and metadata.
- **Retained broad selection notes (lookup only):** Orientation to the advanced-RAG pipeline only; do not implement sentence-window/auto-merging before your baseline.

</details>

<a id="r-ar-mini-12"></a>

<details>
<summary>ar-mini-12 · mini-RAG · Data Pipeline Enhancements — access, scope and verification</summary>

[mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Data Pipeline Enhancements in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Chunk design and metadata; Repeatable ingestion lifecycle.
- **Retained broad selection notes (lookup only):** Only the linked “Data Pipeline Enhancements” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-mini-16"></a>

<details>
<summary>ar-mini-16 · mini-RAG · Semantic Search — access, scope and verification</summary>

[mini-RAG · Semantic Search](https://www.youtube.com/watch?v=V3swQKokJW8) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Semantic Search in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Embeddings and multilingual behavior; Filtering and lexical baseline.
- **Retained broad selection notes (lookup only):** Only the linked “Semantic Search” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-gen-search"></a>

<details>
<summary>ar-gen-search · Search applications · Arabic — access, scope and verification</summary>

[Search applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/08-building-search-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Embeddings and semantic retrieval.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Embeddings and multilingual behavior.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Embeddings and multilingual behavior. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-hf-llm"></a>

<details>
<summary>hf-llm · Hugging Face LLM course — access, scope and verification</summary>

[Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) · Hugging Face · EN course + videos + quizzes

- **Resource Type:** Full course: text, videos and quizzes.
- **Access:** Free.
- **Catalog scope:** Transformer families, tokenization and using pretrained models.
- **Scope/version limits:** Read targeted sections; training an LLM is optional.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Embeddings and multilingual behavior.
- **Retained broad selection notes (lookup only):** Use the semantic-search lesson separately; no general LLM-course completion is assigned.

</details>

<a id="r-st-search"></a>

<details>
<summary>st-search · Sentence Transformers semantic search — access, scope and verification</summary>

[Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) · Sentence Transformers · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Encode documents/queries and score retrieval.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Embeddings and multilingual behavior.
- **Retained broad selection notes (lookup only):** Consult the Bi-encoders; query/document encoding; model card; prefixes; dimensions sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Embeddings and multilingual behavior.
- **Retained broad selection notes (lookup only):** Consult the Bi-encoders; query/document encoding; model card; prefixes; dimensions sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-15"></a>

<details>
<summary>ar-mini-15 · mini-RAG · Vector DB Factory — access, scope and verification</summary>

[mini-RAG · Vector DB Factory](https://www.youtube.com/watch?v=JtS9UkvF_10) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Vector DB Factory in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Vector persistence and exact search.
- **Retained broad selection notes (lookup only):** Only the linked “Vector DB Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

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
- **Retained Level-wide topic association:** Vector persistence and exact search; Filtering and lexical baseline.
- **Retained broad selection notes (lookup only):** Only the linked “The way to PgVector” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

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
- **Retained Level-wide topic association:** Vector persistence and exact search; Filtering and lexical baseline.
- **Retained broad selection notes (lookup only):** Consult the pgvector types; distance operators; deterministic test corpus sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Filtering and lexical baseline.
- **Retained broad selection notes (lookup only):** “Overview of embeddings-based retrieval” and “Pitfalls of retrieval - when simple vector search fails” only.

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
- **Retained Level-wide topic association:** Filtering and lexical baseline.
- **Retained broad selection notes (lookup only):** Consult the Owner/document predicates; full-text search; language configuration sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Repeatable ingestion lifecycle.
- **Retained broad selection notes (lookup only):** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-sqlalchemy"></a>

<details>
<summary>sqlalchemy · SQLAlchemy Unified Tutorial — access, scope and verification</summary>

[SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Mapped classes, relationships, selects and unit of work.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Repeatable ingestion lifecycle.
- **Retained broad selection notes (lookup only):** Review SQLAlchemy transaction/session examples only. Design source hashes, ingestion versions and retry state in your application; these AI lifecycle decisions are your exercise.

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

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

# L07 · RAG Document Preparation, Embeddings, and Semantic Search

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 3 · Grounded Retrieval and Context | 16–24 h | 3/5 | P1 | [L03](../03-Deep-Learning-Foundation-Models/README.md), [L06](../06-Application-State/README.md) |

**Unlocks:** [L08](../08-RAG-Systems/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Convert a small textual PDF into traceable chunks with page provenance. Compare a lexical baseline with embeddings appropriate to the application language. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Database readiness | Persist owner/document/version/chunk metadata with tested ownership. |
| Vector readiness | Explain dot product and cosine and distinguish similarity from probability. |
| Corpus readiness | Use a small permitted textual corpus and list parsing limitations. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Parsing and extraction quality: Extract three pages and manually compare text/order/page numbers with the originals.
- [ ] Chunk design and metadata: Compare two chunk policies and retain exact source offsets or page references.
- [ ] Embeddings and multilingual behavior: Embed Arabic and English queries with the documented prefixes and inspect top results.
- [ ] Vector persistence and exact search: Run exact top-k queries in SQL and verify against a small in-memory baseline.
- [ ] Filtering and lexical baseline: Compare keyword and vector retrieval; test tenant isolation before returning chunks.
- [ ] Repeatable ingestion lifecycle: Ingest the same document twice, change its version, delete it, and assert no stale duplicates.

## Recommended learning path

G4/C6 retrieval basics → mini-RAG processing/search lessons → pgvector exact search → a labeled bilingual retrieval set. Keep page provenance before optimizing.

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
| **L07-T01 · Parsing and extraction quality**<br>Text PDF; page order; tables; scanned PDF limitations; extraction checks | [mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7) (AR video)<br>[mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw) (AR video) | [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html) (EN)<br>[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Extract three pages and manually compare text/order/page numbers with the originals. |
| **L07-T02 · Chunk design and metadata**<br>Size; overlap; headings; stable IDs; source/page/version | [mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw) (AR video)<br>[mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) (AR video) | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Compare two chunk policies and retain exact source offsets or page references. |
| **L07-T03 · Embeddings and multilingual behavior**<br>Bi-encoders; query/document encoding; model card; prefixes; dimensions | [mini-RAG · Semantic Search](https://www.youtube.com/watch?v=V3swQKokJW8) (AR video)<br>[Search applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/08-building-search-applications/README.md) (AR machine-translated text) | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Embed Arabic and English queries with the documented prefixes and inspect top results. |
| **L07-T04 · Vector persistence and exact search**<br>pgvector types; distance operators; deterministic test corpus | [mini-RAG · Vector DB Factory](https://www.youtube.com/watch?v=JtS9UkvF_10) (AR video)<br>[mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE) (AR video) | [pgvector README](https://github.com/pgvector/pgvector) (EN) | Run exact top-k queries in SQL and verify against a small in-memory baseline. |
| **L07-T05 · Filtering and lexical baseline**<br>Owner/document predicates; full-text search; language configuration | [mini-RAG · Semantic Search](https://www.youtube.com/watch?v=V3swQKokJW8) (AR video)<br>[mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE) (AR video)<br>**Scope:** Semantic/vector-search teaching; lexical/hybrid details use PostgreSQL docs. | [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) (EN video + labs) | Compare keyword and vector retrieval; test tenant isolation before returning chunks. |
| **L07-T06 · Repeatable ingestion lifecycle**<br>Content hash; versions; retries; delete/re-index; stale vectors | [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) (AR video)<br>[mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video) | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN) | Ingest the same document twice, change its version, delete it, and assert no stale duplicates. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L07-T01 | F5 PDF212–239; C8 pp.396–402 | [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html) (EN) |
| L07-T02 | G4 pp.74–82; C6 pp.257–266 | [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html) (EN) |
| L07-T03 | C6 pp.257–266; G4 retrieval concepts | [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) (EN)<br>[Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) (EN) |
| L07-T04 | F5 RAG; F7 persistence reference | [pgvector README](https://github.com/pgvector/pgvector) (EN) |
| L07-T05 | C6 retrieval foundations; language behavior is an implementation extension | [pgvector README](https://github.com/pgvector/pgvector) (EN)<br>[PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html) (EN) |
| L07-T06 | C8 processing principles; F7 transactions | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N12 · Data Preparation & Feature Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N17 · Embeddings, Vector DBs & Semantic Search | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N19 · RAG Systems Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L07-E1 | Start with the JSONL corpus, then a permitted 20–50-page text PDF. | Preserve PDF page, printed label if available, and offsets before cleaning. |
| L07-E2 | Handle empty, corrupt, and scanned PDFs explicitly. | Unsupported inputs have a clear failure reason rather than an empty ready index. |
| L07-E3 | Compare two chunk configurations and version the embedding setup. | Save chunker, document, model, and dimension; never mix incompatible embedding spaces. |
| L07-E4 | Implement a keyword baseline and exact vector retrieval. | Evaluate representative queries, including cross-language cases if they belong to the product scope. |
| L07-E5 | Reprocess an identical file and an updated version. | No duplicate chunks, no partially published version, and a clear deletion contract for L11. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Text without provenance | Keep source ID, page, chunk ordinal, version and owner throughout ingestion. |
| Choosing an English-only embedding blindly | Test Arabic/English queries and follow model-card preprocessing. |
| ANN before a baseline | Use exact search to establish correctness and measure before adding an index. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Why overlap chunks?
2. Why store an embedding model version?
3. Can you filter after returning candidates?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | It can preserve boundary context but increases duplicates, cost and retrieval redundancy. |
| 2 | Changing models or dimensions invalidates comparisons and may require re-indexing. |
| 3 | Ownership must be enforced in retrieval; post-filtering alone can leak data or destroy recall. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | Ingestion functions or CLI, corpus manifest, and provenance tests; Lexical and dense retrieval baseline | Every chunk maps to its source. Reprocessing is safe, embedding dimensions match storage, and the implementation remains small enough to debug. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Every chunk maps to its source. Reprocessing is safe, embedding dimensions match storage, and the implementation remains small enough to debug.

## Postpone until justified

- Distributed processing without scale
- Premature ANN or OCR

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L07 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L06](../06-Application-State/README.md) · Next numbered Level: [L08](../08-RAG-Systems/README.md)

# L07 · RAG Document Preparation, Embeddings, and Semantic Search

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 3 · 16–24 focused hours · Difficulty 3/5 · P1**

**You will learn:** Convert a small textual PDF into traceable chunks with page provenance. Compare a lexical baseline with embeddings appropriate to the application language.

**Before starting:** [L03](../03-Deep-Learning-Foundation-Models/README.md), [L06](../06-Application-State/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B21 · F5](../docs/READING_GUIDE.md#b21) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Parsing and extraction quality

**Learn:** Text PDF; page order; tables; scanned PDF limitations; extraction checks.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B21 · F5](../docs/READING_GUIDE.md#b21) — **Read Now**. PDF pp.219–236: document preparation, upload, extraction, chunking, embeddings and vector storage. Web scraping pp.213–218 is optional.
- [B22 · C8](../docs/READING_GUIDE.md#b22) — **Skim**. Printed pp.396–402: processing principles applied to the document corpus. B07 quality is review only.

**Primary · Official documentation / tutorial:** [PyMuPDF RAG extraction](https://pymupdf.readthedocs.io/en/latest/rag.html). Consult the Text PDF; page order; tables; scanned PDF limitations; extraction checks sections/examples only. Do not read the entire documentation site.

**Practice:** Extract three pages and manually compare text/order/page numbers with the originals.

**Completion check:** Three extracted pages retain correct ordering and page identifiers.

### 2. Chunk design and metadata

**Learn:** Size; overlap; headings; stable IDs; source/page/version.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B19 · G4](../docs/READING_GUIDE.md#b19) — **Read Now**. Printed pp.74–82: retrieval, embeddings and grounding intuition. The improvement/code slice is B24.
- [B21 · F5](../docs/READING_GUIDE.md#b21) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video (lesson within playlist):** [mini-RAG · File Processing](https://www.youtube.com/watch?v=gQgr2iwtSBw). Only the linked “File Processing” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Compare two chunk policies and retain exact source offsets or page references.

**Completion check:** Both chunk policies preserve source/version metadata.

### 3. Embeddings and multilingual behavior

**Learn:** Bi-encoders; query/document encoding; model card; prefixes; dimensions.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B20 · C6](../docs/READING_GUIDE.md#b20) — **Read Now**. Printed pp.253–266: retrieval foundations. No agent/memory reading yet.
- [B23 · C3](../docs/READING_GUIDE.md#b23) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html). Consult the Bi-encoders; query/document encoding; model card; prefixes; dimensions sections/examples only. Do not read the entire documentation site.

**Practice:** Embed Arabic and English queries with the documented prefixes and inspect top results.

**Completion check:** Model-card query/passage prefixes are applied to the bilingual test set.

### 4. Vector persistence and exact search

**Learn:** pgvector types; distance operators; deterministic test corpus.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B21 · F5](../docs/READING_GUIDE.md#b21) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video (lesson within playlist):** [mini-RAG · The way to PgVector](https://www.youtube.com/watch?v=g99yq5zlYAE). Only the linked “The way to PgVector” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Run exact top-k queries in SQL and verify against a small in-memory baseline.

**Completion check:** SQL exact top-k agrees with the small deterministic baseline.

### 5. Filtering and lexical baseline

**Learn:** Owner/document predicates; full-text search; language configuration.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B20 · C6](../docs/READING_GUIDE.md#b20) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [PostgreSQL text search controls](https://www.postgresql.org/docs/current/textsearch-controls.html). Consult the Owner/document predicates; full-text search; language configuration sections/examples only. Do not read the entire documentation site.

**Practice:** Compare keyword and vector retrieval; test tenant isolation before returning chunks.

**Completion check:** Owner filters apply before results are returned; lexical/vector results are compared.

### 6. Repeatable ingestion lifecycle

**Learn:** Content hash; versions; retries; delete/re-index; stale vectors.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B21 · F5](../docs/READING_GUIDE.md#b21) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B22 · C8](../docs/READING_GUIDE.md#b22) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/). Review SQLAlchemy transaction/session examples only. Design source hashes, ingestion versions and retry state in your application; these AI lifecycle decisions are your exercise.

**Practice:** Ingest the same document twice, change its version, delete it, and assert no stale duplicates.

**Completion check:** Retry, version change and deletion leave no stale duplicate vectors.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L07-E1:** Start with the JSONL corpus, then a permitted 20–50-page text PDF.
  - **Pass:** Preserve PDF page, printed label if available, and offsets before cleaning.
- [ ] **L07-E2:** Handle empty, corrupt, and scanned PDFs explicitly.
  - **Pass:** Unsupported inputs have a clear failure reason rather than an empty ready index.
- [ ] **L07-E3:** Compare two chunk configurations and version the embedding setup.
  - **Pass:** Save chunker, document, model, and dimension; never mix incompatible embedding spaces.
- [ ] **L07-E4:** Implement a keyword baseline and exact vector retrieval.
  - **Pass:** Evaluate representative queries, including cross-language cases if they belong to the product scope.
- [ ] **L07-E5:** Reprocess an identical file and an updated version.
  - **Pass:** No duplicate chunks, no partially published version, and a clear deletion contract for L11.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S3](../project/milestones/s3.md). Every chunk maps to its source. Reprocessing is safe, embedding dimensions match storage, and the implementation remains small enough to debug.

**Keep:** Ingestion functions or CLI, corpus manifest, and provenance tests; Lexical and dense retrieval baseline.

## What to defer

- Distributed processing without scale
- Premature ANN or OCR

## Record progress and choose the next Level

```bash
python scripts/progress.py set L07 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L08](../08-RAG-Systems/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

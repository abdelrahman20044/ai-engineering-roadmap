# Technical Details · L07

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Database readiness:** Persist owner/document/version/chunk metadata with tested ownership.
- **Vector readiness:** Explain dot product and cosine and distinguish similarity from probability.
- **Corpus readiness:** Use a small permitted textual corpus and list parsing limitations.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Parsing and extraction quality:** Text PDF; page order; tables; scanned PDF limitations; extraction checks.
- **Chunk design and metadata:** Size; overlap; headings; stable IDs; source/page/version.
- **Embeddings and multilingual behavior:** Bi-encoders; query/document encoding; model card; prefixes; dimensions.
- **Vector persistence and exact search:** pgvector types; distance operators; deterministic test corpus.
- **Filtering and lexical baseline:** Owner/document predicates; full-text search; language configuration.
- **Repeatable ingestion lifecycle:** Content hash; versions; retries; delete/re-index; stale vectors.

## Common mistakes and debugging

### Text without provenance

Keep source ID, page, chunk ordinal, version and owner throughout ingestion.

### Choosing an English-only embedding blindly

Test Arabic/English queries and follow model-card preprocessing.

### ANN before a baseline

Use exact search to establish correctness and measure before adding an index.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Why overlap chunks?
2. Why store an embedding model version?
3. Can you filter after returning candidates?

<details>
<summary>Answer guide</summary>

**Why overlap chunks?**

It can preserve boundary context but increases duplicates, cost and retrieval redundancy.

**Why store an embedding model version?**

Changing models or dimensions invalidates comparisons and may require re-indexing.

**Can you filter after returning candidates?**

Ownership must be enforced in retrieval; post-filtering alone can leak data or destroy recall.

</details>

## ITI provenance and industry extensions

- **N12:** Data Preparation & Feature Engineering — official published module title.
- **N17:** Embeddings, Vector DBs & Semantic Search — official published module title.
- **N19:** RAG Systems Engineering — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Extract three pages and manually compare text/order/page numbers with the originals.
- [ ] Compare two chunk policies and retain exact source offsets or page references.
- [ ] Embed Arabic and English queries with the documented prefixes and inspect top results.
- [ ] Run exact top-k queries in SQL and verify against a small in-memory baseline.
- [ ] Compare keyword and vector retrieval; test tenant isolation before returning chunks.
- [ ] Ingest the same document twice, change its version, delete it, and assert no stale duplicates.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

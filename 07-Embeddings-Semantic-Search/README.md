# L07 · RAG Document Preparation, Embeddings, and Semantic Search

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 3 · Grounded Retrieval and Context | 16–24 h | 3/5 | P1 | [L03](../03-Deep-Learning-Foundation-Models/README.md), [L06](../06-Application-State/README.md) |

**Outcome:** Convert a small textual PDF into traceable chunks with page provenance. Compare a lexical baseline with embeddings appropriate to the application language.

**Unlocks:** [L08](../08-RAG-Systems/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Parsing, chunking, metadata | F5 PDF212–239; C8 pp.396–402; [pgvector search and indexing](https://github.com/pgvector/pgvector) | [Practice 1](resources.md#practice-and-evidence) |
| Embeddings and similarity | G4 pp.74–82; C6 pp.257–266; [NumPy absolute beginners tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html) | [Practice 2](resources.md#practice-and-evidence) |
| Exact vector search and filtering | C6 retrieval foundations; [pgvector search and indexing](https://github.com/pgvector/pgvector) | [Practice 3](resources.md#practice-and-evidence) |
| Idempotent re-indexing and deletion | F7 persistence; C8 processing principles; [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N12** — Data Preparation & Feature Engineering.
- **N17** — Embeddings, Vector DBs & Semantic Search.
- **N19** — RAG Systems Engineering.

| ITI topic IDs | Interpretation |
| --- | --- |
| N12, N17, N19 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L07-E1 | Start with the JSONL corpus, then a permitted 20–50-page text PDF. | Preserve PDF page, printed label if available, and offsets before cleaning. |
| L07-E2 | Handle empty, corrupt, and scanned PDFs explicitly. | Unsupported inputs have a clear failure reason rather than an empty ready index. |
| L07-E3 | Compare two chunk configurations and version the embedding setup. | Save chunker, document, model, and dimension; never mix incompatible embedding spaces. |
| L07-E4 | Implement a keyword baseline and exact vector retrieval. | Evaluate representative queries, including cross-language cases if they belong to the product scope. |
| L07-E5 | Reprocess an identical file and an updated version. | No duplicate chunks, no partially published version, and a clear deletion contract for L11. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | Ingestion functions or CLI, corpus manifest, and provenance tests; Lexical and dense retrieval baseline | Every chunk maps to its source. Reprocessing is safe, embedding dimensions match storage, and the implementation remains small enough to debug. |

## Postpone

| Outside this level |
| --- |
| Distributed processing without scale |
| Premature ANN or OCR |

## Record completion

```bash
python scripts/progress.py set L07 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L06](../06-Application-State/README.md) · Next numbered Level: [L08](../08-RAG-Systems/README.md). Follow the prerequisite table if branches differ.

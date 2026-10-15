# M07 — RAG Document Preparation, Embeddings, and Semantic Search

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M03](../m03-dl-foundation-models/README.md), [M06](../m06-persistence/README.md) |
| Personal effort | 16–24 focused hours; not official ITI hours |
| Project milestone | [S3](../../project/milestones/s3.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Convert a small textual PDF into traceable chunks with page provenance. |
| O2 | Compare a lexical baseline with embeddings appropriate to the application language. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N12 | Data Preparation & Feature Engineering | 12 |
| N17 | Embeddings, Vector DBs & Semantic Search | 18 |
| N19 | RAG Systems Engineering | 24 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | G4 printed pp. 74–82; C6 pp. 257–266: retrieval foundations. |
| 2 | F5 PDF 212–239: document ingestion/RAG; C8 pp. 396–402: processing principles adapted to the corpus. |
| 3 | pgvector official documentation: exact search and filtering first; ANN later if measured need exists. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M07-E1 | Start with the JSONL corpus, then a permitted 20–50-page text PDF. | Preserve PDF page, printed label if available, and offsets before cleaning. |
| M07-E2 | Handle empty, corrupt, and scanned PDFs explicitly. | Unsupported inputs have a clear failure reason rather than an empty ready index. |
| M07-E3 | Compare two chunk configurations and version the embedding setup. | Save chunker, document, model, and dimension; never mix incompatible embedding spaces. |
| M07-E4 | Implement a keyword baseline and exact vector retrieval. | Evaluate representative queries, including cross-language cases if they belong to the product scope. |
| M07-E5 | Reprocess an identical file and an updated version. | No duplicate chunks, no partially published version, and a clear deletion contract for M11. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Ingestion functions or CLI, corpus manifest, and provenance tests; Lexical and dense retrieval baseline |
| Pass condition | Every chunk maps to its source. Reprocessing is safe, embedding dimensions match storage, and the implementation remains small enough to debug. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M07 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Distributed processing without scale |
| Premature ANN or OCR |

# Resources · L07 — RAG Document Preparation, Embeddings, and Semantic Search

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | G4 printed pp.74–82; C6 pp.257–266: retrieval foundations. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F5 PDF212–239: document ingestion/RAG; C8 pp.396–402: processing principles adapted to the corpus. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | pgvector official documentation: exact search and filtering first; ANN later if measured need exists. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Parsing, chunking, metadata | [pgvector search and indexing](https://github.com/pgvector/pgvector) | Official tutorial / reference · free | Preserve page numbers and source identifiers through parsing. |
| Embeddings and similarity | [NumPy absolute beginners tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html) | Official tutorial / reference · free | Compare retrieval across two chunk sizes. |
| Exact vector search and filtering | [pgvector search and indexing](https://github.com/pgvector/pgvector) | Official tutorial / reference · free | Apply owner and document filters before returning candidates. |
| Idempotent re-indexing and deletion | [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html) | Official tutorial / reference · free | Re-run ingestion without duplicates and remove deleted sources. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Preserve page numbers and source identifiers through parsing. | Code/test or short measured comparison; explain the result independently. |
| 2 | Compare retrieval across two chunk sizes. | Code/test or short measured comparison; explain the result independently. |
| 3 | Apply owner and document filters before returning candidates. | Code/test or short measured comparison; explain the result independently. |
| 4 | Re-run ingestion without duplicates and remove deleted sources. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

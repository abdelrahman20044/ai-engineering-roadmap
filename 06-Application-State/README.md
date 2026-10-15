# L06 · PostgreSQL, ORM, and AI Application State

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 2 · Reliable LLM Application Basics | 12–18 h | 2/5 | P1 | [L01](../01-Python-FastAPI/README.md) |

**Outcome:** Move from Mongoose-style ODM experience to SQLAlchemy relations, sessions, transactions, and Alembic. Design document, conversation, and journal ownership and versions.

**Unlocks:** [L07](../07-Embeddings-Semantic-Search/README.md), [L11](../11-Security-Responsible-AI/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Models and ORM lifecycle | F7 PDF302–337; [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html) | [Practice 1](resources.md#practice-and-evidence) |
| Async sessions and transactions | F7 engine/session sections; [SQLAlchemy asyncio sessions](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | [Practice 2](resources.md#practice-and-evidence) |
| Schema migrations | F7 schema migration sections; [Alembic migration tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | [Practice 3](resources.md#practice-and-evidence) |
| Ownership and consistency | F8 authorization reference; [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N06** — SQL & NoSQL Database Engineering.
- **N07** — RESTful API, Backend Architecture & Security.
- **N09** — Software Architecture & System Design.

| ITI topic IDs | Interpretation |
| --- | --- |
| N06, N07, N09 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L06-E1 | Design documents, chunks, conversations, messages, and journals with ownership and relational constraints. | Produce an ERD and explain keys, nullability, uniqueness, and ownership boundaries. |
| L06-E2 | Write an initial migration and a version-column migration; simulate a failed write. | A fresh database migrates successfully; transaction rollback leaves consistent state. |
| L06-E3 | Implement a session lifecycle per request/task. | Concurrent tasks do not share one mutable session; cleanup is tested. |
| L06-E4 | Compare a direct SQL query with the ORM equivalent and add pagination. | Explain generated joins and index choices without relearning basic SQL. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | ERD, migrations, and real-database integration tests; Session/transaction lifecycle note | Rebuild the schema from an empty database and prevent partial writes. Explain where transactions begin and end. |

## Postpone

| Outside this level |
| --- |
| Multiple databases without a requirement |
| Repeating SQL or MongoDB fundamentals already demonstrated |

## Record completion

```bash
python scripts/progress.py set L06 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L05](../05-Evaluation/README.md) · Next numbered Level: [L07](../07-Embeddings-Semantic-Search/README.md). Follow the prerequisite table if branches differ.

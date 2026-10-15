# M06 — PostgreSQL, ORM, and AI Application State

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M01](../m01-python-fastapi/README.md) |
| Personal effort | 12–18 focused hours; not official ITI hours |
| Project milestone | [S3](../../project/milestones/s3.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Move from Mongoose-style ODM experience to SQLAlchemy relations, sessions, transactions, and Alembic. |
| O2 | Design document, conversation, and journal ownership and versions. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N06 | SQL & NoSQL Database Engineering | 30 |
| N07 | RESTful API, Backend Architecture & Security | 36 |
| N09 | Software Architecture & System Design | 30 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | F7 PDF 302–337: ORM, engine/session lifecycle, CRUD, and schema migration; skim database comparisons and Prisma. |
| 2 | SQLAlchemy asyncio and Alembic official documentation as needed. |
| 3 | F8 authorization integration is applied in M11. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M06-E1 | Design documents, chunks, conversations, messages, and journals with ownership and relational constraints. | Produce an ERD and explain keys, nullability, uniqueness, and ownership boundaries. |
| M06-E2 | Write an initial migration and a version-column migration; simulate a failed write. | A fresh database migrates successfully; transaction rollback leaves consistent state. |
| M06-E3 | Implement a session lifecycle per request/task. | Concurrent tasks do not share one mutable session; cleanup is tested. |
| M06-E4 | Compare a direct SQL query with the ORM equivalent and add pagination. | Explain generated joins and index choices without relearning basic SQL. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | ERD, migrations, and real-database integration tests; Session/transaction lifecycle note |
| Pass condition | Rebuild the schema from an empty database and prevent partial writes. Explain where transactions begin and end. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M06 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Multiple databases without a requirement |
| Repeating SQL or MongoDB fundamentals already demonstrated |

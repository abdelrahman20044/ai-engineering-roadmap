# L06 · PostgreSQL, ORM, and AI Application State

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 2 · Reliable LLM Application Basics | 12–18 h | 2/5 | P1 | [L01](../01-Python-FastAPI/README.md) |

**Unlocks:** [L07](../07-Embeddings-Semantic-Search/README.md), [L11](../11-Security-Responsible-AI/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Move from Mongoose-style ODM experience to SQLAlchemy relations, sessions, transactions, and Alembic. Design document, conversation, and journal ownership and versions. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| SQL transfer | Use joins, foreign keys and transactions without a new beginner course. |
| API prerequisite | Pass IDs and caller identity through a typed application layer. |
| Persistence reasoning | Explain how Mongo document ownership maps to relational keys. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Relational AI app model: Draw an ERD with ownership and document version boundaries.
- [ ] ORM queries and relationships: Implement a paginated owner-scoped document list and inspect generated SQL.
- [ ] Async sessions and transactions: Force an exception mid-write and prove rollback; run concurrent independent requests.
- [ ] Schema evolution: Upgrade a fresh database and a previous schema; verify expected rows remain.
- [ ] Ownership and indexes: Create two users with similar documents and prove no list/read/write leakage.
- [ ] State consistency: Retry a state change safely and test deletion behavior for related chunks/messages.

## Recommended learning path

F7 → Arabic mini-RAG PostgreSQL migration lesson → SQLAlchemy sessions/transactions → Alembic → ownership tests. Reuse your SQL knowledge.

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
| **L06-T01 · Relational AI app model**<br>User; document/version; chunk; journal; conversation/message; foreign keys | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Draw an ERD with ownership and document version boundaries. |
| **L06-T02 · ORM queries and relationships**<br>select; joins; eager loading; unit of work; pagination | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Implement a paginated owner-scoped document list and inspect generated SQL. |
| **L06-T03 · Async sessions and transactions**<br>AsyncSession; commit/rollback; concurrent tasks; atomic writes | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video)<br>**Scope:** PostgreSQL migration lesson; concurrent AsyncSession semantics require current docs. | [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN) | Force an exception mid-write and prove rollback; run concurrent independent requests. |
| **L06-T04 · Schema evolution**<br>Revision history; upgrades; downgrade/restore choice; data migration | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Upgrade a fresh database and a previous schema; verify expected rows remain. |
| **L06-T05 · Ownership and indexes**<br>Composite keys; uniqueness; access paths; prevent cross-user joins | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video)<br>**Scope:** Relational modelling context; authorization tests require F8/OWASP. | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN) | Create two users with similar documents and prove no list/read/write leakage. |
| **L06-T06 · State consistency**<br>Document hash/version; job state; cascade/delete policy; audit timestamps | [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) (AR video)<br>**Scope:** Ingestion structure; transaction/idempotency guarantees must be implemented and tested separately. | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN) | Retry a state change safely and test deletion behavior for related chunks/messages. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L06-T01 | F7 PDF302–337, primary ORM pass | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN) |
| L06-T02 | F7 ORM/CRUD sections, thorough | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN) |
| L06-T03 | F7 engine/session sections; current async docs are authoritative | [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN)<br>[PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) (EN) |
| L06-T04 | F7 schema migration sections | [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) (EN) |
| L06-T05 | F8 authorization reference, deepen in L11 | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN)<br>[PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) (EN) |
| L06-T06 | F7 persistence; C8 processing principles | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN)<br>[PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N06 · SQL & NoSQL Database Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N07 · RESTful API, Backend Architecture & Security | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N09 · Software Architecture & System Design | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L06-E1 | Design documents, chunks, conversations, messages, and journals with ownership and relational constraints. | Produce an ERD and explain keys, nullability, uniqueness, and ownership boundaries. |
| L06-E2 | Write an initial migration and a version-column migration; simulate a failed write. | A fresh database migrates successfully; transaction rollback leaves consistent state. |
| L06-E3 | Implement a session lifecycle per request/task. | Concurrent tasks do not share one mutable session; cleanup is tested. |
| L06-E4 | Compare a direct SQL query with the ORM equivalent and add pagination. | Explain generated joins and index choices without relearning basic SQL. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| AsyncSession shared across requests | Use one session per request/task and explicit transaction boundaries. |
| Unscoped get-by-ID | Every user-owned query includes caller ownership or an authorized join. |
| Migration only works on your laptop | Test upgrade from empty DB and from the previous schema snapshot. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Session versus transaction?
2. Why migrations instead of create_all in production?
3. What makes ingestion idempotent?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | A session manages ORM state and work; a transaction defines the atomic database boundary. |
| 2 | Changes must be versioned, reviewable and applied predictably to existing data. |
| 3 | A stable identity/version key plus constraints and transaction logic prevent duplicate effects. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | ERD, migrations, and real-database integration tests; Session/transaction lifecycle note | Rebuild the schema from an empty database and prevent partial writes. Explain where transactions begin and end. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Rebuild the schema from an empty database and prevent partial writes. Explain where transactions begin and end.

## Postpone until justified

- Multiple databases without a requirement
- Repeating SQL or MongoDB fundamentals already demonstrated

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L06 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L05](../05-Evaluation/README.md) · Next numbered Level: [L07](../07-Embeddings-Semantic-Search/README.md)

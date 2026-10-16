# Resource Library · L06 — PostgreSQL, ORM, and AI Application State

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

## Book references

Assigned reading is authoritative in [the master order for L06](../docs/READING_GUIDE.md#l06). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B18 · F7](../docs/READING_GUIDE.md#b18).

## Arabic and Egyptian teaching

<a id="r-ar-mini-20"></a>

### mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic

[mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Primary. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Relational AI app model; ORM queries and relationships; Async sessions and transactions; Schema evolution; Ownership and indexes.
- **Assigned portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** PostgreSQL migration lesson; concurrent AsyncSession semantics require current docs. Relational modelling context; authorization tests require F8/OWASP.

<a id="r-ar-mini-12"></a>

### mini-RAG · Data Pipeline Enhancements

[mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** State consistency.
- **Assigned portion:** Only the linked “Data Pipeline Enhancements” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Data Pipeline Enhancements in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Ingestion structure; transaction/idempotency guarantees must be implemented and tested separately.

## English video and guided courses

<a id="r-fcc-api"></a>

### Creating APIs with Python · course index

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)

- **Resource Type:** Full video course (19 hours; selected sections only).
- **Role:** Alternative. **Language:** EN video. **By:** Sanjeev Thiyagarajan · freeCodeCamp.
- **Access:** Free.
- **Use for:** Relational AI app model; ORM queries and relationships; Schema evolution.
- **Assigned portion:** Sections 6 (ORMs), 9 (Relationships) and 11 (Database Migration with Alembic); skip beginner SQL Sections 4–5 if the diagnostic passes.
- **Scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Limit:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

<a id="r-roby"></a>

### FastAPI — The Complete Course

[FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)

- **Resource Type:** Paid full video course.
- **Role:** Optional Advanced. **Language:** EN video. **By:** Eric Roby and Chad Darby.
- **Access:** Paid · variable regional/subscription pricing.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Alternative only: SQLAlchemy relationships and migrations matching L06. Exact lesson numbers not verified.
- **Scope:** Alternative guided backend course for validation, persistence, auth and tests.
- **Limit:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python.

## Practice, labs and quizzes

<a id="r-pg-exercises"></a>

### PostgreSQL Exercises

[PostgreSQL Exercises](https://pgexercises.com/)

- **Resource Type:** Interactive SQL practice platform.
- **Role:** Alternative. **Language:** EN interactive exercises. **By:** PGExercises.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** A short join/aggregate/window diagnostic, then stop when the relevant query works. No complete SQL track.
- **Scope:** Selected joins, aggregation and window exercises for SQL diagnostics.
- **Limit:** Prior SQL knowledge means a short diagnostic, not a full SQL track.

## Official documentation and engineering articles

<a id="r-sqlalchemy"></a>

### SQLAlchemy Unified Tutorial

[SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** SQLAlchemy.
- **Access:** Free.
- **Use for:** Relational AI app model; ORM queries and relationships; State consistency.
- **Assigned portion:** Consult the select; joins; eager loading; unit of work; pagination sections/examples only. Do not read the entire documentation site. Read Working with Transactions and Data Manipulation with the ORM, especially flush/commit/rollback. Use those primitives to reason about failed job/state transitions; the tutorial does not supply an AI-ingestion state machine.
- **Scope:** Mapped classes, relationships, selects and unit of work.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-sqlasync"></a>

### SQLAlchemy asyncio

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** SQLAlchemy.
- **Access:** Free.
- **Use for:** Async sessions and transactions.
- **Assigned portion:** Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes sections/examples only. Do not read the entire documentation site.
- **Scope:** One session per concurrent task; explicit database I/O.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-postgres"></a>

### PostgreSQL transaction isolation

[PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** PostgreSQL.
- **Access:** Free.
- **Use for:** Async sessions and transactions; Ownership and indexes.
- **Assigned portion:** Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes sections/examples only. Do not read the entire documentation site.
- **Scope:** Isolation anomalies and transaction guarantees.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-alembic"></a>

### Alembic tutorial

[Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Alembic.
- **Access:** Free.
- **Use for:** Schema evolution.
- **Assigned portion:** Consult the Revision history; upgrades; downgrade/restore choice; data migration sections/examples only. Do not read the entire documentation site.
- **Scope:** Schema revisions, upgrade and migration history.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-authz"></a>

### Authorization cheat sheet

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OWASP.
- **Access:** Free.
- **Use for:** Ownership and indexes.
- **Assigned portion:** Consult the Composite keys; uniqueness; access paths; prevent cross-user joins sections/examples only. Do not read the entire documentation site.
- **Scope:** Deny-by-default object authorization and least privilege.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pgbackup"></a>

### PostgreSQL backup and restore

[PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** PostgreSQL.
- **Access:** Free.
- **Use for:** State consistency.
- **Assigned portion:** Consult the Document hash/version; job state; cascade/delete policy; audit timestamps sections/examples only. Do not read the entire documentation site.
- **Scope:** Logical backup and restore procedure; verify by restoring.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

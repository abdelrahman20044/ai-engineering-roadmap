# Resource Library · L06 — PostgreSQL, ORM, and AI Application State

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

## Topic navigation

1. [Relational AI app model](#unit-01)
2. [ORM queries and relationships](#unit-02)
3. [Async sessions and transactions](#unit-03)
4. [Schema evolution](#unit-04)
5. [Ownership and indexes](#unit-05)
6. [State consistency](#unit-06)

<a id="unit-01"></a>

## 1. Relational AI app model

[Return to README Step 1](README.md#1-relational-ai-app-model)

**Topic/subtopics:** User; document/version; chunk; journal; conversation/message; foreign keys.

**Required sequence (default route):** the assigned book slice [B18 · F7](../docs/READING_GUIDE.md#b18) **THEN** `ar-mini-20`. Stop each source at the stated portion.

**Choose ONE explanation for SQL schema/relationship basics:** default `ar-mini-20` **OR** `fcc-api`. Keep the assigned F7 slice and the AI ownership/version model exercise. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `sqlalchemy`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-relational-ai-app-model) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B18 · F7](../docs/READING_GUIDE.md#b18)<br>Alireza Parandeh · EN | Book Section | Complementary | Relational AI app model | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b18) |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | Relational AI app model (selected course unit) | Section 4: Databases; Section 6: ORMs, database/schema and SQLAlchemy… [bounds](#unit-01-fcc-api) |
| `sqlalchemy` · [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)<br>SQLAlchemy · EN | Documentation / tutorial | Reference | Mapped classes, relationships, selects and unit of work. | Consult the relevant example for Mapped classes, relationships, selects… [bounds](#unit-01-sqlalchemy) |
| `pg-exercises` · [PostgreSQL Exercises](https://pgexercises.com/)<br>PGExercises · EN interactive exercises | Interactive SQL practice platform | Complementary (as needed) | Selected joins, aggregation and window exercises for SQL… | Selected joins/aggregation/window exercises only for a demonstrated SQL… [bounds](#unit-01-pg-exercises) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-01-fcc-api"></a>

**`fcc-api` — selected portion:** Section 4: Databases; Section 6: ORMs, database/schema and SQLAlchemy examples; review only the relational design gap.

**Relationship:** Substitute only for SQL schema/relationship basics. Keep the assigned F7 slice and the AI ownership/version model exercise.

<a id="unit-01-sqlalchemy"></a>

**`sqlalchemy` — selected portion:** Consult the relevant example for Mapped classes, relationships, selects and unit of work. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-01-pg-exercises"></a>

**`pg-exercises` — selected portion:** Selected joins/aggregation/window exercises only for a demonstrated SQL gap; no full SQL restart.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-02"></a>

## 2. ORM queries and relationships

[Return to README Step 2](README.md#2-orm-queries-and-relationships)

**Topic/subtopics:** select; joins; eager loading; unit of work; pagination.

**Required sequence (default route):** `sqlalchemy`. Stop each source at the stated portion.

**Choose ONE explanation for ORM relationships:** default `sqlalchemy` **OR** `fcc-api`. Its ORM examples use older APIs; consult current SQLAlchemy 2.x for the actual implementation. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-orm-queries-and-relationships) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B18 · F7](../docs/READING_GUIDE.md#b18)<br>Alireza Parandeh · EN | Book Section | Reference | ORM queries and relationships | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b18) |
| `sqlalchemy` · [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)<br>SQLAlchemy · EN | Documentation / tutorial | Primary | Mapped classes, relationships, selects and unit of work. | Consult the select; joins; eager loading; unit of work; pagination… [bounds](#unit-02-sqlalchemy) |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | ORM queries and relationships (selected course unit) | Section 9: Relationships; use current SQLAlchemy 2.x syntax. |
| `roby` · [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)<br>Eric Roby and Chad Darby · EN video | Full Course (paid) | Optional Advanced | Alternative guided backend course for validation,… | Topic bounds; lesson IDs not verified — [details](#unit-02-roby) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-sqlalchemy"></a>

**`sqlalchemy` — selected portion:** Consult the select; joins; eager loading; unit of work; pagination sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-fcc-api"></a>

**`fcc-api` — selected portion:** Section 9: Relationships; use current SQLAlchemy 2.x syntax.

**Relationship:** Substitute only for ORM relationships. Its ORM examples use older APIs; consult current SQLAlchemy 2.x for the actual implementation.

<a id="unit-02-roby"></a>

**`roby` — selected portion:** Optional purchase only: use the topic-specific FastAPI section for a demonstrated gap. Individual current lesson IDs/access not verified; no whole-course requirement.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-03"></a>

## 3. Async sessions and transactions

[Return to README Step 3](README.md#3-async-sessions-and-transactions)

**Topic/subtopics:** AsyncSession; commit/rollback; concurrent tasks; atomic writes.

**Required sequence:** `sqlasync`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `postgres`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-async-sessions-and-transactions) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B18 · F7](../docs/READING_GUIDE.md#b18)<br>Alireza Parandeh · EN | Book Section | Reference | Async sessions and transactions | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b18) |
| `sqlasync` · [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)<br>SQLAlchemy · EN | Documentation / tutorial | Primary | One session per concurrent task; explicit database I/O. | Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes… [bounds](#unit-03-sqlasync) |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `postgres` · [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)<br>PostgreSQL · EN | Documentation / tutorial | Reference | Isolation anomalies and transaction guarantees. | Consult the relevant example for Isolation anomalies and transaction… [bounds](#unit-03-postgres) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-sqlasync"></a>

**`sqlasync` — selected portion:** Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: PostgreSQL migration lesson; concurrent AsyncSession semantics require current docs.

<a id="unit-03-postgres"></a>

**`postgres` — selected portion:** Consult the relevant example for Isolation anomalies and transaction guarantees. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Schema evolution

[Return to README Step 4](README.md#4-schema-evolution)

**Topic/subtopics:** Revision history; upgrades; downgrade/restore choice; data migration.

**Required sequence:** `alembic`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-schema-evolution) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B18 · F7](../docs/READING_GUIDE.md#b18)<br>Alireza Parandeh · EN | Book Section | Reference | Schema evolution | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b18) |
| `alembic` · [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)<br>Alembic · EN | Documentation / tutorial | Primary | Schema revisions, upgrade and migration history. | Consult the Revision history; upgrades; downgrade/restore choice; data… [bounds](#unit-04-alembic) |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Complementary (as needed) | Schema evolution (selected course unit) | Section 11: Alembic. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-alembic"></a>

**`alembic` — selected portion:** Consult the Revision history; upgrades; downgrade/restore choice; data migration sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-fcc-api"></a>

**`fcc-api` — selected portion:** Section 11: Alembic.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-05"></a>

## 5. Ownership and indexes

[Return to README Step 5](README.md#5-ownership-and-indexes)

**Topic/subtopics:** Composite keys; uniqueness; access paths; prevent cross-user joins.

**Required sequence:** `authz`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `postgres`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-ownership-and-indexes) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B18 · F7](../docs/READING_GUIDE.md#b18)<br>Alireza Parandeh · EN | Book Section | Reference | Ownership and indexes | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b18) |
| `authz` · [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Primary | Deny-by-default object authorization and least privilege. | Consult the Composite keys; uniqueness; access paths; prevent cross-user… [bounds](#unit-05-authz) |
| `ar-mini-20` · [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | From Mongo to Postgres + SQLAlchemy & Alembic in a working… | The linked video only; not its playlist. |
| `postgres` · [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)<br>PostgreSQL · EN | Documentation / tutorial | Reference | Isolation anomalies and transaction guarantees. | Consult the relevant example for Isolation anomalies and transaction… [bounds](#unit-05-postgres) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-authz"></a>

**`authz` — selected portion:** Consult the Composite keys; uniqueness; access paths; prevent cross-user joins sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-20"></a>

**`ar-mini-20` — selected portion:** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Relational modelling context; authorization tests require F8/OWASP.

<a id="unit-05-postgres"></a>

**`postgres` — selected portion:** Consult the relevant example for Isolation anomalies and transaction guarantees. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. State consistency

[Return to README Step 6](README.md#6-state-consistency)

**Topic/subtopics:** Document hash/version; job state; cascade/delete policy; audit timestamps.

**Required sequence:** `sqlalchemy`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `pgbackup`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-state-consistency) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B18 · F7](../docs/READING_GUIDE.md#b18)<br>Alireza Parandeh · EN | Book Section | Reference | State consistency | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b18) |
| `sqlalchemy` · [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)<br>SQLAlchemy · EN | Documentation / tutorial | Primary | Mapped classes, relationships, selects and unit of work. | Read Working with Transactions and Data Manipulation with the ORM,… [bounds](#unit-06-sqlalchemy) |
| `ar-mini-12` · [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Data Pipeline Enhancements in a working RAG backend. | The linked video only; not its playlist. |
| `pgbackup` · [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html)<br>PostgreSQL · EN | Documentation / tutorial | Reference | Logical backup and restore procedure; verify by restoring. | Consult the relevant example for Logical backup and restore procedure;… [bounds](#unit-06-pgbackup) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-sqlalchemy"></a>

**`sqlalchemy` — selected portion:** Read Working with Transactions and Data Manipulation with the ORM, especially flush/commit/rollback. Use those primitives to reason about failed job/state transitions; the tutorial does not supply an AI-ingestion state machine.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-mini-12"></a>

**`ar-mini-12` — selected portion:** Only the linked “Data Pipeline Enhancements” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Ingestion structure; transaction/idempotency guarantees must be implemented and tested separately.

<a id="unit-06-pgbackup"></a>

**`pgbackup` — selected portion:** Consult the relevant example for Logical backup and restore procedure; verify by restoring. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-mini-20"></a>

<details>
<summary>ar-mini-20 · mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic — access, scope and verification</summary>

[mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Relational AI app model; ORM queries and relationships; Async sessions and transactions; Schema evolution; Ownership and indexes.
- **Retained broad selection notes (lookup only):** Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-fcc-api"></a>

<details>
<summary>fcc-api · Creating APIs with Python · course index — access, scope and verification</summary>

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) · Sanjeev Thiyagarajan · freeCodeCamp · EN video

- **Resource Type:** Full Course (19 hours; selected sections only).
- **Access:** Free.
- **Catalog scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Scope/version limits:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Relational AI app model; ORM queries and relationships; Schema evolution.
- **Retained broad selection notes (lookup only):** Sections 6 (ORMs), 9 (Relationships) and 11 (Database Migration with Alembic); skip beginner SQL Sections 4–5 if the diagnostic passes.

</details>

<a id="r-sqlalchemy"></a>

<details>
<summary>sqlalchemy · SQLAlchemy Unified Tutorial — access, scope and verification</summary>

[SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Mapped classes, relationships, selects and unit of work.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Relational AI app model; ORM queries and relationships; State consistency.
- **Retained broad selection notes (lookup only):** Consult the select; joins; eager loading; unit of work; pagination sections/examples only. Do not read the entire documentation site. Read Working with Transactions and Data Manipulation with the ORM, especially flush/commit/rollback. Use those primitives to reason about failed job/state transitions; the tutorial does not supply an AI-ingestion state machine.

</details>

<a id="r-sqlasync"></a>

<details>
<summary>sqlasync · SQLAlchemy asyncio — access, scope and verification</summary>

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** One session per concurrent task; explicit database I/O.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Async sessions and transactions.
- **Retained broad selection notes (lookup only):** Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-postgres"></a>

<details>
<summary>postgres · PostgreSQL transaction isolation — access, scope and verification</summary>

[PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) · PostgreSQL · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Isolation anomalies and transaction guarantees.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Async sessions and transactions; Ownership and indexes.
- **Retained broad selection notes (lookup only):** Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-alembic"></a>

<details>
<summary>alembic · Alembic tutorial — access, scope and verification</summary>

[Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) · Alembic · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Schema revisions, upgrade and migration history.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Schema evolution.
- **Retained broad selection notes (lookup only):** Consult the Revision history; upgrades; downgrade/restore choice; data migration sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-authz"></a>

<details>
<summary>authz · Authorization cheat sheet — access, scope and verification</summary>

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · OWASP · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Deny-by-default object authorization and least privilege.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Ownership and indexes.
- **Retained broad selection notes (lookup only):** Consult the Composite keys; uniqueness; access paths; prevent cross-user joins sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-12"></a>

<details>
<summary>ar-mini-12 · mini-RAG · Data Pipeline Enhancements — access, scope and verification</summary>

[mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Data Pipeline Enhancements in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** State consistency.
- **Retained broad selection notes (lookup only):** Only the linked “Data Pipeline Enhancements” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-pgbackup"></a>

<details>
<summary>pgbackup · PostgreSQL backup and restore — access, scope and verification</summary>

[PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) · PostgreSQL · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Logical backup and restore procedure; verify by restoring.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** State consistency.
- **Retained broad selection notes (lookup only):** Consult the Document hash/version; job state; cascade/delete policy; audit timestamps sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-roby"></a>

<details>
<summary>roby · FastAPI — The Complete Course — access, scope and verification</summary>

[FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) · Eric Roby and Chad Darby · EN video

- **Resource Type:** Full Course (paid).
- **Access:** Paid · variable regional/subscription pricing.
- **Catalog scope:** Alternative guided backend course for validation, persistence, auth and tests.
- **Scope/version limits:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Alternative only: SQLAlchemy relationships and migrations matching L06. Exact lesson numbers not verified.

</details>

<a id="r-pg-exercises"></a>

<details>
<summary>pg-exercises · PostgreSQL Exercises — access, scope and verification</summary>

[PostgreSQL Exercises](https://pgexercises.com/) · PGExercises · EN interactive exercises

- **Resource Type:** Interactive SQL practice platform.
- **Access:** Free.
- **Catalog scope:** Selected joins, aggregation and window exercises for SQL diagnostics.
- **Scope/version limits:** Prior SQL knowledge means a short diagnostic, not a full SQL track.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** A short join/aggregate/window diagnostic, then stop when the relevant query works. No complete SQL track.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

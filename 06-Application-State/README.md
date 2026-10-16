# L06 · PostgreSQL, ORM, and AI Application State

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 2 · 12–18 focused hours · Difficulty 2/5 · P1**

**You will learn:** Move from Mongoose-style ODM experience to SQLAlchemy relations, sessions, transactions, and Alembic. Design document, conversation, and journal ownership and versions.

**Before starting:** [L01](../01-Python-FastAPI/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B18 · F7](../docs/READING_GUIDE.md#b18) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Relational AI app model

**Learn:** User; document/version; chunk; journal; conversation/message; foreign keys.

**Required reading:**

- [B18 · F7](../docs/READING_GUIDE.md#b18) — **Read Now**. PDF pp.302–337: SQLAlchemy models, engine/session, CRUD, Alembic. Skim DB comparisons, known SQL and Prisma.

**Primary · Single video (lesson within playlist):** [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0). Only the linked “From Mongo to Postgres + SQLAlchemy & Alembic” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Draw an ERD with ownership and document version boundaries.

**Completion check:** An ERD has user ownership and document/chunk version relationships.

[Alternative · EN video](resources.md#r-fcc-api) (optional) · [Implementation reference](resources.md#r-sqlalchemy)

### 2. ORM queries and relationships

**Learn:** select; joins; eager loading; unit of work; pagination.

**Required reading:**

- [B18 · F7](../docs/READING_GUIDE.md#b18) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/). Consult the select; joins; eager loading; unit of work; pagination sections/examples only. Do not read the entire documentation site.

**Practice:** Implement a paginated owner-scoped document list and inspect generated SQL.

**Completion check:** The paginated query returns only the caller’s records.

[Alternative · AR video](resources.md#r-ar-mini-20) (optional)

### 3. Async sessions and transactions

**Learn:** AsyncSession; commit/rollback; concurrent tasks; atomic writes.

**Required reading:**

- [B18 · F7](../docs/READING_GUIDE.md#b18) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html). Consult the AsyncSession; commit/rollback; concurrent tasks; atomic writes sections/examples only. Do not read the entire documentation site.

**Practice:** Force an exception mid-write and prove rollback; run concurrent independent requests.

**Completion check:** Failure mid-write rolls back; concurrent tasks do not share a session.

[Alternative · AR video](resources.md#r-ar-mini-20) (optional) · [Implementation reference](resources.md#r-postgres)

### 4. Schema evolution

**Learn:** Revision history; upgrades; downgrade/restore choice; data migration.

**Required reading:**

- [B18 · F7](../docs/READING_GUIDE.md#b18) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html). Consult the Revision history; upgrades; downgrade/restore choice; data migration sections/examples only. Do not read the entire documentation site.

**Practice:** Upgrade a fresh database and a previous schema; verify expected rows remain.

**Completion check:** Fresh and previous-schema upgrades retain expected rows.

[Alternative · AR video](resources.md#r-ar-mini-20) (optional)

### 5. Ownership and indexes

**Learn:** Composite keys; uniqueness; access paths; prevent cross-user joins.

**Required reading:**

- [B18 · F7](../docs/READING_GUIDE.md#b18) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Consult the Composite keys; uniqueness; access paths; prevent cross-user joins sections/examples only. Do not read the entire documentation site.

**Practice:** Create two users with similar documents and prove no list/read/write leakage.

**Completion check:** Two-user direct and joined reads do not leak records.

[Alternative · AR video](resources.md#r-ar-mini-20) (optional) · [Implementation reference](resources.md#r-postgres)

### 6. State consistency

**Learn:** Document hash/version; job state; cascade/delete policy; audit timestamps.

**Required reading:**

- [B18 · F7](../docs/READING_GUIDE.md#b18) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/). Read Working with Transactions and Data Manipulation with the ORM, especially flush/commit/rollback. Use those primitives to reason about failed job/state transitions; the tutorial does not supply an AI-ingestion state machine.

**Practice:** Retry a state change safely and test deletion behavior for related chunks/messages.

**Completion check:** Repeated ingestion/state updates do not create duplicate effects.

[Alternative · AR video](resources.md#r-ar-mini-12) (optional) · [Implementation reference](resources.md#r-pgbackup)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L06-E1:** Design documents, chunks, conversations, messages, and journals with ownership and relational constraints.
  - **Pass:** Produce an ERD and explain keys, nullability, uniqueness, and ownership boundaries.
- [ ] **L06-E2:** Write an initial migration and a version-column migration; simulate a failed write.
  - **Pass:** A fresh database migrates successfully; transaction rollback leaves consistent state.
- [ ] **L06-E3:** Implement a session lifecycle per request/task.
  - **Pass:** Concurrent tasks do not share one mutable session; cleanup is tested.
- [ ] **L06-E4:** Compare a direct SQL query with the ORM equivalent and add pagination.
  - **Pass:** Explain generated joins and index choices without relearning basic SQL.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S3](../project/milestones/s3.md). Rebuild the schema from an empty database and prevent partial writes. Explain where transactions begin and end.

**Keep:** ERD, migrations, and real-database integration tests; Session/transaction lifecycle note.

## What to defer

- Multiple databases without a requirement
- Repeating SQL or MongoDB fundamentals already demonstrated

## Record progress and choose the next Level

```bash
python scripts/progress.py set L06 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L07](../07-Embeddings-Semantic-Search/README.md), [L11](../11-Security-Responsible-AI/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

# Technical Details · L06

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **SQL transfer:** Use joins, foreign keys and transactions without a new beginner course.
- **API prerequisite:** Pass IDs and caller identity through a typed application layer.
- **Persistence reasoning:** Explain how Mongo document ownership maps to relational keys.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Relational AI app model:** User; document/version; chunk; journal; conversation/message; foreign keys.
- **ORM queries and relationships:** select; joins; eager loading; unit of work; pagination.
- **Async sessions and transactions:** AsyncSession; commit/rollback; concurrent tasks; atomic writes.
- **Schema evolution:** Revision history; upgrades; downgrade/restore choice; data migration.
- **Ownership and indexes:** Composite keys; uniqueness; access paths; prevent cross-user joins.
- **State consistency:** Document hash/version; job state; cascade/delete policy; audit timestamps.

## Common mistakes and debugging

### AsyncSession shared across requests

Use one session per request/task and explicit transaction boundaries.

### Unscoped get-by-ID

Every user-owned query includes caller ownership or an authorized join.

### Migration only works on your laptop

Test upgrade from empty DB and from the previous schema snapshot.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Session versus transaction?
2. Why migrations instead of create_all in production?
3. What makes ingestion idempotent?

<details>
<summary>Answer guide</summary>

**Session versus transaction?**

A session manages ORM state and work; a transaction defines the atomic database boundary.

**Why migrations instead of create_all in production?**

Changes must be versioned, reviewable and applied predictably to existing data.

**What makes ingestion idempotent?**

A stable identity/version key plus constraints and transaction logic prevent duplicate effects.

</details>

## ITI provenance and industry extensions

- **N06:** SQL & NoSQL Database Engineering — official published module title.
- **N07:** RESTful API, Backend Architecture & Security — official published module title.
- **N09:** Software Architecture & System Design — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Draw an ERD with ownership and document version boundaries.
- [ ] Implement a paginated owner-scoped document list and inspect generated SQL.
- [ ] Force an exception mid-write and prove rollback; run concurrent independent requests.
- [ ] Upgrade a fresh database and a previous schema; verify expected rows remain.
- [ ] Create two users with similar documents and prove no list/read/write leakage.
- [ ] Retry a state change safely and test deletion behavior for related chunks/messages.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

# Resource Library · L06 — PostgreSQL, ORM, and AI Application State

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

F7 → Arabic mini-RAG PostgreSQL migration lesson → SQLAlchemy sessions/transactions → Alembic → ownership tests. Reuse your SQL knowledge.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L06-T01 · Relational AI app model; L06-T02 · ORM queries and relationships; L06-T03 · Async sessions and transactions; L06-T04 · Schema evolution; L06-T05 · Ownership and indexes | From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Data Pipeline Enhancements](https://www.youtube.com/watch?v=4x1DuezZBDU) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L06-T06 · State consistency | Data Pipeline Enhancements in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L06-T01 · Relational AI app model; L06-T02 · ORM queries and relationships; L06-T04 · Schema evolution | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) | Eric Roby and Chad Darby<br>EN video<br>Paid · variable regional/subscription pricing | Optional support for this Level’s assessed exercises | Alternative guided backend course for validation, persistence, auth and tests. **Boundary:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python. |

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| F7 PDF302–337: ORM, engine/session lifecycle, CRUD, and schema migration; skim database comparisons and Prisma. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| SQLAlchemy asyncio and Alembic official documentation as needed. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F8 authorization integration is applied in L11. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [PostgreSQL Exercises](https://pgexercises.com/) | PGExercises<br>EN interactive exercises<br>Free | Optional support for this Level’s assessed exercises | Selected joins, aggregation and window exercises for SQL diagnostics. **Boundary:** Prior SQL knowledge means a short diagnostic, not a full SQL track. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L06-T01 | Draw an ERD with ownership and document version boundaries. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L06-T02 | Implement a paginated owner-scoped document list and inspect generated SQL. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L06-T03 | Force an exception mid-write and prove rollback; run concurrent independent requests. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L06-T04 | Upgrade a fresh database and a previous schema; verify expected rows remain. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L06-T05 | Create two users with similar documents and prove no list/read/write leakage. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L06-T06 | Retry a state change safely and test deletion behavior for related chunks/messages. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) | SQLAlchemy<br>EN<br>Free | L06-T01 · Relational AI app model; L06-T02 · ORM queries and relationships; L06-T06 · State consistency | Mapped classes, relationships, selects and unit of work. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | SQLAlchemy<br>EN<br>Free | L06-T03 · Async sessions and transactions | One session per concurrent task; explicit database I/O. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | PostgreSQL<br>EN<br>Free | L06-T03 · Async sessions and transactions; L06-T05 · Ownership and indexes | Isolation anomalies and transaction guarantees. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | Alembic<br>EN<br>Free | L06-T04 · Schema evolution | Schema revisions, upgrade and migration history. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP<br>EN<br>Free | L06-T05 · Ownership and indexes | Deny-by-default object authorization and least privilege. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) | PostgreSQL<br>EN<br>Free | L06-T06 · State consistency | Logical backup and restore procedure; verify by restoring. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

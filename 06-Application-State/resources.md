# Resources · L06 — PostgreSQL, ORM, and AI Application State

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | F7 PDF302–337: ORM, engine/session lifecycle, CRUD, and schema migration; skim database comparisons and Prisma. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | SQLAlchemy asyncio and Alembic official documentation as needed. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | F8 authorization integration is applied in L11. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Models and ORM lifecycle | [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html) | Official tutorial / reference · free | Persist document, chunk, conversation, and message records. |
| Async sessions and transactions | [SQLAlchemy asyncio sessions](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | Official tutorial / reference · free | Prove concurrent requests never share a mutable session. |
| Schema migrations | [Alembic migration tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | Official tutorial / reference · free | Upgrade an empty database and test a migration. |
| Ownership and consistency | [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | Official tutorial / reference · free | Reject cross-user document and conversation access. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Persist document, chunk, conversation, and message records. | Code/test or short measured comparison; explain the result independently. |
| 2 | Prove concurrent requests never share a mutable session. | Code/test or short measured comparison; explain the result independently. |
| 3 | Upgrade an empty database and test a migration. | Code/test or short measured comparison; explain the result independently. |
| 4 | Reject cross-user document and conversation access. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

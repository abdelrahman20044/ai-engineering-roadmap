# Resources · L10 — Concurrency, Streaming, and Long-Running Jobs

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | F5 PDF187–211 and 253–256; defer GPU-oriented inference internals. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F6 PDF258–301: streaming/SSE and communication tradeoffs. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | FastAPI async/background tasks; Celery task semantics when durable execution is required. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Event loop and blocking I/O | [FastAPI async guide](https://fastapi.tiangolo.com/async/) | Official tutorial / reference · free | Demonstrate and then remove a blocking call in an async route. |
| Streaming and cancellation | [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/) | Official tutorial / reference · free | Stream tokens and stop provider work when the client disconnects. |
| Background work versus durable jobs | [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) | Official tutorial / reference · free | Compare an in-process task with a persisted ingestion job. |
| Retries, idempotency, concurrency limits | [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html) | Official tutorial / reference · free | Retry a failed ingestion safely and bound parallel provider requests. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Demonstrate and then remove a blocking call in an async route. | Code/test or short measured comparison; explain the result independently. |
| 2 | Stream tokens and stop provider work when the client disconnects. | Code/test or short measured comparison; explain the result independently. |
| 3 | Compare an in-process task with a persisted ingestion job. | Code/test or short measured comparison; explain the result independently. |
| 4 | Retry a failed ingestion safely and bound parallel provider requests. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

# Resources · L14 — MLOps, LLMOps, Architecture, and Deployment

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | F12 PDF536–594: Dockerfile, storage, networking, Compose, and image optimization; skim familiar Docker basics. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F11 E2E; C10 Monitoring and Observability pp.465–473. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | F3 serving strategies and C9 performance metrics; GPU optimization remains optional. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Containerization and deployment | [Docker workshop](https://docs.docker.com/get-started/workshop/) | Official tutorial / reference · free | Deploy API and database with health checks and persistent storage. |
| CI and regression checks | [GitHub Actions Python guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | Official tutorial / reference · free | Run tests and fixed evaluation fixtures on a clean checkout. |
| Tracing, metrics, redaction | [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | Official tutorial / reference · free | Trace ingestion, retrieval, provider latency, and errors. |
| Architecture, release, rollback | [Docker workshop](https://docs.docker.com/get-started/workshop/) | Official tutorial / reference · free | Document migration, restore, release, and rollback procedures. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Deploy API and database with health checks and persistent storage. | Code/test or short measured comparison; explain the result independently. |
| 2 | Run tests and fixed evaluation fixtures on a clean checkout. | Code/test or short measured comparison; explain the result independently. |
| 3 | Trace ingestion, retrieval, provider latency, and errors. | Code/test or short measured comparison; explain the result independently. |
| 4 | Document migration, restore, release, and rollback procedures. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

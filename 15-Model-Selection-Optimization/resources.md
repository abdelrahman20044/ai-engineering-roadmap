# Resources · L15 — Model Selection, Cost, Latency, and User Feedback

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | C4 Model Selection pp.179–200 and Cost and Latency pp.177–178. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F10 PDF429–476 selectively; C9 Performance Metrics pp.412–418. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | C10 Feedback Design pp.480–489 and limitations pp.490–491. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Model selection under constraints | [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Official tutorial / reference · free | Compare two models on quality, latency, and cost. |
| Cost and latency budgets | [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | Official tutorial / reference · free | Measure p50/p95 latency, tokens, and cost per request. |
| Caching and optimization | [pgvector search and indexing](https://github.com/pgvector/pgvector) | Official tutorial / reference · free | Add one measured optimization with isolation and invalidation tests. |
| User feedback and monitoring | [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | Official tutorial / reference · free | Capture consented ratings and investigate failure patterns. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Compare two models on quality, latency, and cost. | Code/test or short measured comparison; explain the result independently. |
| 2 | Measure p50/p95 latency, tokens, and cost per request. | Code/test or short measured comparison; explain the result independently. |
| 3 | Add one measured optimization with isolation and invalidation tests. | Code/test or short measured comparison; explain the result independently. |
| 4 | Capture consented ratings and investigate failure patterns. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

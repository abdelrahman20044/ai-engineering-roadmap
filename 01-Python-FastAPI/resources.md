# Resources · L01 — Python, FastAPI, and Service Testing

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | F2, PDF43–82: server, Depends, lifespan, and project structure; skim familiar framework comparisons. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F4, PDF153–186: annotations, Annotated, Pydantic validators, serialization, and settings; skim primitive types. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | F11, PDF500–518: pytest, fixtures, parameterization, async tests, and mocking; revisit as needed. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 4 | FastAPI documentation: types, request/response models, dependencies, and testing. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Typing and validation | [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | Official tutorial / reference · free | Reject malformed requests and verify response serialization. |
| Dependencies and lifecycle | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | Official tutorial / reference · free | Swap a fake model adapter with a dependency override. |
| Generators and cleanup | [Python tutorial: classes and generators](https://docs.python.org/3/tutorial/classes.html) | Official tutorial / reference · free | Batch records and prove cleanup on exceptions. |
| Fixtures and service tests | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | Official tutorial / reference · free | Cover validation, provider failure, and timeout behavior. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Reject malformed requests and verify response serialization. | Code/test or short measured comparison; explain the result independently. |
| 2 | Swap a fake model adapter with a dependency override. | Code/test or short measured comparison; explain the result independently. |
| 3 | Batch records and prove cleanup on exceptions. | Code/test or short measured comparison; explain the result independently. |
| 4 | Cover validation, provider failure, and timeout behavior. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

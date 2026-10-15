# Resources · L04 — Prompt Engineering, Structured Outputs, and LLM Integration

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | G2: What if we coded it?, printed pp.42–45; skip Langflow setup. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | G3 pp.48–56 and 68–72: prompt quality, techniques, and the coding explanation. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | F3 external serving, F4 validation, and F5 PDF203–208 provider APIs. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 4 | C5 pp.218–234: context efficiency and prompt versioning; C2 structured outputs as needed. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Prompt construction and versioning | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Version a prompt and compare outputs on fixed examples. |
| Provider adapters and failure contracts | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | Official tutorial / reference · free | Integrate one provider with explicit timeout and retry policy. |
| Structured outputs | [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | Official tutorial / reference · free | Validate malformed model output without accepting silent corruption. |
| Translate low-code examples into code | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | Official tutorial / reference · free | Build a single-call endpoint without Langflow. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Version a prompt and compare outputs on fixed examples. | Code/test or short measured comparison; explain the result independently. |
| 2 | Integrate one provider with explicit timeout and retry policy. | Code/test or short measured comparison; explain the result independently. |
| 3 | Validate malformed model output without accepting silent corruption. | Code/test or short measured comparison; explain the result independently. |
| 4 | Build a single-call endpoint without Langflow. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

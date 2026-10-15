# Resources · L09 — Context Engineering, Memory, and Conversations

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | Anthropic: context selection/retrieval and long-horizon sections. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C5 pp.218–219; C6 Memory pp.300–304; C10 Enhance Context p.450. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Context budgets and context rot | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Compare focused evidence to distractor-heavy long context. |
| Selection and just-in-time retrieval | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Log why each passage or journal entry entered context. |
| Structured memory with provenance | [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html) | Official tutorial / reference · free | Add user-editable memory with source and deletion semantics. |
| Compaction and retained facts | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Measure lost facts after summarization before enabling compaction. |
| Sub-agent decision boundary | [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | Official tutorial / reference · free | Write a decision record; implement only after bounded-agent evidence. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Compare focused evidence to distractor-heavy long context. | Code/test or short measured comparison; explain the result independently. |
| 2 | Log why each passage or journal entry entered context. | Code/test or short measured comparison; explain the result independently. |
| 3 | Add user-editable memory with source and deletion semantics. | Code/test or short measured comparison; explain the result independently. |
| 4 | Measure lost facts after summarization before enabling compaction. | Code/test or short measured comparison; explain the result independently. |
| 5 | Write a decision record; implement only after bounded-agent evidence. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

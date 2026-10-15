# Resources · L12 — Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | G5 printed pp.102–107 and 122–127; G6 pp.130–132 for patterns, with implementation examples optional. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C6 Agents pp.275–299: tools, planning, and failure modes. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | Anthropic: JIT context and sub-agent sections, interpreted through project experiments. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Tool schemas and validation | [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | Official tutorial / reference · free | Expose read-only search with validated arguments. |
| Workflow versus agent | [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | Official tutorial / reference · free | Compare a deterministic workflow with a bounded tool loop. |
| Stop conditions, budget, errors | [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | Official tutorial / reference · free | Set maximum steps, timeout, and tool-failure tests. |
| Multi-agent orchestration tradeoffs | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Evaluate one partitioned task; retain a single agent if no gain. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Expose read-only search with validated arguments. | Code/test or short measured comparison; explain the result independently. |
| 2 | Compare a deterministic workflow with a bounded tool loop. | Code/test or short measured comparison; explain the result independently. |
| 3 | Set maximum steps, timeout, and tool-failure tests. | Code/test or short measured comparison; explain the result independently. |
| 4 | Evaluate one partitioned task; retain a single agent if no gain. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

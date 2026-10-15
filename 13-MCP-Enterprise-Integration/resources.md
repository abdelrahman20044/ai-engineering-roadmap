# Resources · L13 — MCP, Enterprise Integration, and AI Workflows

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | MCP official architecture and the chosen SDK version; the books are not a sufficient MCP reference. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C10 pp.472–473: orchestration; G8 conceptual reference only; C6 tool contracts as needed. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Client, host, server roles | [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | Official tutorial / reference · free | Diagram a read-only document-search integration. |
| Tools, resources, contracts | [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | Official tutorial / reference · free | Build one local read-only tool with explicit schemas. |
| Trust boundaries and enterprise adapters | [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Official tutorial / reference · free | Treat server results as untrusted and enforce caller permissions. |
| Workflow orchestration | [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | Official tutorial / reference · free | Keep business rules in tested application code. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Diagram a read-only document-search integration. | Code/test or short measured comparison; explain the result independently. |
| 2 | Build one local read-only tool with explicit schemas. | Code/test or short measured comparison; explain the result independently. |
| 3 | Treat server results as untrusted and enforce caller permissions. | Code/test or short measured comparison; explain the result independently. |
| 4 | Keep business rules in tested application code. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

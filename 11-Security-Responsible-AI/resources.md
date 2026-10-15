# Resources · L11 — Security, Authorization, and Responsible AI

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | F8 PDF338–400: FastAPI authorization implementation; skim familiar JWT concepts. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F9 PDF401–428; C5 pp.235–250; C10 pp.451–455. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | OWASP GenAI Prompt Injection: server-enforced permissions and least privilege. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| FastAPI authentication and ownership | [FastAPI OAuth2 and JWT tutorial](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) | Official tutorial / reference · free | Port known JWT concepts and test owner boundaries. |
| Prompt injection and tool permissions | [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Official tutorial / reference · free | Use a malicious PDF fixture and enforce authorization server-side. |
| Abuse controls and privacy | [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Official tutorial / reference · free | Limit upload size, redact logs, and verify deletion. |
| Responsible reflection UX | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Separate cited book claims, journal facts, and generated suggestions. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Port known JWT concepts and test owner boundaries. | Code/test or short measured comparison; explain the result independently. |
| 2 | Use a malicious PDF fixture and enforce authorization server-side. | Code/test or short measured comparison; explain the result independently. |
| 3 | Limit upload size, redact logs, and verify deletion. | Code/test or short measured comparison; explain the result independently. |
| 4 | Separate cited book claims, journal facts, and generated suggestions. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

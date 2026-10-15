# L11 · Security, Authorization, and Responsible AI

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 16–24 h | 3/5 | P1 | [L06](../06-Application-State/README.md), [L08](../08-RAG-Systems/README.md) |

**Outcome:** Enforce ownership before retrieval, source viewing, history, memory, and job access. Constrain untrusted content, tools, uploads, and consumption.

**Unlocks:** [L12](../12-Tools-Agents/README.md), [L14](../14-LLMOps-Deployment/README.md), [L16](../16-Capstone-Career/README.md), [L18](../18-Supporting-Frontend/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| FastAPI authentication and ownership | F8 PDF338–400; [FastAPI OAuth2 and JWT tutorial](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) | [Practice 1](resources.md#practice-and-evidence) |
| Prompt injection and tool permissions | C5 pp.235–250; F9 PDF401–428; [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | [Practice 2](resources.md#practice-and-evidence) |
| Abuse controls and privacy | C10 pp.451–455; F9 security; [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | [Practice 3](resources.md#practice-and-evidence) |
| Responsible reflection UX | C4 criteria; C10 feedback; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N07** — RESTful API, Backend Architecture & Security.
- **N20** — AI Evaluation, Safety & Responsible AI.
- **N26** — AI Security, Governance & Compliance.

| ITI topic IDs | Interpretation |
| --- | --- |
| N07, N20, N26 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L11-E1 | Build an A/B access matrix across every resource endpoint, source viewer, cache, and job state. | User B cannot retrieve, read, edit, or delete user A data. |
| L11-E2 | Index a passage that tries to change instructions or expose another journal. | Authorization remains independent of the model and document instructions. |
| L11-E3 | Set file/page/token/request/tool/retry limits. | Oversized requests and abuse have bounded, tested failure behavior. |
| L11-E4 | Delete a document and its derived data, memory links, and caches. | Document active deletion and backup retention separately. |
| L11-E5 | Threat-model upload/storage/provider/logs/tools and use synthetic journals. | No secret or sensitive journal content appears in default logs or browser configuration. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S4](../project/milestones/s4.md) | Threat model, authorization integration tests, and security matrix; Deletion and retention policy | Pass designed isolation tests before public deployment. Passing tests is not proof of universal security; retrieved text does not grant tool privileges. |

## Postpone

| Outside this level |
| --- |
| System prompts as authorization controls |
| Unapproved autonomous write tools |

## Record completion

```bash
python scripts/progress.py set L11 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L10](../10-Concurrency-Streaming-Jobs/README.md) · Next numbered Level: [L12](../12-Tools-Agents/README.md). Follow the prerequisite table if branches differ.

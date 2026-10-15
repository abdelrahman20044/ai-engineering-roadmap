# L18 · Supporting TypeScript and React UI

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 6 · Optional Specialization and Supporting UI | 12–20 h | 2/5 | P3 | [L01](../01-Python-FastAPI/README.md), [L04](../04-LLM-Applications-Prompts/README.md), [L11](../11-Security-Responsible-AI/README.md) |

**Outcome:** Build a small accessible client for API errors, streaming, and evidence display. Distinguish product UI needs from a complete React/TypeScript curriculum.

**Unlocks:** Optional extension; no core level depends on it.

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| React and TypeScript bridge | Official tutorial; F6 client reference; [React with TypeScript](https://react.dev/learn/typescript) | [Practice 1](resources.md#practice-and-evidence) |
| Streaming client and auth contracts | F6 communication; F8 auth; [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 2](resources.md#practice-and-evidence) |
| UI debugging and scope | F11 E2E reference; [React with TypeScript](https://react.dev/learn/typescript) | [Practice 3](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N05** — Software Testing & Full-Stack Debugging.
- **N08** — Frontend TypeScript & React.

| ITI topic IDs | Interpretation |
| --- | --- |
| N05, N08 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L18-E1 | Type requests, responses, and citations; add upload/question/journal forms. | Handle loading, empty, and failure states. |
| L18-E2 | Display source snippets and pages using server metadata. | Test keyboard navigation, long text, and RTL if supported by the product. |
| L18-E3 | Integrate authentication and streaming without browser secrets. | Document cookie/bearer/CORS/CSRF choices for the client. |
| L18-E4 | Test a normal UI journey and unauthorized access. | The UI exposes backend failures rather than masking them. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S7](../project/milestones/s7.md) | Small React/TypeScript client, API contract, and UI/accessibility test notes | A basic UI is required by the capstone. React specifically is optional for this self-study Core, while explicit React/TypeScript coverage remains visible in the ITI mapping. |

## Postpone

| Outside this level |
| --- |
| Advanced frontend design |
| Pausing AI engineering until a complete frontend course is finished |

## Record completion

```bash
python scripts/progress.py set L18 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L17](../17-Fine-Tuning-Advanced-Serving/README.md) · Next numbered Level: End. Follow the prerequisite table if branches differ.

# L00 · Baseline Assessment and Product Scope

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 3–5 h | 1/5 | P0 | Baseline backend experience |

**Outcome:** Identify transferable backend skills and specific gaps. Define users, requirements, failure cases, and acceptance evidence.

**Unlocks:** [L01](../01-Python-FastAPI/README.md), [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Transfer existing backend skills | C1 pp.28–46; [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 1](resources.md#practice-and-evidence) |
| Define product and failure cases | C1 pp.28–34; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 2](resources.md#practice-and-evidence) |
| Evaluation before implementation | C4 pp.200–207; [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | [Practice 3](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N01** — Modern Software Engineering & Git Collaboration.
- **N03** — SDLC & Requirements Engineering.
- **N09** — Software Architecture & System Design.
- **N30** — Effective Communication Skills.
- **N31** — Work Ethics Workshop.

| ITI topic IDs | Interpretation |
| --- | --- |
| N01, N03, N09, N30, N31 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L00-E1 | Explain a JWT/RBAC flow, Zod validation, and an integration test from CRM. Write a typed JSON cleaner and a test without AI. | Record demonstrated skills and gaps; distinguish prior evidence from assumptions. |
| L00-E2 | Write five user stories and three failure cases: missing evidence, unreadable document, and unauthorized resource access. | Each story has an observable acceptance condition. |
| L00-E3 | Choose a small permitted corpus, specify input/output contracts and three non-goals, and create the first ADR. | A one-page scope and ten initial questions are sufficient to start building. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S0](../project/milestones/s0.md) | baseline.md with links to prior work; project-scope.md and the first ADR | Explain the use case and the first deliverable in two minutes. Review only demonstrated gaps rather than restarting backend fundamentals. |

## Postpone

| Outside this level |
| --- |
| Repeating JavaScript, HTTP, Git, or Docker basics after passing diagnostics |
| Microservices or buying a GPU before a need exists |

## Record completion

```bash
python scripts/progress.py set L00 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: Start · Next numbered Level: [L01](../01-Python-FastAPI/README.md). Follow the prerequisite table if branches differ.

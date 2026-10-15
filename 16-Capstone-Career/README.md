# L16 · Capstone Release, Technical Defense, and Career Evidence

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 5 · Operating and Demonstrating AI Systems | 12–18 h | 4/5 | P2 | [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md), [L08](../08-RAG-Systems/README.md), [L09](../09-Context-Memory/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md), [L12](../12-Tools-Agents/README.md), [L13](../13-MCP-Enterprise-Integration/README.md), [L14](../14-LLMOps-Deployment/README.md), [L15](../15-Model-Selection-Optimization/README.md) |

**Outcome:** Demonstrate a usable AI application with evaluation and operating evidence. Explain and modify the implementation independently and communicate honest limitations.

**Unlocks:** Optional extension; no core level depends on it.

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Independent release and technical defense | C1 planning; F11 E2E; C4 evaluation; [GitHub Actions Python guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | [Practice 1](resources.md#practice-and-evidence) |
| Portfolio and system explanation | C10 architecture and feedback review; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 2](resources.md#practice-and-evidence) |
| ML/DL interview foundations | G1; C2 focused review; [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | [Practice 3](resources.md#practice-and-evidence) |
| Backend interview bridge | F2/F4/F5/F7/F8 selected review; [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N27** — Graduation Project.
- **N28** — Effective Presentation Skills.
- **N29** — Freelancing Fundamentals.
- **N30** — Effective Communication Skills.
- **N31** — Work Ethics Workshop.
- **N32** — CV Writing & Interviewing Skills.

| ITI topic IDs | Interpretation |
| --- | --- |
| N27, N28, N29, N30, N31, N32 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L16-E1 | Demonstrate upload → question → source → journal connection → conversation → deletion through a basic UI. | Include failure paths and cross-user access tests. |
| L16-E2 | Freeze configuration and run the final independent holdout. | Analyze three major failures and disclose remaining limitations. |
| L16-E3 | Publish application setup docs, ERD/architecture, ADRs, runbook, and a 3–5-minute demo. | A reviewer can reproduce the demo with synthetic data. |
| L16-E4 | Run a mock defense: write an endpoint, query, and test without AI; diagnose a trace. | Explain framework, model, retrieval, and single-agent decisions. |
| L16-E5 | Draft evidence-based CV claims and a scoped freelance proposal. | Only measured figures are used; discuss data ethics, delivery scope, and communication. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S7](../project/milestones/s7.md) | Versioned release, demo, evaluation report/dashboard, and defense notes | Run, explain, modify, and evaluate the system. This is a self-study gate, not an ITI credential or hiring guarantee. L17/L18 remain optional. |

## Postpone

| Outside this level |
| --- |
| Waiting for every advanced topic before applying |
| Inflated metrics or unsupported production-ready claims |

## Record completion

```bash
python scripts/progress.py set L16 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L15](../15-Model-Selection-Optimization/README.md) · Next numbered Level: [L17](../17-Fine-Tuning-Advanced-Serving/README.md). Follow the prerequisite table if branches differ.

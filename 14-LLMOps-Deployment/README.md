# L14 · MLOps, LLMOps, Architecture, and Deployment

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 5 · Operating and Demonstrating AI Systems | 20–30 h | 4/5 | P2 | [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md) |

**Outcome:** Version model/prompt/corpus/evaluation artifacts and trace execution. Release, restore, and diagnose an AI service and its worker.

**Unlocks:** [L15](../15-Model-Selection-Optimization/README.md), [L16](../16-Capstone-Career/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Containerization and deployment | F12 PDF536–594; [Docker workshop](https://docs.docker.com/get-started/workshop/) | [Practice 1](resources.md#practice-and-evidence) |
| CI and regression checks | F11 E2E; C10 pp.465–473; [GitHub Actions Python guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | [Practice 2](resources.md#practice-and-evidence) |
| Tracing, metrics, redaction | C10 pp.465–473; [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | [Practice 3](resources.md#practice-and-evidence) |
| Architecture, release, rollback | F3 serving; F12 deployment; [Docker workshop](https://docs.docker.com/get-started/workshop/) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N01** — Modern Software Engineering & Git Collaboration.
- **N05** — Software Testing & Full-Stack Debugging.
- **N09** — Software Architecture & System Design.
- **N10** — Cloud-Native Deployment & Platform Mapping.
- **N15** — MLOps Basics & Model Serving.
- **N25** — LLMOps & Production Readiness for AI Applications.

| ITI topic IDs | Interpretation |
| --- | --- |
| N01, N05, N09, N10, N15, N25 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L14-E1 | Document application architecture and ADRs for inference, state, and worker boundaries. | Explain failure boundaries and why a modular monolith is sufficient. |
| L14-E2 | Add trace IDs and stage timings for parsing/retrieval/model calls, TTFT, errors, and usage. | Sensitive content is redacted; representative failures can be located from a trace. |
| L14-E3 | Build CI for deterministic tests and checks, with separately budgeted live evaluation. | Model or prompt changes trigger an explicit regression review. |
| L14-E4 | Containerize and test fresh migration, persistent restart, backup/restore, and readiness. | Record an actual restore, not just a backup command. |
| L14-E5 | Deploy once to a suitable environment or demonstrate a reproducible local operating setup. | Test outage and rollback; public access requires HTTPS/auth/secrets controls. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S6](../project/milestones/s6.md) | Runbook, CI, release manifest, and traces; Deployment/local operating demo plus restore evidence | Reproduce a release, restore state, diagnose failure, and state operating limits. Docker alone is not production readiness. |

## Postpone

| Outside this level |
| --- |
| Kubernetes or multiple observability products by default |
| A GPU cluster before a measured serving requirement |

## Record completion

```bash
python scripts/progress.py set L14 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L13](../13-MCP-Enterprise-Integration/README.md) · Next numbered Level: [L15](../15-Model-Selection-Optimization/README.md). Follow the prerequisite table if branches differ.

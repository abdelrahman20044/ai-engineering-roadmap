# M14 — MLOps, LLMOps, Architecture, and Deployment

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P2 |
| Prerequisites | [M10](../m10-async-streaming-jobs/README.md), [M11](../m11-security/README.md) |
| Personal effort | 20–30 focused hours; not official ITI hours |
| Project milestone | [S6](../../project/milestones/s6.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Version model/prompt/corpus/evaluation artifacts and trace execution. |
| O2 | Release, restore, and diagnose an AI service and its worker. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N01 | Modern Software Engineering & Git Collaboration | 18 |
| N05 | Software Testing & Full-Stack Debugging | 30 |
| N09 | Software Architecture & System Design | 30 |
| N10 | Cloud-Native Deployment & Platform Mapping | 24 |
| N15 | MLOps Basics & Model Serving | 18 |
| N25 | LLMOps & Production Readiness for AI Applications | 18 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | F12 PDF 536–594: Dockerfile, storage, networking, Compose, and image optimization; skim familiar Docker basics. |
| 2 | F11 E2E; C10 Monitoring and Observability pp. 465–473. |
| 3 | F3 serving strategies and C9 performance metrics; GPU optimization remains optional. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M14-E1 | Document application architecture and ADRs for inference, state, and worker boundaries. | Explain failure boundaries and why a modular monolith is sufficient. |
| M14-E2 | Add trace IDs and stage timings for parsing/retrieval/model calls, TTFT, errors, and usage. | Sensitive content is redacted; representative failures can be located from a trace. |
| M14-E3 | Build CI for deterministic tests and checks, with separately budgeted live evaluation. | Model or prompt changes trigger an explicit regression review. |
| M14-E4 | Containerize and test fresh migration, persistent restart, backup/restore, and readiness. | Record an actual restore, not just a backup command. |
| M14-E5 | Deploy once to a suitable environment or demonstrate a reproducible local operating setup. | Test outage and rollback; public access requires HTTPS/auth/secrets controls. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Runbook, CI, release manifest, and traces; Deployment/local operating demo plus restore evidence |
| Pass condition | Reproduce a release, restore state, diagnose failure, and state operating limits. Docker alone is not production readiness. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M14 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Kubernetes or multiple observability products by default |
| A GPU cluster before a measured serving requirement |

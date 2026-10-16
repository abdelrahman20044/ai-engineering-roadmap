# L14 · MLOps, LLMOps, Architecture, and Deployment

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 5 · Operating and Demonstrating AI Systems | 20–30 h | 4/5 | P2 | [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md) |

**Unlocks:** [L15](../15-Model-Selection-Optimization/README.md), [L16](../16-Capstone-Career/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Version model/prompt/corpus/evaluation artifacts and trace execution. Release, restore, and diagnose an AI service and its worker. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Application readiness | API, database and worker run locally with known setup commands. |
| Test readiness | Fast deterministic suite and bounded eval cases run independently. |
| Ops reasoning | Distinguish liveness, readiness, migration and dependency failure. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Containers and service topology: Start the stack from a clean checkout and preserve uploaded documents/database state across restarts.
- [ ] CI and evaluation gates: Fail a PR/commit check on a deliberately broken ownership test and retain the report.
- [ ] Version and release metadata: Attach a version manifest to a demo/evaluation result so it can be reproduced.
- [ ] Tracing and metrics: Trace upload and question flows; create a dashboard or query for errors, latency and usage.
- [ ] Deployment and safe operation: Deploy one small environment and document startup, migration and dependency-outage behavior.
- [ ] Recovery and incident handling: Restore a backup into a fresh DB and write a short incident report for an induced failure.

## Recommended learning path

F12 selective Docker → mini-RAG deployment lessons → CI + immutable version metadata → trace one request → backup/restore and rollback drill.

| Pass | Work to do | Stop condition |
| --- | --- | --- |
| 1 · Orient | Use the assigned book/article focus and one Arabic or English explanation for each unfamiliar topic. | Explain the mechanism in your own words. |
| 2 · Implement | Work through the numbered topic outputs below; integrate them into the assessed exercises. | The specified behavior is reproducible in your own code. |
| 3 · Verify | Run the failure cases, self-check and milestone acceptance contract. | Evidence and remaining limitations are recorded. |

The resource library contains alternatives and optional depth. The effort estimate covers a selected path plus implementation, not watching every listed course. Choose Arabic teaching when it speeds understanding, then consult the English API reference for exact behavior.

## What you learn and exactly where

Each numbered row is a learning unit. **Arabic teaching**, **machine-translated Arabic text**, **English videos**, and **English documentation** are labeled separately. A missing verified Arabic resource is stated explicitly; a loosely related video is not presented as full coverage.

| Topic and required subtopics | Arabic route | English route | Build or verify |
| --- | --- | --- | --- |
| **L14-T01 · Containers and service topology**<br>API/worker/db; images; networks; volumes; configuration; health | [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) (AR video)<br>[mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video)<br>[LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides) | Start the stack from a clean checkout and preserve uploaded documents/database state across restarts. |
| **L14-T02 · CI and evaluation gates**<br>Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts | [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) (AR video)<br>[mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Fail a PR/commit check on a deliberately broken ownership test and retain the report. |
| **L14-T03 · Version and release metadata**<br>Code/model/prompt/corpus/index/eval identifiers; config diff | [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text) | [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides)<br>[Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) (EN) | Attach a version manifest to a demo/evaluation result so it can be reproduced. |
| **L14-T04 · Tracing and metrics**<br>Spans; retrieval latency; provider timing; errors; token use; redaction | [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) (AR video)<br>**Scope:** Deployment/monitoring context; detailed span instrumentation uses OpenTelemetry. | [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides) | Trace upload and question flows; create a dashboard or query for errors, latency and usage. |
| **L14-T05 · Deployment and safe operation**<br>Health/readiness; migration order; worker limits; secret injection | [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) (AR video)<br>[mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Deploy one small environment and document startup, migration and dependency-outage behavior. |
| **L14-T06 · Recovery and incident handling**<br>Restore; release rollback; runbook; retention; injected failure | [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) (AR video) | [Postmortem culture](https://sre.google/sre-book/postmortem-culture/) (EN chapter)<br>[PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) (EN) | Restore a backup into a fresh DB and write a short incident report for an induced failure. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L14-T01 | F12 PDF536–594; skim Docker basics already known | [Docker workshop](https://docs.docker.com/get-started/workshop/) (EN) |
| L14-T02 | F11 E2E; F12 deployment | [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) (EN) |
| L14-T03 | C10 architecture; F12 release reference | [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) (EN) |
| L14-T04 | C10 pp.465–473, primary | [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN)<br>[Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/) (EN) |
| L14-T05 | F3 serving strategies; F12 deployment | [Docker workshop](https://docs.docker.com/get-started/workshop/) (EN)<br>[Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) (EN) |
| L14-T06 | C10 monitoring; F12 persistence/networking | [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) (EN)<br>[Postmortem culture](https://sre.google/sre-book/postmortem-culture/) (EN chapter) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N01 · Modern Software Engineering & Git Collaboration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N05 · Software Testing & Full-Stack Debugging | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N09 · Software Architecture & System Design | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N10 · Cloud-Native Deployment & Platform Mapping | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N15 · MLOps Basics & Model Serving | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N25 · LLMOps & Production Readiness for AI Applications | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L14-E1 | Document application architecture and ADRs for inference, state, and worker boundaries. | Explain failure boundaries and why a modular monolith is sufficient. |
| L14-E2 | Add trace IDs and stage timings for parsing/retrieval/model calls, TTFT, errors, and usage. | Sensitive content is redacted; representative failures can be located from a trace. |
| L14-E3 | Build CI for deterministic tests and checks, with separately budgeted live evaluation. | Model or prompt changes trigger an explicit regression review. |
| L14-E4 | Containerize and test fresh migration, persistent restart, backup/restore, and readiness. | Record an actual restore, not just a backup command. |
| L14-E5 | Deploy once to a suitable environment or demonstrate a reproducible local operating setup. | Test outage and rollback; public access requires HTTPS/auth/secrets controls. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Container runs therefore production-ready | Test persistence, health, secrets, worker restart and restore. |
| Only log final model text | Trace parser/retriever/provider stages while redacting private content. |
| Deploy with no recovery plan | Test restore/rollback and define who can apply a migration. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What belongs in a trace?
2. What must be versioned?
3. Backup equals restore?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | A correlation ID, stage timing, selected model/config and safe error/usage attributes; avoid raw private journals. |
| 2 | Code, model, prompt, corpus/index, embedding/chunk policy and evaluation set. |
| 3 | No; a backup is evidence only after a successful restore and consistency check. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S6](../project/milestones/s6.md) | Runbook, CI, release manifest, and traces; Deployment/local operating demo plus restore evidence | Reproduce a release, restore state, diagnose failure, and state operating limits. Docker alone is not production readiness. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Reproduce a release, restore state, diagnose failure, and state operating limits. Docker alone is not production readiness.

## Postpone until justified

- Kubernetes or multiple observability products by default
- A GPU cluster before a measured serving requirement

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L14 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L13](../13-MCP-Enterprise-Integration/README.md) · Next numbered Level: [L15](../15-Model-Selection-Optimization/README.md)

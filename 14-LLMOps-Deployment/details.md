# Technical Details · L14

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Application readiness:** API, database and worker run locally with known setup commands.
- **Test readiness:** Fast deterministic suite and bounded eval cases run independently.
- **Ops reasoning:** Distinguish liveness, readiness, migration and dependency failure.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Containers and service topology:** API/worker/db; images; networks; volumes; configuration; health.
- **CI and evaluation gates:** Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts.
- **Version and release metadata:** Code/model/prompt/corpus/index/eval identifiers; config diff.
- **Tracing and metrics:** Spans; retrieval latency; provider timing; errors; token use; redaction.
- **Deployment and safe operation:** Health/readiness; migration order; worker limits; secret injection.
- **Recovery and incident handling:** Restore; release rollback; runbook; retention; injected failure.

## Common mistakes and debugging

### Container runs therefore production-ready

Test persistence, health, secrets, worker restart and restore.

### Only log final model text

Trace parser/retriever/provider stages while redacting private content.

### Deploy with no recovery plan

Test restore/rollback and define who can apply a migration.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. What belongs in a trace?
2. What must be versioned?
3. Backup equals restore?

<details>
<summary>Answer guide</summary>

**What belongs in a trace?**

A correlation ID, stage timing, selected model/config and safe error/usage attributes; avoid raw private journals.

**What must be versioned?**

Code, model, prompt, corpus/index, embedding/chunk policy and evaluation set.

**Backup equals restore?**

No; a backup is evidence only after a successful restore and consistency check.

</details>

## ITI provenance and industry extensions

- **N01:** Modern Software Engineering & Git Collaboration — official published module title.
- **N05:** Software Testing & Full-Stack Debugging — official published module title.
- **N09:** Software Architecture & System Design — official published module title.
- **N10:** Cloud-Native Deployment & Platform Mapping — official published module title.
- **N15:** MLOps Basics & Model Serving — official published module title.
- **N25:** LLMOps & Production Readiness for AI Applications — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Start the stack from a clean checkout and preserve uploaded documents/database state across restarts.
- [ ] Fail a PR/commit check on a deliberately broken ownership test and retain the report.
- [ ] Attach a version manifest to a demo/evaluation result so it can be reproduced.
- [ ] Trace upload and question flows; create a dashboard or query for errors, latency and usage.
- [ ] Deploy one small environment and document startup, migration and dependency-outage behavior.
- [ ] Restore a backup into a fresh DB and write a short incident report for an induced failure.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

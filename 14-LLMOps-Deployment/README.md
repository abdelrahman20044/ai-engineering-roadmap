# L14 · MLOps, LLMOps, Architecture, and Deployment

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 5 · 20–30 focused hours · Difficulty 4/5 · P2**

**You will learn:** Version model/prompt/corpus/evaluation artifacts and trace execution. Release, restore, and diagnose an AI service and its worker.

**Before starting:** [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B39 · F12](../docs/READING_GUIDE.md#b39) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Containers and service topology

**Learn:** API/worker/db; images; networks; volumes; configuration; health.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B39 · F12](../docs/READING_GUIDE.md#b39) — **Read Now**. PDF pp.536–594: images, persistence, networks, Compose and deployment. Skim familiar Docker basics.

**Primary · Official documentation / tutorial:** [Docker workshop](https://docs.docker.com/get-started/workshop/). Consult the API/worker/db; images; networks; volumes; configuration; health sections/examples only. Do not read the entire documentation site.

**Practice:** Start the stack from a clean checkout and preserve uploaded documents/database state across restarts.

**Completion check:** The complete stack starts cleanly and retains persisted state after restart.

### 2. CI and evaluation gates

**Learn:** Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B38 · F11](../docs/READING_GUIDE.md#b38) — **Read Now**. PDF pp.529–534: end-to-end test boundaries and vertical/horizontal scenarios. Unit, behavioral and retrieval tests are review.

**Primary · Official documentation / tutorial:** [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python). Consult the Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts sections/examples only. Do not read the entire documentation site.

**Practice:** Fail a PR/commit check on a deliberately broken ownership test and retain the report.

**Completion check:** A deliberately broken ownership/eval fixture causes a failed CI check.

### 3. Version and release metadata

**Learn:** Code/model/prompt/corpus/index/eval identifiers; config diff.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B37 · C10](../docs/READING_GUIDE.md#b37) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B39 · F12](../docs/READING_GUIDE.md#b39) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Documentation tutorial:** [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository). Read Creating a release, Editing a release and Comparing releases. Attach your own prompt/model/corpus/evaluation manifest; GitHub release documentation does not define AI artifact versioning.

**Practice:** Attach a version manifest to a demo/evaluation result so it can be reproduced.

**Completion check:** The release manifest identifies code, model, prompt, corpus/index and eval versions.

### 4. Tracing and metrics

**Learn:** Spans; retrieval latency; provider timing; errors; token use; redaction.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B39a · C10](../docs/READING_GUIDE.md#b39a) — **Read Now**. Printed pp.465–471: monitoring/observability. Orchestration pp.472–473 was B37 and is review only.

**Primary · Official documentation / tutorial:** [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/). Consult the Spans; retrieval latency; provider timing; errors; token use; redaction sections/examples only. Do not read the entire documentation site.

**Practice:** Trace upload and question flows; create a dashboard or query for errors, latency and usage.

**Completion check:** A safe trace links stages; latency/error/usage queries work without raw journals.

### 5. Deployment and safe operation

**Learn:** Health/readiness; migration order; worker limits; secret injection.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B39 · F12](../docs/READING_GUIDE.md#b39) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video (lesson within playlist):** [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg). Only the linked “App Deployments 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Deploy one small environment and document startup, migration and dependency-outage behavior.

**Completion check:** Startup, migrations and dependency outages have documented behavior.

### 6. Recovery and incident handling

**Learn:** Restore; release rollback; runbook; retention; injected failure.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B39a · C10](../docs/READING_GUIDE.md#b39a) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html). Read pg_dump, restoring the dump, and handling large databases only as needed. Perform a database restore drill; application rollback/runbook policies are your own operational exercise.

**Practice:** Restore a backup into a fresh DB and write a short incident report for an induced failure.

**Completion check:** A fresh restore succeeds and an injected incident has a written follow-up.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L14-E1:** Document application architecture and ADRs for inference, state, and worker boundaries.
  - **Pass:** Explain failure boundaries and why a modular monolith is sufficient.
- [ ] **L14-E2:** Add trace IDs and stage timings for parsing/retrieval/model calls, TTFT, errors, and usage.
  - **Pass:** Sensitive content is redacted; representative failures can be located from a trace.
- [ ] **L14-E3:** Build CI for deterministic tests and checks, with separately budgeted live evaluation.
  - **Pass:** Model or prompt changes trigger an explicit regression review.
- [ ] **L14-E4:** Containerize and test fresh migration, persistent restart, backup/restore, and readiness.
  - **Pass:** Record an actual restore, not just a backup command.
- [ ] **L14-E5:** Deploy once to a suitable environment or demonstrate a reproducible local operating setup.
  - **Pass:** Test outage and rollback; public access requires HTTPS/auth/secrets controls.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S6](../project/milestones/s6.md). Reproduce a release, restore state, diagnose failure, and state operating limits. Docker alone is not production readiness.

**Keep:** Runbook, CI, release manifest, and traces; Deployment/local operating demo plus restore evidence.

## What to defer

- Kubernetes or multiple observability products by default
- A GPU cluster before a measured serving requirement

## Record progress and choose the next Level

```bash
python scripts/progress.py set L14 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L15](../15-Model-Selection-Optimization/README.md), [L16](../16-Capstone-Career/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

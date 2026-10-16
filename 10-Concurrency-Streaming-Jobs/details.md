# Technical Details · L10

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **API readiness:** Fake slow/error providers exist so tests are reproducible.
- **Persistence readiness:** A job has stable IDs and persisted states.
- **Concurrency basics:** Explain I/O waiting versus CPU work.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Event loop execution:** await; sync call boundaries; blocking demo; I/O versus CPU.
- **Timeouts and bounded parallelism:** Total deadlines; per-stage timeouts; semaphore/pool; retry backoff.
- **Streaming protocol:** StreamingResponse; SSE framing; partial output; completion/error events.
- **Cancellation and disconnects:** Client abort; generator cleanup; provider stop; partial persistence.
- **Background versus durable jobs:** In-process work; broker/worker; queued/running/failed; restart recovery.
- **Idempotent retries and worker tests:** Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy.

## Common mistakes and debugging

### async around blocking code

A sync parser/model call still blocks; isolate it explicitly.

### Retry duplicates writes

Use stable job identity and transactional effects.

### Browser stops but provider continues

Propagate cancellation and record abandoned work and usage.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. When is BackgroundTasks insufficient?
2. What does at-least-once imply?
3. Why bound concurrency?

<details>
<summary>Answer guide</summary>

**When is BackgroundTasks insufficient?**

When work must survive a process restart, needs retries/queues or long-running execution.

**What does at-least-once imply?**

The same task may execute more than once; effects must be idempotent.

**Why bound concurrency?**

To prevent pool exhaustion, provider rate-limit storms and unbounded memory usage.

</details>

## ITI provenance and industry extensions

- **N02:** Advanced Python Programming for AI Engineers — official published module title.
- **N18:** Asynchronous Processing & Streaming — official published module title.
- **N25:** LLMOps & Production Readiness for AI Applications — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Run concurrent requests to a sleeping/blocking fake provider and compare latency.
- [ ] Bound in-flight provider calls and test timeout plus cancellation without leaked tasks.
- [ ] Build a stream consumer test that receives incremental events and one terminal event.
- [ ] Disconnect mid-response; verify cleanup and a defined partial-message state.
- [ ] Move document processing into a worker and observe job status via the API.
- [ ] Kill/restart a worker, retry the same job and verify no duplicate chunks or false success.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

# L10 · Concurrency, Streaming, and Long-Running Jobs

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 4 · 16–24 focused hours · Difficulty 3/5 · P1**

**You will learn:** Separate I/O concurrency from CPU parallelism and avoid blocking the event loop. Handle streaming cancellation, timeouts, and restartable ingestion jobs.

**Before starting:** [L08](../08-RAG-Systems/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B31 · F5](../docs/READING_GUIDE.md#b31) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Event loop execution

**Learn:** await; sync call boundaries; blocking demo; I/O versus CPU.

**Required reading:**

- [B31 · F5](../docs/READING_GUIDE.md#b31) — **Read Now**. PDF pp.187–210: concurrency/async foundations; pp.253–256: background work/summary. pp.211–212 were B13; pp.240–252 advanced inference is optional in L17.

**Primary · Single video:** [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc). The single linked video. No other channel/playlist content is assigned.

**Practice:** Run concurrent requests to a sleeping/blocking fake provider and compare latency.

**Completion check:** Concurrent request measurements expose and then remove the blocking call.

[Alternative · AR video](resources.md#r-ar-mini-24) (optional) · [Implementation reference](resources.md#r-async)

### 2. Timeouts and bounded parallelism

**Learn:** Total deadlines; per-stage timeouts; semaphore/pool; retry backoff.

**Required reading:**

- [B31 · F5](../docs/READING_GUIDE.md#b31) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html). Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry backoff sections/examples only. Do not read the entire documentation site.

**Practice:** Bound in-flight provider calls and test timeout plus cancellation without leaked tasks.

**Completion check:** Timeout/cancel tests leave no leaked tasks or unbounded requests.

[Alternative · EN video](resources.md#r-async-video) (optional) · [Implementation reference](resources.md#r-httpx)

### 3. Streaming protocol

**Learn:** StreamingResponse; SSE framing; partial output; completion/error events.

**Required reading:**

- [B32 · F6](../docs/READING_GUIDE.md#b32) — **Read Now**. PDF pp.258–269: protocol choice/polling/SSE; pp.278–290: stream/SSE server and client. Skim comparison pp.270–277; WebSocket build pp.291–301 is optional.

**Primary · Official documentation / tutorial:** [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/). Consult the StreamingResponse; SSE framing; partial output; completion/error events sections/examples only. Do not read the entire documentation site.

**Practice:** Build a stream consumer test that receives incremental events and one terminal event.

**Completion check:** Incremental events have valid framing and one terminal event.

[Implementation reference](resources.md#r-fetch)

### 4. Cancellation and disconnects

**Learn:** Client abort; generator cleanup; provider stop; partial persistence.

**Required reading:**

- [B32 · F6](../docs/READING_GUIDE.md#b32) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html). Consult the Client abort; generator cleanup; provider stop; partial persistence sections/examples only. Do not read the entire documentation site.

**Practice:** Disconnect mid-response; verify cleanup and a defined partial-message state.

**Completion check:** A disconnect closes resources and defines the partial-message state.

[Alternative · EN](resources.md#r-stream) (optional) · [Implementation reference](resources.md#r-stream)

### 5. Background versus durable jobs

**Learn:** In-process work; broker/worker; queued/running/failed; restart recovery.

**Required reading:**

- [B31 · F5](../docs/READING_GUIDE.md#b31) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video (lesson within playlist):** [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo). Only the linked “Celery Workers 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Move document processing into a worker and observe job status via the API.

**Completion check:** A restarted worker exposes consistent persisted job state.

[Alternative · AR video](resources.md#r-ar-mini-25) (optional) · [Implementation reference](resources.md#r-background)

### 6. Idempotent retries and worker tests

**Learn:** Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy.

**Required reading:**

- [B31 · F5](../docs/READING_GUIDE.md#b31) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html). Consult the Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy sections/examples only. Do not read the entire documentation site.

**Practice:** Kill/restart a worker, retry the same job and verify no duplicate chunks or false success.

**Completion check:** Duplicate delivery creates no duplicate chunks or false success.

[Alternative · AR video](resources.md#r-ar-mini-24) (optional) · [Implementation reference](resources.md#r-sqlasync)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L10-E1:** Run five concurrent fake I/O requests and probe /health while work is pending.
  - **Pass:** Demonstrate a blocking mistake and a suitable correction; async alone does not solve CPU-heavy parsing.
- [ ] **L10-E2:** Implement streaming with a final structured metadata event.
  - **Pass:** Test disconnect, partial provider failure, time limits, and cleanup.
- [ ] **L10-E3:** Define queued/running/succeeded/failed/cancelled job states and ownership.
  - **Pass:** Replay duplicate messages and restart a worker without duplicating chunks.
- [ ] **L10-E4:** Choose one queue if durability is needed and specify acknowledgment/retry/backoff.
  - **Pass:** Test actual crash behavior; BackgroundTasks is not a durable queue and exactly-once is not assumed.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S4](../project/milestones/s4.md). Light endpoints remain responsive during I/O waits. Partial output is not presented as complete success, and failed indexing never replaces a ready version.

**Keep:** Concurrency experiment, streaming tests, and job lifecycle; Replay and crash-recovery evidence.

## What to defer

- Additional messaging/workflow platforms without a requirement
- WebSockets solely because token streaming is needed

## Record progress and choose the next Level

```bash
python scripts/progress.py set L10 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L14](../14-LLMOps-Deployment/README.md), [L16](../16-Capstone-Career/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

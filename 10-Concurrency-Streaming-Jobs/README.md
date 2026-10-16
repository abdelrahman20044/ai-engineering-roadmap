# L10 · Concurrency, Streaming, and Long-Running Jobs

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 16–24 h | 3/5 | P1 | [L08](../08-RAG-Systems/README.md) |

**Unlocks:** [L14](../14-LLMOps-Deployment/README.md), [L16](../16-Capstone-Career/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Separate I/O concurrency from CPU parallelism and avoid blocking the event loop. Handle streaming cancellation, timeouts, and restartable ingestion jobs. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| API readiness | Fake slow/error providers exist so tests are reproducible. |
| Persistence readiness | A job has stable IDs and persisted states. |
| Concurrency basics | Explain I/O waiting versus CPU work. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Event loop execution: Run concurrent requests to a sleeping/blocking fake provider and compare latency.
- [ ] Timeouts and bounded parallelism: Bound in-flight provider calls and test timeout plus cancellation without leaked tasks.
- [ ] Streaming protocol: Build a stream consumer test that receives incremental events and one terminal event.
- [ ] Cancellation and disconnects: Disconnect mid-response; verify cleanup and a defined partial-message state.
- [ ] Background versus durable jobs: Move document processing into a worker and observe job status via the API.
- [ ] Idempotent retries and worker tests: Kill/restart a worker, retry the same job and verify no duplicate chunks or false success.

## Recommended learning path

F5 event-loop sections → a blocking-route experiment → F6 streaming → cancellation → mini-RAG Celery lessons and durable ingestion.

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
| **L10-T01 · Event loop execution**<br>await; sync call boundaries; blocking demo; I/O versus CPU | [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) (AR video)<br>**Scope:** Worker architecture context; event-loop internals use F5/ArjanCodes. | [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc) (EN video) | Run concurrent requests to a sleeping/blocking fake provider and compare latency. |
| **L10-T02 · Timeouts and bounded parallelism**<br>Total deadlines; per-stage timeouts; semaphore/pool; retry backoff | **Arabic gap:** no directly matching resource verified; use the English route. | [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc) (EN video)<br>[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN) | Bound in-flight provider calls and test timeout plus cancellation without leaked tasks. |
| **L10-T03 · Streaming protocol**<br>StreamingResponse; SSE framing; partial output; completion/error events | **Arabic gap:** no directly matching resource verified; use the English route. | [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) (EN) | Build a stream consumer test that receives incremental events and one terminal event. |
| **L10-T04 · Cancellation and disconnects**<br>Client abort; generator cleanup; provider stop; partial persistence | **Arabic gap:** no directly matching resource verified; use the English route. | [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN)<br>[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) (EN) | Disconnect mid-response; verify cleanup and a defined partial-message state. |
| **L10-T05 · Background versus durable jobs**<br>In-process work; broker/worker; queued/running/failed; restart recovery | [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) (AR video)<br>[mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc) (AR video) | [First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) (EN) | Move document processing into a worker and observe job status via the API. |
| **L10-T06 · Idempotent retries and worker tests**<br>Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy | [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) (AR video)<br>[mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc) (AR video) | [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html) (EN) | Kill/restart a worker, retry the same job and verify no duplicate chunks or false success. |

**Arabic coverage boundary:** The Arabic worker lessons cover Celery integration. Detailed Python cancellation, structured concurrency and disconnect semantics were not verified in a dedicated Arabic course; use Python/FastAPI docs and F5/F6 for those subtopics.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L10-T01 | F5 PDF187–211, first pass | [Concurrency and async/await](https://fastapi.tiangolo.com/async/) (EN)<br>[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN) |
| L10-T02 | F5 PDF187–211 and 253–256 | [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN)<br>[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) (EN) |
| L10-T03 | F6 PDF258–301, streaming first; WebSockets selective | [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) (EN)<br>[Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) (EN) |
| L10-T04 | F6 communication tradeoffs | [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN)<br>[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) (EN) |
| L10-T05 | F5 background-work sections; Celery is a targeted extension | [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) (EN)<br>[First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) (EN) |
| L10-T06 | F5 jobs and F11 test principles | [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html) (EN)<br>[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N02 · Advanced Python Programming for AI Engineers | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N18 · Asynchronous Processing & Streaming | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N25 · LLMOps & Production Readiness for AI Applications | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L10-E1 | Run five concurrent fake I/O requests and probe /health while work is pending. | Demonstrate a blocking mistake and a suitable correction; async alone does not solve CPU-heavy parsing. |
| L10-E2 | Implement streaming with a final structured metadata event. | Test disconnect, partial provider failure, time limits, and cleanup. |
| L10-E3 | Define queued/running/succeeded/failed/cancelled job states and ownership. | Replay duplicate messages and restart a worker without duplicating chunks. |
| L10-E4 | Choose one queue if durability is needed and specify acknowledgment/retry/backoff. | Test actual crash behavior; BackgroundTasks is not a durable queue and exactly-once is not assumed. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| async around blocking code | A sync parser/model call still blocks; isolate it explicitly. |
| Retry duplicates writes | Use stable job identity and transactional effects. |
| Browser stops but provider continues | Propagate cancellation and record abandoned work and usage. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. When is BackgroundTasks insufficient?
2. What does at-least-once imply?
3. Why bound concurrency?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | When work must survive a process restart, needs retries/queues or long-running execution. |
| 2 | The same task may execute more than once; effects must be idempotent. |
| 3 | To prevent pool exhaustion, provider rate-limit storms and unbounded memory usage. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S4](../project/milestones/s4.md) | Concurrency experiment, streaming tests, and job lifecycle; Replay and crash-recovery evidence | Light endpoints remain responsive during I/O waits. Partial output is not presented as complete success, and failed indexing never replaces a ready version. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Light endpoints remain responsive during I/O waits. Partial output is not presented as complete success, and failed indexing never replaces a ready version.

## Postpone until justified

- Additional messaging/workflow platforms without a requirement
- WebSockets solely because token streaming is needed

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L10 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L09](../09-Context-Memory/README.md) · Next numbered Level: [L11](../11-Security-Responsible-AI/README.md)

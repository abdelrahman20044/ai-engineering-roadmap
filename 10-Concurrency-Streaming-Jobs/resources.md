# Resource Library · L10 — Concurrency, Streaming, and Long-Running Jobs

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** The Arabic worker lessons cover Celery integration. Detailed Python cancellation, structured concurrency and disconnect semantics were not verified in a dedicated Arabic course; use Python/FastAPI docs and F5/F6 for those subtopics.

## Book references

Assigned reading is authoritative in [the master order for L10](../docs/READING_GUIDE.md#l10). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B31 · F5](../docs/READING_GUIDE.md#b31), [B32 · F6](../docs/READING_GUIDE.md#b32).

**Previously covered / lookup only:** [B06 · F11](../docs/READING_GUIDE.md#b06), [B13 · F5](../docs/READING_GUIDE.md#b13). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-mini-24"></a>

### mini-RAG · Celery Workers 1/2

[mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Primary. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Event loop execution; Background versus durable jobs; Idempotent retries and worker tests.
- **Assigned portion:** Only the linked “Celery Workers 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Celery Workers 1/2 in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Worker architecture context; event-loop internals use F5/ArjanCodes.

<a id="r-ar-mini-25"></a>

### mini-RAG · Celery Workers 2/2

[mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Background versus durable jobs; Idempotent retries and worker tests.
- **Assigned portion:** Only the linked “Celery Workers 2/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Celery Workers 2/2 in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

## English video and guided courses

<a id="r-async-video"></a>

### Next-Level Concurrent Programming in Python with Asyncio

[Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc)

- **Resource Type:** Single video.
- **Role:** Primary. **Language:** EN video. **By:** ArjanCodes.
- **Access:** Free.
- **Use for:** Event loop execution; Timeouts and bounded parallelism.
- **Assigned portion:** The single linked video. No other channel/playlist content is assigned.
- **Scope:** I/O concurrency, async generators and architecture tradeoffs.
- **Limit:** Older video; use current asyncio TaskGroup/timeout semantics for new code.

## Slides, notebooks and repositories

<a id="r-mini-code"></a>

### mini-RAG lesson index and source branches

[mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)

- **Resource Type:** Course repository / lesson index.
- **Role:** Reference. **Language:** AR explanations / Python code. **By:** Abu Bakr Soliman.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers.
- **Limit:** Educational reference, not a security or correctness certification.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Official documentation and engineering articles

<a id="r-async"></a>

### Concurrency and async/await

[Concurrency and async/await](https://fastapi.tiangolo.com/async/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Event loop execution.
- **Assigned portion:** Consult the await; sync call boundaries; blocking demo; I/O versus CPU sections/examples only. Do not read the entire documentation site.
- **Scope:** I/O concurrency versus parallelism and route execution.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-asyncio"></a>

### asyncio tasks

[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Python.
- **Access:** Free.
- **Use for:** Event loop execution; Timeouts and bounded parallelism; Cancellation and disconnects.
- **Assigned portion:** Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry backoff sections/examples only. Do not read the entire documentation site. Consult the Client abort; generator cleanup; provider stop; partial persistence sections/examples only. Do not read the entire documentation site.
- **Scope:** Task groups, cancellation, timeouts and concurrency.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-httpx"></a>

### HTTPX timeouts

[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** HTTPX.
- **Access:** Free.
- **Use for:** Timeouts and bounded parallelism.
- **Assigned portion:** Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry backoff sections/examples only. Do not read the entire documentation site.
- **Scope:** Connect/read/write/pool timeouts for provider calls.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-stream"></a>

### FastAPI custom responses

[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Streaming protocol; Cancellation and disconnects.
- **Assigned portion:** Consult the StreamingResponse; SSE framing; partial output; completion/error events sections/examples only. Do not read the entire documentation site.
- **Scope:** StreamingResponse and generator behavior; frame your own event stream correctly.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-fetch"></a>

### Using Fetch

[Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** MDN.
- **Access:** Free.
- **Use for:** Streaming protocol.
- **Assigned portion:** Consult the StreamingResponse; SSE framing; partial output; completion/error events sections/examples only. Do not read the entire documentation site.
- **Scope:** HTTP errors, response bodies, streaming and abort signals.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-celery"></a>

### First steps with Celery

[First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Celery.
- **Access:** Free.
- **Use for:** Background versus durable jobs.
- **Assigned portion:** Consult the In-process work; broker/worker; queued/running/failed; restart recovery sections/examples only. Do not read the entire documentation site.
- **Scope:** Create a worker, submit a task and observe results.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-background"></a>

### FastAPI background tasks

[FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Background versus durable jobs.
- **Assigned portion:** Consult the In-process work; broker/worker; queued/running/failed; restart recovery sections/examples only. Do not read the entire documentation site.
- **Scope:** In-process post-response work; not durable job execution.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-jobs"></a>

### Celery task semantics

[Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Celery.
- **Access:** Free.
- **Use for:** Idempotent retries and worker tests.
- **Assigned portion:** Consult the Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy sections/examples only. Do not read the entire documentation site.
- **Scope:** Retries, acknowledgment and idempotent task design.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-sqlasync"></a>

### SQLAlchemy asyncio

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** SQLAlchemy.
- **Access:** Free.
- **Use for:** Idempotent retries and worker tests.
- **Assigned portion:** Consult the Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy sections/examples only. Do not read the entire documentation site.
- **Scope:** One session per concurrent task; explicit database I/O.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

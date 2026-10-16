# Resource Library · L10 — Concurrency, Streaming, and Long-Running Jobs

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** The Arabic worker lessons cover Celery integration. Detailed Python cancellation, structured concurrency and disconnect semantics were not verified in a dedicated Arabic course; use Python/FastAPI docs and F5/F6 for those subtopics.

## Topic navigation

1. [Event loop execution](#unit-01)
2. [Timeouts and bounded parallelism](#unit-02)
3. [Streaming protocol](#unit-03)
4. [Cancellation and disconnects](#unit-04)
5. [Background versus durable jobs](#unit-05)
6. [Idempotent retries and worker tests](#unit-06)

<a id="unit-01"></a>

## 1. Event loop execution

[Return to README Step 1](README.md#1-event-loop-execution)

**Topic/subtopics:** await; sync call boundaries; blocking demo; I/O versus CPU.

**Required sequence (default route):** the assigned book slice [B31 · F5](../docs/READING_GUIDE.md#b31) **THEN** `async-video`. Stop each source at the stated portion.

**Choose ONE explanation for async I/O foundations:** default `async-video` **OR** `async`. The bounded concurrency/cancellation exercises remain required whichever explanation you use. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `asyncio`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-event-loop-execution) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B31 · F5](../docs/READING_GUIDE.md#b31)<br>Alireza Parandeh · EN | Book Section | Complementary | Event loop execution | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b31) |
| `async-video` · [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc)<br>ArjanCodes · EN video | Single Video | Primary | I/O concurrency, async generators and architecture… | The single linked video. No other channel/playlist content is assigned. |
| `ar-mini-24` · [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Celery Workers 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `async` · [Concurrency and async/await](https://fastapi.tiangolo.com/async/)<br>FastAPI · EN | Documentation / tutorial | Alternative | I/O concurrency versus parallelism and route execution. | Consult the relevant example for I/O concurrency versus parallelism and… [bounds](#unit-01-async) |
| `asyncio` · [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)<br>Python · EN | Documentation / tutorial | Reference | Task groups, cancellation, timeouts and concurrency. | Consult the relevant example for Task groups, cancellation, timeouts and… [bounds](#unit-01-asyncio) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-async-video"></a>

**`async-video` — selected portion:** The single linked video. No other channel/playlist content is assigned.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-mini-24"></a>

**`ar-mini-24` — selected portion:** Only the linked “Celery Workers 1/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Worker architecture context; event-loop internals use F5/ArjanCodes.

<a id="unit-01-async"></a>

**`async` — selected portion:** Consult the relevant example for I/O concurrency versus parallelism and route execution. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Substitute only for async I/O foundations. The bounded concurrency/cancellation exercises remain required whichever explanation you use.

<a id="unit-01-asyncio"></a>

**`asyncio` — selected portion:** Consult the relevant example for Task groups, cancellation, timeouts and concurrency. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-02"></a>

## 2. Timeouts and bounded parallelism

[Return to README Step 2](README.md#2-timeouts-and-bounded-parallelism)

**Topic/subtopics:** Total deadlines; per-stage timeouts; semaphore/pool; retry backoff.

**Required sequence:** `asyncio`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `httpx`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-timeouts-and-bounded-parallelism) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B31 · F5](../docs/READING_GUIDE.md#b31)<br>Alireza Parandeh · EN | Book Section | Reference | Timeouts and bounded parallelism | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b31) |
| `asyncio` · [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)<br>Python · EN | Documentation / tutorial | Primary | Task groups, cancellation, timeouts and concurrency. | Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry… [bounds](#unit-02-asyncio) |
| `async-video` · [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc)<br>ArjanCodes · EN video | Single Video | Complementary (as needed) | I/O concurrency, async generators and architecture… | Topic bounds; lesson IDs not verified — [details](#unit-02-async-video) |
| `httpx` · [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/)<br>HTTPX · EN | Documentation / tutorial | Reference | Connect/read/write/pool timeouts for provider calls. | Consult the relevant example for Connect/read/write/pool timeouts for… [bounds](#unit-02-httpx) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-asyncio"></a>

**`asyncio` — selected portion:** Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry backoff sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-async-video"></a>

**`async-video` — selected portion:** Only the linked lesson on I/O concurrency, async generators and architecture tradeoffs. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-httpx"></a>

**`httpx` — selected portion:** Consult the relevant example for Connect/read/write/pool timeouts for provider calls. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Streaming protocol

[Return to README Step 3](README.md#3-streaming-protocol)

**Topic/subtopics:** StreamingResponse; SSE framing; partial output; completion/error events.

**Required sequence:** the assigned book slice [B32 · F6](../docs/READING_GUIDE.md#b32) **THEN** `stream`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `fetch`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-streaming-protocol) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B32 · F6](../docs/READING_GUIDE.md#b32)<br>Alireza Parandeh · EN | Book Section | Complementary | Streaming protocol | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b32) |
| `stream` · [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)<br>FastAPI · EN | Documentation / tutorial | Primary | StreamingResponse and generator behavior; frame your own… | Consult the StreamingResponse; SSE framing; partial output;… [bounds](#unit-03-stream) |
| `fetch` · [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)<br>MDN · EN | Documentation / tutorial | Reference | HTTP errors, response bodies, streaming and abort signals. | Consult the relevant example for HTTP errors, response bodies, streaming… [bounds](#unit-03-fetch) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-stream"></a>

**`stream` — selected portion:** Consult the StreamingResponse; SSE framing; partial output; completion/error events sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-fetch"></a>

**`fetch` — selected portion:** Consult the relevant example for HTTP errors, response bodies, streaming and abort signals. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Cancellation and disconnects

[Return to README Step 4](README.md#4-cancellation-and-disconnects)

**Topic/subtopics:** Client abort; generator cleanup; provider stop; partial persistence.

**Required sequence:** `asyncio`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `stream`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-cancellation-and-disconnects) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B32 · F6](../docs/READING_GUIDE.md#b32)<br>Alireza Parandeh · EN | Book Section | Reference | Cancellation and disconnects | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b32) |
| `asyncio` · [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)<br>Python · EN | Documentation / tutorial | Primary | Task groups, cancellation, timeouts and concurrency. | Consult the Client abort; generator cleanup; provider stop; partial… [bounds](#unit-04-asyncio) |
| `stream` · [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)<br>FastAPI · EN | Documentation / tutorial | Reference | StreamingResponse and generator behavior; frame your own… | Consult the relevant example for StreamingResponse and generator behavior;… [bounds](#unit-04-stream) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-asyncio"></a>

**`asyncio` — selected portion:** Consult the Client abort; generator cleanup; provider stop; partial persistence sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-stream"></a>

**`stream` — selected portion:** Consult the relevant example for StreamingResponse and generator behavior; frame your own event stream correctly. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Background versus durable jobs

[Return to README Step 5](README.md#5-background-versus-durable-jobs)

**Topic/subtopics:** In-process work; broker/worker; queued/running/failed; restart recovery.

**Required sequence:** `ar-mini-24` **THEN** `ar-mini-25` (a different required capability). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `celery`, `background`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-background-versus-durable-jobs) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B31 · F5](../docs/READING_GUIDE.md#b31)<br>Alireza Parandeh · EN | Book Section | Reference | Background versus durable jobs | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b31) |
| `ar-mini-24` · [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | Celery Workers 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-25` · [mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (required) | Celery Workers 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `celery` · [First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)<br>Celery · EN | Documentation / tutorial | Reference | Create a worker, submit a task and observe results. | Consult the relevant example for Create a worker, submit a task and… [bounds](#unit-05-celery) |
| `background` · [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)<br>FastAPI · EN | Documentation / tutorial | Reference | In-process post-response work; not durable job execution. | Consult the relevant example for In-process post-response work; not… [bounds](#unit-05-background) |
| `mini-code` · [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)<br>Abu Bakr Soliman · AR explanations / Python code | Course repository / lesson index | Optional Advanced | Match each lesson to its tutorial branch; compare… | Only the branch corresponding to this topic’s named mini-RAG lesson.… [bounds](#unit-05-mini-code) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-ar-mini-24"></a>

**`ar-mini-24` — selected portion:** Only the linked “Celery Workers 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-25"></a>

**`ar-mini-25` — selected portion:** Only the linked “Celery Workers 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Required after the primary: a distinct capability, not a replacement.

<a id="unit-05-celery"></a>

**`celery` — selected portion:** Consult the relevant example for Create a worker, submit a task and observe results. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-background"></a>

**`background` — selected portion:** Consult the relevant example for In-process post-response work; not durable job execution. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-mini-code"></a>

**`mini-code` — selected portion:** Only the branch corresponding to this topic’s named mini-RAG lesson. Inspect after writing your own implementation.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-06"></a>

## 6. Idempotent retries and worker tests

[Return to README Step 6](README.md#6-idempotent-retries-and-worker-tests)

**Topic/subtopics:** Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy.

**Required sequence:** `jobs`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `sqlasync`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-idempotent-retries-and-worker-tests) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B31 · F5](../docs/READING_GUIDE.md#b31)<br>Alireza Parandeh · EN | Book Section | Reference | Idempotent retries and worker tests | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b31) |
| `jobs` · [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html)<br>Celery · EN | Documentation / tutorial | Primary | Retries, acknowledgment and idempotent task design. | Consult the Acks; duplicate delivery; poisoned inputs; retry budget;… [bounds](#unit-06-jobs) |
| `ar-mini-24` · [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Celery Workers 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-25` · [mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Celery Workers 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `sqlasync` · [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)<br>SQLAlchemy · EN | Documentation / tutorial | Reference | One session per concurrent task; explicit database I/O. | Consult the relevant example for One session per concurrent task; explicit… [bounds](#unit-06-sqlasync) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-jobs"></a>

**`jobs` — selected portion:** Consult the Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-mini-24"></a>

**`ar-mini-24` — selected portion:** Only the linked “Celery Workers 1/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-ar-mini-25"></a>

**`ar-mini-25` — selected portion:** Only the linked “Celery Workers 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-sqlasync"></a>

**`sqlasync` — selected portion:** Consult the relevant example for One session per concurrent task; explicit database I/O. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-mini-24"></a>

<details>
<summary>ar-mini-24 · mini-RAG · Celery Workers 1/2 — access, scope and verification</summary>

[mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Celery Workers 1/2 in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Event loop execution; Background versus durable jobs; Idempotent retries and worker tests.
- **Retained broad selection notes (lookup only):** Only the linked “Celery Workers 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-async-video"></a>

<details>
<summary>async-video · Next-Level Concurrent Programming in Python with Asyncio — access, scope and verification</summary>

[Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc) · ArjanCodes · EN video

- **Resource Type:** Single Video.
- **Access:** Free.
- **Catalog scope:** I/O concurrency, async generators and architecture tradeoffs.
- **Scope/version limits:** Older video; use current asyncio TaskGroup/timeout semantics for new code.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Event loop execution; Timeouts and bounded parallelism.
- **Retained broad selection notes (lookup only):** The single linked video. No other channel/playlist content is assigned.

</details>

<a id="r-async"></a>

<details>
<summary>async · Concurrency and async/await — access, scope and verification</summary>

[Concurrency and async/await](https://fastapi.tiangolo.com/async/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** I/O concurrency versus parallelism and route execution.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Event loop execution.
- **Retained broad selection notes (lookup only):** Consult the await; sync call boundaries; blocking demo; I/O versus CPU sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-asyncio"></a>

<details>
<summary>asyncio · asyncio tasks — access, scope and verification</summary>

[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) · Python · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Task groups, cancellation, timeouts and concurrency.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Event loop execution; Timeouts and bounded parallelism; Cancellation and disconnects.
- **Retained broad selection notes (lookup only):** Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry backoff sections/examples only. Do not read the entire documentation site. Consult the Client abort; generator cleanup; provider stop; partial persistence sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-httpx"></a>

<details>
<summary>httpx · HTTPX timeouts — access, scope and verification</summary>

[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) · HTTPX · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Connect/read/write/pool timeouts for provider calls.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Timeouts and bounded parallelism.
- **Retained broad selection notes (lookup only):** Consult the Total deadlines; per-stage timeouts; semaphore/pool; retry backoff sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-stream"></a>

<details>
<summary>stream · FastAPI custom responses — access, scope and verification</summary>

[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** StreamingResponse and generator behavior; frame your own event stream correctly.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Streaming protocol; Cancellation and disconnects.
- **Retained broad selection notes (lookup only):** Consult the StreamingResponse; SSE framing; partial output; completion/error events sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-fetch"></a>

<details>
<summary>fetch · Using Fetch — access, scope and verification</summary>

[Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) · MDN · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** HTTP errors, response bodies, streaming and abort signals.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Streaming protocol.
- **Retained broad selection notes (lookup only):** Consult the StreamingResponse; SSE framing; partial output; completion/error events sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-25"></a>

<details>
<summary>ar-mini-25 · mini-RAG · Celery Workers 2/2 — access, scope and verification</summary>

[mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Celery Workers 2/2 in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Background versus durable jobs; Idempotent retries and worker tests.
- **Retained broad selection notes (lookup only):** Only the linked “Celery Workers 2/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-celery"></a>

<details>
<summary>celery · First steps with Celery — access, scope and verification</summary>

[First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) · Celery · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Create a worker, submit a task and observe results.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Background versus durable jobs.
- **Retained broad selection notes (lookup only):** Consult the In-process work; broker/worker; queued/running/failed; restart recovery sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-background"></a>

<details>
<summary>background · FastAPI background tasks — access, scope and verification</summary>

[FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** In-process post-response work; not durable job execution.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Background versus durable jobs.
- **Retained broad selection notes (lookup only):** Consult the In-process work; broker/worker; queued/running/failed; restart recovery sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-jobs"></a>

<details>
<summary>jobs · Celery task semantics — access, scope and verification</summary>

[Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html) · Celery · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Retries, acknowledgment and idempotent task design.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Idempotent retries and worker tests.
- **Retained broad selection notes (lookup only):** Consult the Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-sqlasync"></a>

<details>
<summary>sqlasync · SQLAlchemy asyncio — access, scope and verification</summary>

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** One session per concurrent task; explicit database I/O.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Idempotent retries and worker tests.
- **Retained broad selection notes (lookup only):** Consult the Acks; duplicate delivery; poisoned inputs; retry budget; dead-letter policy sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-mini-code"></a>

<details>
<summary>mini-code · mini-RAG lesson index and source branches — access, scope and verification</summary>

[mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag) · Abu Bakr Soliman · AR explanations / Python code

- **Resource Type:** Course repository / lesson index.
- **Access:** Free.
- **Catalog scope:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers.
- **Scope/version limits:** Educational reference, not a security or correctness certification.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. Optional lookup; implement only the portion that addresses the named gap.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

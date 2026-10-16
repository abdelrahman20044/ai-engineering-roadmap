# Resource Library · L10 — Concurrency, Streaming, and Long-Running Jobs

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

F5 event-loop sections → a blocking-route experiment → F6 streaming → cancellation → mini-RAG Celery lessons and durable ingestion.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

The Arabic worker lessons cover Celery integration. Detailed Python cancellation, structured concurrency and disconnect semantics were not verified in a dedicated Arabic course; use Python/FastAPI docs and F5/F6 for those subtopics.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L10-T01 · Event loop execution; L10-T05 · Background versus durable jobs; L10-T06 · Idempotent retries and worker tests | Celery Workers 1/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Celery Workers 2/2](https://www.youtube.com/watch?v=SZ5Aznjf8Kc) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L10-T05 · Background versus durable jobs; L10-T06 · Idempotent retries and worker tests | Celery Workers 2/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc) | ArjanCodes<br>EN video<br>Free | L10-T01 · Event loop execution; L10-T02 · Timeouts and bounded parallelism | I/O concurrency, async generators and architecture tradeoffs. **Boundary:** Older video; use current asyncio TaskGroup/timeout semantics for new code. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag) | Abu Bakr Soliman<br>AR explanations / Python code<br>Free | Optional support for this Level’s assessed exercises | Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. **Boundary:** Educational reference, not a security or correctness certification. |

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| F5 PDF187–211 and 253–256; defer GPU-oriented inference internals. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F6 PDF258–301: streaming/SSE and communication tradeoffs. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| FastAPI async/background tasks; Celery task semantics when durable execution is required. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L10-T01 | Run concurrent requests to a sleeping/blocking fake provider and compare latency. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L10-T02 | Bound in-flight provider calls and test timeout plus cancellation without leaked tasks. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L10-T03 | Build a stream consumer test that receives incremental events and one terminal event. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L10-T04 | Disconnect mid-response; verify cleanup and a defined partial-message state. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L10-T05 | Move document processing into a worker and observe job status via the API. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L10-T06 | Kill/restart a worker, retry the same job and verify no duplicate chunks or false success. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Concurrency and async/await](https://fastapi.tiangolo.com/async/) | FastAPI<br>EN<br>Free | L10-T01 · Event loop execution | I/O concurrency versus parallelism and route execution. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) | Python<br>EN<br>Free | L10-T01 · Event loop execution; L10-T02 · Timeouts and bounded parallelism; L10-T04 · Cancellation and disconnects | Task groups, cancellation, timeouts and concurrency. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) | HTTPX<br>EN<br>Free | L10-T02 · Timeouts and bounded parallelism | Connect/read/write/pool timeouts for provider calls. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) | FastAPI<br>EN<br>Free | L10-T03 · Streaming protocol; L10-T04 · Cancellation and disconnects | StreamingResponse and generator behavior; frame your own event stream correctly. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | MDN<br>EN<br>Free | L10-T03 · Streaming protocol | HTTP errors, response bodies, streaming and abort signals. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) | Celery<br>EN<br>Free | L10-T05 · Background versus durable jobs | Create a worker, submit a task and observe results. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) | FastAPI<br>EN<br>Free | L10-T05 · Background versus durable jobs | In-process post-response work; not durable job execution. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html) | Celery<br>EN<br>Free | L10-T06 · Idempotent retries and worker tests | Retries, acknowledgment and idempotent task design. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | SQLAlchemy<br>EN<br>Free | L10-T06 · Idempotent retries and worker tests | One session per concurrent task; explicit database I/O. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

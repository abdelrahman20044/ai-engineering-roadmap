# M10 — Concurrency, Streaming, and Long-Running Jobs

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M08](../m08-rag/README.md) |
| Personal effort | 16–24 focused hours; not official ITI hours |
| Project milestone | [S4](../../project/milestones/s4.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Separate I/O concurrency from CPU parallelism and avoid blocking the event loop. |
| O2 | Handle streaming cancellation, timeouts, and restartable ingestion jobs. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N02 | Advanced Python Programming for AI Engineers | 30 |
| N18 | Asynchronous Processing & Streaming | 18 |
| N25 | LLMOps & Production Readiness for AI Applications | 18 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | F5 PDF 187–211 and 253–256; defer GPU-oriented inference internals. |
| 2 | F6 PDF 258–301: streaming/SSE and communication tradeoffs. |
| 3 | FastAPI async/background tasks; Celery task semantics when durable execution is required. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M10-E1 | Run five concurrent fake I/O requests and probe /health while work is pending. | Demonstrate a blocking mistake and a suitable correction; async alone does not solve CPU-heavy parsing. |
| M10-E2 | Implement streaming with a final structured metadata event. | Test disconnect, partial provider failure, time limits, and cleanup. |
| M10-E3 | Define queued/running/succeeded/failed/cancelled job states and ownership. | Replay duplicate messages and restart a worker without duplicating chunks. |
| M10-E4 | Choose one queue if durability is needed and specify acknowledgment/retry/backoff. | Test actual crash behavior; BackgroundTasks is not a durable queue and exactly-once is not assumed. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Concurrency experiment, streaming tests, and job lifecycle; Replay and crash-recovery evidence |
| Pass condition | Light endpoints remain responsive during I/O waits. Partial output is not presented as complete success, and failed indexing never replaces a ready version. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M10 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Additional messaging/workflow platforms without a requirement |
| WebSockets solely because token streaming is needed |

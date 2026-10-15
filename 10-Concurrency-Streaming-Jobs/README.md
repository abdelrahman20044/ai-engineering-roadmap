# L10 · Concurrency, Streaming, and Long-Running Jobs

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 16–24 h | 3/5 | P1 | [L08](../08-RAG-Systems/README.md) |

**Outcome:** Separate I/O concurrency from CPU parallelism and avoid blocking the event loop. Handle streaming cancellation, timeouts, and restartable ingestion jobs.

**Unlocks:** [L14](../14-LLMOps-Deployment/README.md), [L16](../16-Capstone-Career/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Event loop and blocking I/O | F5 PDF187–211,253–256; [FastAPI async guide](https://fastapi.tiangolo.com/async/) | [Practice 1](resources.md#practice-and-evidence) |
| Streaming and cancellation | F6 PDF258–301; [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 2](resources.md#practice-and-evidence) |
| Background work versus durable jobs | F5 job sections; [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) | [Practice 3](resources.md#practice-and-evidence) |
| Retries, idempotency, concurrency limits | F5 concurrency sections; [Celery task semantics](https://docs.celeryq.dev/en/stable/userguide/tasks.html) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N02** — Advanced Python Programming for AI Engineers.
- **N18** — Asynchronous Processing & Streaming.
- **N25** — LLMOps & Production Readiness for AI Applications.

| ITI topic IDs | Interpretation |
| --- | --- |
| N02, N18, N25 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L10-E1 | Run five concurrent fake I/O requests and probe /health while work is pending. | Demonstrate a blocking mistake and a suitable correction; async alone does not solve CPU-heavy parsing. |
| L10-E2 | Implement streaming with a final structured metadata event. | Test disconnect, partial provider failure, time limits, and cleanup. |
| L10-E3 | Define queued/running/succeeded/failed/cancelled job states and ownership. | Replay duplicate messages and restart a worker without duplicating chunks. |
| L10-E4 | Choose one queue if durability is needed and specify acknowledgment/retry/backoff. | Test actual crash behavior; BackgroundTasks is not a durable queue and exactly-once is not assumed. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S4](../project/milestones/s4.md) | Concurrency experiment, streaming tests, and job lifecycle; Replay and crash-recovery evidence | Light endpoints remain responsive during I/O waits. Partial output is not presented as complete success, and failed indexing never replaces a ready version. |

## Postpone

| Outside this level |
| --- |
| Additional messaging/workflow platforms without a requirement |
| WebSockets solely because token streaming is needed |

## Record completion

```bash
python scripts/progress.py set L10 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L09](../09-Context-Memory/README.md) · Next numbered Level: [L11](../11-Security-Responsible-AI/README.md). Follow the prerequisite table if branches differ.

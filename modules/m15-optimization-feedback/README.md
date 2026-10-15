# M15 — Model Selection, Cost, Latency, and User Feedback

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P2 |
| Prerequisites | [M05](../m05-evaluation/README.md), [M14](../m14-llmops-deployment/README.md) |
| Personal effort | 12–18 focused hours; not official ITI hours |
| Project milestone | [S6](../../project/milestones/s6.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Improve a measured bottleneck without sacrificing quality or isolation. |
| O2 | Interpret user feedback as a signal rather than unquestioned labels. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N20 | AI Evaluation, Safety & Responsible AI | 12 |
| N25 | LLMOps & Production Readiness for AI Applications | 18 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | C4 Model Selection pp. 179–200 and Cost and Latency pp. 177–178. |
| 2 | F10 PDF 429–476 selectively; C9 Performance Metrics pp. 412–418. |
| 3 | C10 Feedback Design pp. 480–489 and limitations pp. 490–491. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M15-E1 | Compare two model settings or models on the same workload. | Report case count, quality, usage/cost basis, p50/p95, TTFT, date, and environment. |
| M15-E2 | Change context size, output length, or retrieval calls as one controlled experiment. | A latency win that breaks citation quality is not presented as an overall improvement. |
| M15-E3 | If caching is justified, define tenant/model/prompt/corpus keys and invalidation. | Test cross-user isolation and deletion before enabling the cache. |
| M15-E4 | Classify synthetic thumbs/comments into style, factual, retrieval, and other failures. | Define a review loop; dislike is not automatically a factual-error training label. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Model scorecard, controlled optimization report, and feedback taxonomy |
| Pass condition | Every decision has a baseline, configuration, sample size, and limitations. Similarity is not answer confidence and feedback is not automatically ground truth. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M15 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Semantic caching before invalidation rules |
| Many-model routing or GPU tuning without a bottleneck |

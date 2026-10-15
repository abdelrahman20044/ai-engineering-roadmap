# L15 · Model Selection, Cost, Latency, and User Feedback

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 5 · Operating and Demonstrating AI Systems | 12–18 h | 4/5 | P2 | [L05](../05-Evaluation/README.md), [L14](../14-LLMOps-Deployment/README.md) |

**Outcome:** Improve a measured bottleneck without sacrificing quality or isolation. Interpret user feedback as a signal rather than unquestioned labels.

**Unlocks:** [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Model selection under constraints | C4 pp.179–200; [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | [Practice 1](resources.md#practice-and-evidence) |
| Cost and latency budgets | C4 pp.177–178; C9 pp.412–418; [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | [Practice 2](resources.md#practice-and-evidence) |
| Caching and optimization | F10 PDF429–476 selectively; [pgvector search and indexing](https://github.com/pgvector/pgvector) | [Practice 3](resources.md#practice-and-evidence) |
| User feedback and monitoring | C10 pp.480–491; [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N20** — AI Evaluation, Safety & Responsible AI.
- **N25** — LLMOps & Production Readiness for AI Applications.

| ITI topic IDs | Interpretation |
| --- | --- |
| N20, N25 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L15-E1 | Compare two model settings or models on the same workload. | Report case count, quality, usage/cost basis, p50/p95, TTFT, date, and environment. |
| L15-E2 | Change context size, output length, or retrieval calls as one controlled experiment. | A latency win that breaks citation quality is not presented as an overall improvement. |
| L15-E3 | If caching is justified, define tenant/model/prompt/corpus keys and invalidation. | Test cross-user isolation and deletion before enabling the cache. |
| L15-E4 | Classify synthetic thumbs/comments into style, factual, retrieval, and other failures. | Define a review loop; dislike is not automatically a factual-error training label. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S6](../project/milestones/s6.md) | Model scorecard, controlled optimization report, and feedback taxonomy | Every decision has a baseline, configuration, sample size, and limitations. Similarity is not answer confidence and feedback is not automatically ground truth. |

## Postpone

| Outside this level |
| --- |
| Semantic caching before invalidation rules |
| Many-model routing or GPU tuning without a bottleneck |

## Record completion

```bash
python scripts/progress.py set L15 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L14](../14-LLMOps-Deployment/README.md) · Next numbered Level: [L16](../16-Capstone-Career/README.md). Follow the prerequisite table if branches differ.

# Technical Details · L15

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Baseline readiness:** Quality, citation, security and latency results have version metadata.
- **Observability readiness:** Measure stage timing and usage without private content logging.
- **Selection discipline:** Hold corpus/prompt/eval fixed for model comparison.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Model selection for the product:** Language; task quality; license; privacy; context; availability.
- **Latency and throughput:** TTFT; end-to-end p50/p95; concurrency; stage budgets.
- **Cost accounting:** Input/output tokens; retries; embeddings; reranking; local hardware assumptions.
- **Safe caching:** Cache key; tenant boundary; source/version invalidation; expiry.
- **Measured optimization:** Prompt/context reduction; search tuning; caching; queue/backpressure.
- **Feedback and monitoring loop:** Consent; ratings; corrections; failure review; feedback bias.

## Common mistakes and debugging

### Leaderboard wins equal product wins

Evaluate your bilingual corpus and workload under actual constraints.

### Global cache key

Include ownership, model/prompt/corpus versions and deletion invalidation.

### Thumbs-up equals ground truth

Feedback is biased and sparse; review failure examples before changing behavior.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Why p95 as well as p50?
2. Cost per request?
3. When optimize?

<details>
<summary>Answer guide</summary>

**Why p95 as well as p50?**

Median hides slow tail experiences; report concurrency and sample count too.

**Cost per request?**

Measure input/output tokens and provider prices or local compute assumptions, plus retries/reranking when relevant.

**When optimize?**

After a reproducible bottleneck is identified and a quality/permission regression gate exists.

</details>

## ITI provenance and industry extensions

- **N20:** AI Evaluation, Safety & Responsible AI — official published module title.
- **N25:** LLMOps & Production Readiness for AI Applications — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Compare two feasible models on the same queries and configuration table.
- [ ] Measure cold/warm runs and concurrency with a fixed workload; show bottleneck spans.
- [ ] Report cost/request using explicit dated assumptions and a hard experiment budget.
- [ ] Test similar questions from two users and deleted sources before enabling a cache.
- [ ] Change one bottleneck factor and retain before/after quality, latency and cost results.
- [ ] Capture optional feedback, triage three cases and propose a measured follow-up experiment.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

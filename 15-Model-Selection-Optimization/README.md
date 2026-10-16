# L15 · Model Selection, Cost, Latency, and User Feedback

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 5 · 12–18 focused hours · Difficulty 4/5 · P2**

**You will learn:** Improve a measured bottleneck without sacrificing quality or isolation. Interpret user feedback as a signal rather than unquestioned labels.

**Before starting:** [L05](../05-Evaluation/README.md), [L14](../14-LLMOps-Deployment/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B40 · C4](../docs/READING_GUIDE.md#b40) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Model selection for the product

**Learn:** Language; task quality; license; privacy; context; availability.

**Required reading:**

- [B40 · C4](../docs/READING_GUIDE.md#b40) — **Read Now**. Printed pp.179–200: model selection. Cost/latency pp.177–178 are B16 review.

**Primary · Book section:** [B40 · C4](../docs/READING_GUIDE.md#b40). Follow the assigned portion above; use the library references during implementation.

**Practice:** Compare two feasible models on the same queries and configuration table.

**Completion check:** Both model candidates use the same corpus, prompts and held-out task definition.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-intro) (optional) · [Implementation reference](resources.md#r-e5)

### 2. Latency and throughput

**Learn:** TTFT; end-to-end p50/p95; concurrency; stage budgets.

**Required reading:**

- [B42 · C9](../docs/READING_GUIDE.md#b42) — **Read Now**. Printed pp.412–418: performance metrics. Rest of C9 is Optional Advanced in L17.

**Primary · Official documentation / tutorial:** [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html). Consult the TTFT; end-to-end p50/p95; concurrency; stage budgets sections/examples only. Do not read the entire documentation site.

**Practice:** Measure cold/warm runs and concurrency with a fixed workload; show bottleneck spans.

**Completion check:** Cold/warm p50/p95 and concurrency/sample counts are stated.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-lifecycle) (optional) · [Implementation reference](resources.md#r-otel)

### 3. Cost accounting

**Learn:** Input/output tokens; retries; embeddings; reranking; local hardware assumptions.

**Required reading:**

- [B42 · C9](../docs/READING_GUIDE.md#b42) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Book section:** [B42 · C9](../docs/READING_GUIDE.md#b42). Follow the assigned portion above; use the library references during implementation.

**Practice:** Report cost/request using explicit dated assumptions and a hard experiment budget.

**Completion check:** Per-request costs include explicit dated price or hardware assumptions.

[Alternative · AR video](resources.md#r-ar-mini-19) (optional) · [Implementation reference](resources.md#r-otel)

### 4. Safe caching

**Learn:** Cache key; tenant boundary; source/version invalidation; expiry.

**Required reading:**

- [B41 · F10](../docs/READING_GUIDE.md#b41) — **Read Now**. PDF pp.429–476: choose caching/performance sections addressing your measured bottleneck; do not implement every technique.

**Primary · Book section:** [B41 · F10](../docs/READING_GUIDE.md#b41). Follow the assigned portion above; use the library references during implementation.

**Practice:** Test similar questions from two users and deleted sources before enabling a cache.

**Completion check:** Cache tests separate tenants and invalidate changed/deleted sources.

[Alternative · AR video](resources.md#r-ar-mini-20) (optional) · [Implementation reference](resources.md#r-sqlasync)

### 5. Measured optimization

**Learn:** Prompt/context reduction; search tuning; caching; queue/backpressure.

**Required reading:**

- [B41 · F10](../docs/READING_GUIDE.md#b41) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official repository / implementation guide:** [pgvector README](https://github.com/pgvector/pgvector). Read pgvector’s Querying, Indexing, Filtering and Hybrid Search sections relevant to a measured retrieval bottleneck. Test one change; provider caching/backpressure are separate techniques from F10, not pgvector features.

**Practice:** Change one bottleneck factor and retain before/after quality, latency and cost results.

**Completion check:** The one-factor optimization passes existing quality/security gates.

[Alternative · AR machine-translated text](resources.md#r-ar-agent-context) (optional) · [Implementation reference](resources.md#r-locust)

### 6. Feedback and monitoring loop

**Learn:** Consent; ratings; corrections; failure review; feedback bias.

**Required reading:**

- [B43 · C10](../docs/READING_GUIDE.md#b43) — **Read Now**. Printed pp.480–491: feedback design and limitations. Do not restart architecture/observability sections.

**Primary · Single lecture video + slides:** [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/). Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Feedback and monitoring loop. Exact timestamps are not assigned.

**Practice:** Capture optional feedback, triage three cases and propose a measured follow-up experiment.

**Completion check:** Three feedback cases have consented signals and a proposed testable follow-up.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-ux) (optional) · [Implementation reference](resources.md#r-otel)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L15-E1:** Compare two model settings or models on the same workload.
  - **Pass:** Report case count, quality, usage/cost basis, p50/p95, TTFT, date, and environment.
- [ ] **L15-E2:** Change context size, output length, or retrieval calls as one controlled experiment.
  - **Pass:** A latency win that breaks citation quality is not presented as an overall improvement.
- [ ] **L15-E3:** If caching is justified, define tenant/model/prompt/corpus keys and invalidation.
  - **Pass:** Test cross-user isolation and deletion before enabling the cache.
- [ ] **L15-E4:** Classify synthetic thumbs/comments into style, factual, retrieval, and other failures.
  - **Pass:** Define a review loop; dislike is not automatically a factual-error training label.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S6](../project/milestones/s6.md). Every decision has a baseline, configuration, sample size, and limitations. Similarity is not answer confidence and feedback is not automatically ground truth.

**Keep:** Model scorecard, controlled optimization report, and feedback taxonomy.

## What to defer

- Semantic caching before invalidation rules
- Many-model routing or GPU tuning without a bottleneck

## Record progress and choose the next Level

```bash
python scripts/progress.py set L15 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

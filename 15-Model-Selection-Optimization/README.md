# L15 · Model Selection, Cost, Latency, and User Feedback

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 5 · Operating and Demonstrating AI Systems | 12–18 h | 4/5 | P2 | [L05](../05-Evaluation/README.md), [L14](../14-LLMOps-Deployment/README.md) |

**Unlocks:** [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Improve a measured bottleneck without sacrificing quality or isolation. Interpret user feedback as a signal rather than unquestioned labels. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Baseline readiness | Quality, citation, security and latency results have version metadata. |
| Observability readiness | Measure stage timing and usage without private content logging. |
| Selection discipline | Hold corpus/prompt/eval fixed for model comparison. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Model selection for the product: Compare two feasible models on the same queries and configuration table.
- [ ] Latency and throughput: Measure cold/warm runs and concurrency with a fixed workload; show bottleneck spans.
- [ ] Cost accounting: Report cost/request using explicit dated assumptions and a hard experiment budget.
- [ ] Safe caching: Test similar questions from two users and deleted sources before enabling a cache.
- [ ] Measured optimization: Change one bottleneck factor and retain before/after quality, latency and cost results.
- [ ] Feedback and monitoring loop: Capture optional feedback, triage three cases and propose a measured follow-up experiment.

## Recommended learning path

C4 model selection → comparable runs → C9 metrics → one bottleneck experiment → C10 feedback loop. Keep quality gates active during optimization.

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
| **L15-T01 · Model selection for the product**<br>Language; task quality; license; privacy; context; availability | [Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md) (AR machine-translated text)<br>**Scope:** Model/application orientation; controlled selection is taught by C4 and English evaluation resources. | [LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/) (EN video + slides)<br>[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) | Compare two feasible models on the same queries and configuration table. |
| **L15-T02 · Latency and throughput**<br>TTFT; end-to-end p50/p95; concurrency; stage budgets | [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text)<br>**Scope:** Lifecycle orientation; tail-latency measurement uses C9/Locust. | [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html) (EN) | Measure cold/warm runs and concurrency with a fixed workload; show bottleneck spans. |
| **L15-T03 · Cost accounting**<br>Input/output tokens; retries; embeddings; reranking; local hardware assumptions | [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) (AR video)<br>**Scope:** Local model-serving context; cost accounting uses C4/C9 and measured usage. | [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN) | Report cost/request using explicit dated assumptions and a hard experiment budget. |
| **L15-T04 · Safe caching**<br>Cache key; tenant boundary; source/version invalidation; expiry | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video)<br>**Scope:** Database ownership context only; cache-key/invalidation design is an industry extension. | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN)<br>[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN) | Test similar questions from two users and deleted sources before enabling a cache. |
| **L15-T05 · Measured optimization**<br>Prompt/context reduction; search tuning; caching; queue/backpressure | [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) (AR machine-translated text) | [Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) (EN video + labs) | Change one bottleneck factor and retain before/after quality, latency and cost results. |
| **L15-T06 · Feedback and monitoring loop**<br>Consent; ratings; corrections; failure review; feedback bias | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text)<br>[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text) | [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) (EN video + slides) | Capture optional feedback, triage three cases and propose a measured follow-up experiment. |

**Arabic coverage boundary:** Arabic lifecycle and deployment material provides context. Dedicated Arabic instruction for controlled model selection, tail latency and cache isolation was not verified; use C4/C9/C10 and the English engineering material.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L15-T01 | C4 pp.179–200, primary | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN)<br>[Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-small) (EN) |
| L15-T02 | C9 pp.412–418; C4 pp.177–178 | [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html) (EN)<br>[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN) |
| L15-T03 | C4 pp.177–178; F10 selective | [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN)<br>[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) (EN) |
| L15-T04 | F10 PDF429–476, cache sections after profiling | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN)<br>[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN) |
| L15-T05 | F10 selective; C9 metrics first | [pgvector README](https://github.com/pgvector/pgvector) (EN)<br>[Locust quickstart](https://docs.locust.io/en/stable/quickstart.html) (EN) |
| L15-T06 | C10 pp.480–491, primary | [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N20 · AI Evaluation, Safety & Responsible AI | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N25 · LLMOps & Production Readiness for AI Applications | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L15-E1 | Compare two model settings or models on the same workload. | Report case count, quality, usage/cost basis, p50/p95, TTFT, date, and environment. |
| L15-E2 | Change context size, output length, or retrieval calls as one controlled experiment. | A latency win that breaks citation quality is not presented as an overall improvement. |
| L15-E3 | If caching is justified, define tenant/model/prompt/corpus keys and invalidation. | Test cross-user isolation and deletion before enabling the cache. |
| L15-E4 | Classify synthetic thumbs/comments into style, factual, retrieval, and other failures. | Define a review loop; dislike is not automatically a factual-error training label. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Leaderboard wins equal product wins | Evaluate your bilingual corpus and workload under actual constraints. |
| Global cache key | Include ownership, model/prompt/corpus versions and deletion invalidation. |
| Thumbs-up equals ground truth | Feedback is biased and sparse; review failure examples before changing behavior. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Why p95 as well as p50?
2. Cost per request?
3. When optimize?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Median hides slow tail experiences; report concurrency and sample count too. |
| 2 | Measure input/output tokens and provider prices or local compute assumptions, plus retries/reranking when relevant. |
| 3 | After a reproducible bottleneck is identified and a quality/permission regression gate exists. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S6](../project/milestones/s6.md) | Model scorecard, controlled optimization report, and feedback taxonomy | Every decision has a baseline, configuration, sample size, and limitations. Similarity is not answer confidence and feedback is not automatically ground truth. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Every decision has a baseline, configuration, sample size, and limitations. Similarity is not answer confidence and feedback is not automatically ground truth.

## Postpone until justified

- Semantic caching before invalidation rules
- Many-model routing or GPU tuning without a bottleneck

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L15 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L14](../14-LLMOps-Deployment/README.md) · Next numbered Level: [L16](../16-Capstone-Career/README.md)

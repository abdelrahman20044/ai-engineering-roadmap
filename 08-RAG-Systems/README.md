# L08 · RAG Systems, Citations, and Retrieval Improvement

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 3 · 18–28 focused hours · Difficulty 3/5 · P1**

**You will learn:** Build retrieval → context → generation with verifiable citations. Diagnose failures and justify hybrid search or reranking through comparison.

**Before starting:** [L05](../05-Evaluation/README.md), [L07](../07-Embeddings-Semantic-Search/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B24 · G4](../docs/READING_GUIDE.md#b24) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. RAG orchestration

**Learn:** Question → retrieve → assemble context → generate → validate → cite.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B24 · G4](../docs/READING_GUIDE.md#b24) — **Read Now**. Printed pp.94–100: improvement ideas and code explanation. Do not restart pp.74–82.
- [B25 · F5](../docs/READING_GUIDE.md#b25) — **Read Now**. PDF pp.237–239: retrieval into generation and the integrated RAG answer flow. Reuse B21 ingestion code.

**Primary · Single video (lesson within playlist):** [mini-RAG · Augmented Answers](https://www.youtube.com/watch?v=1Wx8BoM5pLU). Only the linked “Augmented Answers” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Ship /ask with passages, source IDs and a defined no-evidence response.

**Completion check:** /ask returns permitted passages and a defined no-evidence response.

### 2. Citation correctness

**Learn:** Allowed IDs; source resolution; page display; claim support.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B26 · F11](../docs/READING_GUIDE.md#b26) — **Read Now**. PDF pp.519–522: integration tests, particularly retrieval/vector-database boundaries. Behavioral testing pp.523–528 is B17 review.

**Primary · Documentation: assertions reference:** [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/). The assertion type matching Citation correctness; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Practice:** Inject fabricated source IDs and unrelated real sources; catch both failure types.

**Completion check:** Both a fake ID and an unrelated real citation are caught.

### 3. Ranking evaluation

**Learn:** Recall@k; MRR/NDCG; relevant-document versus relevant-chunk labels.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B20 · C6](../docs/READING_GUIDE.md#b20) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B27 · C6](../docs/READING_GUIDE.md#b27) — **Read Now**. Printed pp.267–274: retrieval improvements and tradeoffs. pp.253–266 are B20 review.

**Primary · Official documentation / tutorial:** [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html). InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.

**Practice:** Compute a tiny ranking example manually and match the implementation.

**Completion check:** Manual MRR/Recall example agrees with the evaluator.

### 4. Hybrid search

**Learn:** Lexical + dense; candidate union; reciprocal rank fusion; filters.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B27 · C6](../docs/READING_GUIDE.md#b27) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official repository / implementation guide:** [pgvector README](https://github.com/pgvector/pgvector). Consult the Lexical + dense; candidate union; reciprocal rank fusion; filters sections/examples only. Do not read the entire documentation site.

**Practice:** Compare lexical-only, vector-only and hybrid on identical owner-filtered queries.

**Completion check:** Lexical, dense and hybrid use the same labeled queries and owner filters.

### 5. Reranking and query changes

**Learn:** Cross-encoder; candidate count; query rewrite; multilingual checks.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B27 · C6](../docs/READING_GUIDE.md#b27) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html). Consult the Cross-encoder; candidate count; query rewrite; multilingual checks sections/examples only. Do not read the entire documentation site.

**Practice:** Add reranking only if evidence ranking improves enough to justify extra latency.

**Completion check:** The quality gain and added reranking latency are reported together.

### 6. Answer reliability and ablations

**Learn:** Abstention; conflicting sources; context-only checks; retriever/generator failures.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B15 · C3](../docs/READING_GUIDE.md#b15) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B17 · F11](../docs/READING_GUIDE.md#b17) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Documentation / evaluation tutorials:** [Ragas evaluation documentation](https://docs.ragas.io/en/stable/). Consult the Abstention; conflicting sources; context-only checks; retriever/generator failures sections/examples only. Do not read the entire documentation site.

**Practice:** Freeze a baseline, change one factor, report quality/citation/latency plus three failed cases.

**Completion check:** One-factor ablation includes failed cases, citation checks and latency.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L08-E1:** Generate an evidence whitelist, validate references, and display server-provided source/page/snippet.
  - **Pass:** Reject invented IDs and review whether cited passages actually support claims.
- [ ] **L08-E2:** Measure hit@5 and recall@5 using evidence labels; run generation with oracle context.
  - **Pass:** Distinguish parsing, retrieval, and generation failures.
- [ ] **L08-E3:** Compare lexical and dense retrieval; trial one hybrid/RRF or reranker approach if justified.
  - **Pass:** Keep the same dataset and report quality, latency, and cost differences.
- [ ] **L08-E4:** Change one chunking or top-k setting at a time.
  - **Pass:** Save fixed settings and negative results rather than presenting only wins.
- [ ] **L08-E5:** Test no-answer, contradictory sources, and an existing but irrelevant citation.
  - **Pass:** The system does not invent support; similarity is not interpreted as answer confidence.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S3](../project/milestones/s3.md). Explain five failures using evidence. References both exist and support the answer under review. Report thresholds as your project targets, not official ITI standards.

**Keep:** Measured RAG MVP and citation contract tests; Before/after report and failure taxonomy.

## What to defer

- Agentic retrieval before a measured baseline
- Fine-tuning as a parser repair strategy

## Record progress and choose the next Level

```bash
python scripts/progress.py set L08 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L09](../09-Context-Memory/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md), [L16](../16-Capstone-Career/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

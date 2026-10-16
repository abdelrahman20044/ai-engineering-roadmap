# L05 · Evaluation Engineering

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 2 · 14–22 focused hours · Difficulty 3/5 · P0**

**You will learn:** Define datasets and rubrics before expanding the application. Distinguish deterministic tests, component evaluation, and end-to-end quality.

**Before starting:** [L04](../04-LLM-Applications-Prompts/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B16 · C4](../docs/READING_GUIDE.md#b16) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Task criteria and failure taxonomy

**Learn:** Correctness; groundedness; abstention; privacy; severity.

**Required reading:**

- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Read Now**. Printed pp.160–178: task criteria and operational criteria. pp.200–207 were previewed in B03; review/apply, do not restart.

**Primary · Book section:** [B16 · C4](../docs/READING_GUIDE.md#b16). Follow the assigned portion above; use the library references during implementation.

**Practice:** Write a rubric with anchored pass/fail examples and name five failure classes.

**Completion check:** Each rubric label has an anchored pass/fail example.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-lifecycle) (optional)

### 2. Evaluation dataset design

**Learn:** Question strata; reference evidence; train/dev/holdout; versions.

**Required reading:**

- [B03 · C4](../docs/READING_GUIDE.md#b03) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Book section:** [B03 · C4](../docs/READING_GUIDE.md#b03). Follow the assigned portion above; use the library references during implementation.

**Practice:** Version development cases and a separate holdout with source labels.

**Completion check:** Development and holdout cases have different IDs and sources.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-lifecycle) (optional)

### 3. Deterministic component checks

**Learn:** JSON schema; source IDs; ownership; parser contracts; golden fixtures.

**Required reading:**

- [B06 · F11](../docs/READING_GUIDE.md#b06) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B15 · C3](../docs/READING_GUIDE.md#b15) — **Read Now**. Printed pp.114–117 and 125–147: challenges, exact measures, similarity and AI judges. Defer entropy derivations.

**Primary · Official documentation / tutorial:** [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html). Read pytest’s fixtures introduction, fixture scope and teardown sections. Reuse L01 tests; design deterministic component assertions for your own failure cases.

**Practice:** Add exact checks that catch a valid-looking answer with an invalid citation.

**Completion check:** A fabricated citation ID fails even if the prose looks plausible.

[Alternative · EN video + problem sets](resources.md#r-cs50-tests) (optional) · [Implementation reference](resources.md#r-promptfoo)

### 4. Human review and AI judges

**Learn:** Rubric anchors; blind labels; disagreement; bias; judge prompts.

**Required reading:**

- [B15 · C3](../docs/READING_GUIDE.md#b15) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B17 · F11](../docs/READING_GUIDE.md#b17) — **Read Now**. PDF pp.495–500: model-testing challenges; pp.523–528: behavioral tests. Reuse pytest knowledge from B06.

**Primary · Book section:** [B15 · C3](../docs/READING_GUIDE.md#b15). Follow the assigned portion above; use the library references during implementation.

**Practice:** Label a small sample twice and compare judge/human disagreements by category.

**Completion check:** Human/judge disagreements are listed and analyzed, not hidden in an average.

[Alternative · EN video + labs](resources.md#r-dla-eval) (optional) · [Implementation reference](resources.md#r-ragas)

### 5. Retrieval versus answer metrics

**Learn:** Recall@k; MRR; faithfulness; answer relevance; no-evidence behavior.

**Required reading:**

- [B15 · C3](../docs/READING_GUIDE.md#b15) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html). InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.

**Practice:** Report retrieval and generation failures as separate tables.

**Completion check:** Retrieval and answer failures appear in separate result fields.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-rag) (optional) · [Implementation reference](resources.md#r-ragas)

### 6. Regression gates and uncertainty

**Learn:** Counts; confidence caveats; stochastic repeats; release decision.

**Required reading:**

- [B03 · C4](../docs/READING_GUIDE.md#b03) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B17 · F11](../docs/READING_GUIDE.md#b17) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python). Consult the Counts; confidence caveats; stochastic repeats; release decision sections/examples only. Do not read the entire documentation site.

**Practice:** Run a fixed eval suite and retain model/prompt/corpus versions with the results.

**Completion check:** A failed fixture blocks the gate and the result retains model/prompt/data versions.

[Alternative · EN video + problem sets](resources.md#r-cs50-tests) (optional) · [Implementation reference](resources.md#r-promptfoo)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L05-E1:** Use the twelve public seed cases for practice and author thirty development cases.
  - **Pass:** Include answerable, no-answer, multi-evidence, language, and security categories; review labels manually.
- [ ] **L05-E2:** Create a separate holdout before tuning; label document/page/spans.
  - **Pass:** Do not call supplied examples unseen; preserve labels when chunk IDs change.
- [ ] **L05-E3:** Write 0–2 rubrics for correctness, groundedness, and relevance.
  - **Pass:** Calibrate a model judge against human review and document disagreements.
- [ ] **L05-E4:** Define an evaluation run manifest.
  - **Pass:** Record dataset/model/prompt/corpus versions, case count, latency, and cost or usage.
- [ ] **L05-E5:** Specify retrieval and tool metrics before those components are built.
  - **Pass:** Implement retrieval metrics in L08 and tool/task metrics in L12; do not claim these experiments are already complete.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S3](../project/milestones/s3.md). Explain what success means and why. Public seed data is not holdout, mocks do not assess model quality, and judges are not the sole source of truth.

**Keep:** Authored evaluation data, rubric, and run manifest; A report showing real failures as well as successes.

## What to defer

- An elaborate evaluation platform before useful labels
- Repeated tuning against the final holdout

## Record progress and choose the next Level

```bash
python scripts/progress.py set L05 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L08](../08-RAG-Systems/README.md), [L12](../12-Tools-Agents/README.md), [L15](../15-Model-Selection-Optimization/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

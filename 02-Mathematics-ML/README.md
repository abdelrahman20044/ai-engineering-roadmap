# L02 · Practical Mathematics, ML, and Data Preparation

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 1 · 16–24 focused hours · Difficulty 2/5 · P1**

**You will learn:** Understand vectors, matrices, similarity, probability, loss, and gradients through small examples. Run an ML baseline with correct splits, preprocessing, and evaluation. Recognize leakage and distinguish a similarity score from a calibrated probability.

**Before starting:** [L00](../00-Orientation/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Vectors and matrix intuition

**Learn:** Shapes; dot product; norms; cosine; matrix multiplication.

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Official documentation / tutorial:** [NumPy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html). Consult the Shapes; dot product; norms; cosine; matrix multiplication sections/examples only. Do not read the entire documentation site.

**Practice:** Calculate a two-vector cosine by hand and match NumPy within tolerance.

**Completion check:** Hand and NumPy cosine values agree within numeric tolerance.

[Alternative · AR video](resources.md#r-ar-regression) (optional)

### 2. Probability and uncertainty

**Learn:** Conditional probability; expectation; noisy measurements; sample size.

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Modular course: videos + interactive exercises:** [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/). Logistic Regression probability interpretation and its Check Your Understanding exercise only.

**Practice:** Explain a conditional-probability example and report raw counts beside a rate.

**Completion check:** Report raw counts and explain why a small measured rate is uncertain.

[Alternative · AR video](resources.md#r-ar-ml) (optional) · [Implementation reference](resources.md#r-metrics)

### 3. Loss and gradient intuition

**Learn:** Loss versus metric; slope; learning rate; optimization.

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Modular course: videos + interactive exercises:** [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/). Linear Regression: loss and gradient-descent sections only.

**Practice:** Take one manual gradient step on a scalar loss and show whether it improved.

**Completion check:** A manual gradient step changes the scalar loss in the expected direction.

[Alternative · AR video](resources.md#r-ar-regression) (optional) · [Implementation reference](resources.md#r-optimize)

### 4. Preparation and split discipline

**Learn:** Missing values; scaling; train/validation/test; grouped/temporal leakage.

**Required reading:**

- [B07 · C8](../docs/READING_GUIDE.md#b07) — **Skim**. Printed pp.368–371: data quality. Use as motivation; scikit-learn teaches the actual foundation lab.

**Primary · Official documentation / tutorial:** [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html). Consult the Missing values; scaling; train/validation/test; grouped/temporal leakage sections/examples only. Do not read the entire documentation site.

**Practice:** Fit preprocessing on train only; create a deliberately leaky comparison and explain it.

**Completion check:** The test set never participates in fitting preprocessing.

[Alternative · AR video](resources.md#r-ar-sklearn) (optional) · [Implementation reference](resources.md#r-split)

### 5. ML families and baselines

**Learn:** Regression; classification; clustering intuition; overfitting; regularization.

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Modular course: videos + interactive exercises:** [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/). Regression/classification overview plus Datasets/Overfitting sections needed for the baseline; no entire-course replay.

**Practice:** Compare one simple classifier with a dummy baseline and describe train/test behavior.

**Completion check:** A dummy baseline and a fitted classifier are compared on held-out data.

[Alternative · AR video](resources.md#r-ar-regression) (optional) · [Implementation reference](resources.md#r-sklearn)

### 6. Metrics for the task

**Learn:** Confusion matrix; precision/recall; F1; MAE; ranking is a later task.

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Official documentation / tutorial:** [Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html). Consult the Confusion matrix; precision/recall; F1; MAE; ranking is a later task sections/examples only. Do not read the entire documentation site.

**Practice:** Choose metrics for an imbalanced classifier and explain an error-cost tradeoff.

**Completion check:** Explain the confusion matrix and why the chosen metric fits error costs.

[Alternative · AR video](resources.md#r-ar-classification) (optional)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L02-E1:** Calculate dot products, norms, and cosine for [1,0] and [0,1]; implement zero-vector handling and explain matrix shapes.
  - **Pass:** Check orthogonal-vector similarity, identical-vector similarity, and the zero-vector policy.
- [ ] **L02-E2:** Build a confusion matrix from eight predictions and calculate precision, recall, and F1.
  - **Pass:** Show denominators and handling of undefined cases; explain what each metric misses.
- [ ] **L02-E3:** Train a small logistic regression or decision tree on public toy or synthetic data; compare a majority baseline.
  - **Pass:** Fit preprocessing only on training data; save split, seed, and metrics.
- [ ] **L02-E4:** Create an intentionally leaky experiment, then repair it.
  - **Pass:** Identify the leaked information and reproduce both configurations; no target score is required.
- [ ] **L02-E5:** Explain a small loss curve, gradient descent, overfitting, and regularization.
  - **Pass:** Describe the direction of an update and the difference between training and generalization.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S2](../project/milestones/s2.md). Compute simple similarity and classification metrics, explain train/validation/test, and reproduce the ML experiment without leaking test information.

**Keep:** math-notes.md and a small reproducible ML script or notebook; Leakage comparison with data source or generation seed.

## What to defer

- A full Data Science specialization
- Advanced proofs or prolonged competition tuning

## Record progress and choose the next Level

```bash
python scripts/progress.py set L02 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

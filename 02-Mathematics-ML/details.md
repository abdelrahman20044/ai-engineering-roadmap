# Technical Details · L02

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Math baseline:** Manipulate arrays and explain a mean, probability and function slope.
- **Python prerequisite:** Write functions and load a small tabular dataset.
- **Application link:** Explain why retrieval similarity and predictive confidence are different.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Vectors and matrix intuition:** Shapes; dot product; norms; cosine; matrix multiplication.
- **Probability and uncertainty:** Conditional probability; expectation; noisy measurements; sample size.
- **Loss and gradient intuition:** Loss versus metric; slope; learning rate; optimization.
- **Preparation and split discipline:** Missing values; scaling; train/validation/test; grouped/temporal leakage.
- **ML families and baselines:** Regression; classification; clustering intuition; overfitting; regularization.
- **Metrics for the task:** Confusion matrix; precision/recall; F1; MAE; ranking is a later task.

## Common mistakes and debugging

### Leakage during preprocessing

Fit transforms only on training data and prove it in a pipeline.

### Accuracy on an imbalanced set

Compare to a trivial baseline and inspect precision/recall.

### Turning this into a long DS track

Stop after one correct baseline and a short explanation of uncertainty.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. What is data leakage?
2. Why normalize vectors?
3. Is cosine 0.8 an 80% probability?

<details>
<summary>Answer guide</summary>

**What is data leakage?**

Training or selection uses information unavailable at prediction time, including test-set preprocessing.

**Why normalize vectors?**

It changes similarity geometry; cosine compares direction after accounting for magnitude.

**Is cosine 0.8 an 80% probability?**

No. It is a geometric score, not a calibrated event probability.

</details>

## ITI provenance and industry extensions

- **N11:** Mathematical Foundations — official published module title.
- **N12:** Data Preparation & Feature Engineering — official published module title.
- **N13:** Machine Learning Fundamentals — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Calculate a two-vector cosine by hand and match NumPy within tolerance.
- [ ] Explain a conditional-probability example and report raw counts beside a rate.
- [ ] Take one manual gradient step on a scalar loss and show whether it improved.
- [ ] Fit preprocessing on train only; create a deliberately leaky comparison and explain it.
- [ ] Compare one simple classifier with a dummy baseline and describe train/test behavior.
- [ ] Choose metrics for an imbalanced classifier and explain an error-cost tradeoff.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

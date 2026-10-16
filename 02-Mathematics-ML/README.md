# L02 · Practical Mathematics, ML, and Data Preparation

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 16–24 h | 2/5 | P1 | [L00](../00-Orientation/README.md) |

**Unlocks:** [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Understand vectors, matrices, similarity, probability, loss, and gradients through small examples. Run an ML baseline with correct splits, preprocessing, and evaluation. Recognize leakage and distinguish a similarity score from a calibrated probability. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Math baseline | Manipulate arrays and explain a mean, probability and function slope. |
| Python prerequisite | Write functions and load a small tabular dataset. |
| Application link | Explain why retrieval similarity and predictive confidence are different. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Vectors and matrix intuition: Calculate a two-vector cosine by hand and match NumPy within tolerance.
- [ ] Probability and uncertainty: Explain a conditional-probability example and report raw counts beside a rate.
- [ ] Loss and gradient intuition: Take one manual gradient step on a scalar loss and show whether it improved.
- [ ] Preparation and split discipline: Fit preprocessing on train only; create a deliberately leaky comparison and explain it.
- [ ] ML families and baselines: Compare one simple classifier with a dummy baseline and describe train/test behavior.
- [ ] Metrics for the task: Choose metrics for an imbalanced classifier and explain an error-cost tradeoff.

## Recommended learning path

Selected Arabic regression/classification or visual math → scikit-learn split/pipeline lab. Keep the scope to foundations that explain AI-system decisions.

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
| **L02-T01 · Vectors and matrix intuition**<br>Shapes; dot product; norms; cosine; matrix multiplication | [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo) (AR video)<br>**Scope:** Regression math orientation; cosine/norm implementation uses the English/NumPy path. | [Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra) (EN video) | Calculate a two-vector cosine by hand and match NumPy within tolerance. |
| **L02-T02 · Probability and uncertainty**<br>Conditional probability; expectation; noisy measurements; sample size | [Art of Machine Learning · ML introduction](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Vf1RAHyBo4tRzT8lEavPhR) (AR video)<br>**Scope:** ML orientation; conditional-probability exercises use Google MLCC. | [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) (EN videos + interactive exercises) | Explain a conditional-probability example and report raw counts beside a rate. |
| **L02-T03 · Loss and gradient intuition**<br>Loss versus metric; slope; learning rate; optimization | [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo) (AR video) | [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) (EN videos + interactive exercises)<br>[Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) (EN video) | Take one manual gradient step on a scalar loss and show whether it improved. |
| **L02-T04 · Preparation and split discipline**<br>Missing values; scaling; train/validation/test; grouped/temporal leakage | [Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k) (AR video) | [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) (EN videos + interactive exercises) | Fit preprocessing on train only; create a deliberately leaky comparison and explain it. |
| **L02-T05 · ML families and baselines**<br>Regression; classification; clustering intuition; overfitting; regularization | [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo) (AR video)<br>[Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU) (AR video) | [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) (EN videos + interactive exercises) | Compare one simple classifier with a dummy baseline and describe train/test behavior. |
| **L02-T06 · Metrics for the task**<br>Confusion matrix; precision/recall; F1; MAE; ranking is a later task | [Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU) (AR video)<br>[Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k) (AR video) | [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) (EN videos + interactive exercises) | Choose metrics for an imbalanced classifier and explain an error-cost tradeoff. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L02-T01 | C3 pp.125–135, similarity context; books do not teach full linear algebra | [NumPy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html) (EN) |
| L02-T02 | C3 pp.114–117, evaluation uncertainty motivation | [Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) (EN)<br>[Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) (EN) |
| L02-T03 | G1 pp.9–22 and C2 pp.58–87 are orientation; use the lab for foundations | [Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) (EN) |
| L02-T04 | C8 pp.368–371 and 396–402, principles only | [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) (EN)<br>[Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) (EN) |
| L02-T05 | G1 pp.9–22; C2 pp.58–87 skim; full practical gap covered by scikit-learn | [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) (EN) |
| L02-T06 | C4 pp.160–178 links metric choice to product objectives | [Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N11 · Mathematical Foundations | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N12 · Data Preparation & Feature Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N13 · Machine Learning Fundamentals | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L02-E1 | Calculate dot products, norms, and cosine for [1,0] and [0,1]; implement zero-vector handling and explain matrix shapes. | Check orthogonal-vector similarity, identical-vector similarity, and the zero-vector policy. |
| L02-E2 | Build a confusion matrix from eight predictions and calculate precision, recall, and F1. | Show denominators and handling of undefined cases; explain what each metric misses. |
| L02-E3 | Train a small logistic regression or decision tree on public toy or synthetic data; compare a majority baseline. | Fit preprocessing only on training data; save split, seed, and metrics. |
| L02-E4 | Create an intentionally leaky experiment, then repair it. | Identify the leaked information and reproduce both configurations; no target score is required. |
| L02-E5 | Explain a small loss curve, gradient descent, overfitting, and regularization. | Describe the direction of an update and the difference between training and generalization. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Leakage during preprocessing | Fit transforms only on training data and prove it in a pipeline. |
| Accuracy on an imbalanced set | Compare to a trivial baseline and inspect precision/recall. |
| Turning this into a long DS track | Stop after one correct baseline and a short explanation of uncertainty. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What is data leakage?
2. Why normalize vectors?
3. Is cosine 0.8 an 80% probability?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Training or selection uses information unavailable at prediction time, including test-set preprocessing. |
| 2 | It changes similarity geometry; cosine compares direction after accounting for magnitude. |
| 3 | No. It is a geometric score, not a calibrated event probability. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S2](../project/milestones/s2.md) | math-notes.md and a small reproducible ML script or notebook; Leakage comparison with data source or generation seed | Compute simple similarity and classification metrics, explain train/validation/test, and reproduce the ML experiment without leaking test information. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Compute simple similarity and classification metrics, explain train/validation/test, and reproduce the ML experiment without leaking test information.

## Postpone until justified

- A full Data Science specialization
- Advanced proofs or prolonged competition tuning

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L02 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L01](../01-Python-FastAPI/README.md) · Next numbered Level: [L03](../03-Deep-Learning-Foundation-Models/README.md)

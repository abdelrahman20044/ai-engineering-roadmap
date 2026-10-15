# L02 · Practical Mathematics, ML, and Data Preparation

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 16–24 h | 2/5 | P1 | [L00](../00-Orientation/README.md) |

**Outcome:** Understand vectors, matrices, similarity, probability, loss, and gradients through small examples. Run an ML baseline with correct splits, preprocessing, and evaluation. Recognize leakage and distinguish a similarity score from a calibrated probability.

**Unlocks:** [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Vectors, dot products, cosine similarity | C3 pp.125–135; [NumPy absolute beginners tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html) | [Practice 1](resources.md#practice-and-evidence) |
| Splits, preprocessing, leakage | C8 pp.368–371,396–402; [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | [Practice 2](resources.md#practice-and-evidence) |
| Regression, classification, metrics | G1 pp.9–22; C2 pp.58–87; [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | [Practice 3](resources.md#practice-and-evidence) |
| Probability and uncertainty | C3 pp.114–117; [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N11** — Mathematical Foundations.
- **N12** — Data Preparation & Feature Engineering.
- **N13** — Machine Learning Fundamentals.

| ITI topic IDs | Interpretation |
| --- | --- |
| N11, N12, N13 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L02-E1 | Calculate dot products, norms, and cosine for [1,0] and [0,1]; implement zero-vector handling and explain matrix shapes. | Check orthogonal-vector similarity, identical-vector similarity, and the zero-vector policy. |
| L02-E2 | Build a confusion matrix from eight predictions and calculate precision, recall, and F1. | Show denominators and handling of undefined cases; explain what each metric misses. |
| L02-E3 | Train a small logistic regression or decision tree on public toy or synthetic data; compare a majority baseline. | Fit preprocessing only on training data; save split, seed, and metrics. |
| L02-E4 | Create an intentionally leaky experiment, then repair it. | Identify the leaked information and reproduce both configurations; no target score is required. |
| L02-E5 | Explain a small loss curve, gradient descent, overfitting, and regularization. | Describe the direction of an update and the difference between training and generalization. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S2](../project/milestones/s2.md) | math-notes.md and a small reproducible ML script or notebook; Leakage comparison with data source or generation seed | Compute simple similarity and classification metrics, explain train/validation/test, and reproduce the ML experiment without leaking test information. |

## Postpone

| Outside this level |
| --- |
| A full Data Science specialization |
| Advanced proofs or prolonged competition tuning |

## Record completion

```bash
python scripts/progress.py set L02 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L01](../01-Python-FastAPI/README.md) · Next numbered Level: [L03](../03-Deep-Learning-Foundation-Models/README.md). Follow the prerequisite table if branches differ.

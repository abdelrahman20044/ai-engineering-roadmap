# M02 — Practical Mathematics, ML, and Data Preparation

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M00](../m00-orientation/README.md) |
| Personal effort | 16–24 focused hours; not official ITI hours |
| Project milestone | [S2](../../project/milestones/s2.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Understand vectors, matrices, similarity, probability, loss, and gradients through small examples. |
| O2 | Run an ML baseline with correct splits, preprocessing, and evaluation. |
| O3 | Recognize leakage and distinguish a similarity score from a calibrated probability. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N11 | Mathematical Foundations | 24 |
| N12 | Data Preparation & Feature Engineering | 12 |
| N13 | Machine Learning Fundamentals | 24 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | G1, printed pp. 9–22, and C2 pp. 58–87: conceptual orientation, not a complete ML curriculum. |
| 2 | C3 pp. 125–135: functional correctness, similarity, and embeddings. |
| 3 | C8 pp. 368–371 and 396–402: quality and processing principles. |
| 4 | Required gap resource: scikit-learn Common Pitfalls; consult split, preprocessing, and metric documentation for the lab. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M02-E1 | Calculate dot products, norms, and cosine for [1,0] and [0,1]; implement zero-vector handling and explain matrix shapes. | Check orthogonal-vector similarity, identical-vector similarity, and the zero-vector policy. |
| M02-E2 | Build a confusion matrix from eight predictions and calculate precision, recall, and F1. | Show denominators and handling of undefined cases; explain what each metric misses. |
| M02-E3 | Train a small logistic regression or decision tree on public toy or synthetic data; compare a majority baseline. | Fit preprocessing only on training data; save split, seed, and metrics. |
| M02-E4 | Create an intentionally leaky experiment, then repair it. | Identify the leaked information and reproduce both configurations; no target score is required. |
| M02-E5 | Explain a small loss curve, gradient descent, overfitting, and regularization. | Describe the direction of an update and the difference between training and generalization. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | math-notes.md and a small reproducible ML script or notebook; Leakage comparison with data source or generation seed |
| Pass condition | Compute simple similarity and classification metrics, explain train/validation/test, and reproduce the ML experiment without leaking test information. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M02 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| A full Data Science specialization |
| Advanced proofs or prolonged competition tuning |

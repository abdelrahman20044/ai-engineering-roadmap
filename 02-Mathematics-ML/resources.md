# Resources · L02 — Practical Mathematics, ML, and Data Preparation

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | G1, printed pp.9–22, and C2 pp.58–87: conceptual orientation, not a complete ML curriculum. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C3 pp.125–135: functional correctness, similarity, and embeddings. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | C8 pp.368–371 and 396–402: quality and processing principles. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 4 | Required gap resource: scikit-learn Common Pitfalls; consult split, preprocessing, and metric documentation for the lab. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Vectors, dot products, cosine similarity | [NumPy absolute beginners tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html) | Official tutorial / reference · free | Compute cosine similarity by hand and with NumPy. |
| Splits, preprocessing, leakage | [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Official tutorial / reference · free | Fit preprocessing on training data only. |
| Regression, classification, metrics | [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Official tutorial / reference · free | Compare a baseline classifier with a simple trained model. |
| Probability and uncertainty | [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Official tutorial / reference · free | Explain conditional probability and why a small test set is noisy. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Compute cosine similarity by hand and with NumPy. | Code/test or short measured comparison; explain the result independently. |
| 2 | Fit preprocessing on training data only. | Code/test or short measured comparison; explain the result independently. |
| 3 | Compare a baseline classifier with a simple trained model. | Code/test or short measured comparison; explain the result independently. |
| 4 | Explain conditional probability and why a small test set is noisy. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

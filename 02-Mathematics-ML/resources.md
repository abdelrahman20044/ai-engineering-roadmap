# Resource Library · L02 — Practical Mathematics, ML, and Data Preparation

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Selected Arabic regression/classification or visual math → scikit-learn split/pipeline lab. Keep the scope to foundations that explain AI-system decisions.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo) | Hesham Asem · Egypt<br>AR video<br>Free | L02-T01 · Vectors and matrix intuition; L02-T03 · Loss and gradient intuition; L02-T05 · ML families and baselines | Regression intuition, fitting and errors. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |
| [Art of Machine Learning · ML introduction](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Vf1RAHyBo4tRzT8lEavPhR) | Hesham Asem · Egypt<br>AR video<br>Free | L02-T02 · Probability and uncertainty | Supervised versus unsupervised learning and the prediction problem. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |
| [Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k) | Hesham Asem · Egypt<br>AR video<br>Free | L02-T04 · Preparation and split discipline; L02-T06 · Metrics for the task | Practical model fitting and metrics; update older APIs. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |
| [Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU) | Hesham Asem · Egypt<br>AR video<br>Free | L02-T05 · ML families and baselines; L02-T06 · Metrics for the task | Classification and decision boundaries. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra) | Grant Sanderson · 3Blue1Brown<br>EN video<br>Free | L02-T01 · Vectors and matrix intuition | Vectors, dot products and linear transformations: visualize embedding geometry. **Boundary:** Eigenvalue proofs are optional for this roadmap. |
| [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) | Google for Developers<br>EN videos + interactive exercises<br>Free | L02-T02 · Probability and uncertainty; L02-T03 · Loss and gradient intuition; L02-T04 · Preparation and split discipline; L02-T05 · ML families and baselines; L02-T06 · Metrics for the task | Select regression, classification, numerical data, overfitting and probability checks. **Boundary:** Short topic modules only; does not add a Data Science specialization. |
| [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) | Grant Sanderson · 3Blue1Brown<br>EN video<br>Free | L02-T03 · Loss and gradient intuition | Neural-network and backpropagation intuition; select transformer/attention explanations when ready. **Boundary:** Pair visualization with the tiny PyTorch lab. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Instructor course index](https://github.com/HeshamAsem/Course/blob/master/0.md) | Hesham Asem<br>AR<br>Free | Optional support for this Level’s assessed exercises | Source for the named Arabic ML playlists and lecture material. **Boundary:** Use selected sections only. |

## 4 · Paid alternatives

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) | DeepLearning.AI · Stanford Online · Andrew Ng<br>EN video + labs<br>Paid assessment/subscription; preview and aid availability vary | Optional support for this Level’s assessed exercises | Optional structured regression, classification, overfitting and learning fundamentals. **Boundary:** Much broader than L02; select only the foundation gap rather than completing it before building. |

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| G1, printed pp.9–22, and C2 pp.58–87: conceptual orientation, not a complete ML curriculum. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C3 pp.125–135: functional correctness, similarity, and embeddings. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C8 pp.368–371 and 396–402: quality and processing principles. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| Required gap resource: scikit-learn Common Pitfalls; consult split, preprocessing, and metric documentation for the lab. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [PostgreSQL Exercises](https://pgexercises.com/) | PGExercises<br>EN interactive exercises<br>Free | Optional support for this Level’s assessed exercises | Selected joins, aggregation and window exercises for SQL diagnostics. **Boundary:** Prior SQL knowledge means a short diagnostic, not a full SQL track. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L02-T01 | Calculate a two-vector cosine by hand and match NumPy within tolerance. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L02-T02 | Explain a conditional-probability example and report raw counts beside a rate. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L02-T03 | Take one manual gradient step on a scalar loss and show whether it improved. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L02-T04 | Fit preprocessing on train only; create a deliberately leaky comparison and explain it. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L02-T05 | Compare one simple classifier with a dummy baseline and describe train/test behavior. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L02-T06 | Choose metrics for an imbalanced classifier and explain an error-cost tradeoff. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [NumPy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html) | NumPy<br>EN<br>Free | L02-T01 · Vectors and matrix intuition | Arrays, shapes, indexing and vectorized arithmetic. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) | scikit-learn<br>EN<br>Free | L02-T02 · Probability and uncertainty; L02-T06 · Metrics for the task | Metric choice and interpretation; not retrieval ranking formulas. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) | scikit-learn<br>EN<br>Free | L02-T02 · Probability and uncertainty; L02-T04 · Preparation and split discipline | Train/test split and repeated evaluation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | PyTorch<br>EN<br>Free | L02-T03 · Loss and gradient intuition | Loss, optimizer, training and evaluation loops. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | scikit-learn<br>EN<br>Free | L02-T04 · Preparation and split discipline; L02-T05 · ML families and baselines | Splitting, preprocessing and leakage prevention. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

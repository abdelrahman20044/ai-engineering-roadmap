# Resource Library · L02 — Practical Mathematics, ML, and Data Preparation

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

## Topic navigation

1. [Vectors and matrix intuition](#unit-01)
2. [Probability and uncertainty](#unit-02)
3. [Loss and gradient intuition](#unit-03)
4. [Preparation and split discipline](#unit-04)
5. [ML families and baselines](#unit-05)
6. [Metrics for the task](#unit-06)

<a id="unit-01"></a>

## 1. Vectors and matrix intuition

[Return to README Step 1](README.md#1-vectors-and-matrix-intuition)

**Topic/subtopics:** Shapes; dot product; norms; cosine; matrix multiplication.

**Required sequence (default route):** `numpy`. Stop each source at the stated portion.

**Choose ONE explanation for vector/dot-product intuition:** default `numpy` **OR** `linear`. The NumPy array/similarity exercise still needs the NumPy reference. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-vectors-and-matrix-intuition) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `numpy` · [NumPy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html)<br>NumPy · EN | Documentation / tutorial | Primary | Arrays, shapes, indexing and vectorized arithmetic. | Consult the Shapes; dot product; norms; cosine; matrix multiplication… [bounds](#unit-01-numpy) |
| `ar-regression` · [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Regression intuition, fitting and errors. | Topic bounds; lesson IDs not verified — [details](#unit-01-ar-regression) |
| `linear` · [Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra)<br>Grant Sanderson · 3Blue1Brown · EN video | Video series / lesson collection | Alternative | Vectors, dot products and linear transformations:… | Vectors, linear combinations and dot-products lesson; use the direct… [bounds](#unit-01-linear) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-numpy"></a>

**`numpy` — selected portion:** Consult the Shapes; dot product; norms; cosine; matrix multiplication sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-regression"></a>

**`ar-regression` — selected portion:** Only Regression intuition, fitting and errors. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Regression math orientation; cosine/norm implementation uses the English/NumPy path.

<a id="unit-01-linear"></a>

**`linear` — selected portion:** Vectors, linear combinations and dot-products lesson; use the direct dot-product link in source notes for the similarity experiment.

**Relationship:** Substitute only for vector/dot-product intuition. The NumPy array/similarity exercise still needs the NumPy reference.

</details>

<a id="unit-02"></a>

## 2. Probability and uncertainty

[Return to README Step 2](README.md#2-probability-and-uncertainty)

**Topic/subtopics:** Conditional probability; expectation; noisy measurements; sample size.

**Required sequence:** `google-ml`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `metrics`, `split`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-probability-and-uncertainty) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `google-ml` · [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)<br>Google for Developers · EN videos + interactive exercises | Modular course: videos + interactive exercises | Primary | Select regression, classification, numerical data,… | Logistic Regression probability interpretation and its Check Your Understanding exercise only. |
| `ar-ml` · [Art of Machine Learning · ML introduction](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Vf1RAHyBo4tRzT8lEavPhR)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Supervised versus unsupervised learning and the prediction… | Topic bounds; lesson IDs not verified — [details](#unit-02-ar-ml) |
| `metrics` · [Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)<br>scikit-learn · EN | Documentation / tutorial | Reference | Metric choice and interpretation; not retrieval ranking… | Consult the relevant example for Metric choice and interpretation; not… [bounds](#unit-02-metrics) |
| `split` · [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)<br>scikit-learn · EN | Documentation / tutorial | Reference | Train/test split and repeated evaluation. | Consult the relevant example for Train/test split and repeated evaluation.… [bounds](#unit-02-split) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-google-ml"></a>

**`google-ml` — selected portion:** Logistic Regression probability interpretation and its Check Your Understanding exercise only.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-ml"></a>

**`ar-ml` — selected portion:** Only Supervised versus unsupervised learning and the prediction problem. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: ML orientation; conditional-probability exercises use Google MLCC.

<a id="unit-02-metrics"></a>

**`metrics` — selected portion:** Consult the relevant example for Metric choice and interpretation; not retrieval ranking formulas. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-02-split"></a>

**`split` — selected portion:** Consult the relevant example for Train/test split and repeated evaluation. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Loss and gradient intuition

[Return to README Step 3](README.md#3-loss-and-gradient-intuition)

**Topic/subtopics:** Loss versus metric; slope; learning rate; optimization.

**Required sequence:** `google-ml`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `optimize`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-loss-and-gradient-intuition) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `google-ml` · [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)<br>Google for Developers · EN videos + interactive exercises | Modular course: videos + interactive exercises | Primary | Select regression, classification, numerical data,… | Linear Regression: loss and gradient-descent sections only. |
| `ar-regression` · [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Regression intuition, fitting and errors. | Topic bounds; lesson IDs not verified — [details](#unit-03-ar-regression) |
| `nn-visual` · [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks)<br>Grant Sanderson · 3Blue1Brown · EN video | Video series / lesson collection | Complementary (as needed) | Neural-network and backpropagation intuition; select… | Neural-network overview, gradient descent or backpropagation lesson… [bounds](#unit-03-nn-visual) |
| `optimize` · [Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)<br>PyTorch · EN | Documentation / tutorial | Reference | Loss, optimizer, training and evaluation loops. | Consult the relevant example for Loss, optimizer, training and evaluation… [bounds](#unit-03-optimize) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-google-ml"></a>

**`google-ml` — selected portion:** Linear Regression: loss and gradient-descent sections only.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-regression"></a>

**`ar-regression` — selected portion:** Only Regression intuition, fitting and errors. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-nn-visual"></a>

**`nn-visual` — selected portion:** Neural-network overview, gradient descent or backpropagation lesson matching this group; direct lesson links are in source notes.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-optimize"></a>

**`optimize` — selected portion:** Consult the relevant example for Loss, optimizer, training and evaluation loops. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Preparation and split discipline

[Return to README Step 4](README.md#4-preparation-and-split-discipline)

**Topic/subtopics:** Missing values; scaling; train/validation/test; grouped/temporal leakage.

**Required sequence:** the assigned book slice [B07 · C8](../docs/READING_GUIDE.md#b07) **THEN** `sklearn`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `split`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-preparation-and-split-discipline) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B07 · C8](../docs/READING_GUIDE.md#b07)<br>Chip Huyen · EN | Book Section | Complementary | Preparation and split discipline | [Skim: exact assigned slice](../docs/READING_GUIDE.md#b07) |
| `sklearn` · [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)<br>scikit-learn · EN | Documentation / tutorial | Primary | Splitting, preprocessing and leakage prevention. | Consult the Missing values; scaling; train/validation/test;… [bounds](#unit-04-sklearn) |
| `ar-sklearn` · [Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Practical model fitting and metrics; update older APIs. | Topic bounds; lesson IDs not verified — [details](#unit-04-ar-sklearn) |
| `google-ml` · [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)<br>Google for Developers · EN videos + interactive exercises | Modular course: videos + interactive exercises | Complementary (as needed) | Select regression, classification, numerical data,… | Working with Numerical Data and Datasets/Overfitting; preprocessing and leakage checks. |
| `split` · [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)<br>scikit-learn · EN | Documentation / tutorial | Reference | Train/test split and repeated evaluation. | Consult the relevant example for Train/test split and repeated evaluation.… [bounds](#unit-04-split) |
| `pg-exercises` · [PostgreSQL Exercises](https://pgexercises.com/)<br>PGExercises · EN interactive exercises | Interactive SQL practice platform | Complementary (as needed) | Selected joins, aggregation and window exercises for SQL… | Selected joins/aggregation/window exercises only for a demonstrated SQL… [bounds](#unit-04-pg-exercises) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-sklearn"></a>

**`sklearn` — selected portion:** Consult the Missing values; scaling; train/validation/test; grouped/temporal leakage sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-sklearn"></a>

**`ar-sklearn` — selected portion:** Only Practical model fitting and metrics; update older APIs. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-google-ml"></a>

**`google-ml` — selected portion:** Working with Numerical Data and Datasets/Overfitting; preprocessing and leakage checks.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-split"></a>

**`split` — selected portion:** Consult the relevant example for Train/test split and repeated evaluation. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-04-pg-exercises"></a>

**`pg-exercises` — selected portion:** Selected joins/aggregation/window exercises only for a demonstrated SQL gap; no full SQL restart.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-05"></a>

## 5. ML families and baselines

[Return to README Step 5](README.md#5-ml-families-and-baselines)

**Topic/subtopics:** Regression; classification; clustering intuition; overfitting; regularization.

**Required sequence:** `google-ml`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `sklearn`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-ml-families-and-baselines) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `google-ml` · [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)<br>Google for Developers · EN videos + interactive exercises | Modular course: videos + interactive exercises | Primary | Select regression, classification, numerical data,… | Regression/classification overview plus Datasets/Overfitting sections… [bounds](#unit-05-google-ml) |
| `ar-regression` · [Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Regression intuition, fitting and errors. | Topic bounds; lesson IDs not verified — [details](#unit-05-ar-regression) |
| `ar-classification` · [Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Classification and decision boundaries. | Topic bounds; lesson IDs not verified — [details](#unit-05-ar-classification) |
| `sklearn` · [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)<br>scikit-learn · EN | Documentation / tutorial | Reference | Splitting, preprocessing and leakage prevention. | Consult the relevant example for Splitting, preprocessing and leakage… [bounds](#unit-05-sklearn) |
| `ng-ml` · [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)<br>DeepLearning.AI · Stanford Online · Andrew Ng · EN video + labs | Paid multi-course specialization | Optional Advanced | Optional structured regression, classification,… | Topic bounds; lesson IDs not verified — [details](#unit-05-ng-ml) |
| `hesham-index` · [Instructor course index](https://github.com/HeshamAsem/Course/blob/master/0.md)<br>Hesham Asem · AR | Instructor playlist index | Optional Advanced | Source for the named Arabic ML playlists and lecture… | Consult the relevant example for Source for the named Arabic ML playlists… [bounds](#unit-05-hesham-index) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-google-ml"></a>

**`google-ml` — selected portion:** Regression/classification overview plus Datasets/Overfitting sections needed for the baseline; no entire-course replay.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-regression"></a>

**`ar-regression` — selected portion:** Only Regression intuition, fitting and errors. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-ar-classification"></a>

**`ar-classification` — selected portion:** Only Classification and decision boundaries. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-sklearn"></a>

**`sklearn` — selected portion:** Consult the relevant example for Splitting, preprocessing and leakage prevention. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-ng-ml"></a>

**`ng-ml` — selected portion:** Optional purchase only: use the topic-specific regression/classification units for a demonstrated gap. Individual current lesson IDs/access not verified; no whole-course requirement.

**Relationship:** Optional depth/purchase; does not block the completion gate.

<a id="unit-05-hesham-index"></a>

**`hesham-index` — selected portion:** Consult the relevant example for Source for the named Arabic ML playlists and lecture material. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-06"></a>

## 6. Metrics for the task

[Return to README Step 6](README.md#6-metrics-for-the-task)

**Topic/subtopics:** Confusion matrix; precision/recall; F1; MAE; ranking is a later task.

**Required sequence (default route):** `metrics`. Stop each source at the stated portion.

**Choose ONE explanation for classification metric intuition:** default `metrics` **OR** `google-ml`. Use the metric API reference for your implementation in either route. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-metrics-for-the-task) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `metrics` · [Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)<br>scikit-learn · EN | Documentation / tutorial | Primary | Metric choice and interpretation; not retrieval ranking… | Consult the Confusion matrix; precision/recall; F1; MAE; ranking is a… [bounds](#unit-06-metrics) |
| `ar-classification` · [Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Classification and decision boundaries. | Topic bounds; lesson IDs not verified — [details](#unit-06-ar-classification) |
| `ar-sklearn` · [Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Practical model fitting and metrics; update older APIs. | Topic bounds; lesson IDs not verified — [details](#unit-06-ar-sklearn) |
| `google-ml` · [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)<br>Google for Developers · EN videos + interactive exercises | Modular course: videos + interactive exercises | Alternative | Select regression, classification, numerical data,… | Classification: Accuracy, recall, precision and related Check Your Understanding questions. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-metrics"></a>

**`metrics` — selected portion:** Consult the Confusion matrix; precision/recall; F1; MAE; ranking is a later task sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-classification"></a>

**`ar-classification` — selected portion:** Only Classification and decision boundaries. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-ar-sklearn"></a>

**`ar-sklearn` — selected portion:** Only Practical model fitting and metrics; update older APIs. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-google-ml"></a>

**`google-ml` — selected portion:** Classification: Accuracy, recall, precision and related Check Your Understanding questions.

**Relationship:** Substitute only for classification metric intuition. Use the metric API reference for your implementation in either route.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-regression"></a>

<details>
<summary>ar-regression · Art of Machine Learning · Regression — access, scope and verification</summary>

[Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo) · Hesham Asem · Egypt · AR video

- **Resource Type:** Playlist (YouTube).
- **Access:** Free.
- **Catalog scope:** Regression intuition, fitting and errors.
- **Scope/version limits:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Vectors and matrix intuition; Loss and gradient intuition; ML families and baselines.
- **Retained broad selection notes (lookup only):** Regression/loss intuition relevant to the baseline. Exact individual lesson numbers/timestamps not verified; use the English visual/MLCC route for precise subtopics.

</details>

<a id="r-linear"></a>

<details>
<summary>linear · Essence of linear algebra — access, scope and verification</summary>

[Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra) · Grant Sanderson · 3Blue1Brown · EN video

- **Resource Type:** Video series / lesson collection.
- **Access:** Free.
- **Catalog scope:** Vectors, dot products and linear transformations: visualize embedding geometry.
- **Scope/version limits:** Eigenvalue proofs are optional for this roadmap.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Vectors and matrix intuition.
- **Retained broad selection notes (lookup only):** Use “Vectors, what even are they?”, “Linear transformations and matrices” and “Dot products and duality” by title. No whole-series assignment; exact playback timestamps not assigned.

**Verified direct lessons:** [Dot products and duality](https://www.3blue1brown.com/lessons/dot-products/). Follow only the lesson for the selected concept.

</details>

<a id="r-numpy"></a>

<details>
<summary>numpy · NumPy beginners guide — access, scope and verification</summary>

[NumPy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html) · NumPy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Arrays, shapes, indexing and vectorized arithmetic.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Vectors and matrix intuition.
- **Retained broad selection notes (lookup only):** Consult the Shapes; dot product; norms; cosine; matrix multiplication sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-ml"></a>

<details>
<summary>ar-ml · Art of Machine Learning · ML introduction — access, scope and verification</summary>

[Art of Machine Learning · ML introduction](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Vf1RAHyBo4tRzT8lEavPhR) · Hesham Asem · Egypt · AR video

- **Resource Type:** Playlist (YouTube).
- **Access:** Free.
- **Catalog scope:** Supervised versus unsupervised learning and the prediction problem.
- **Scope/version limits:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Probability and uncertainty.
- **Retained broad selection notes (lookup only):** Introduction playlist only for ML-family vocabulary. Individual probability lessons were not verified; use MLCC for those exercises.

</details>

<a id="r-google-ml"></a>

<details>
<summary>google-ml · Machine Learning Crash Course — access, scope and verification</summary>

[Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) · Google for Developers · EN videos + interactive exercises

- **Resource Type:** Modular course: videos + interactive exercises.
- **Access:** Free.
- **Catalog scope:** Select regression, classification, numerical data, overfitting and probability checks.
- **Scope/version limits:** Short topic modules only; does not add a Data Science specialization.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Probability and uncertainty; Loss and gradient intuition; Preparation and split discipline; ML families and baselines; Metrics for the task.
- **Retained broad selection notes (lookup only):** Logistic Regression probability interpretation and its Check Your Understanding exercise only. Linear Regression: loss and gradient-descent sections only. Regression/classification overview plus Datasets/Overfitting sections needed for the baseline; no entire-course replay.

</details>

<a id="r-metrics"></a>

<details>
<summary>metrics · Classification and regression metrics — access, scope and verification</summary>

[Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) · scikit-learn · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Metric choice and interpretation; not retrieval ranking formulas.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Probability and uncertainty; Metrics for the task.
- **Retained broad selection notes (lookup only):** Consult the Confusion matrix; precision/recall; F1; MAE; ranking is a later task sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-split"></a>

<details>
<summary>split · Cross-validation — access, scope and verification</summary>

[Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) · scikit-learn · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Train/test split and repeated evaluation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Probability and uncertainty; Preparation and split discipline.
- **Retained broad selection notes (lookup only):** Consult the Conditional probability; expectation; noisy measurements; sample size sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-nn-visual"></a>

<details>
<summary>nn-visual · Neural networks visual series — access, scope and verification</summary>

[Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) · Grant Sanderson · 3Blue1Brown · EN video

- **Resource Type:** Video series / lesson collection.
- **Access:** Free.
- **Catalog scope:** Neural-network and backpropagation intuition; select transformer/attention explanations when ready.
- **Scope/version limits:** Pair visualization with the tiny PyTorch lab.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Loss and gradient intuition.
- **Retained broad selection notes (lookup only):** “Gradient descent, how neural networks learn” for loss/gradient intuition only.

**Verified direct lessons:** [What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation/) · [Gradient descent, how neural networks learn](https://www.3blue1brown.com/lessons/gradient-descent/) · [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention/). Follow only the lesson for the selected concept.

</details>

<a id="r-optimize"></a>

<details>
<summary>optimize · Optimization loop — access, scope and verification</summary>

[Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) · PyTorch · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Loss, optimizer, training and evaluation loops.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Loss and gradient intuition.
- **Retained broad selection notes (lookup only):** Consult the Loss versus metric; slope; learning rate; optimization sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-sklearn"></a>

<details>
<summary>ar-sklearn · Art of Machine Learning · scikit-learn — access, scope and verification</summary>

[Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k) · Hesham Asem · Egypt · AR video

- **Resource Type:** Playlist (YouTube).
- **Access:** Free.
- **Catalog scope:** Practical model fitting and metrics; update older APIs.
- **Scope/version limits:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Preparation and split discipline; Metrics for the task.
- **Retained broad selection notes (lookup only):** Only fit/predict/preprocessing/metrics relevant to the lab; exact video numbers not verified. Current scikit-learn docs take precedence.

</details>

<a id="r-sklearn"></a>

<details>
<summary>sklearn · Common ML pitfalls — access, scope and verification</summary>

[Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) · scikit-learn · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Splitting, preprocessing and leakage prevention.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Preparation and split discipline; ML families and baselines.
- **Retained broad selection notes (lookup only):** Consult the Missing values; scaling; train/validation/test; grouped/temporal leakage sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-classification"></a>

<details>
<summary>ar-classification · Art of Machine Learning · Classification — access, scope and verification</summary>

[Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU) · Hesham Asem · Egypt · AR video

- **Resource Type:** Playlist (YouTube).
- **Access:** Free.
- **Catalog scope:** Classification and decision boundaries.
- **Scope/version limits:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** ML families and baselines; Metrics for the task.
- **Retained broad selection notes (lookup only):** Classification/decision-boundary intuition and the metrics you use. Individual lesson numbers not verified; do not complete the entire playlist by default.

</details>

<a id="r-ng-ml"></a>

<details>
<summary>ng-ml · Machine Learning Specialization — access, scope and verification</summary>

[Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) · DeepLearning.AI · Stanford Online · Andrew Ng · EN video + labs

- **Resource Type:** Paid multi-course specialization.
- **Access:** Paid assessment/subscription; preview and aid availability vary.
- **Catalog scope:** Optional structured regression, classification, overfitting and learning fundamentals.
- **Scope/version limits:** Much broader than L02; select only the foundation gap rather than completing it before building.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Optional remediation: supervised-learning regression/classification and overfitting units. Exact current lesson IDs were not verified; no entire-specialization requirement.

</details>

<a id="r-hesham-index"></a>

<details>
<summary>hesham-index · Instructor course index — access, scope and verification</summary>

[Instructor course index](https://github.com/HeshamAsem/Course/blob/master/0.md) · Hesham Asem · AR

- **Resource Type:** Instructor playlist index.
- **Access:** Free.
- **Catalog scope:** Source for the named Arabic ML playlists and lecture material.
- **Scope/version limits:** Use selected sections only.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Source for the named Arabic ML playlists and lecture material. Optional lookup; implement only the portion that addresses the named gap.

</details>

<a id="r-pg-exercises"></a>

<details>
<summary>pg-exercises · PostgreSQL Exercises — access, scope and verification</summary>

[PostgreSQL Exercises](https://pgexercises.com/) · PGExercises · EN interactive exercises

- **Resource Type:** Interactive SQL practice platform.
- **Access:** Free.
- **Catalog scope:** Selected joins, aggregation and window exercises for SQL diagnostics.
- **Scope/version limits:** Prior SQL knowledge means a short diagnostic, not a full SQL track.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** A short join/aggregate/window diagnostic, then stop when the relevant query works. No complete SQL track.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

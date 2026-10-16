# Resource Library · L02 — Practical Mathematics, ML, and Data Preparation

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

## Book references

Assigned reading is authoritative in [the master order for L02](../docs/READING_GUIDE.md#l02). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B07 · C8](../docs/READING_GUIDE.md#b07).

## Arabic and Egyptian teaching

<a id="r-ar-regression"></a>

### Art of Machine Learning · Regression

[Art of Machine Learning · Regression](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo)

- **Resource Type:** YouTube playlist.
- **Role:** Alternative. **Language:** AR video. **By:** Hesham Asem · Egypt.
- **Access:** Free.
- **Use for:** Vectors and matrix intuition; Loss and gradient intuition; ML families and baselines.
- **Assigned portion:** Regression/loss intuition relevant to the baseline. Exact individual lesson numbers/timestamps not verified; use the English visual/MLCC route for precise subtopics.
- **Scope:** Regression intuition, fitting and errors.
- **Limit:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.

**Arabic scope note:** Regression math orientation; cosine/norm implementation uses the English/NumPy path.

<a id="r-ar-ml"></a>

### Art of Machine Learning · ML introduction

[Art of Machine Learning · ML introduction](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Vf1RAHyBo4tRzT8lEavPhR)

- **Resource Type:** YouTube playlist.
- **Role:** Alternative. **Language:** AR video. **By:** Hesham Asem · Egypt.
- **Access:** Free.
- **Use for:** Probability and uncertainty.
- **Assigned portion:** Introduction playlist only for ML-family vocabulary. Individual probability lessons were not verified; use MLCC for those exercises.
- **Scope:** Supervised versus unsupervised learning and the prediction problem.
- **Limit:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.

**Arabic scope note:** ML orientation; conditional-probability exercises use Google MLCC.

<a id="r-ar-sklearn"></a>

### Art of Machine Learning · scikit-learn

[Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k)

- **Resource Type:** YouTube playlist.
- **Role:** Alternative. **Language:** AR video. **By:** Hesham Asem · Egypt.
- **Access:** Free.
- **Use for:** Preparation and split discipline; Metrics for the task.
- **Assigned portion:** Only fit/predict/preprocessing/metrics relevant to the lab; exact video numbers not verified. Current scikit-learn docs take precedence.
- **Scope:** Practical model fitting and metrics; update older APIs.
- **Limit:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.

<a id="r-ar-classification"></a>

### Art of Machine Learning · Classification

[Art of Machine Learning · Classification](https://www.youtube.com/playlist?list=PL6-3IRz2XF5Uq7PkI_PWOm_DLC2CFvSzU)

- **Resource Type:** YouTube playlist.
- **Role:** Alternative. **Language:** AR video. **By:** Hesham Asem · Egypt.
- **Access:** Free.
- **Use for:** ML families and baselines; Metrics for the task.
- **Assigned portion:** Classification/decision-boundary intuition and the metrics you use. Individual lesson numbers not verified; do not complete the entire playlist by default.
- **Scope:** Classification and decision boundaries.
- **Limit:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.

## English video and guided courses

<a id="r-linear"></a>

### Essence of linear algebra

[Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra)

- **Resource Type:** Video series / lesson collection.
- **Role:** Alternative. **Language:** EN video. **By:** Grant Sanderson · 3Blue1Brown.
- **Access:** Free.
- **Use for:** Vectors and matrix intuition.
- **Assigned portion:** Use “Vectors, what even are they?”, “Linear transformations and matrices” and “Dot products and duality” by title. No whole-series assignment; exact playback timestamps not assigned.
- **Scope:** Vectors, dot products and linear transformations: visualize embedding geometry.
- **Limit:** Eigenvalue proofs are optional for this roadmap.

**Direct lesson choices:** [Dot products and duality](https://www.3blue1brown.com/lessons/dot-products/). These are alternatives; follow only the chosen topic.

<a id="r-google-ml"></a>

### Machine Learning Crash Course

[Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)

- **Resource Type:** Modular course: videos + interactive exercises.
- **Role:** Primary. **Language:** EN videos + interactive exercises. **By:** Google for Developers.
- **Access:** Free.
- **Use for:** Probability and uncertainty; Loss and gradient intuition; Preparation and split discipline; ML families and baselines; Metrics for the task.
- **Assigned portion:** Logistic Regression probability interpretation and its Check Your Understanding exercise only. Linear Regression: loss and gradient-descent sections only. Regression/classification overview plus Datasets/Overfitting sections needed for the baseline; no entire-course replay.
- **Scope:** Select regression, classification, numerical data, overfitting and probability checks.
- **Limit:** Short topic modules only; does not add a Data Science specialization.

<a id="r-nn-visual"></a>

### Neural networks visual series

[Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks)

- **Resource Type:** Video series / lesson collection.
- **Role:** Alternative. **Language:** EN video. **By:** Grant Sanderson · 3Blue1Brown.
- **Access:** Free.
- **Use for:** Loss and gradient intuition.
- **Assigned portion:** “Gradient descent, how neural networks learn” for loss/gradient intuition only.
- **Scope:** Neural-network and backpropagation intuition; select transformer/attention explanations when ready.
- **Limit:** Pair visualization with the tiny PyTorch lab.

**Direct lesson choices:** [What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation/) · [Gradient descent, how neural networks learn](https://www.3blue1brown.com/lessons/gradient-descent/) · [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention/). These are alternatives; follow only the chosen topic.

## Slides, notebooks and repositories

<a id="r-hesham-index"></a>

### Instructor course index

[Instructor course index](https://github.com/HeshamAsem/Course/blob/master/0.md)

- **Resource Type:** Instructor playlist index.
- **Role:** Reference. **Language:** AR. **By:** Hesham Asem.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Source for the named Arabic ML playlists and lecture material. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Source for the named Arabic ML playlists and lecture material.
- **Limit:** Use selected sections only.

## Paid alternatives

<a id="r-ng-ml"></a>

### Machine Learning Specialization

[Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)

- **Resource Type:** Paid multi-course specialization.
- **Role:** Optional Advanced. **Language:** EN video + labs. **By:** DeepLearning.AI · Stanford Online · Andrew Ng.
- **Access:** Paid assessment/subscription; preview and aid availability vary.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Optional remediation: supervised-learning regression/classification and overfitting units. Exact current lesson IDs were not verified; no entire-specialization requirement.
- **Scope:** Optional structured regression, classification, overfitting and learning fundamentals.
- **Limit:** Much broader than L02; select only the foundation gap rather than completing it before building.

## Practice, labs and quizzes

<a id="r-pg-exercises"></a>

### PostgreSQL Exercises

[PostgreSQL Exercises](https://pgexercises.com/)

- **Resource Type:** Interactive SQL practice platform.
- **Role:** Alternative. **Language:** EN interactive exercises. **By:** PGExercises.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** A short join/aggregate/window diagnostic, then stop when the relevant query works. No complete SQL track.
- **Scope:** Selected joins, aggregation and window exercises for SQL diagnostics.
- **Limit:** Prior SQL knowledge means a short diagnostic, not a full SQL track.

## Official documentation and engineering articles

<a id="r-numpy"></a>

### NumPy beginners guide

[NumPy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** NumPy.
- **Access:** Free.
- **Use for:** Vectors and matrix intuition.
- **Assigned portion:** Consult the Shapes; dot product; norms; cosine; matrix multiplication sections/examples only. Do not read the entire documentation site.
- **Scope:** Arrays, shapes, indexing and vectorized arithmetic.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-metrics"></a>

### Classification and regression metrics

[Classification and regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** scikit-learn.
- **Access:** Free.
- **Use for:** Probability and uncertainty; Metrics for the task.
- **Assigned portion:** Consult the Confusion matrix; precision/recall; F1; MAE; ranking is a later task sections/examples only. Do not read the entire documentation site.
- **Scope:** Metric choice and interpretation; not retrieval ranking formulas.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-split"></a>

### Cross-validation

[Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** scikit-learn.
- **Access:** Free.
- **Use for:** Probability and uncertainty; Preparation and split discipline.
- **Assigned portion:** Consult the Conditional probability; expectation; noisy measurements; sample size sections/examples only. Do not read the entire documentation site.
- **Scope:** Train/test split and repeated evaluation.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-optimize"></a>

### Optimization loop

[Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** PyTorch.
- **Access:** Free.
- **Use for:** Loss and gradient intuition.
- **Assigned portion:** Consult the Loss versus metric; slope; learning rate; optimization sections/examples only. Do not read the entire documentation site.
- **Scope:** Loss, optimizer, training and evaluation loops.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-sklearn"></a>

### Common ML pitfalls

[Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** scikit-learn.
- **Access:** Free.
- **Use for:** Preparation and split discipline; ML families and baselines.
- **Assigned portion:** Consult the Missing values; scaling; train/validation/test; grouped/temporal leakage sections/examples only. Do not read the entire documentation site.
- **Scope:** Splitting, preprocessing and leakage prevention.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

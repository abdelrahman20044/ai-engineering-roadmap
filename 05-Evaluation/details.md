# Technical Details · L05

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Working endpoint:** Run the same request repeatedly and capture output/config.
- **Test separation:** Distinguish HTTP correctness from answer usefulness.
- **Dataset hygiene:** Keep development examples apart from release holdout.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Task criteria and failure taxonomy:** Correctness; groundedness; abstention; privacy; severity.
- **Evaluation dataset design:** Question strata; reference evidence; train/dev/holdout; versions.
- **Deterministic component checks:** JSON schema; source IDs; ownership; parser contracts; golden fixtures.
- **Human review and AI judges:** Rubric anchors; blind labels; disagreement; bias; judge prompts.
- **Retrieval versus answer metrics:** Recall@k; MRR; faithfulness; answer relevance; no-evidence behavior.
- **Regression gates and uncertainty:** Counts; confidence caveats; stochastic repeats; release decision.

## Common mistakes and debugging

### One combined RAG score

Measure retrieval, citations, generation and system behavior separately.

### Judge treated as ground truth

Compare human/judge disagreement and inspect bias and failure modes.

### Threshold invented after results

State intended thresholds before comparing candidates; report sample counts and uncertainty.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. What belongs in a holdout?
2. Why calibrate an AI judge?
3. What is an actionable eval failure?

<details>
<summary>Answer guide</summary>

**What belongs in a holdout?**

Cases not used to tune prompts, retrieval settings or model selection.

**Why calibrate an AI judge?**

A judge can favor style, verbosity or a model family and miss real task failures.

**What is an actionable eval failure?**

A labeled failure tied to a reproducible case and an identifiable component or product requirement.

</details>

## ITI provenance and industry extensions

- **N05:** Software Testing & Full-Stack Debugging — official published module title.
- **N20:** AI Evaluation, Safety & Responsible AI — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Write a rubric with anchored pass/fail examples and name five failure classes.
- [ ] Version development cases and a separate holdout with source labels.
- [ ] Add exact checks that catch a valid-looking answer with an invalid citation.
- [ ] Label a small sample twice and compare judge/human disagreements by category.
- [ ] Report retrieval and generation failures as separate tables.
- [ ] Run a fixed eval suite and retain model/prompt/corpus versions with the results.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

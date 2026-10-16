# Technical Details · L17

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Failure evidence:** Show a task failure that prompting, retrieval or model choice did not solve.
- **Training readiness:** Explain loss, optimizer, leakage and held-out evaluation.
- **Budget readiness:** Choose hardware/runtime and stop conditions before any training run.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Fine-tuning decision:** Prompt versus RAG versus model switch versus adaptation.
- **Dataset engineering:** Representative tasks; quality; deduplication; consent/license; split boundaries.
- **PEFT and SFT:** LoRA/adapters; target modules; data format; training config; checkpoints.
- **Holdout and regression evaluation:** Task improvement; general behavior; safety/grounding regressions.
- **Quantization and inference:** Precision; model memory; hardware; batching; throughput versus latency.
- **Model-serving boundary:** Separate runtime; adapter deployment; version rollback; lifecycle cost.

## Common mistakes and debugging

### Fine-tuning for changing factual documents

RAG may be a better mechanism; demonstrate the actual adaptation need.

### Train/eval near-duplicates

Split by source or task group and audit leakage.

### Quantization improves everything

Measure memory, speed and quality; hardware compatibility varies.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. When fine-tune?
2. What is LoRA?
3. What must compare?

<details>
<summary>Answer guide</summary>

**When fine-tune?**

When a stable task/behavior gap and sufficient representative data justify training and maintenance costs.

**What is LoRA?**

A parameter-efficient adaptation method using trainable low-rank updates instead of full-weight training.

**What must compare?**

The same independent task cases before/after tuning, including regressions, memory, latency and cost.

</details>

## ITI provenance and industry extensions

- **N12:** Data Preparation & Feature Engineering — official published module title.
- **N15:** MLOps Basics & Model Serving — official published module title.
- **N21:** Fine-Tuning & Model Customization — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Write a go/no-go ADR with the failure cases and cheaper alternatives already tested.
- [ ] Create a small data card, split-by-source policy and duplicate/leakage checks.
- [ ] Run one bounded small-model adapter experiment and save configuration and provenance.
- [ ] Compare tuned/untuned models on an independent set and report negative outcomes too.
- [ ] Benchmark memory/latency/quality before and after one compatible optimization.
- [ ] Serve the chosen artifact separately and prove a rollback to the baseline model.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

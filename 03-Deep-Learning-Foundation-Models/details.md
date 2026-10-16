# Technical Details · L03

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Math readiness (review L02 if needed):** Explain a loss, gradient, train/test split and vector shape.
- **Python readiness:** Use a small tensor/array and inspect dimensions.
- **System boundary:** Separate a web server process from a model-serving process.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Tensors and neural network structure:** Layers; activations; shapes; device; dtype.
- **Backpropagation and optimization:** Autograd; computational graph; gradients; train versus eval.
- **Language-model foundations:** Next-token prediction; pretraining; SFT; preference tuning.
- **Tokens, context and sampling:** Tokenizer; context limit; output length; temperature; top-p.
- **Attention and transformer intuition:** Queries/keys/values; attention weights; positional information.
- **Training versus model serving:** API provider; local server; model license; memory/latency budget.

## Common mistakes and debugging

### Skipping shapes

Print shape/dtype/device at each step and assert expected dimensions.

### Assuming sampling is fully deterministic

Record model/version/config and repeat outputs; temperature zero is not a universal reproducibility guarantee.

### Training before integration

Use a CPU toy model for understanding; integrate an existing model for the app.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. What does backpropagation compute?
2. Why do token counts differ in Arabic and English?
3. What is post-training versus inference?

<details>
<summary>Answer guide</summary>

**What does backpropagation compute?**

Derivatives of a loss with respect to parameters using the chain rule.

**Why do token counts differ in Arabic and English?**

The tokenizer vocabulary and segmentation differ; measure the actual model tokenizer.

**What is post-training versus inference?**

Post-training updates parameters or preferences; inference uses the selected parameters to produce outputs.

</details>

## ITI provenance and industry extensions

- **N14:** Deep Learning & Neural Networks — official published module title.
- **N15:** MLOps Basics & Model Serving — official published module title.
- **N16:** LLM Fundamentals & GenAI Landscape — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Run a small forward pass and assert each intermediate shape.
- [ ] Check a scalar derivative manually and train a small CPU network for a few steps.
- [ ] Explain where knowledge, instruction behavior and application context enter the system.
- [ ] Measure token counts for Arabic/English prompts and compare two sampling settings.
- [ ] Explain attention using a short sentence and trace tensor dimensions conceptually.
- [ ] Call one local or hosted inference endpoint behind an adapter and record the resource boundary.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

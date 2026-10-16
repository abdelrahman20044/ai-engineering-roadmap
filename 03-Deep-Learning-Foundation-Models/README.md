# L03 · Deep Learning, Foundation Models, and Serving

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 12–18 h | 3/5 | P0 | [L00](../00-Orientation/README.md) |

**Unlocks:** [L04](../04-LLM-Applications-Prompts/README.md), [L07](../07-Embeddings-Semantic-Search/README.md), [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Distinguish pretraining, supervised fine-tuning, preference tuning, and inference. Understand layers, autograd, attention, tokenization, sampling, and resource constraints. Choose an external provider or local inference endpoint with a reasoned boundary. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Math readiness (review L02 if needed) | Explain a loss, gradient, train/test split and vector shape. |
| Python readiness | Use a small tensor/array and inspect dimensions. |
| System boundary | Separate a web server process from a model-serving process. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Tensors and neural network structure: Run a small forward pass and assert each intermediate shape.
- [ ] Backpropagation and optimization: Check a scalar derivative manually and train a small CPU network for a few steps.
- [ ] Language-model foundations: Explain where knowledge, instruction behavior and application context enter the system.
- [ ] Tokens, context and sampling: Measure token counts for Arabic/English prompts and compare two sampling settings.
- [ ] Attention and transformer intuition: Explain attention using a short sentence and trace tensor dimensions conceptually.
- [ ] Training versus model serving: Call one local or hosted inference endpoint behind an adapter and record the resource boundary.

## Recommended learning path

G1 + C2 conceptual sections → visual attention/backpropagation → a tiny CPU PyTorch lab and one inference endpoint. Train no large model here.

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
| **L03-T01 · Tensors and neural network structure**<br>Layers; activations; shapes; device; dtype | [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) (AR video) | [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) (EN video) | Run a small forward pass and assert each intermediate shape. |
| **L03-T02 · Backpropagation and optimization**<br>Autograd; computational graph; gradients; train versus eval | [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) (AR video) | [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) (EN video + notebooks) | Check a scalar derivative manually and train a small CPU network for a few steps. |
| **L03-T03 · Language-model foundations**<br>Next-token prediction; pretraining; SFT; preference tuning | [Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md) (AR machine-translated text)<br>[Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) (AR video) | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Explain where knowledge, instruction behavior and application context enter the system. |
| **L03-T04 · Tokens, context and sampling**<br>Tokenizer; context limit; output length; temperature; top-p | [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) (AR machine-translated text) | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Measure token counts for Arabic/English prompts and compare two sampling settings. |
| **L03-T05 · Attention and transformer intuition**<br>Queries/keys/values; attention weights; positional information | [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) (AR video)<br>**Scope:** Neural-network prerequisites only; no verified Arabic attention lesson is assigned. | [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) (EN video)<br>[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) (EN video + notebooks) | Explain attention using a short sentence and trace tensor dimensions conceptually. |
| **L03-T06 · Training versus model serving**<br>API provider; local server; model license; memory/latency budget | [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) (AR video) | [LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/) (EN video + slides) | Call one local or hosted inference endpoint behind an adapter and record the resource boundary. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L03-T01 | G1 pp.1–22; C2 architecture, conceptual | [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) (EN) |
| L03-T02 | C2 conceptual foundations; tiny PyTorch lab supplies implementation depth | [Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) (EN)<br>[Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) (EN) |
| L03-T03 | C2 pp.49–87; skim architecture proofs | [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) (EN) |
| L03-T04 | C2 pp.88–105, read sampling carefully | [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) (EN)<br>[Ollama API introduction](https://docs.ollama.com/api/introduction) (EN) |
| L03-T05 | C2 architecture sections, conceptual; mathematical derivations optional | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) |
| L03-T06 | F3 PDF83–105 and 136–150; defer audio/video/3D examples | [Ollama API introduction](https://docs.ollama.com/api/introduction) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N14 · Deep Learning & Neural Networks | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N15 · MLOps Basics & Model Serving | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N16 · LLM Fundamentals & GenAI Landscape | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L03-E1 | Implement a tiny linear layer, loss, backward pass, and optimizer step in PyTorch. | Record tensor shapes, inspect gradients, and explain the update. Use L02 exercise E1 first if vectors are unfamiliar. |
| L03-E2 | Explore tokenization for representative inputs, optionally including Arabic and English. | Distinguish characters, tokens, context capacity, and embedding dimensions. |
| L03-E3 | Run five prompts using two sampling settings on one model. | Record settings and variation; low temperature is not treated as a determinism guarantee. |
| L03-E4 | Draw client → FastAPI → provider and compare external versus local serving. | Document timeouts, lifecycle, privacy/resource constraints, and actual hardware assumptions. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Skipping shapes | Print shape/dtype/device at each step and assert expected dimensions. |
| Assuming sampling is fully deterministic | Record model/version/config and repeat outputs; temperature zero is not a universal reproducibility guarantee. |
| Training before integration | Use a CPU toy model for understanding; integrate an existing model for the app. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What does backpropagation compute?
2. Why do token counts differ in Arabic and English?
3. What is post-training versus inference?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Derivatives of a loss with respect to parameters using the chain rule. |
| 2 | The tokenizer vocabulary and segmentation differ; measure the actual model tokenizer. |
| 3 | Post-training updates parameters or preferences; inference uses the selected parameters to produce outputs. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S2](../project/milestones/s2.md) | tiny-autograd.py and tokenization observations; Model selection card and serving ADR | Explain next-token prediction and attention conceptually, demonstrate the autograd lab, and run inference. L02 may proceed in parallel; completing all ML topics is not a prerequisite for the first model API call. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Explain next-token prediction and attention conceptually, demonstrate the autograd lab, and run inference. L02 may proceed in parallel; completing all ML topics is not a prerequisite for the first model API call.

## Postpone until justified

- Training a transformer from scratch
- Audio/video/3D serving and distributed GPU training

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L03 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L02](../02-Mathematics-ML/README.md) · Next numbered Level: [L04](../04-LLM-Applications-Prompts/README.md)

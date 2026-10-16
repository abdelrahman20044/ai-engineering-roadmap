# L17 · Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 6 · Optional Specialization and Supporting UI | 18–32 h | 4/5 | P3 · optional | [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md), [L05](../05-Evaluation/README.md), [L15](../15-Model-Selection-Optimization/README.md) |

**Unlocks:** No further required Level; use the evidence to apply or specialize.

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Choose between prompt changes, RAG, model selection, and fine-tuning using failure evidence. Understand SFT/LoRA, curation, quantization, and serving tradeoffs. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Failure evidence | Show a task failure that prompting, retrieval or model choice did not solve. |
| Training readiness | Explain loss, optimizer, leakage and held-out evaluation. |
| Budget readiness | Choose hardware/runtime and stop conditions before any training run. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Fine-tuning decision: Write a go/no-go ADR with the failure cases and cheaper alternatives already tested.
- [ ] Dataset engineering: Create a small data card, split-by-source policy and duplicate/leakage checks.
- [ ] PEFT and SFT: Run one bounded small-model adapter experiment and save configuration and provenance.
- [ ] Holdout and regression evaluation: Compare tuned/untuned models on an independent set and report negative outcomes too.
- [ ] Quantization and inference: Benchmark memory/latency/quality before and after one compatible optimization.
- [ ] Model-serving boundary: Serve the chosen artifact separately and prove a rollback to the baseline model.

## Recommended learning path

Optional: C7 go/no-go → curated train/dev/holdout data → one small LoRA experiment → compare to baseline → serve only if justified.

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
| **L17-T01 · Fine-tuning decision**<br>Prompt versus RAG versus model switch versus adaptation | [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md) (AR machine-translated text) | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Write a go/no-go ADR with the failure cases and cheaper alternatives already tested. |
| **L17-T02 · Dataset engineering**<br>Representative tasks; quality; deduplication; consent/license; split boundaries | [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md) (AR machine-translated text)<br>[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Create a small data card, split-by-source policy and duplicate/leakage checks. |
| **L17-T03 · PEFT and SFT**<br>LoRA/adapters; target modules; data format; training config; checkpoints | [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md) (AR machine-translated text) | [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) (EN video + notebooks) | Run one bounded small-model adapter experiment and save configuration and provenance. |
| **L17-T04 · Holdout and regression evaluation**<br>Task improvement; general behavior; safety/grounding regressions | **Arabic gap:** no directly matching resource verified; use the English route. | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) | Compare tuned/untuned models on an independent set and report negative outcomes too. |
| **L17-T05 · Quantization and inference**<br>Precision; model memory; hardware; batching; throughput versus latency | [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) (AR video)<br>**Scope:** Local serving context only; quantization and batching need current English serving docs. | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Benchmark memory/latency/quality before and after one compatible optimization. |
| **L17-T06 · Model-serving boundary**<br>Separate runtime; adapter deployment; version rollback; lifecycle cost | [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) (AR video)<br>[mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) (AR video)<br>**Scope:** Serving/deployment context; tuned-artifact deployment uses current serving documentation. | [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) (EN) | Serve the chosen artifact separately and prove a rollback to the baseline model. |

**Arabic coverage boundary:** Arabic translated fine-tuning material supplies concepts. No complete Arabic course on the specific PEFT/SFT/versioned-serving workflow was verified; current Hugging Face/vLLM resources are primary for the experiment.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L17-T01 | C7 pp.311–318 first | [PEFT quicktour](https://huggingface.co/docs/peft/quicktour) (EN) |
| L17-T02 | C8 curation/processing selectively | [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) (EN) |
| L17-T03 | C7 selected tactics; C8 data preparation | [PEFT quicktour](https://huggingface.co/docs/peft/quicktour) (EN)<br>[TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) (EN) |
| L17-T04 | C3/C4 evaluation applied; do not tune on holdout | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L17-T05 | C9 selected optimization; F5 batching optional | [bitsandbytes quantization](https://huggingface.co/docs/transformers/quantization/bitsandbytes) (EN)<br>[vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) (EN) |
| L17-T06 | F3 serving/F12 deployment review; C9 deeper only as needed | [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) (EN)<br>[Ollama API introduction](https://docs.ollama.com/api/introduction) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N12 · Data Preparation & Feature Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N15 · MLOps Basics & Model Serving | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N21 · Fine-Tuning & Model Customization | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L17-E1 | Write a decision memo contrasting missing knowledge with task/style adaptation. | Choose not to fine-tune when the failure evidence does not justify it. |
| L17-E2 | Design a training dataset card with schema, rights, privacy, deduplication, and splits. | Private journals are not implicitly repurposed as training data. |
| L17-E3 | Optionally run a tiny PEFT experiment on permitted data if resources allow. | Compare a prompt baseline on independent holdout; otherwise deliver a resource-aware experiment plan. |
| L17-E4 | Optionally compare quantized or batched local serving. | Report memory/latency/quality on the actual hardware; no invented runs. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Fine-tuning for changing factual documents | RAG may be a better mechanism; demonstrate the actual adaptation need. |
| Train/eval near-duplicates | Split by source or task group and audit leakage. |
| Quantization improves everything | Measure memory, speed and quality; hardware compatibility varies. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. When fine-tune?
2. What is LoRA?
3. What must compare?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | When a stable task/behavior gap and sufficient representative data justify training and maintenance costs. |
| 2 | A parameter-efficient adaptation method using trainable low-rank updates instead of full-weight training. |
| 3 | The same independent task cases before/after tuning, including regressions, memory, latency and cost. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S7](../project/milestones/s7.md) | Customization decision, dataset card, and experiment plan; Run report only if a training/serving experiment was actually executed | A conceptual decision can be completed without a GPU. Practical training is not marked done without run evidence. This module is optional for Core completion. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

A conceptual decision can be completed without a GPU. Practical training is not marked done without run evidence. This module is optional for Core completion.

## Postpone until justified

- Training a foundation model
- Paying for compute without a hypothesis and evaluation

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L17 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L16](../16-Capstone-Career/README.md) · Next numbered Level: [L18](../18-Supporting-Frontend/README.md)

# L17 · Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 6 · Optional Specialization and Supporting UI | 18–32 h | 4/5 | P3 | [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md), [L05](../05-Evaluation/README.md), [L15](../15-Model-Selection-Optimization/README.md) |

**Outcome:** Choose between prompt changes, RAG, model selection, and fine-tuning using failure evidence. Understand SFT/LoRA, curation, quantization, and serving tradeoffs.

**Unlocks:** Optional extension; no core level depends on it.

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| When fine-tuning is justified | C7 pp.311–318; [Hugging Face PEFT quickstart](https://huggingface.co/docs/peft/quicktour) | [Practice 1](resources.md#practice-and-evidence) |
| Dataset engineering and PEFT | C7 selected tactics; C8 curation; [Hugging Face PEFT quickstart](https://huggingface.co/docs/peft/quicktour) | [Practice 2](resources.md#practice-and-evidence) |
| Advanced inference tradeoffs | C9 selected optimization; F5 batching; [PyTorch tensors quickstart](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) | [Practice 3](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N12** — Data Preparation & Feature Engineering.
- **N15** — MLOps Basics & Model Serving.
- **N21** — Fine-Tuning & Model Customization.

| ITI topic IDs | Interpretation |
| --- | --- |
| N12, N15, N21 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L17-E1 | Write a decision memo contrasting missing knowledge with task/style adaptation. | Choose not to fine-tune when the failure evidence does not justify it. |
| L17-E2 | Design a training dataset card with schema, rights, privacy, deduplication, and splits. | Private journals are not implicitly repurposed as training data. |
| L17-E3 | Optionally run a tiny PEFT experiment on permitted data if resources allow. | Compare a prompt baseline on independent holdout; otherwise deliver a resource-aware experiment plan. |
| L17-E4 | Optionally compare quantized or batched local serving. | Report memory/latency/quality on the actual hardware; no invented runs. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S7](../project/milestones/s7.md) | Customization decision, dataset card, and experiment plan; Run report only if a training/serving experiment was actually executed | A conceptual decision can be completed without a GPU. Practical training is not marked done without run evidence. This module is optional for Core completion. |

## Postpone

| Outside this level |
| --- |
| Training a foundation model |
| Paying for compute without a hypothesis and evaluation |

## Record completion

```bash
python scripts/progress.py set L17 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L16](../16-Capstone-Career/README.md) · Next numbered Level: [L18](../18-Supporting-Frontend/README.md). Follow the prerequisite table if branches differ.

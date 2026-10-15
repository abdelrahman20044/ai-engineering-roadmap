# M16 — Fine-Tuning, Dataset Engineering, and Advanced Serving

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P3 |
| Prerequisites | [M02](../m02-math-ml/README.md), [M03](../m03-dl-foundation-models/README.md), [M05](../m05-evaluation/README.md), [M15](../m15-optimization-feedback/README.md) |
| Personal effort | 18–32 focused hours; not official ITI hours |
| Project milestone | [S7](../../project/milestones/s7.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Choose between prompt changes, RAG, model selection, and fine-tuning using failure evidence. |
| O2 | Understand SFT/LoRA, curation, quantization, and serving tradeoffs. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N12 | Data Preparation & Feature Engineering | 12 |
| N15 | MLOps Basics & Model Serving | 18 |
| N21 | Fine-Tuning & Model Customization | 18 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | C7 When to Finetune pp. 311–318 first; selected PEFT/tactics only for the chosen experiment. |
| 2 | C8 curation/processing and C9 optimization when relevant. |
| 3 | F5 batching and paged attention as later serving references. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M16-E1 | Write a decision memo contrasting missing knowledge with task/style adaptation. | Choose not to fine-tune when the failure evidence does not justify it. |
| M16-E2 | Design a training dataset card with schema, rights, privacy, deduplication, and splits. | Private journals are not implicitly repurposed as training data. |
| M16-E3 | Optionally run a tiny PEFT experiment on permitted data if resources allow. | Compare a prompt baseline on independent holdout; otherwise deliver a resource-aware experiment plan. |
| M16-E4 | Optionally compare quantized or batched local serving. | Report memory/latency/quality on the actual hardware; no invented runs. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Customization decision, dataset card, and experiment plan; Run report only if a training/serving experiment was actually executed |
| Pass condition | A conceptual decision can be completed without a GPU. Practical training is not marked done without run evidence. This module is optional for Core completion. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M16 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Training a foundation model |
| Paying for compute without a hypothesis and evaluation |

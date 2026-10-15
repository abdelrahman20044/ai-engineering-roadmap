# M03 — Deep Learning, Foundation Models, and Serving

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P0 |
| Prerequisites | [M00](../m00-orientation/README.md) |
| Personal effort | 12–18 focused hours; not official ITI hours |
| Project milestone | [S2](../../project/milestones/s2.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Distinguish pretraining, supervised fine-tuning, preference tuning, and inference. |
| O2 | Understand layers, autograd, attention, tokenization, sampling, and resource constraints. |
| O3 | Choose an external provider or local inference endpoint with a reasoned boundary. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N14 | Deep Learning & Neural Networks | 18 |
| N15 | MLOps Basics & Model Serving | 18 |
| N16 | LLM Fundamentals & GenAI Landscape | 18 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | G1, printed pp. 1–22: conceptual reading; skim material already understood. |
| 2 | C2 pp. 49–111: skim architecture/post-training; focus on sampling and structured outputs, pp. 88–105. |
| 3 | F3 PDF 83–105 for language models and PDF 136–150 for serving strategies; defer multimodal examples. |
| 4 | PyTorch Tensors and Autograd quickstarts: one tiny CPU lab. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M03-E1 | Implement a tiny linear layer, loss, backward pass, and optimizer step in PyTorch. | Record tensor shapes, inspect gradients, and explain the update. Use M02 exercise E1 first if vectors are unfamiliar. |
| M03-E2 | Explore tokenization for representative inputs, optionally including Arabic and English. | Distinguish characters, tokens, context capacity, and embedding dimensions. |
| M03-E3 | Run five prompts using two sampling settings on one model. | Record settings and variation; low temperature is not treated as a determinism guarantee. |
| M03-E4 | Draw client → FastAPI → provider and compare external versus local serving. | Document timeouts, lifecycle, privacy/resource constraints, and actual hardware assumptions. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | tiny-autograd.py and tokenization observations; Model selection card and serving ADR |
| Pass condition | Explain next-token prediction and attention conceptually, demonstrate the autograd lab, and run inference. M02 may proceed in parallel; completing all ML topics is not a prerequisite for the first model API call. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M03 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Training a transformer from scratch |
| Audio/video/3D serving and distributed GPU training |

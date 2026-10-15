# L03 · Deep Learning, Foundation Models, and Serving

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 12–18 h | 3/5 | P0 | [L00](../00-Orientation/README.md) |

**Outcome:** Distinguish pretraining, supervised fine-tuning, preference tuning, and inference. Understand layers, autograd, attention, tokenization, sampling, and resource constraints. Choose an external provider or local inference endpoint with a reasoned boundary.

**Unlocks:** [L04](../04-LLM-Applications-Prompts/README.md), [L07](../07-Embeddings-Semantic-Search/README.md), [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Tensors and gradient descent | G1 pp.1–22; C2 pp.49–87; [PyTorch tensors quickstart](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) | [Practice 1](resources.md#practice-and-evidence) |
| Backpropagation and autograd | C2 conceptual architecture sections; [PyTorch autograd quickstart](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) | [Practice 2](resources.md#practice-and-evidence) |
| Tokens, attention, sampling | C2 pp.88–105; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 3](resources.md#practice-and-evidence) |
| Serving versus training | F3 PDF83–105,136–150; [FastAPI async guide](https://fastapi.tiangolo.com/async/) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N14** — Deep Learning & Neural Networks.
- **N15** — MLOps Basics & Model Serving.
- **N16** — LLM Fundamentals & GenAI Landscape.

| ITI topic IDs | Interpretation |
| --- | --- |
| N14, N15, N16 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L03-E1 | Implement a tiny linear layer, loss, backward pass, and optimizer step in PyTorch. | Record tensor shapes, inspect gradients, and explain the update. Use L02 exercise E1 first if vectors are unfamiliar. |
| L03-E2 | Explore tokenization for representative inputs, optionally including Arabic and English. | Distinguish characters, tokens, context capacity, and embedding dimensions. |
| L03-E3 | Run five prompts using two sampling settings on one model. | Record settings and variation; low temperature is not treated as a determinism guarantee. |
| L03-E4 | Draw client → FastAPI → provider and compare external versus local serving. | Document timeouts, lifecycle, privacy/resource constraints, and actual hardware assumptions. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S2](../project/milestones/s2.md) | tiny-autograd.py and tokenization observations; Model selection card and serving ADR | Explain next-token prediction and attention conceptually, demonstrate the autograd lab, and run inference. L02 may proceed in parallel; completing all ML topics is not a prerequisite for the first model API call. |

## Postpone

| Outside this level |
| --- |
| Training a transformer from scratch |
| Audio/video/3D serving and distributed GPU training |

## Record completion

```bash
python scripts/progress.py set L03 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L02](../02-Mathematics-ML/README.md) · Next numbered Level: [L04](../04-LLM-Applications-Prompts/README.md). Follow the prerequisite table if branches differ.

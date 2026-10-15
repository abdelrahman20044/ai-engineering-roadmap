# Resources · L03 — Deep Learning, Foundation Models, and Serving

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | G1, printed pp.1–22: conceptual reading; skim material already understood. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C2 pp.49–111: skim architecture/post-training; focus on sampling and structured outputs, pp.88–105. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | F3 PDF83–105 for language models and PDF136–150 for serving strategies; defer multimodal examples. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 4 | PyTorch Tensors and Autograd quickstarts: one tiny CPU lab. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Tensors and gradient descent | [PyTorch tensors quickstart](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) | Official tutorial / reference · free | Inspect shapes and train a tiny CPU model. |
| Backpropagation and autograd | [PyTorch autograd quickstart](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) | Official tutorial / reference · free | Calculate a scalar derivative and check autograd. |
| Tokens, attention, sampling | [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Official tutorial / reference · free | Compare temperature settings while holding prompts fixed. |
| Serving versus training | [FastAPI async guide](https://fastapi.tiangolo.com/async/) | Official tutorial / reference · free | Draw the boundary between API process and inference service. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Inspect shapes and train a tiny CPU model. | Code/test or short measured comparison; explain the result independently. |
| 2 | Calculate a scalar derivative and check autograd. | Code/test or short measured comparison; explain the result independently. |
| 3 | Compare temperature settings while holding prompts fixed. | Code/test or short measured comparison; explain the result independently. |
| 4 | Draw the boundary between API process and inference service. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

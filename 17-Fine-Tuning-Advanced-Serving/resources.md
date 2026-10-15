# Resources · L17 — Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | C7 When to Finetune pp.311–318 first; selected PEFT/tactics only for the chosen experiment. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C8 curation/processing and C9 optimization when relevant. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | F5 batching and paged attention as later serving references. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| When fine-tuning is justified | [Hugging Face PEFT quickstart](https://huggingface.co/docs/peft/quicktour) | Official tutorial / reference · free | Write a failure-driven go/no-go decision before training. |
| Dataset engineering and PEFT | [Hugging Face PEFT quickstart](https://huggingface.co/docs/peft/quicktour) | Official tutorial / reference · free | Separate training and held-out examples and run a small adapter experiment. |
| Advanced inference tradeoffs | [PyTorch tensors quickstart](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) | Official tutorial / reference · free | Benchmark memory and latency before choosing quantization or batching. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Write a failure-driven go/no-go decision before training. | Code/test or short measured comparison; explain the result independently. |
| 2 | Separate training and held-out examples and run a small adapter experiment. | Code/test or short measured comparison; explain the result independently. |
| 3 | Benchmark memory and latency before choosing quantization or batching. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

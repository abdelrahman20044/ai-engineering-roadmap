# Resources · L05 — Evaluation Engineering

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | C4 pp.200–207: Design Your Evaluation Pipeline; introduce during L00 and implement here. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | C3 pp.114–117 and 125–147: challenges, exact evaluation, AI judges, and limitations. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | C4 pp.160–178: criteria; F11 PDF495–533: model testing and retrieval/behavioral evaluation. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Evaluation datasets and criteria | [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Official tutorial / reference · free | Separate development cases from a held-out release set. |
| Exact checks and component evaluation | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | Official tutorial / reference · free | Test citations and contracts separately from answer quality. |
| AI judges and calibration | [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | Official tutorial / reference · free | Compare judge labels with human labels and inspect disagreement. |
| Regression gates and uncertainty | [GitHub Actions Python guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | Official tutorial / reference · free | Publish a reproducible baseline and failure taxonomy. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Separate development cases from a held-out release set. | Code/test or short measured comparison; explain the result independently. |
| 2 | Test citations and contracts separately from answer quality. | Code/test or short measured comparison; explain the result independently. |
| 3 | Compare judge labels with human labels and inspect disagreement. | Code/test or short measured comparison; explain the result independently. |
| 4 | Publish a reproducible baseline and failure taxonomy. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

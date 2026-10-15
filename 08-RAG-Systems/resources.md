# Resources · L08 — RAG Systems, Citations, and Retrieval Improvement

[← Level](README.md) · [Roadmap](../README.md) · [Book locator](../docs/READING_GUIDE.md)

Use one primary explanation per topic, then build. Supplementary references solve a specific gap; they are not extra courses to finish.

## Required book sections

| Order | Verified assignment | How to use |
| --- | --- | --- |
| 1 | G4 printed pp.94–100: improvements and coding explanation. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 2 | F5 RAG and F11 PDF519–527 retrieval integration. | Read the named focus, then implement. Follow explicit skim/defer instructions. |
| 3 | C6 pp.253–274, especially pp.267–272; C4 component evaluation. | Read the named focus, then implement. Follow explicit skim/defer instructions. |

G = Andrea De Mauro, *Grokking AI Applications*. F = Alireza Parandeh, *Building Generative AI Services with FastAPI*. C = Chip Huyen, *AI Engineering*. G/C pages are printed; F pages are PDF viewer positions. Exact chapter titles and editions: [book locator](../docs/READING_GUIDE.md). Books are supplied/owned separately and are not redistributed.

## Topic-specific tutorials and official references

| Topic | Resource | Type / cost | Read or do |
| --- | --- | --- | --- |
| Retrieve-then-generate baseline | [pgvector search and indexing](https://github.com/pgvector/pgvector) | Official tutorial / reference · free | Return source passages with every grounded response. |
| Citation correctness and abstention | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | Official tutorial / reference · free | Reject unsupported source IDs and test no-evidence questions. |
| Hybrid retrieval and reranking | [pgvector search and indexing](https://github.com/pgvector/pgvector) | Official tutorial / reference · free | Compare vector-only with hybrid search on the same query set. |
| Recall and ranking metrics | [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Official tutorial / reference · free | Measure Recall@k and reciprocal rank independently of generation. |

## Practice and evidence

| Practice | Task | Evidence to retain |
| --- | --- | --- |
| 1 | Return source passages with every grounded response. | Code/test or short measured comparison; explain the result independently. |
| 2 | Reject unsupported source IDs and test no-evidence questions. | Code/test or short measured comparison; explain the result independently. |
| 3 | Compare vector-only with hybrid search on the same query set. | Code/test or short measured comparison; explain the result independently. |
| 4 | Measure Recall@k and reciprocal rank independently of generation. | Code/test or short measured comparison; explain the result independently. |

The [Level exercises](README.md#practical-exercises) define the assessed work; these topic drills are smaller warm-ups, not additional portfolio projects. Use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

## Reading depth and overlap

| Decision | Guidance |
| --- | --- |
| Primary implementation | FastAPI book for backend mechanics; official docs resolve version differences. |
| Primary concept | Grokking for accessible first exposure; Chip for evaluation and tradeoffs. |
| Skip duplication | Do not repeat the same prompt, HTTP, SQL, JWT, or Docker introduction in three sources. |
| Optional depth | Follow this Level’s postpone list; advanced material is triggered by measured failures. |

[← Level](README.md) · [Next work](../progress/PROGRESS.md)

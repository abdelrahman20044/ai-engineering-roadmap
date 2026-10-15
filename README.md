# AI Engineering Learning Roadmap

**A personalized, prerequisite-based roadmap for building, evaluating, and operating LLM applications.** Built primarily from the ITI Native AI Developer curriculum, three selected books, and Anthropic’s Context Engineering article.

Designed for **Abdelrahman**, a Computer Science graduate with Node.js/Express, MongoDB, authentication, testing, Docker, Python fundamentals, and SQL experience. Transfer those skills; do not restart programming fundamentals.

![AI Engineering roadmap](assets/roadmap.svg)

## Start here

| Step | Open or run | Result |
|---|---|---|
| 1 | [START_HERE.md](START_HERE.md) | Complete the baseline and scope the product |
| 2 | [M01: Python and FastAPI](modules/m01-python-fastapi/README.md) | Start building immediately |
| 3 | [Prerequisite roadmap](docs/ROADMAP.md) | Follow dependencies rather than a fixed calendar |
| 4 | [Reading guide](docs/READING_GUIDE.md) | Read only the sections needed for the current module |
| 5 | [Project milestones](project/README.md) | Build the same application incrementally |
| 6 | [Progress tracker](progress/README.md) | Record evidence, blockers, and completion |

```bash
python scripts/validate.py
python scripts/progress.py next
python scripts/progress.py set M00 in_progress
```

Repository tools require **Python 3.10+ and the standard library**. Install application and ML dependencies in separate environments when a lab requires them. The repository provides learning tasks and tooling, not a completed AI application.

## Curriculum

| Module | Focus | Hard prerequisites | Reading anchors | Priority |
|---|---|---|---|---|
| [M00](modules/m00-orientation/README.md) | Baseline Assessment and Product Scope | — | C1/C4 | P0 |
| [M01](modules/m01-python-fastapi/README.md) | Python, FastAPI, and Service Testing | M00 | F2/F4/F11 | P0 |
| [M02](modules/m02-math-ml/README.md) | Practical Mathematics, ML, and Data Preparation | M00 | G1/C2/C3/C8 + ML docs | P1 |
| [M03](modules/m03-dl-foundation-models/README.md) | Deep Learning, Foundation Models, and Serving | M00 | G1/F3/C2 + PyTorch | P0 |
| [M04](modules/m04-prompt-structured-output/README.md) | Prompt Engineering, Structured Outputs, and LLM Integration | M01, M03 | G2–3/F3–5/C5 | P0 |
| [M05](modules/m05-evaluation/README.md) | Evaluation Engineering | M04 | C3–4/F11 | P0 |
| [M06](modules/m06-persistence/README.md) | PostgreSQL, ORM, and AI Application State | M01 | F7 | P1 |
| [M07](modules/m07-ingestion-embeddings/README.md) | RAG Document Preparation, Embeddings, and Semantic Search | M03, M06 | G4/F5/C6/C8 | P1 |
| [M08](modules/m08-rag/README.md) | RAG Systems, Citations, and Retrieval Improvement | M05, M07 | G4/F5/F11/C4/C6 | P1 |
| [M09](modules/m09-context-memory/README.md) | Context Engineering, Memory, and Conversations | M08 | C5–6/C10 + Anthropic | P1 |
| [M10](modules/m10-async-streaming-jobs/README.md) | Concurrency, Streaming, and Long-Running Jobs | M08 | F5–6 | P1 |
| [M11](modules/m11-security/README.md) | Security, Authorization, and Responsible AI | M06, M08 | F8–9/C5/C10 | P1 |
| [M12](modules/m12-tools-agents/README.md) | Tool Calling, Bounded Agents, and Multi-Agent Decisions | M05, M09, M11 | G5–6/C6 + Anthropic | P1 |
| [M13](modules/m13-mcp-workflows/README.md) | MCP, Enterprise Integration, and AI Workflows | M12 | C10 + MCP docs | P2 |
| [M14](modules/m14-llmops-deployment/README.md) | MLOps, LLMOps, Architecture, and Deployment | M10, M11 | F3/F11–12/C10 | P2 |
| [M15](modules/m15-optimization-feedback/README.md) | Model Selection, Cost, Latency, and User Feedback | M05, M14 | F10/C4/C9–10 | P2 |
| [M16](modules/m16-customization/README.md) | Fine-Tuning, Dataset Engineering, and Advanced Serving | M02, M03, M05, M15 | C7–9/F5 | P3 |
| [M17](modules/m17-capstone/README.md) | Capstone Release, Technical Defense, and Career Evidence | M02, M03, M08, M09, M10, M11, M12, M13, M14, M15 | C1/C4/F11/C10 review | P2 |
| [M18](modules/m18-frontend/README.md) | Supporting TypeScript and React UI | M01, M04, M11 | React docs/F6/F8 | P3 |

| Priority | Meaning |
|---|---|
| P0 | Start building and establish evaluation early |
| P1 | Complete the grounded application and required scientific foundations |
| P2 | Integrate, operate, optimize, and defend the application |
| P3 | Optional advanced or supporting coverage; M16/M18 do not block Core completion |

## Project

**Book-Grounded Reflection Assistant:** upload permitted documents, ask questions with verifiable source citations, connect selected journal entries to source ideas, maintain bounded conversation context, and use authorized tools where justified.

| Release | Evidence |
|---|---|
| MVP | Document provenance, retrieval, grounded answers, citations, and evaluation |
| Intermediate | Journals, context/memory, authorization, streaming, and reliable jobs |
| Production-oriented | Bounded agents, MCP integration, CI, traces, recovery, deployment, and cost/quality reports |
| Optional depth | Fine-tuning experiments or React/TypeScript support |

## Repository map

| Area | Contents |
|---|---|
| [modules](docs/ROADMAP.md) | 19 modules, 84 exercises, prerequisites, reading, and acceptance evidence |
| [ITI coverage](docs/ITI_COVERAGE.md) | Traceability for all 32 published syllabus items |
| [Reading guide](docs/READING_GUIDE.md) | Verified chapter/section references, read/skim/defer decisions |
| [project](project/README.md) | Eight milestones with delivery gates |
| [exercises](exercises/README.md) | Synthetic corpus, journals, and public seed evaluation cases |
| [templates](templates/README.md) | Evidence, experiments, ADRs, threat model, model card, and runbook |
| [Progress tables](progress/PROGRESS.md) | GitHub-readable dashboard, [CSV and CLI instructions](progress/README.md) |
| [Operating guidance](docs/EVALUATION.md) | Evaluation, [security](docs/SECURITY.md), and [context](docs/CONTEXT_ENGINEERING.md) |
| [Sources](docs/SOURCES.md) | Verified references and explicit uncertainty |
| [Repository guide](docs/REPOSITORY_GUIDE.md) | Commands, packaging, and optional GitHub setup |
| [OVERVIEW.html](OVERVIEW.html) | Standalone English reader |

## Effort and scope

| Item | Policy |
|---|---|
| Core effort | Approximately **233–355 focused hours**, adjusted through diagnostics |
| At 15–20 hours/week | Roughly 12–24 weeks for the comprehensive Core; the first measured RAG release arrives earlier |
| Existing skills | Skim familiar backend topics; use evidence and targeted transfer exercises |
| Foundations | Mathematics, ML, and DL remain in Core with small practical labs |
| Scope | AI Engineering only; document preparation and background jobs support the AI product |
| Frameworks | Direct SDKs first; orchestration frameworks only when justified |
| Progress | Starts at zero; completion is self-reported and evidence-linked |

The official brochure states **678 hours**, while its listed items sum to **696**. This discrepancy is unresolved. Official hours are not personal study estimates. FastAPI/PostgreSQL/SQLAlchemy are implementation recommendations, not tools explicitly mandated by the brochure.

Sources were checked on **15 October 2026**. This independent roadmap does not depend on ITI acceptance and is not a credential or hiring guarantee. Books are referenced, not redistributed. CRM was inspected read-only and is not modified.

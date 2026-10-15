# Chapter and Section Reading Guide

[Home](../README.md) · [Levels](ROADMAP.md) · [Sources](SOURCES.md)

| Code | Book | Page convention |
|---|---|---|
| G | Grokking AI Applications — Andrea De Mauro | Printed page numbers |
| F | Building Generative AI Services with FastAPI — Alireza Parandeh | PDF viewer pages, starting at1 |
| C | AI Engineering — Chip Huyen | Printed page numbers |

The tables of contents and relevant excerpts were checked in the supplied PDFs. These are locators, not assignments to read every page. The module file defines the exact pass and prerequisites. Read a concept once, implement it in the same application, and consult the second source for a specific unresolved question.

| Chapter | Verified location | Depth and focus | Module |
| --- | --- | --- | --- |
| G1 | Peeking inside the black box, pp. 1–22 | Conceptual: tokens, model limits, application versus model | L03; early orientation in L00 |
| G2 | Building your first GenAI app, pp. 23–45 | Skim Langflow; focus on What if we coded it?, pp. 42–45 | L04 |
| G3 | Writing the right prompt, pp. 47–72 | Focus pp. 48–56 and68–72; skim UI templates | L04 |
| G4 | Augmenting LLMs with your own documents, pp. 73–100 | Focus pp. 74–82 and94–100; translate concepts to your code | L07–L08 |
| G5 | Tools and agents, pp. 101–127 | Focus pp. 102–107 and122–127; skip duplicate travel-app setup | L12 |
| G6 | Implementing agentic structures, pp. 129–171 | Read patterns pp. 130–132; implementation optional after comparison | L12 |
| G7 | Integrating GenAI in your data ecosystem, pp. 173–210 | Optional overview; KNIME setup not assigned | Optional |
| G8 | Deploying and orchestrating GenAI apps, pp. 211–240 | Optional conceptual reference; F12/C10 are primary | L13–L14 |
| F1 | Introduction, PDF 23–42 | Skim project orientation | L00 |
| F2 | Getting Started with FastAPI, PDF 43–82 | Deep: server, Depends, lifespan, structure; skim familiar web concepts | L01 |
| F4 | Implementing Type-Safe AI Services, PDF 153–186 | Deep: annotations, Pydantic, constraints, serialization, settings | L01/L04 |
| F3 | AI Integration and Model Serving, PDF 83–152 | Text/serving focus; external serving PDF 142–145; defer audio/video/3D | L03–L04 |
| F5 | Achieving Concurrency in AI Workloads, PDF 187–257 | Read provider I/O, RAG, event loop, and jobs in separate passes; defer GPU internals | L04/L07/L08/L10 |
| F7 | Integrating Databases into AI Services, PDF 302–337 | Deep ORM/session/CRUD/Alembic; skim comparisons and Prisma | L06 |
| F11 | Testing AI Services, PDF 477–535 | pytest first, then retrieval/behavioral/E2E tests; avoid repeating testing theory | L01/L05/L08/L12/L14/L16 |
| F8 | Authentication and Authorization, PDF 338–400 | Deep FastAPI implementation and ownership; skim known JWT/RBAC theory | L11 |
| F6 | Real-Time Communication with Generative Models, PDF 258–301 | Streaming/SSE/cancellation first; WebSockets only if justified | L10 |
| F9 | Securing AI Services, PDF 401–428 | Rate limits, abuse, guardrails and their limits; update with OWASP | L11 |
| F10 | Optimizing AI Services, PDF 429–476 | Selective after measurement; caching requires isolation/invalidation | L15 |
| F12 | Deployment of AI Services, PDF 536–594 | Dockerfile/storage/networking/Compose/optimization; skim familiar basics | L14 |
| C1 | Introduction, pp. 1–47 | Planning pp. 28–34 and stack pp. 35–46; skim history | L00 |
| C2 | Understanding Foundation Models, pp. 49–111 | Sampling/structured outputs pp. 88–105; conceptual architecture/post-training | L03–L04 |
| C3 | Evaluation Methodology, pp. 113–156 | Challenges114–117; exact125–135; judge136–147; defer entropy derivations | L05 |
| C4 | Evaluate AI Systems, pp. 159–208 | Pipeline200–207 early; criteria160–178; selection179–200 later | L00/L05/L15 |
| C5 | Prompt Engineering, pp. 211–251 | Context218–219; versioning233–234; defense235–250; skim duplicated basics | L04/L09/L11 |
| C6 | RAG and Agents, pp. 253–305 | Retrieval253–274; agents275–299; memory300–304, at their module gates | L07/L08/L09/L12 |
| C7 | Finetuning, pp. 307–361 | When to Finetune311–318 before optional PEFT experiments | L17 |
| C8 | Dataset Engineering, pp. 363–403 | Quality368–371 and processing396–402; training synthesis later | L02/L07/L17 |
| C9 | Inference Optimization, pp. 405–447 | Metrics412–418 first; advanced serving only if justified | L10/L15/L17 |
| C10 | AI Engineering Architecture and User Feedback, pp. 449–492 | Context450; guardrails451–455; observability465–473; feedback480–491 | L09/L14/L15 |

| Additional area | Why another source is necessary |
|---|---|
| Practical ML/DL | L02/L03 use focused scikit-learn/PyTorch documentation; the three books do not provide a complete foundations course |
| MCP | L13 requires official protocol/SDK documentation |
| React/TypeScript | L18 is supporting optional coverage; the AI books are not a React curriculum |

Deep reading means implementing and explaining a decision, not reproducing every example. Low-code setup, duplicate chatbots, and unneeded model modalities are intentionally minimized.

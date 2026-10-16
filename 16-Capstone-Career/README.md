# L16 · Capstone Release, Technical Defense, and Career Evidence

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 5 · Operating and Demonstrating AI Systems | 12–18 h | 4/5 | P2 | [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md), [L08](../08-RAG-Systems/README.md), [L09](../09-Context-Memory/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md), [L12](../12-Tools-Agents/README.md), [L13](../13-MCP-Enterprise-Integration/README.md), [L14](../14-LLMOps-Deployment/README.md), [L15](../15-Model-Selection-Optimization/README.md) |

**Unlocks:** No further required Level; use the evidence to apply or specialize.

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Demonstrate a usable AI application with evaluation and operating evidence. Explain and modify the implementation independently and communicate honest limitations. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Core project readiness | Upload, ask, cite, journal connection, history and deletion work end-to-end. |
| Evidence readiness | CI, holdout, security matrix and traces have reproducible artifacts. |
| Independence | Modify and test a small feature without generated code. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Reproducible capstone release: A reviewer runs the release on synthetic data from a clean checkout.
- [ ] Final evaluation and limitations: Freeze the config, run holdout once for release assessment and analyze three failures.
- [ ] Architecture and technical defense: Present a 5-minute demo and a deeper 20-minute walkthrough with one rejected option.
- [ ] AI fundamentals interview bridge: Answer conceptual questions using your own experiment or failure example.
- [ ] Backend and operations defense: Write an endpoint, query and test independently; diagnose a supplied failing trace.
- [ ] Career evidence and communication: Write three evidence-backed CV bullets and a scoped delivery proposal with assumptions and acceptance criteria.

## Recommended learning path

No new large course: assemble the evidence, run an untouched holdout, ship a reproducible release and defend the decisions. Apply while improving documented gaps.

| Pass | Work to do | Stop condition |
| --- | --- | --- |
| 1 · Orient | Use the assigned book/article focus and one Arabic or English explanation for each unfamiliar topic. | Explain the mechanism in your own words. |
| 2 · Implement | Work through the numbered topic outputs below; integrate them into the assessed exercises. | The specified behavior is reproducible in your own code. |
| 3 · Verify | Run the failure cases, self-check and milestone acceptance contract. | Evidence and remaining limitations are recorded. |

The resource library contains alternatives and optional depth. The effort estimate covers a selected path plus implementation, not watching every listed course. Choose Arabic teaching when it speeds understanding, then consult the English API reference for exact behavior.

## What you learn and exactly where

Each numbered row is a learning unit. **Arabic teaching**, **machine-translated Arabic text**, **English videos**, and **English documentation** are labeled separately. A missing verified Arabic resource is stated explicitly; a loosely related video is not presented as full coverage.

| Topic and required subtopics | Arabic route | English route | Build or verify |
| --- | --- | --- | --- |
| **L16-T01 · Reproducible capstone release**<br>Setup; seed corpus; secrets template; migrations; version manifest | [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) (AR video)<br>[mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | A reviewer runs the release on synthetic data from a clean checkout. |
| **L16-T02 · Final evaluation and limitations**<br>Untouched holdout; raw counts; source/citation results; failure taxonomy | [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text) | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Freeze the config, run holdout once for release assessment and analyze three failures. |
| **L16-T03 · Architecture and technical defense**<br>ERD; request trace; ADR; provider boundary; agent/no-agent rationale | [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) (AR video)<br>[Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) (AR machine-translated text) | [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides) | Present a 5-minute demo and a deeper 20-minute walkthrough with one rejected option. |
| **L16-T04 · AI fundamentals interview bridge**<br>ML leakage; gradients; tokens; embeddings; retrieval; sampling | [Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k) (AR video)<br>[Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) (AR video) | [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) (EN course + videos + quizzes) | Answer conceptual questions using your own experiment or failure example. |
| **L16-T05 · Backend and operations defense**<br>Auth; SQL; transaction; async; worker; deployment; trace diagnosis | [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) (AR video)<br>[mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video)<br>[Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc) (EN video) | Write an endpoint, query and test independently; diagnose a supplied failing trace. |
| **L16-T06 · Career evidence and communication**<br>Role-specific CV; scoped proposal; ethical claims; status reporting | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text)<br>[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides) | Write three evidence-backed CV bullets and a scoped delivery proposal with assumptions and acceptance criteria. |

**Arabic coverage boundary:** Arabic project orientation and UX/lifecycle lessons support presentation. A verified Arabic AI-engineering interview bank was not found. The Level self-checks and mock defense are recommendations, not official ITI interview questions.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L16-T01 | F11 E2E/F12 review only | [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) (EN)<br>[Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) (EN) |
| L16-T02 | C4 pipeline review; no full re-read | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L16-T03 | C1 planning/C10 architecture review | [Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record) (EN)<br>[Technical Writing One](https://developers.google.com/tech-writing/one) (EN) |
| L16-T04 | G1/C2 focused revision; C3/C6 as needed | [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) (EN)<br>[InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) (EN) |
| L16-T05 | F2/F4/F5/F7/F8 selective revision | [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN)<br>[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN) |
| L16-T06 | C10 feedback; ITI professional topics are practiced through project artifacts | [Technical Writing One](https://developers.google.com/tech-writing/one) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N27 · Graduation Project | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N28 · Effective Presentation Skills | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N29 · Freelancing Fundamentals | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N30 · Effective Communication Skills | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N31 · Work Ethics Workshop | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N32 · CV Writing & Interviewing Skills | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L16-E1 | Demonstrate upload → question → source → journal connection → conversation → deletion through a basic UI. | Include failure paths and cross-user access tests. |
| L16-E2 | Freeze configuration and run the final independent holdout. | Analyze three major failures and disclose remaining limitations. |
| L16-E3 | Publish application setup docs, ERD/architecture, ADRs, runbook, and a 3–5-minute demo. | A reviewer can reproduce the demo with synthetic data. |
| L16-E4 | Run a mock defense: write an endpoint, query, and test without AI; diagnose a trace. | Explain framework, model, retrieval, and single-agent decisions. |
| L16-E5 | Draft evidence-based CV claims and a scoped freelance proposal. | Only measured figures are used; discuss data ethics, delivery scope, and communication. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Another demo without evidence | Link reproducible tests, datasets, configs and failure analysis. |
| Production claim exceeds deployment | Describe what was exercised and remaining limits precisely. |
| Study every optional resource before applying | Use the role checklist and apply after demonstrable core competence. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. How defend a rejected technology?
2. What makes a CV metric credible?
3. How present failure?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | State the requirement, options, evidence, tradeoff and trigger for reconsidering the decision. |
| 2 | A reproducible measurement with workload, sample size, environment and configuration. |
| 3 | Show the case, root cause, mitigation, verification and remaining limitation. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S7](../project/milestones/s7.md) | Versioned release, demo, evaluation report/dashboard, and defense notes | Run, explain, modify, and evaluate the system. This is a self-study gate, not an ITI credential or hiring guarantee. L17/L18 remain optional. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Run, explain, modify, and evaluate the system. This is a self-study gate, not an ITI credential or hiring guarantee. L17/L18 remain optional.

## Postpone until justified

- Waiting for every advanced topic before applying
- Inflated metrics or unsupported production-ready claims

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L16 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L15](../15-Model-Selection-Optimization/README.md) · Next numbered Level: [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

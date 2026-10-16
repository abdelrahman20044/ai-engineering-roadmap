# L00 · Baseline Assessment and Product Scope

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 3–5 h | 1/5 | P0 | Existing backend/Python/SQL experience |

**Unlocks:** [L01](../01-Python-FastAPI/README.md), [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Identify transferable backend skills and specific gaps. Define users, requirements, failure cases, and acceptance evidence. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Backend transfer | Explain validation, auth, persistence and one integration test from CRM. |
| Python/SQL baseline | Write a JSON transformation and a small join without generated code. |
| Product reasoning | Name a user, their question, a failure and observable success. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Transfer backend skills: Record a comparison with one existing CRM implementation and one Python gap.
- [ ] Choose the user problem: Write five user stories with acceptance conditions and only one first-release flow.
- [ ] Define answer contracts: Write three response examples: supported, unsupported and unauthorized.
- [ ] Plan evaluation evidence: Create ten initial questions with source references; label these development cases.
- [ ] Learn independently: Explain the use case in two minutes and implement a tiny change without AI.

## Recommended learning path

C1 planning → mini-RAG orientation → your scope and diagnostic. Spend hours defining a testable first slice, not choosing a framework.

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
| **L00-T01 · Transfer backend skills**<br>Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries | [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) (AR video + code)<br>[Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) (AR video + assignments) | [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) (EN video + problem sets) | Record a comparison with one existing CRM implementation and one Python gap. |
| **L00-T02 · Choose the user problem**<br>Book questions; journal connections; non-goals; permitted document corpus | [mini-RAG · About the Course ماذا ولمـــاذا](https://www.youtube.com/watch?v=Vv6e2Rb1Q6w&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj) (AR video)<br>[mini-RAG · What will we build ماذا سنبنى في المشروع](https://www.youtube.com/watch?v=_l5S5CdxE-Q&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=2) (AR video) | [Launch an LLM App in One Hour](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/launch-an-llm-app-in-one-hour/) (EN video + slides) | Write five user stories with acceptance conditions and only one first-release flow. |
| **L00-T03 · Define answer contracts**<br>Evidence versus suggestion; no-evidence behavior; ownership | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text) | [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) (EN video + slides) | Write three response examples: supported, unsupported and unauthorized. |
| **L00-T04 · Plan evaluation evidence**<br>Answerable/unanswerable questions; expected source; fixed synthetic cases | [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text) | [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides) | Create ten initial questions with source references; label these development cases. |
| **L00-T05 · Learn independently**<br>Read → recall → implement → test → explain; AI assistance boundaries | [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) (AR video) | [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) (EN video + problem sets) | Explain the use case in two minutes and implement a tiny change without AI. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L00-T01 | C1 pp.35–46; F2 project-structure reference only | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) (EN) |
| L00-T02 | C1 pp.28–34 | [Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record) (EN) |
| L00-T03 | C4 pp.160–178, skim criteria; C1 planning | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN) |
| L00-T04 | C4 pp.200–207, preview pipeline | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L00-T05 | No additional chapter; use the baseline exercise | [Technical Writing One](https://developers.google.com/tech-writing/one) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N01 · Modern Software Engineering & Git Collaboration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N03 · SDLC & Requirements Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N09 · Software Architecture & System Design | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N30 · Effective Communication Skills | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N31 · Work Ethics Workshop | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L00-E1 | Explain a JWT/RBAC flow, Zod validation, and an integration test from CRM. Write a typed JSON cleaner and a test without AI. | Record demonstrated skills and gaps; distinguish prior evidence from assumptions. |
| L00-E2 | Write five user stories and three failure cases: missing evidence, unreadable document, and unauthorized resource access. | Each story has an observable acceptance condition. |
| L00-E3 | Choose a small permitted corpus, specify input/output contracts and three non-goals, and create the first ADR. | A one-page scope and ten initial questions are sufficient to start building. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Planning everything | Freeze three non-goals and build the first endpoint next. |
| Vague AI success | Turn “helpful answer” into groundedness, citation and abstention criteria. |
| Copying a tutorial product | Use your own reflection/journal user stories and corpus. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What makes the first release small?
2. What counts as prior skill evidence?
3. Why draft evaluation questions now?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | One user flow, a small corpus, explicit non-goals and observable acceptance criteria. |
| 2 | A specific route, test, schema or commit you can explain and modify. |
| 3 | They expose ambiguous scope and establish a baseline before optimization. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S0](../project/milestones/s0.md) | baseline.md with links to prior work; project-scope.md and the first ADR | Explain the use case and the first deliverable in two minutes. Review only demonstrated gaps rather than restarting backend fundamentals. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Explain the use case and the first deliverable in two minutes. Review only demonstrated gaps rather than restarting backend fundamentals.

## Postpone until justified

- Repeating JavaScript, HTTP, Git, or Docker basics after passing diagnostics
- Microservices or buying a GPU before a need exists

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L00 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Next numbered Level: [L01](../01-Python-FastAPI/README.md)

# L01 · Python, FastAPI, and Service Testing

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 14–20 h | 2/5 | P0 | [L00](../00-Orientation/README.md) |

**Unlocks:** [L04](../04-LLM-Applications-Prompts/README.md), [L06](../06-Application-State/README.md), [L18](../18-Supporting-Frontend/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Use type hints, Pydantic, dependency injection, and lifespan management. Separate HTTP handlers from application logic and test the service. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Python transfer | Use functions, OOP, exceptions, modules and virtual environments without a beginner walkthrough. |
| HTTP transfer | Explain status codes, validation and middleware from Express. |
| Testing transfer | Write one success and one failure assertion independently. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Modern Python tooling and types: Type a provider interface and explain what is checked statically versus at runtime.
- [ ] Request and response contracts: Reject missing, malformed and unexpected values with an explicit response contract.
- [ ] Routes and application boundaries: Create /health and /reflect with application logic outside the route handler.
- [ ] Dependency injection and lifecycle: Swap providers in a test and assert the lifespan client closes after shutdown.
- [ ] Iteration and resource cleanup: Batch a record iterator and prove cleanup when its consumer raises.
- [ ] Deterministic service tests: Run validation, provider-error and dependency-override tests with no external calls.

## Recommended learning path

F2/F4 selective reading → mini-RAG lessons 5–6 or CS50 testing → a fake-provider API. Add pytest from the first endpoint.

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
| **L01-T01 · Modern Python tooling and types**<br>Environment; dependency pinning; type hints; Annotated; optional versus nullable | [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) (AR video + assignments)<br>**Scope:** Language/OOP refresher only; use F4/typing docs for Annotated and modern types. | [Python typing](https://docs.python.org/3/library/typing.html) (EN)<br>[CS50P · Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/) (EN video + problem sets) | Type a provider interface and explain what is checked statically versus at runtime. |
| **L01-T02 · Request and response contracts**<br>Pydantic validation; serialization; constraints; strictness; errors | [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) (AR video + code)<br>[mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Reject missing, malformed and unexpected values with an explicit response contract. |
| **L01-T03 · Routes and application boundaries**<br>APIRouter; config; handlers versus services; fake provider | [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) (AR video)<br>[mini-RAG · Nested Routes + Env Values](https://www.youtube.com/watch?v=CrR2Bz2Y7Hw&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=6) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Create /health and /reflect with application logic outside the route handler. |
| **L01-T04 · Dependency injection and lifecycle**<br>Depends; dependency overrides; shared HTTP client; lifespan teardown | [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) (AR video)<br>**Scope:** FastAPI orientation only; dependency teardown and override details are in F2/current docs. | [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) (EN)<br>[FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/) (EN) | Swap providers in a test and assert the lifespan client closes after shutdown. |
| **L01-T05 · Iteration and resource cleanup**<br>Generators; batching; with; context managers; exceptions | [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) (AR video + assignments) | [Context managers](https://docs.python.org/3/library/contextlib.html) (EN) | Batch a record iterator and prove cleanup when its consumer raises. |
| **L01-T06 · Deterministic service tests**<br>Fixtures; parametrization; mocks; API contracts; error branches | [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) (AR video + assignments)<br>**Scope:** General Python preparation; pytest fixtures/mocking use the English testing path. | [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) (EN video + problem sets) | Run validation, provider-error and dependency-override tests with no external calls. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L01-T01 | F4 PDF153–186, read type-related sections; skim primitive types | [Python typing](https://docs.python.org/3/library/typing.html) (EN) |
| L01-T02 | F4 PDF153–186, read thoroughly | [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) (EN)<br>[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) (EN) |
| L01-T03 | F2 PDF43–82, selective framework setup | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) (EN) |
| L01-T04 | F2 Depends/lifespan sections, read thoroughly | [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) (EN)<br>[FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/) (EN)<br>[Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) (EN) |
| L01-T05 | Python-specific gap: official contextlib tutorial; no invented book section | [Context managers](https://docs.python.org/3/library/contextlib.html) (EN) |
| L01-T06 | F11 PDF500–518, first testing pass | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) (EN)<br>[Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N02 · Advanced Python Programming for AI Engineers | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N05 · Software Testing & Full-Stack Debugging | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N07 · RESTful API, Backend Architecture & Security | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L01-E1 | Implement /health and POST /reflect with an explicitly fake provider. Test valid, missing, invalid, and provider-timeout cases. | Tests make no live model calls and assert documented responses. |
| L01-E2 | Write a context manager for a resource and a generator for batched records. | An exception triggers cleanup; batches preserve the expected records. |
| L01-E3 | Replace the provider using a dependency override. | The API contract stays the same when fake and real adapters are swapped. |
| L01-E4 | Explain annotations versus runtime validation and def versus async def. Add one endpoint without copying a solution. | Demonstrate the distinction with a failing validation case; deepen concurrency in L10. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Annotations treated as validation | Show a plain typed function accepting a bad value and a Pydantic model rejecting it. |
| One global mutable client/session | Initialize shared clients in lifespan; use request/task-specific state. |
| Tests call a paid model | Override the provider and make tests deterministic. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Why Depends rather than manual construction in every route?
2. Does async make CPU work faster?
3. What must cleanup prove?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | It provides a declared lifecycle and an override seam while keeping application logic testable. |
| 2 | No; it enables cooperative I/O concurrency. CPU work needs a different execution boundary. |
| 3 | Resources close on both success and exceptions; tests verify the teardown. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S1](../project/milestones/s1.md) | Application skeleton in a separate implementation repository; Tests, pinned dependencies, and setup instructions | A clean checkout runs the API and tests. Provider failures have defined responses, and you can add and test a small feature independently. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

A clean checkout runs the API and tests. Provider failures have defined responses, and you can add and test a small feature independently.

## Postpone until justified

- A complete Python beginner course if diagnostics pass
- Agent frameworks and elaborate class hierarchies

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L01 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L00](../00-Orientation/README.md) · Next numbered Level: [L02](../02-Mathematics-ML/README.md)

# Resource Library · L01 — Python, FastAPI, and Service Testing

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

## Topic navigation

1. [Routes and application boundaries](#unit-01)
2. [Dependency injection and lifecycle](#unit-02)
3. [Modern Python tooling and types](#unit-03)
4. [Request and response contracts](#unit-04)
5. [Iteration and resource cleanup](#unit-05)
6. [Deterministic service tests](#unit-06)

<a id="unit-01"></a>

## 1. Routes and application boundaries

[Return to README Step 1](README.md#1-routes-and-application-boundaries)

**Topic/subtopics:** APIRouter; config; handlers versus services; fake provider.

**Required sequence (default route):** the assigned book slice [B04 · F2](../docs/READING_GUIDE.md#b04) **THEN** `ar-mini-6`. Stop each source at the stated portion.

**Choose ONE explanation for FastAPI path operations:** default `ar-mini-6` **OR** `fcc-api`. Retain the assigned F2 layout/setup reading; a routing explanation alone does not replace it. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `fastapi`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-routes-and-application-boundaries) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B04 · F2](../docs/READING_GUIDE.md#b04)<br>Alireza Parandeh · EN | Book Section | Complementary | Routes and application boundaries | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b04) |
| `ar-mini-6` · [mini-RAG · Nested Routes + Env Values](https://www.youtube.com/watch?v=CrR2Bz2Y7Hw&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=6)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | Nested Routes + Env Values in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-4` · [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Project Architecture in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | Routes and application boundaries (selected course unit) | Section 3: Starting FastAPI; Path operations. |
| `fastapi` · [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)<br>FastAPI · EN | Documentation / tutorial | Reference | Request/response models and routing. | Consult the relevant example for Request/response models and routing.… [bounds](#unit-01-fastapi) |
| `roby` · [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)<br>Eric Roby and Chad Darby · EN video | Full Course (paid) | Optional Advanced | Alternative guided backend course for validation,… | Topic bounds; lesson IDs not verified — [details](#unit-01-roby) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-mini-6"></a>

**`ar-mini-6` — selected portion:** Only the linked “Nested Routes + Env Values” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-mini-4"></a>

**`ar-mini-4` — selected portion:** Only the linked “Project Architecture” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-fcc-api"></a>

**`fcc-api` — selected portion:** Section 3: Starting FastAPI; Path operations.

**Relationship:** Substitute only for FastAPI path operations. Retain the assigned F2 layout/setup reading; a routing explanation alone does not replace it.

<a id="unit-01-fastapi"></a>

**`fastapi` — selected portion:** Consult the relevant example for Request/response models and routing. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-01-roby"></a>

**`roby` — selected portion:** Optional purchase only: use the topic-specific FastAPI section for a demonstrated gap. Individual current lesson IDs/access not verified; no whole-course requirement.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-02"></a>

## 2. Dependency injection and lifecycle

[Return to README Step 2](README.md#2-dependency-injection-and-lifecycle)

**Topic/subtopics:** Depends; dependency overrides; shared HTTP client; lifespan teardown.

**Required sequence:** `dependencies` **THEN** `lifespan` (a different required capability). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `fastapi-testing`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-dependency-injection-and-lifecycle) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B04 · F2](../docs/READING_GUIDE.md#b04)<br>Alireza Parandeh · EN | Book Section | Reference | Dependency injection and lifecycle | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b04) |
| `dependencies` · [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)<br>FastAPI · EN | Documentation / tutorial | Primary | Dependency injection and test seams. | Read FastAPI’s Dependencies introduction and dependency overrides; follow… [bounds](#unit-02-dependencies) |
| `ar-mini-5` · [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Welcome to FastAPI in a working RAG backend. | The linked video only; not its playlist. |
| `lifespan` · [FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/)<br>FastAPI · EN | Documentation / tutorial | Complementary (required) | Initialize and close shared clients predictably. | FastAPI Lifespan: async context manager, initialization and cleanup… [bounds](#unit-02-lifespan) |
| `fastapi-testing` · [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/)<br>FastAPI · EN | Documentation / tutorial | Reference | Swap provider implementations in API tests. | Consult the relevant example for Swap provider implementations in API… [bounds](#unit-02-fastapi-testing) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-dependencies"></a>

**`dependencies` — selected portion:** Read FastAPI’s Dependencies introduction and dependency overrides; follow its lifespan link for startup/teardown. Implement shared-client lifetime yourself using those primitives.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mini-5"></a>

**`ar-mini-5` — selected portion:** Only the linked “Welcome to FastAPI” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: FastAPI orientation only; dependency teardown and override details are in F2/current docs.

<a id="unit-02-lifespan"></a>

**`lifespan` — selected portion:** FastAPI Lifespan: async context manager, initialization and cleanup examples. This complements Depends; it is not the same topic.

**Relationship:** Required after the primary: a distinct capability, not a replacement.

<a id="unit-02-fastapi-testing"></a>

**`fastapi-testing` — selected portion:** Consult the relevant example for Swap provider implementations in API tests. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Modern Python tooling and types

[Return to README Step 3](README.md#3-modern-python-tooling-and-types)

**Topic/subtopics:** Environment; dependency pinning; type hints; Annotated; optional versus nullable.

**Required sequence:** the assigned book slice [B05 · F4](../docs/READING_GUIDE.md#b05) **THEN** `python-types`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-modern-python-tooling-and-types) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B05 · F4](../docs/READING_GUIDE.md#b05)<br>Alireza Parandeh · EN | Book Section | Complementary | Modern Python tooling and types | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b05) |
| `python-types` · [Python typing](https://docs.python.org/3/library/typing.html)<br>Python · EN | Documentation / tutorial | Primary | Type aliases, generics and annotations versus runtime… | Read typing’s Annotated, Optional and basic collection annotations; use… [bounds](#unit-03-python-types) |
| `ar-python` · [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/)<br>Osama Elzero · Egypt · AR video + assignments | Full Course / study-plan index | Complementary (as needed) | Functions, OOP, modules, generators and exceptions: select… | #094 Type Hinting only; Annotated/nullable details still use the typing reference. |
| `cs50-oop` · [CS50P · Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/)<br>Harvard · David Malan · EN video + problem sets | Course unit: lecture + problem set | Complementary (as needed) | Classes, properties and validation; compare with your… | Consult the relevant example for Classes, properties and validation;… [bounds](#unit-03-cs50-oop) |
| `exercism` · [Exercism Python track](https://exercism.org/tracks/python)<br>Exercism · EN | Practice platform / automated exercises | Complementary (as needed) | Small Python exercises with automated tests and community… | One Python exercise matching the diagnostic gap; complete its tests and explain the solution. |
| `ar-python-practice` · [Python assignments](https://elzero.org/category/assignments/python-assignments/)<br>Elzero Web School · AR | Exercise collection | Complementary (as needed) | Topic-indexed Python exercises. | One matching quiz/exercise set for the stated topic; do not complete the whole platform. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-python-types"></a>

**`python-types` — selected portion:** Read typing’s Annotated, Optional and basic collection annotations; use your existing environment setup. This page explains typing, not dependency management.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-python"></a>

**`ar-python` — selected portion:** #094 Type Hinting only; Annotated/nullable details still use the typing reference.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Language/OOP refresher only; use F4/typing docs for Annotated and modern types.

<a id="unit-03-cs50-oop"></a>

**`cs50-oop` — selected portion:** Consult the relevant example for Classes, properties and validation; compare with your Python OOP background. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-exercism"></a>

**`exercism` — selected portion:** One Python exercise matching the diagnostic gap; complete its tests and explain the solution.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-ar-python-practice"></a>

**`ar-python-practice` — selected portion:** One matching quiz/exercise set for the stated topic; do not complete the whole platform.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-04"></a>

## 4. Request and response contracts

[Return to README Step 4](README.md#4-request-and-response-contracts)

**Topic/subtopics:** Pydantic validation; serialization; constraints; strictness; errors.

**Required sequence (default route):** `pydantic`. Stop each source at the stated portion.

**Choose ONE explanation for Pydantic request/response models:** default `pydantic` **OR** `fcc-api`. Use current Pydantic documentation for syntax and strictness in either route. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `fastapi`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-request-and-response-contracts) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B05 · F4](../docs/READING_GUIDE.md#b05)<br>Alireza Parandeh · EN | Book Section | Reference | Request and response contracts | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b05) |
| `pydantic` · [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)<br>Pydantic · EN | Documentation / tutorial | Primary | Validation, coercion, strictness and serialization. | Consult the Pydantic validation; serialization; constraints; strictness;… [bounds](#unit-04-pydantic) |
| `ar-api` · [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)<br>Pythonation · Arabic Python community · AR video + code | Single Video + companion repository | Complementary (as needed) | Turn Python functions into validated HTTP endpoints and… | Consult the relevant example for Turn Python functions into validated HTTP… [bounds](#unit-04-ar-api) |
| `ar-mini-5` · [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Welcome to FastAPI in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | Request and response contracts (selected course unit) | Section 3: Schema Validation with Pydantic; Section 7: Response Model. |
| `fastapi` · [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)<br>FastAPI · EN | Documentation / tutorial | Reference | Request/response models and routing. | Consult the relevant example for Request/response models and routing.… [bounds](#unit-04-fastapi) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-pydantic"></a>

**`pydantic` — selected portion:** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-api"></a>

**`ar-api` — selected portion:** Consult the relevant example for Turn Python functions into validated HTTP endpoints and inspect the companion app. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-ar-mini-5"></a>

**`ar-mini-5` — selected portion:** Only the linked “Welcome to FastAPI” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-fcc-api"></a>

**`fcc-api` — selected portion:** Section 3: Schema Validation with Pydantic; Section 7: Response Model.

**Relationship:** Substitute only for Pydantic request/response models. Use current Pydantic documentation for syntax and strictness in either route.

<a id="unit-04-fastapi"></a>

**`fastapi` — selected portion:** Consult the relevant example for Request/response models and routing. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Iteration and resource cleanup

[Return to README Step 5](README.md#5-iteration-and-resource-cleanup)

**Topic/subtopics:** Generators; batching; with; context managers; exceptions.

**Required sequence:** `python-context`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-iteration-and-resource-cleanup) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `python-context` · [Context managers](https://docs.python.org/3/library/contextlib.html)<br>Python · EN | Documentation / tutorial | Primary | Resource cleanup with contextmanager and… | Read contextmanager/asynccontextmanager and closing/aclosing examples.… [bounds](#unit-05-python-context) |
| `ar-python` · [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/)<br>Osama Elzero · Egypt · AR video + assignments | Full Course / study-plan index | Complementary (as needed) | Functions, OOP, modules, generators and exceptions: select… | #081 Iterable Vs Iterator; #082 Generators; #090–092 exceptions. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-python-context"></a>

**`python-context` — selected portion:** Read contextmanager/asynccontextmanager and closing/aclosing examples. Review Python generators only if the diagnostic shows a gap; batching is your exercise, not a contextlib API.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-python"></a>

**`ar-python` — selected portion:** #081 Iterable Vs Iterator; #082 Generators; #090–092 exceptions.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-06"></a>

## 6. Deterministic service tests

[Return to README Step 6](README.md#6-deterministic-service-tests)

**Topic/subtopics:** Fixtures; parametrization; mocks; API contracts; error branches.

**Required sequence:** the assigned book slice [B06 · F11](../docs/READING_GUIDE.md#b06) **THEN** `cs50-tests`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `pytest`, `fastapi-testing`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-deterministic-service-tests) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B06 · F11](../docs/READING_GUIDE.md#b06)<br>Alireza Parandeh · EN | Book Section | Complementary | Deterministic service tests | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b06) |
| `cs50-tests` · [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)<br>Harvard · David Malan · EN video + problem sets | Course unit: lecture + problem set | Primary | pytest, assertions and test-driven reasoning; do the… | Week 5 “Unit Tests”: lecture sections on assert/pytest and associated… [bounds](#unit-06-cs50-tests) |
| `ar-python` · [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/)<br>Osama Elzero · Egypt · AR video + assignments | Full Course / study-plan index | Complementary (as needed) | Functions, OOP, modules, generators and exceptions: select… | #090–092 exceptions only as prerequisite review. Does not teach pytest fixtures or HTTP tests. |
| `pytest` · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)<br>pytest · EN | Documentation / tutorial | Reference | Fixtures, scope, teardown and dependency isolation. | Consult the relevant example for Fixtures, scope, teardown and dependency… [bounds](#unit-06-pytest) |
| `fastapi-testing` · [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/)<br>FastAPI · EN | Documentation / tutorial | Reference | Swap provider implementations in API tests. | Consult the relevant example for Swap provider implementations in API… [bounds](#unit-06-fastapi-testing) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-cs50-tests"></a>

**`cs50-tests` — selected portion:** Week 5 “Unit Tests”: lecture sections on assert/pytest and associated problem-set tasks for your diagnostic gaps.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-python"></a>

**`ar-python` — selected portion:** #090–092 exceptions only as prerequisite review. Does not teach pytest fixtures or HTTP tests.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: General Python preparation; pytest fixtures/mocking use the English testing path.

<a id="unit-06-pytest"></a>

**`pytest` — selected portion:** Consult the relevant example for Fixtures, scope, teardown and dependency isolation. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-06-fastapi-testing"></a>

**`fastapi-testing` — selected portion:** Consult the relevant example for Swap provider implementations in API tests. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-python"></a>

<details>
<summary>ar-python · Mastering Python study plan — access, scope and verification</summary>

[Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) · Osama Elzero · Egypt · AR video + assignments

- **Resource Type:** Full Course / study-plan index.
- **Access:** Free.
- **Catalog scope:** Functions, OOP, modules, generators and exceptions: select only diagnostic gaps.
- **Scope/version limits:** Skip the beginner sequence after passing L00.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Modern Python tooling and types; Iteration and resource cleanup; Deterministic service tests.
- **Retained broad selection notes (lookup only):** Only lessons #081 Iterable Vs Iterator, #082 Generators, #090–092 exceptions and #094 Type Hinting if the diagnostic shows a gap. OOP #103–116 is remediation only.

</details>

<a id="r-python-types"></a>

<details>
<summary>python-types · Python typing — access, scope and verification</summary>

[Python typing](https://docs.python.org/3/library/typing.html) · Python · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Type aliases, generics and annotations versus runtime checking.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Modern Python tooling and types.
- **Retained broad selection notes (lookup only):** Read typing’s Annotated, Optional and basic collection annotations; use your existing environment setup. This page explains typing, not dependency management.

</details>

<a id="r-cs50-oop"></a>

<details>
<summary>cs50-oop · CS50P · Object-Oriented Programming — access, scope and verification</summary>

[CS50P · Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/) · Harvard · David Malan · EN video + problem sets

- **Resource Type:** Course unit: lecture + problem set.
- **Access:** Free.
- **Catalog scope:** Classes, properties and validation; compare with your Python OOP background.
- **Scope/version limits:** Remediation only, not mandatory replay.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Modern Python tooling and types.
- **Retained broad selection notes (lookup only):** Week 8: classes, properties and validation only if OOP diagnostics fail; otherwise skip.

</details>

<a id="r-ar-api"></a>

<details>
<summary>ar-api · Pythonation FastAPI tutorial and companion code — access, scope and verification</summary>

[Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) · Pythonation · Arabic Python community · AR video + code

- **Resource Type:** Single Video + companion repository.
- **Access:** Free.
- **Catalog scope:** Turn Python functions into validated HTTP endpoints and inspect the companion app.
- **Scope/version limits:** Introductory; lifecycle, production security and async depth need the official docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Request and response contracts.
- **Retained broad selection notes (lookup only):** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-5"></a>

<details>
<summary>ar-mini-5 · mini-RAG · Welcome to FastAPI — access, scope and verification</summary>

[mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Welcome to FastAPI in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Request and response contracts; Dependency injection and lifecycle.
- **Retained broad selection notes (lookup only):** Only the linked “Welcome to FastAPI” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-fcc-api"></a>

<details>
<summary>fcc-api · Creating APIs with Python · course index — access, scope and verification</summary>

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) · Sanjeev Thiyagarajan · freeCodeCamp · EN video

- **Resource Type:** Full Course (19 hours; selected sections only).
- **Access:** Free.
- **Catalog scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Scope/version limits:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Request and response contracts; Routes and application boundaries.
- **Retained broad selection notes (lookup only):** Section 3: Starting FastAPI, Path operations, Schema Validation with Pydantic; Section 7: Response Model; Section 16: Fixtures, Parametrize, FastAPI TestClient.

</details>

<a id="r-pydantic"></a>

<details>
<summary>pydantic · Pydantic models — access, scope and verification</summary>

[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) · Pydantic · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Validation, coercion, strictness and serialization.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Request and response contracts.
- **Retained broad selection notes (lookup only):** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-fastapi"></a>

<details>
<summary>fastapi · FastAPI tutorial — access, scope and verification</summary>

[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Request/response models and routing.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Request and response contracts; Routes and application boundaries.
- **Retained broad selection notes (lookup only):** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-4"></a>

<details>
<summary>ar-mini-4 · mini-RAG · Project Architecture — access, scope and verification</summary>

[mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Project Architecture in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Routes and application boundaries.
- **Retained broad selection notes (lookup only):** Only the linked “Project Architecture” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-mini-6"></a>

<details>
<summary>ar-mini-6 · mini-RAG · Nested Routes + Env Values — access, scope and verification</summary>

[mini-RAG · Nested Routes + Env Values](https://www.youtube.com/watch?v=CrR2Bz2Y7Hw&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=6) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Nested Routes + Env Values in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Routes and application boundaries.
- **Retained broad selection notes (lookup only):** Only the linked “Nested Routes + Env Values” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-dependencies"></a>

<details>
<summary>dependencies · FastAPI dependencies — access, scope and verification</summary>

[FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Dependency injection and test seams.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Dependency injection and lifecycle.
- **Retained broad selection notes (lookup only):** Read FastAPI’s Dependencies introduction and dependency overrides; follow its lifespan link for startup/teardown. Implement shared-client lifetime yourself using those primitives.

</details>

<a id="r-lifespan"></a>

<details>
<summary>lifespan · FastAPI lifespan — access, scope and verification</summary>

[FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Initialize and close shared clients predictably.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Dependency injection and lifecycle.
- **Retained broad selection notes (lookup only):** Consult the Depends; dependency overrides; shared HTTP client; lifespan teardown sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-fastapi-testing"></a>

<details>
<summary>fastapi-testing · Testing dependencies with overrides — access, scope and verification</summary>

[Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Swap provider implementations in API tests.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Dependency injection and lifecycle; Deterministic service tests.
- **Retained broad selection notes (lookup only):** Consult the Depends; dependency overrides; shared HTTP client; lifespan teardown sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-python-context"></a>

<details>
<summary>python-context · Context managers — access, scope and verification</summary>

[Context managers](https://docs.python.org/3/library/contextlib.html) · Python · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Resource cleanup with contextmanager and asynccontextmanager.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Iteration and resource cleanup.
- **Retained broad selection notes (lookup only):** Read contextmanager/asynccontextmanager and closing/aclosing examples. Review Python generators only if the diagnostic shows a gap; batching is your exercise, not a contextlib API.

</details>

<a id="r-cs50-tests"></a>

<details>
<summary>cs50-tests · CS50P · Unit Tests — access, scope and verification</summary>

[CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) · Harvard · David Malan · EN video + problem sets

- **Resource Type:** Course unit: lecture + problem set.
- **Access:** Free.
- **Catalog scope:** pytest, assertions and test-driven reasoning; do the associated exercises.
- **Scope/version limits:** Skip unrelated beginner lectures.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Deterministic service tests.
- **Retained broad selection notes (lookup only):** Week 5 “Unit Tests”: lecture sections on assert/pytest and associated problem-set tasks for your diagnostic gaps.

</details>

<a id="r-pytest"></a>

<details>
<summary>pytest · pytest fixtures — access, scope and verification</summary>

[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · pytest · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Fixtures, scope, teardown and dependency isolation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Deterministic service tests.
- **Retained broad selection notes (lookup only):** Consult the Fixtures; parametrization; mocks; API contracts; error branches sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-roby"></a>

<details>
<summary>roby · FastAPI — The Complete Course — access, scope and verification</summary>

[FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) · Eric Roby and Chad Darby · EN video

- **Resource Type:** Full Course (paid).
- **Access:** Paid · variable regional/subscription pricing.
- **Catalog scope:** Alternative guided backend course for validation, persistence, auth and tests.
- **Scope/version limits:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Alternative only: validation/dependencies/testing sections matching L01. Exact current lesson numbers were not verified; no full-course assignment.

</details>

<a id="r-exercism"></a>

<details>
<summary>exercism · Exercism Python track — access, scope and verification</summary>

[Exercism Python track](https://exercism.org/tracks/python) · Exercism · EN

- **Resource Type:** Practice platform / automated exercises.
- **Access:** Free.
- **Catalog scope:** Small Python exercises with automated tests and community feedback.
- **Scope/version limits:** Choose typing, iteration and error-handling gaps, not hundreds of exercises.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Choose one iteration/error-handling exercise matching the failed Python diagnostic. No full-track requirement.

</details>

<a id="r-ar-python-practice"></a>

<details>
<summary>ar-python-practice · Python assignments — access, scope and verification</summary>

[Python assignments](https://elzero.org/category/assignments/python-assignments/) · Elzero Web School · AR

- **Resource Type:** Exercise collection.
- **Access:** Free.
- **Catalog scope:** Topic-indexed Python exercises.
- **Scope/version limits:** Self-checked assignments; not an externally proctored assessment.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Assignments paired with the chosen #081–094 lessons; do not restart the full study plan.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

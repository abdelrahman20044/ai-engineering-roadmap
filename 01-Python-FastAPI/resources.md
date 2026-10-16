# Resource Library · L01 — Python, FastAPI, and Service Testing

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

## Book references

Assigned reading is authoritative in [the master order for L01](../docs/READING_GUIDE.md#l01). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B04 · F2](../docs/READING_GUIDE.md#b04), [B05 · F4](../docs/READING_GUIDE.md#b05), [B06 · F11](../docs/READING_GUIDE.md#b06).

## Arabic and Egyptian teaching

<a id="r-ar-python"></a>

### Mastering Python study plan

[Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/)

- **Resource Type:** Full video course / study-plan index.
- **Role:** Alternative. **Language:** AR video + assignments. **By:** Osama Elzero · Egypt.
- **Access:** Free.
- **Use for:** Modern Python tooling and types; Iteration and resource cleanup; Deterministic service tests.
- **Assigned portion:** Only lessons #081 Iterable Vs Iterator, #082 Generators, #090–092 exceptions and #094 Type Hinting if the diagnostic shows a gap. OOP #103–116 is remediation only.
- **Scope:** Functions, OOP, modules, generators and exceptions: select only diagnostic gaps.
- **Limit:** Skip the beginner sequence after passing L00.

**Arabic scope note:** Language/OOP refresher only; use F4/typing docs for Annotated and modern types. General Python preparation; pytest fixtures/mocking use the English testing path.

<a id="r-ar-api"></a>

### Pythonation FastAPI tutorial and companion code

[Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)

- **Resource Type:** Single video + companion repository.
- **Role:** Alternative. **Language:** AR video + code. **By:** Pythonation · Arabic Python community.
- **Access:** Free.
- **Use for:** Request and response contracts.
- **Assigned portion:** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.
- **Scope:** Turn Python functions into validated HTTP endpoints and inspect the companion app.
- **Limit:** Introductory; lifecycle, production security and async depth need the official docs.

<a id="r-ar-mini-5"></a>

### mini-RAG · Welcome to FastAPI

[mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Request and response contracts; Dependency injection and lifecycle.
- **Assigned portion:** Only the linked “Welcome to FastAPI” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Welcome to FastAPI in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** FastAPI orientation only; dependency teardown and override details are in F2/current docs.

<a id="r-ar-mini-4"></a>

### mini-RAG · Project Architecture

[mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Routes and application boundaries.
- **Assigned portion:** Only the linked “Project Architecture” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Project Architecture in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

<a id="r-ar-mini-6"></a>

### mini-RAG · Nested Routes + Env Values

[mini-RAG · Nested Routes + Env Values](https://www.youtube.com/watch?v=CrR2Bz2Y7Hw&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=6)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Primary. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Routes and application boundaries.
- **Assigned portion:** Only the linked “Nested Routes + Env Values” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Nested Routes + Env Values in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

## English video and guided courses

<a id="r-cs50-oop"></a>

### CS50P · Object-Oriented Programming

[CS50P · Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/)

- **Resource Type:** Course unit: lecture + problem set.
- **Role:** Alternative. **Language:** EN video + problem sets. **By:** Harvard · David Malan.
- **Access:** Free.
- **Use for:** Modern Python tooling and types.
- **Assigned portion:** Week 8: classes, properties and validation only if OOP diagnostics fail; otherwise skip.
- **Scope:** Classes, properties and validation; compare with your Python OOP background.
- **Limit:** Remediation only, not mandatory replay.

<a id="r-fcc-api"></a>

### Creating APIs with Python · course index

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)

- **Resource Type:** Full video course (19 hours; selected sections only).
- **Role:** Alternative. **Language:** EN video. **By:** Sanjeev Thiyagarajan · freeCodeCamp.
- **Access:** Free.
- **Use for:** Request and response contracts; Routes and application boundaries.
- **Assigned portion:** Section 3: Starting FastAPI, Path operations, Schema Validation with Pydantic; Section 7: Response Model; Section 16: Fixtures, Parametrize, FastAPI TestClient.
- **Scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Limit:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.

<a id="r-cs50-tests"></a>

### CS50P · Unit Tests

[CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)

- **Resource Type:** Course unit: lecture + problem set.
- **Role:** Primary. **Language:** EN video + problem sets. **By:** Harvard · David Malan.
- **Access:** Free.
- **Use for:** Deterministic service tests.
- **Assigned portion:** Week 5 “Unit Tests”: lecture sections on assert/pytest and associated problem-set tasks for your diagnostic gaps.
- **Scope:** pytest, assertions and test-driven reasoning; do the associated exercises.
- **Limit:** Skip unrelated beginner lectures.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

<a id="r-roby"></a>

### FastAPI — The Complete Course

[FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)

- **Resource Type:** Paid full video course.
- **Role:** Optional Advanced. **Language:** EN video. **By:** Eric Roby and Chad Darby.
- **Access:** Paid · variable regional/subscription pricing.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Alternative only: validation/dependencies/testing sections matching L01. Exact current lesson numbers were not verified; no full-course assignment.
- **Scope:** Alternative guided backend course for validation, persistence, auth and tests.
- **Limit:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python.

## Practice, labs and quizzes

<a id="r-exercism"></a>

### Exercism Python track

[Exercism Python track](https://exercism.org/tracks/python)

- **Resource Type:** Practice platform / automated exercises.
- **Role:** Alternative. **Language:** EN. **By:** Exercism.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Choose one iteration/error-handling exercise matching the failed Python diagnostic. No full-track requirement.
- **Scope:** Small Python exercises with automated tests and community feedback.
- **Limit:** Choose typing, iteration and error-handling gaps, not hundreds of exercises.

<a id="r-ar-python-practice"></a>

### Python assignments

[Python assignments](https://elzero.org/category/assignments/python-assignments/)

- **Resource Type:** Exercise collection.
- **Role:** Alternative. **Language:** AR. **By:** Elzero Web School.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Assignments paired with the chosen #081–094 lessons; do not restart the full study plan.
- **Scope:** Topic-indexed Python exercises.
- **Limit:** Self-checked assignments; not an externally proctored assessment.

## Official documentation and engineering articles

<a id="r-python-types"></a>

### Python typing

[Python typing](https://docs.python.org/3/library/typing.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Python.
- **Access:** Free.
- **Use for:** Modern Python tooling and types.
- **Assigned portion:** Read typing’s Annotated, Optional and basic collection annotations; use your existing environment setup. This page explains typing, not dependency management.
- **Scope:** Type aliases, generics and annotations versus runtime checking.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pydantic"></a>

### Pydantic models

[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Pydantic.
- **Access:** Free.
- **Use for:** Request and response contracts.
- **Assigned portion:** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.
- **Scope:** Validation, coercion, strictness and serialization.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-fastapi"></a>

### FastAPI tutorial

[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Request and response contracts; Routes and application boundaries.
- **Assigned portion:** Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.
- **Scope:** Request/response models and routing.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-dependencies"></a>

### FastAPI dependencies

[FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Dependency injection and lifecycle.
- **Assigned portion:** Read FastAPI’s Dependencies introduction and dependency overrides; follow its lifespan link for startup/teardown. Implement shared-client lifetime yourself using those primitives.
- **Scope:** Dependency injection and test seams.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-lifespan"></a>

### FastAPI lifespan

[FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Dependency injection and lifecycle.
- **Assigned portion:** Consult the Depends; dependency overrides; shared HTTP client; lifespan teardown sections/examples only. Do not read the entire documentation site.
- **Scope:** Initialize and close shared clients predictably.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-fastapi-testing"></a>

### Testing dependencies with overrides

[Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** Dependency injection and lifecycle; Deterministic service tests.
- **Assigned portion:** Consult the Depends; dependency overrides; shared HTTP client; lifespan teardown sections/examples only. Do not read the entire documentation site.
- **Scope:** Swap provider implementations in API tests.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-python-context"></a>

### Context managers

[Context managers](https://docs.python.org/3/library/contextlib.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Python.
- **Access:** Free.
- **Use for:** Iteration and resource cleanup.
- **Assigned portion:** Read contextmanager/asynccontextmanager and closing/aclosing examples. Review Python generators only if the diagnostic shows a gap; batching is your exercise, not a contextlib API.
- **Scope:** Resource cleanup with contextmanager and asynccontextmanager.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pytest"></a>

### pytest fixtures

[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** pytest.
- **Access:** Free.
- **Use for:** Deterministic service tests.
- **Assigned portion:** Consult the Fixtures; parametrization; mocks; API contracts; error branches sections/examples only. Do not read the entire documentation site.
- **Scope:** Fixtures, scope, teardown and dependency isolation.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

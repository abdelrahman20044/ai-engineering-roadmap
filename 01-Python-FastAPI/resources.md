# Resource Library · L01 — Python, FastAPI, and Service Testing

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

F2/F4 selective reading → mini-RAG lessons 5–6 or CS50 testing → a fake-provider API. Add pytest from the first endpoint.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) | Osama Elzero · Egypt<br>AR video + assignments<br>Free | L01-T01 · Modern Python tooling and types; L01-T05 · Iteration and resource cleanup; L01-T06 · Deterministic service tests | Functions, OOP, modules, generators and exceptions: select only diagnostic gaps. **Boundary:** Skip the beginner sequence after passing L00. |
| [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) | Pythonation · Arabic Python community<br>AR video + code<br>Free | L01-T02 · Request and response contracts | Turn Python functions into validated HTTP endpoints and inspect the companion app. **Boundary:** Introductory; lifecycle, production security and async depth need the official docs. |
| [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L01-T02 · Request and response contracts; L01-T04 · Dependency injection and lifecycle | Welcome to FastAPI in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L01-T03 · Routes and application boundaries | Project Architecture in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Nested Routes + Env Values](https://www.youtube.com/watch?v=CrR2Bz2Y7Hw&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=6) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L01-T03 · Routes and application boundaries | Nested Routes + Env Values in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [CS50P · Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/) | Harvard · David Malan<br>EN video + problem sets<br>Free | L01-T01 · Modern Python tooling and types | Classes, properties and validation; compare with your Python OOP background. **Boundary:** Remediation only, not mandatory replay. |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L01-T02 · Request and response contracts; L01-T03 · Routes and application boundaries | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |
| [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) | Harvard · David Malan<br>EN video + problem sets<br>Free | L01-T06 · Deterministic service tests | pytest, assertions and test-driven reasoning; do the associated exercises. **Boundary:** Skip unrelated beginner lectures. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) | Eric Roby and Chad Darby<br>EN video<br>Paid · variable regional/subscription pricing | Optional support for this Level’s assessed exercises | Alternative guided backend course for validation, persistence, auth and tests. **Boundary:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python. |

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| F2, PDF43–82: server, Depends, lifespan, and project structure; skim familiar framework comparisons. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F4, PDF153–186: annotations, Annotated, Pydantic validators, serialization, and settings; skim primitive types. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F11, PDF500–518: pytest, fixtures, parameterization, async tests, and mocking; revisit as needed. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| FastAPI documentation: types, request/response models, dependencies, and testing. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Exercism Python track](https://exercism.org/tracks/python) | Exercism<br>EN<br>Free | Optional support for this Level’s assessed exercises | Small Python exercises with automated tests and community feedback. **Boundary:** Choose typing, iteration and error-handling gaps, not hundreds of exercises. |
| [Python assignments](https://elzero.org/category/assignments/python-assignments/) | Elzero Web School<br>AR<br>Free | Optional support for this Level’s assessed exercises | Topic-indexed Python exercises. **Boundary:** Self-checked assignments; not an externally proctored assessment. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L01-T01 | Type a provider interface and explain what is checked statically versus at runtime. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L01-T02 | Reject missing, malformed and unexpected values with an explicit response contract. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L01-T03 | Create /health and /reflect with application logic outside the route handler. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L01-T04 | Swap providers in a test and assert the lifespan client closes after shutdown. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L01-T05 | Batch a record iterator and prove cleanup when its consumer raises. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L01-T06 | Run validation, provider-error and dependency-override tests with no external calls. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Python typing](https://docs.python.org/3/library/typing.html) | Python<br>EN<br>Free | L01-T01 · Modern Python tooling and types | Type aliases, generics and annotations versus runtime checking. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | Pydantic<br>EN<br>Free | L01-T02 · Request and response contracts | Validation, coercion, strictness and serialization. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | FastAPI<br>EN<br>Free | L01-T02 · Request and response contracts; L01-T03 · Routes and application boundaries | Request/response models and routing. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) | FastAPI<br>EN<br>Free | L01-T04 · Dependency injection and lifecycle | Dependency injection and test seams. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/) | FastAPI<br>EN<br>Free | L01-T04 · Dependency injection and lifecycle | Initialize and close shared clients predictably. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) | FastAPI<br>EN<br>Free | L01-T04 · Dependency injection and lifecycle; L01-T06 · Deterministic service tests | Swap provider implementations in API tests. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Context managers](https://docs.python.org/3/library/contextlib.html) | Python<br>EN<br>Free | L01-T05 · Iteration and resource cleanup | Resource cleanup with contextmanager and asynccontextmanager. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | pytest<br>EN<br>Free | L01-T06 · Deterministic service tests | Fixtures, scope, teardown and dependency isolation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

# M01 — Python, FastAPI, and Service Testing

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P0 |
| Prerequisites | [M00](../m00-orientation/README.md) |
| Personal effort | 14–20 focused hours; not official ITI hours |
| Project milestone | [S1](../../project/milestones/s1.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Use type hints, Pydantic, dependency injection, and lifespan management. |
| O2 | Separate HTTP handlers from application logic and test the service. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N02 | Advanced Python Programming for AI Engineers | 30 |
| N05 | Software Testing & Full-Stack Debugging | 30 |
| N07 | RESTful API, Backend Architecture & Security | 36 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | F2, PDF 43–82: server, Depends, lifespan, and project structure; skim familiar framework comparisons. |
| 2 | F4, PDF 153–186: annotations, Annotated, Pydantic validators, serialization, and settings; skim primitive types. |
| 3 | F11, PDF 500–518: pytest, fixtures, parameterization, async tests, and mocking; revisit as needed. |
| 4 | FastAPI documentation: types, request/response models, dependencies, and testing. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M01-E1 | Implement /health and POST /reflect with an explicitly fake provider. Test valid, missing, invalid, and provider-timeout cases. | Tests make no live model calls and assert documented responses. |
| M01-E2 | Write a context manager for a resource and a generator for batched records. | An exception triggers cleanup; batches preserve the expected records. |
| M01-E3 | Replace the provider using a dependency override. | The API contract stays the same when fake and real adapters are swapped. |
| M01-E4 | Explain annotations versus runtime validation and def versus async def. Add one endpoint without copying a solution. | Demonstrate the distinction with a failing validation case; deepen concurrency in M10. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Application skeleton in a separate implementation repository; Tests, pinned dependencies, and setup instructions |
| Pass condition | A clean checkout runs the API and tests. Provider failures have defined responses, and you can add and test a small feature independently. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M01 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| A complete Python beginner course if diagnostics pass |
| Agent frameworks and elaborate class hierarchies |

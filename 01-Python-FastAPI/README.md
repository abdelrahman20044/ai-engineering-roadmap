# L01 · Python, FastAPI, and Service Testing

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 1 · Engineering and Model Foundations | 14–20 h | 2/5 | P0 | [L00](../00-Orientation/README.md) |

**Outcome:** Use type hints, Pydantic, dependency injection, and lifespan management. Separate HTTP handlers from application logic and test the service.

**Unlocks:** [L04](../04-LLM-Applications-Prompts/README.md), [L06](../06-Application-State/README.md), [L18](../18-Supporting-Frontend/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Typing and validation | F4 PDF153–186; [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | [Practice 1](resources.md#practice-and-evidence) |
| Dependencies and lifecycle | F2 PDF43–82; [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 2](resources.md#practice-and-evidence) |
| Generators and cleanup | F4 selected Python sections; [Python tutorial: classes and generators](https://docs.python.org/3/tutorial/classes.html) | [Practice 3](resources.md#practice-and-evidence) |
| Fixtures and service tests | F11 PDF500–518; [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N02** — Advanced Python Programming for AI Engineers.
- **N05** — Software Testing & Full-Stack Debugging.
- **N07** — RESTful API, Backend Architecture & Security.

| ITI topic IDs | Interpretation |
| --- | --- |
| N02, N05, N07 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L01-E1 | Implement /health and POST /reflect with an explicitly fake provider. Test valid, missing, invalid, and provider-timeout cases. | Tests make no live model calls and assert documented responses. |
| L01-E2 | Write a context manager for a resource and a generator for batched records. | An exception triggers cleanup; batches preserve the expected records. |
| L01-E3 | Replace the provider using a dependency override. | The API contract stays the same when fake and real adapters are swapped. |
| L01-E4 | Explain annotations versus runtime validation and def versus async def. Add one endpoint without copying a solution. | Demonstrate the distinction with a failing validation case; deepen concurrency in L10. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S1](../project/milestones/s1.md) | Application skeleton in a separate implementation repository; Tests, pinned dependencies, and setup instructions | A clean checkout runs the API and tests. Provider failures have defined responses, and you can add and test a small feature independently. |

## Postpone

| Outside this level |
| --- |
| A complete Python beginner course if diagnostics pass |
| Agent frameworks and elaborate class hierarchies |

## Record completion

```bash
python scripts/progress.py set L01 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L00](../00-Orientation/README.md) · Next numbered Level: [L02](../02-Mathematics-ML/README.md). Follow the prerequisite table if branches differ.

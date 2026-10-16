# Technical Details · L01

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Python transfer:** Use functions, OOP, exceptions, modules and virtual environments without a beginner walkthrough.
- **HTTP transfer:** Explain status codes, validation and middleware from Express.
- **Testing transfer:** Write one success and one failure assertion independently.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Routes and application boundaries:** APIRouter; config; handlers versus services; fake provider.
- **Dependency injection and lifecycle:** Depends; dependency overrides; shared HTTP client; lifespan teardown.
- **Modern Python tooling and types:** Environment; dependency pinning; type hints; Annotated; optional versus nullable.
- **Request and response contracts:** Pydantic validation; serialization; constraints; strictness; errors.
- **Iteration and resource cleanup:** Generators; batching; with; context managers; exceptions.
- **Deterministic service tests:** Fixtures; parametrization; mocks; API contracts; error branches.

## Common mistakes and debugging

### Annotations treated as validation

Show a plain typed function accepting a bad value and a Pydantic model rejecting it.

### One global mutable client/session

Initialize shared clients in lifespan; use request/task-specific state.

### Tests call a paid model

Override the provider and make tests deterministic.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Why Depends rather than manual construction in every route?
2. Does async make CPU work faster?
3. What must cleanup prove?

<details>
<summary>Answer guide</summary>

**Why Depends rather than manual construction in every route?**

It provides a declared lifecycle and an override seam while keeping application logic testable.

**Does async make CPU work faster?**

No; it enables cooperative I/O concurrency. CPU work needs a different execution boundary.

**What must cleanup prove?**

Resources close on both success and exceptions; tests verify the teardown.

</details>

## ITI provenance and industry extensions

- **N02:** Advanced Python Programming for AI Engineers — official published module title.
- **N05:** Software Testing & Full-Stack Debugging — official published module title.
- **N07:** RESTful API, Backend Architecture & Security — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Create /health and /reflect with application logic outside the route handler.
- [ ] Swap providers in a test and assert the lifespan client closes after shutdown.
- [ ] Type a provider interface and explain what is checked statically versus at runtime.
- [ ] Reject missing, malformed and unexpected values with an explicit response contract.
- [ ] Batch a record iterator and prove cleanup when its consumer raises.
- [ ] Run validation, provider-error and dependency-override tests with no external calls.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

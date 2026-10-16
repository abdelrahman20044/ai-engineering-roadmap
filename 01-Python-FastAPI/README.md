# L01 · Python, FastAPI, and Service Testing

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 1 · 14–20 focused hours · Difficulty 2/5 · P0**

**You will learn:** Use type hints, Pydantic, dependency injection, and lifespan management. Separate HTTP handlers from application logic and test the service.

**Before starting:** [L00](../00-Orientation/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B04 · F2](../docs/READING_GUIDE.md#b04) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Routes and application boundaries

**Learn:** APIRouter; config; handlers versus services; fake provider.

**Required reading:**

- [B04 · F2](../docs/READING_GUIDE.md#b04) — **Read Now**. PDF pp.43–82: server setup, Depends, lifespan and project boundaries. Skim familiar HTTP/framework comparisons.

**Primary · Single video (lesson within playlist):** [mini-RAG · Nested Routes + Env Values](https://www.youtube.com/watch?v=CrR2Bz2Y7Hw&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=6). Only the linked “Nested Routes + Env Values” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Create /health and /reflect with application logic outside the route handler.

**Completion check:** A clean checkout serves /health and /reflect with a fake provider.

[Alternative · AR video](resources.md#r-ar-mini-4) (optional) · [Implementation reference](resources.md#r-fastapi)

### 2. Dependency injection and lifecycle

**Learn:** Depends; dependency overrides; shared HTTP client; lifespan teardown.

**Required reading:**

- [B04 · F2](../docs/READING_GUIDE.md#b04) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/). Read FastAPI’s Dependencies introduction and dependency overrides; follow its lifespan link for startup/teardown. Implement shared-client lifetime yourself using those primitives.

**Practice:** Swap providers in a test and assert the lifespan client closes after shutdown.

**Completion check:** An override swaps providers and shutdown closes the shared client.

[Alternative · AR video](resources.md#r-ar-mini-5) (optional) · [Implementation reference](resources.md#r-lifespan)

### 3. Modern Python tooling and types

**Learn:** Environment; dependency pinning; type hints; Annotated; optional versus nullable.

**Required reading:**

- [B05 · F4](../docs/READING_GUIDE.md#b05) — **Read Now**. PDF pp.153–186: annotations, Annotated, Pydantic constraints/serialization/settings. Skim primitive Python types.

**Primary · Official documentation / tutorial:** [Python typing](https://docs.python.org/3/library/typing.html). Read typing’s Annotated, Optional and basic collection annotations; use your existing environment setup. This page explains typing, not dependency management.

**Practice:** Type a provider interface and explain what is checked statically versus at runtime.

**Completion check:** Explain why annotation alone does not reject an invalid value.

[Alternative · AR video + assignments](resources.md#r-ar-python) (optional)

### 4. Request and response contracts

**Learn:** Pydantic validation; serialization; constraints; strictness; errors.

**Required reading:**

- [B05 · F4](../docs/READING_GUIDE.md#b05) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/). Consult the Pydantic validation; serialization; constraints; strictness; errors sections/examples only. Do not read the entire documentation site.

**Practice:** Reject missing, malformed and unexpected values with an explicit response contract.

**Completion check:** Malformed and missing fields return documented errors.

[Alternative · AR video + code](resources.md#r-ar-api) (optional) · [Implementation reference](resources.md#r-fastapi)

### 5. Iteration and resource cleanup

**Learn:** Generators; batching; with; context managers; exceptions.

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Official documentation / tutorial:** [Context managers](https://docs.python.org/3/library/contextlib.html). Read contextmanager/asynccontextmanager and closing/aclosing examples. Review Python generators only if the diagnostic shows a gap; batching is your exercise, not a contextlib API.

**Practice:** Batch a record iterator and prove cleanup when its consumer raises.

**Completion check:** An exception still runs cleanup; batching loses no records.

[Alternative · AR video + assignments](resources.md#r-ar-python) (optional)

### 6. Deterministic service tests

**Learn:** Fixtures; parametrization; mocks; API contracts; error branches.

**Required reading:**

- [B06 · F11](../docs/READING_GUIDE.md#b06) — **Read Now**. PDF pp.501–518: unit tests, pytest fixtures/parametrization, async tests and doubles. Other Chapter 11 sections are later assignments.

**Primary · Course unit: lecture + problem set:** [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/). Week 5 “Unit Tests”: lecture sections on assert/pytest and associated problem-set tasks for your diagnostic gaps.

**Practice:** Run validation, provider-error and dependency-override tests with no external calls.

**Completion check:** Tests cover validation, provider errors and an override without live calls.

[Alternative · AR video + assignments](resources.md#r-ar-python) (optional) · [Implementation reference](resources.md#r-pytest)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L01-E1:** Implement /health and POST /reflect with an explicitly fake provider. Test valid, missing, invalid, and provider-timeout cases.
  - **Pass:** Tests make no live model calls and assert documented responses.
- [ ] **L01-E2:** Write a context manager for a resource and a generator for batched records.
  - **Pass:** An exception triggers cleanup; batches preserve the expected records.
- [ ] **L01-E3:** Replace the provider using a dependency override.
  - **Pass:** The API contract stays the same when fake and real adapters are swapped.
- [ ] **L01-E4:** Explain annotations versus runtime validation and def versus async def. Add one endpoint without copying a solution.
  - **Pass:** Demonstrate the distinction with a failing validation case; deepen concurrency in L10.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S1](../project/milestones/s1.md). A clean checkout runs the API and tests. Provider failures have defined responses, and you can add and test a small feature independently.

**Keep:** Application skeleton in a separate implementation repository; Tests, pinned dependencies, and setup instructions.

## What to defer

- A complete Python beginner course if diagnostics pass
- Agent frameworks and elaborate class hierarchies

## Record progress and choose the next Level

```bash
python scripts/progress.py set L01 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L04](../04-LLM-Applications-Prompts/README.md), [L06](../06-Application-State/README.md), [L18](../18-Supporting-Frontend/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

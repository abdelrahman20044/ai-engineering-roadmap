# Technical Details · L11

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Auth transfer:** Explain JWT validation and role versus object permission.
- **RAG readiness:** Document retrieval and source display are separate access paths.
- **Job readiness:** Job IDs and state can be tied to a caller.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **FastAPI authentication:** Hashing; token verification; expiry; dependencies; cookie/header choice.
- **Object-level authorization:** Owner predicates; chunks; sources; messages; memories; jobs.
- **Prompt injection and excessive agency:** Malicious documents; tool output instructions; least privilege.
- **Upload and parser security:** Size/type limits; path traversal; storage names; resource limits.
- **Privacy, deletion and observability:** Journal sensitivity; consent; redaction; retention; cache/vector cleanup.
- **Responsible answer behavior:** Attribution; uncertainty; book claim versus suggestion; feedback/appeal.

## Common mistakes and debugging

### Prompt as an access-control system

Permission checks execute in backend code before data/tools are exposed.

### Sanitize then trust everything

Treat retrieved text/tool output as untrusted throughout execution.

### Log all prompts for debugging

Redact sensitive fields and define retention/erasure behavior.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Authentication versus authorization?
2. Why indirect prompt injection?
3. What is a safe reflection boundary?

<details>
<summary>Answer guide</summary>

**Authentication versus authorization?**

Identity verification versus permission to perform a specific action on a specific object.

**Why indirect prompt injection?**

A document or tool result can carry instructions even when the user query is benign.

**What is a safe reflection boundary?**

Separate cited book content, personal journal facts and generated suggestions; avoid unsupported clinical claims.

</details>

## ITI provenance and industry extensions

- **N07:** RESTful API, Backend Architecture & Security — official published module title.
- **N20:** AI Evaluation, Safety & Responsible AI — official published module title.
- **N26:** AI Security, Governance & Compliance — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Test invalid, expired and missing tokens and define the client session contract.
- [ ] Build a two-user access matrix and test direct object reads and indirect retrieval.
- [ ] Place hostile instructions in a PDF fixture and test backend-enforced tool/data restrictions.
- [ ] Reject oversized/invalid files and prevent user-supplied path writes.
- [ ] Delete a document/journal and prove it disappears from retrieval, memory and permitted logs.
- [ ] Test unsupported advice, conflicting text and correction requests with a documented response rubric.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

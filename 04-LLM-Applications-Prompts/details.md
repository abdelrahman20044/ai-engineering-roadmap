# Technical Details · L04

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **L01 readiness:** A fake provider can be replaced through a tested dependency.
- **Model readiness:** Explain tokens, sampling and context limits.
- **Contract readiness:** Specify expected response fields and provider error behavior.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Instructions and examples:** Task; role; delimiters; few-shot examples; output constraints.
- **Prompt lifecycle:** Template variables; version control; config; regression cases.
- **Provider integration:** SDK/HTTP boundary; errors; credentials via environment; limits.
- **Structured output validation:** Schema; enum/constraints; invalid JSON; refusal; repair boundary.
- **Untrusted input boundaries:** Document text versus instructions; evidence labels; tool output trust.
- **Small AI endpoint:** One call; request IDs; output contract; no low-code dependency.

## Common mistakes and debugging

### Prompt only works for the demo

Use fixed ordinary, ambiguous and adversarial cases.

### Schema equals truth

Validate output structure and separately evaluate grounding/correctness.

### Blind retry loops

Retry only transient failures within a total deadline and record usage.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. What is prompt versioning?
2. Why an adapter?
3. Can JSON mode guarantee a correct answer?

<details>
<summary>Answer guide</summary>

**What is prompt versioning?**

Store template, examples, model/config and test results so comparisons are reproducible.

**Why an adapter?**

Provider SDK and transport details stay outside business logic and test contracts.

**Can JSON mode guarantee a correct answer?**

No; parseability, schema validity and factual correctness are different checks.

</details>

## ITI provenance and industry extensions

- **N04:** Prompt / Context Engineering & Structured Outputs — official published module title.
- **N16:** LLM Fundamentals & GenAI Landscape — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Compare a baseline and revised prompt on ten fixed examples.
- [ ] Store prompt v1/v2 and record the exact configuration and changed failures.
- [ ] Implement a real adapter with connect/read timeout and a fake equivalent.
- [ ] Reject invalid schema output and distinguish provider refusal from parse failure.
- [ ] Test a journal entry that tries to override system behavior and record the failure.
- [ ] Ship /reflect with explicit error behavior and a reproducible curl example.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

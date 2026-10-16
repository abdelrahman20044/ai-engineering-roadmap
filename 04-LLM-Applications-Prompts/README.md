# L04 · Prompt Engineering, Structured Outputs, and LLM Integration

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 2 · 10–16 focused hours · Difficulty 2/5 · P0**

**You will learn:** Design instructions, examples, schemas, and untrusted-input boundaries. Integrate one model behind an adapter with controlled error handling.

**Before starting:** [L01](../01-Python-FastAPI/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B10 · G2](../docs/READING_GUIDE.md#b10) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Instructions and examples

**Learn:** Task; role; delimiters; few-shot examples; output constraints.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B10 · G2](../docs/READING_GUIDE.md#b10) — **Read Now**. Printed pp.42–45: What if we coded it? Skim pp.23–41 only for orientation; no Langflow setup requirement.
- [B11 · G3](../docs/READING_GUIDE.md#b11) — **Read Now**. Printed pp.48–56 and 68–72: prompt techniques and their implementation. Skim repeated UI examples.

**Primary · Interactive tutorial / notebook exercises:** [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial). Consult the Task; role; delimiters; few-shot examples; output constraints sections/examples only. Do not read the entire documentation site.

**Practice:** Compare a baseline and revised prompt on ten fixed examples.

**Completion check:** The revised prompt is compared on the same ten cases as the baseline.

### 2. Prompt lifecycle

**Learn:** Template variables; version control; config; regression cases.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B14 · C5](../docs/READING_GUIDE.md#b14) — **Skim**. Printed pp.218–234: context efficiency, prompt construction/versioning. Skim prompt techniques already learned in B11.

**Primary · Documentation: assertions reference:** [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/). The assertion type matching Prompt lifecycle; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Practice:** Store prompt v1/v2 and record the exact configuration and changed failures.

**Completion check:** Prompt versions and changed failure cases are recorded.

### 3. Provider integration

**Learn:** SDK/HTTP boundary; errors; credentials via environment; limits.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B12 · F3](../docs/READING_GUIDE.md#b12) — **Read Now**. PDF pp.142–147: external serving/API boundary. The overlap page 142 is a section transition, not a chapter restart.
- [B13 · F5](../docs/READING_GUIDE.md#b13) — **Read Now**. PDF pp.211–212: async handler/provider call example. Use current HTTP client docs; full concurrency theory is B31.

**Primary · Single video (lesson within playlist):** [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY). Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Implement a real adapter with connect/read timeout and a fake equivalent.

**Completion check:** A fake and real adapter implement the same timeout/error contract.

### 4. Structured output validation

**Learn:** Schema; enum/constraints; invalid JSON; refusal; repair boundary.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B05 · F4](../docs/READING_GUIDE.md#b05) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs). Consult the Schema; enum/constraints; invalid JSON; refusal; repair boundary sections/examples only. Do not read the entire documentation site.

**Practice:** Reject invalid schema output and distinguish provider refusal from parse failure.

**Completion check:** Invalid schema output is rejected; schema validity is not reported as factual correctness.

### 5. Untrusted input boundaries

**Learn:** Document text versus instructions; evidence labels; tool output trust.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B14 · C5](../docs/READING_GUIDE.md#b14) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). Consult the Document text versus instructions; evidence labels; tool output trust sections/examples only. Do not read the entire documentation site.

**Practice:** Test a journal entry that tries to override system behavior and record the failure.

**Completion check:** A hostile journal entry cannot change backend permissions.

### 6. Small AI endpoint

**Learn:** One call; request IDs; output contract; no low-code dependency.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B10 · G2](../docs/READING_GUIDE.md#b10) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video (lesson within playlist):** [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5). Only the linked “Welcome to FastAPI” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Ship /reflect with explicit error behavior and a reproducible curl example.

**Completion check:** The endpoint has an independent test and a reproducible example request.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L04-E1:** Use the supplied synthetic excerpts to return an answer and references drawn from a supplied ID list.
  - **Pass:** Validate the response schema on the server and reject unknown reference IDs.
- [ ] **L04-E2:** Test valid JSON containing a wrong claim, malformed output, timeout, and HTTP429.
  - **Pass:** Separate schema failure, factual failure, and transport failure.
- [ ] **L04-E3:** Compare zero-shot with two few-shot examples on ten cases.
  - **Pass:** Save prompt/model versions, usage, latency, and the observed differences.
- [ ] **L04-E4:** Implement bounded retries for selected transient failures.
  - **Pass:** Permanent failures do not loop; time and attempt limits are tested.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S2](../project/milestones/s2.md). No secrets are committed. Valid JSON is not mistaken for a correct answer. The same application logic works with fake and real providers.

**Keep:** Provider adapter, versioned prompt, and structured-output tests; Small prompt comparison report.

## What to defer

- Many providers at once
- Prompt frameworks or autonomous agent loops

## Record progress and choose the next Level

```bash
python scripts/progress.py set L04 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L05](../05-Evaluation/README.md), [L18](../18-Supporting-Frontend/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

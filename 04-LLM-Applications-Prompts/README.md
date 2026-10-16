# L04 · Prompt Engineering, Structured Outputs, and LLM Integration

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 2 · Reliable LLM Application Basics | 10–16 h | 2/5 | P0 | [L01](../01-Python-FastAPI/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md) |

**Unlocks:** [L05](../05-Evaluation/README.md), [L18](../18-Supporting-Frontend/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Design instructions, examples, schemas, and untrusted-input boundaries. Integrate one model behind an adapter with controlled error handling. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| L01 readiness | A fake provider can be replaced through a tested dependency. |
| Model readiness | Explain tokens, sampling and context limits. |
| Contract readiness | Specify expected response fields and provider error behavior. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Instructions and examples: Compare a baseline and revised prompt on ten fixed examples.
- [ ] Prompt lifecycle: Store prompt v1/v2 and record the exact configuration and changed failures.
- [ ] Provider integration: Implement a real adapter with connect/read timeout and a fake equivalent.
- [ ] Structured output validation: Reject invalid schema output and distinguish provider refusal from parse failure.
- [ ] Untrusted input boundaries: Test a journal entry that tries to override system behavior and record the failure.
- [ ] Small AI endpoint: Ship /reflect with explicit error behavior and a reproducible curl example.

## Recommended learning path

G2 code section + G3 → one provider adapter → validated output → a fixed prompt comparison. Read C5 for failure analysis after the first call.

| Pass | Work to do | Stop condition |
| --- | --- | --- |
| 1 · Orient | Use the assigned book/article focus and one Arabic or English explanation for each unfamiliar topic. | Explain the mechanism in your own words. |
| 2 · Implement | Work through the numbered topic outputs below; integrate them into the assessed exercises. | The specified behavior is reproducible in your own code. |
| 3 · Verify | Run the failure cases, self-check and milestone acceptance contract. | Evidence and remaining limitations are recorded. |

The resource library contains alternatives and optional depth. The effort estimate covers a selected path plus implementation, not watching every listed course. Choose Arabic teaching when it speeds understanding, then consult the English API reference for exact behavior.

## What you learn and exactly where

Each numbered row is a learning unit. **Arabic teaching**, **machine-translated Arabic text**, **English videos**, and **English documentation** are labeled separately. A missing verified Arabic resource is stated explicitly; a loosely related video is not presented as full coverage.

| Topic and required subtopics | Arabic route | English route | Build or verify |
| --- | --- | --- | --- |
| **L04-T01 · Instructions and examples**<br>Task; role; delimiters; few-shot examples; output constraints | [Prompt engineering fundamentals · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/04-prompt-engineering-fundamentals/README.md) (AR machine-translated text) | [Learn to Spell: Prompt Engineering](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/prompt-engineering/) (EN video + slides) | Compare a baseline and revised prompt on ten fixed examples. |
| **L04-T02 · Prompt lifecycle**<br>Template variables; version control; config; regression cases | [Advanced prompts · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/05-advanced-prompts/README.md) (AR machine-translated text) | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) | Store prompt v1/v2 and record the exact configuration and changed failures. |
| **L04-T03 · Provider integration**<br>SDK/HTTP boundary; errors; credentials via environment; limits | [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) (AR video)<br>[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Implement a real adapter with connect/read timeout and a fake equivalent. |
| **L04-T04 · Structured output validation**<br>Schema; enum/constraints; invalid JSON; refusal; repair boundary | [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) (AR video + code)<br>**Scope:** Pydantic/API validation orientation; model-constrained output requires the English reference. | [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs) (EN) | Reject invalid schema output and distinguish provider refusal from parse failure. |
| **L04-T05 · Untrusted input boundaries**<br>Document text versus instructions; evidence labels; tool output trust | [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md) (AR machine-translated text) | [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) (EN course + videos + exercises) | Test a journal entry that tries to override system behavior and record the failure. |
| **L04-T06 · Small AI endpoint**<br>One call; request IDs; output contract; no low-code dependency | [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) (AR video)<br>[mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) (AR video) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Ship /reflect with explicit error behavior and a reproducible curl example. |

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L04-T01 | G3 pp.48–56 and 68–72, primary; C5 skim duplicate basics | [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) (EN) |
| L04-T02 | C5 pp.218–234, versioning focus | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L04-T03 | G2 pp.42–45; F3 serving and F5 PDF203–208 | [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) (EN)<br>[Ollama API introduction](https://docs.ollama.com/api/introduction) (EN) |
| L04-T04 | F4 PDF153–186; C2 pp.88–105 as needed | [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs) (EN)<br>[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) (EN) |
| L04-T05 | C5 pp.235–250 preview; full security gate in L11 | [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (EN) |
| L04-T06 | G2 code section; F2/F4 implementation reference | [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N04 · Prompt / Context Engineering & Structured Outputs | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N16 · LLM Fundamentals & GenAI Landscape | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L04-E1 | Use the supplied synthetic excerpts to return an answer and references drawn from a supplied ID list. | Validate the response schema on the server and reject unknown reference IDs. |
| L04-E2 | Test valid JSON containing a wrong claim, malformed output, timeout, and HTTP429. | Separate schema failure, factual failure, and transport failure. |
| L04-E3 | Compare zero-shot with two few-shot examples on ten cases. | Save prompt/model versions, usage, latency, and the observed differences. |
| L04-E4 | Implement bounded retries for selected transient failures. | Permanent failures do not loop; time and attempt limits are tested. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Prompt only works for the demo | Use fixed ordinary, ambiguous and adversarial cases. |
| Schema equals truth | Validate output structure and separately evaluate grounding/correctness. |
| Blind retry loops | Retry only transient failures within a total deadline and record usage. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What is prompt versioning?
2. Why an adapter?
3. Can JSON mode guarantee a correct answer?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Store template, examples, model/config and test results so comparisons are reproducible. |
| 2 | Provider SDK and transport details stay outside business logic and test contracts. |
| 3 | No; parseability, schema validity and factual correctness are different checks. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S2](../project/milestones/s2.md) | Provider adapter, versioned prompt, and structured-output tests; Small prompt comparison report | No secrets are committed. Valid JSON is not mistaken for a correct answer. The same application logic works with fake and real providers. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

No secrets are committed. Valid JSON is not mistaken for a correct answer. The same application logic works with fake and real providers.

## Postpone until justified

- Many providers at once
- Prompt frameworks or autonomous agent loops

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L04 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L03](../03-Deep-Learning-Foundation-Models/README.md) · Next numbered Level: [L05](../05-Evaluation/README.md)

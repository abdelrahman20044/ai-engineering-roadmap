# L04 · Prompt Engineering, Structured Outputs, and LLM Integration

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 2 · Reliable LLM Application Basics | 10–16 h | 2/5 | P0 | [L01](../01-Python-FastAPI/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md) |

**Outcome:** Design instructions, examples, schemas, and untrusted-input boundaries. Integrate one model behind an adapter with controlled error handling.

**Unlocks:** [L05](../05-Evaluation/README.md), [L18](../18-Supporting-Frontend/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Prompt construction and versioning | G3 pp.48–56,68–72; C5 pp.218–234; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 1](resources.md#practice-and-evidence) |
| Provider adapters and failure contracts | F3 external serving; F5 PDF203–208; [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 2](resources.md#practice-and-evidence) |
| Structured outputs | C2 pp.88–105; F4 PDF153–186; [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | [Practice 3](resources.md#practice-and-evidence) |
| Translate low-code examples into code | G2 pp.42–45; [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N04** — Prompt / Context Engineering & Structured Outputs.
- **N16** — LLM Fundamentals & GenAI Landscape.

| ITI topic IDs | Interpretation |
| --- | --- |
| N04, N16 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L04-E1 | Use the supplied synthetic excerpts to return an answer and references drawn from a supplied ID list. | Validate the response schema on the server and reject unknown reference IDs. |
| L04-E2 | Test valid JSON containing a wrong claim, malformed output, timeout, and HTTP429. | Separate schema failure, factual failure, and transport failure. |
| L04-E3 | Compare zero-shot with two few-shot examples on ten cases. | Save prompt/model versions, usage, latency, and the observed differences. |
| L04-E4 | Implement bounded retries for selected transient failures. | Permanent failures do not loop; time and attempt limits are tested. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S2](../project/milestones/s2.md) | Provider adapter, versioned prompt, and structured-output tests; Small prompt comparison report | No secrets are committed. Valid JSON is not mistaken for a correct answer. The same application logic works with fake and real providers. |

## Postpone

| Outside this level |
| --- |
| Many providers at once |
| Prompt frameworks or autonomous agent loops |

## Record completion

```bash
python scripts/progress.py set L04 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L03](../03-Deep-Learning-Foundation-Models/README.md) · Next numbered Level: [L05](../05-Evaluation/README.md). Follow the prerequisite table if branches differ.

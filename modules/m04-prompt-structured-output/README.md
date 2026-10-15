# M04 — Prompt Engineering, Structured Outputs, and LLM Integration

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P0 |
| Prerequisites | [M01](../m01-python-fastapi/README.md), [M03](../m03-dl-foundation-models/README.md) |
| Personal effort | 10–16 focused hours; not official ITI hours |
| Project milestone | [S2](../../project/milestones/s2.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Design instructions, examples, schemas, and untrusted-input boundaries. |
| O2 | Integrate one model behind an adapter with controlled error handling. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N04 | Prompt / Context Engineering & Structured Outputs | 24 |
| N16 | LLM Fundamentals & GenAI Landscape | 18 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | G2: What if we coded it?, printed pp. 42–45; skip Langflow setup. |
| 2 | G3 pp. 48–56 and 68–72: prompt quality, techniques, and the coding explanation. |
| 3 | F3 external serving, F4 validation, and F5 PDF 203–208 provider APIs. |
| 4 | C5 pp. 218–234: context efficiency and prompt versioning; C2 structured outputs as needed. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M04-E1 | Use the supplied synthetic excerpts to return an answer and references drawn from a supplied ID list. | Validate the response schema on the server and reject unknown reference IDs. |
| M04-E2 | Test valid JSON containing a wrong claim, malformed output, timeout, and HTTP429. | Separate schema failure, factual failure, and transport failure. |
| M04-E3 | Compare zero-shot with two few-shot examples on ten cases. | Save prompt/model versions, usage, latency, and the observed differences. |
| M04-E4 | Implement bounded retries for selected transient failures. | Permanent failures do not loop; time and attempt limits are tested. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Provider adapter, versioned prompt, and structured-output tests; Small prompt comparison report |
| Pass condition | No secrets are committed. Valid JSON is not mistaken for a correct answer. The same application logic works with fake and real providers. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M04 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Many providers at once |
| Prompt frameworks or autonomous agent loops |

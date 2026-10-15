# M17 — Capstone Release, Technical Defense, and Career Evidence

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P2 |
| Prerequisites | [M02](../m02-math-ml/README.md), [M03](../m03-dl-foundation-models/README.md), [M08](../m08-rag/README.md), [M09](../m09-context-memory/README.md), [M10](../m10-async-streaming-jobs/README.md), [M11](../m11-security/README.md), [M12](../m12-tools-agents/README.md), [M13](../m13-mcp-workflows/README.md), [M14](../m14-llmops-deployment/README.md), [M15](../m15-optimization-feedback/README.md) |
| Personal effort | 12–18 focused hours; not official ITI hours |
| Project milestone | [S7](../../project/milestones/s7.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Demonstrate a usable AI application with evaluation and operating evidence. |
| O2 | Explain and modify the implementation independently and communicate honest limitations. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N27 | Graduation Project | 60 |
| N28 | Effective Presentation Skills | 18 |
| N29 | Freelancing Fundamentals | 12 |
| N30 | Effective Communication Skills | 12 |
| N31 | Work Ethics Workshop | 3 |
| N32 | CV Writing & Interviewing Skills | 15 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | Review C1 milestones/maintenance, C4 evaluation, F11 E2E, and C10 feedback only where needed. |
| 2 | No large new chapter; close real gaps in the evidence. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M17-E1 | Demonstrate upload → question → source → journal connection → conversation → deletion through a basic UI. | Include failure paths and cross-user access tests. |
| M17-E2 | Freeze configuration and run the final independent holdout. | Analyze three major failures and disclose remaining limitations. |
| M17-E3 | Publish application setup docs, ERD/architecture, ADRs, runbook, and a 3–5-minute demo. | A reviewer can reproduce the demo with synthetic data. |
| M17-E4 | Run a mock defense: write an endpoint, query, and test without AI; diagnose a trace. | Explain framework, model, retrieval, and single-agent decisions. |
| M17-E5 | Draft evidence-based CV claims and a scoped freelance proposal. | Only measured figures are used; discuss data ethics, delivery scope, and communication. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Versioned release, demo, evaluation report/dashboard, and defense notes |
| Pass condition | Run, explain, modify, and evaluate the system. This is a self-study gate, not an ITI credential or hiring guarantee. M16/M18 remain optional. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M17 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Waiting for every advanced topic before applying |
| Inflated metrics or unsupported production-ready claims |

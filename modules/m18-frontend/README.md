# M18 — Supporting TypeScript and React UI

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P3 |
| Prerequisites | [M01](../m01-python-fastapi/README.md), [M04](../m04-prompt-structured-output/README.md), [M11](../m11-security/README.md) |
| Personal effort | 12–20 focused hours; not official ITI hours |
| Project milestone | [S7](../../project/milestones/s7.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Build a small accessible client for API errors, streaming, and evidence display. |
| O2 | Distinguish product UI needs from a complete React/TypeScript curriculum. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N05 | Software Testing & Full-Stack Debugging | 30 |
| N08 | Frontend TypeScript & React | 42 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | React official Using TypeScript and Learn: a necessary gap resource if choosing React. |
| 2 | F6 client/streaming and F8 authentication contracts as references. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M18-E1 | Type requests, responses, and citations; add upload/question/journal forms. | Handle loading, empty, and failure states. |
| M18-E2 | Display source snippets and pages using server metadata. | Test keyboard navigation, long text, and RTL if supported by the product. |
| M18-E3 | Integrate authentication and streaming without browser secrets. | Document cookie/bearer/CORS/CSRF choices for the client. |
| M18-E4 | Test a normal UI journey and unauthorized access. | The UI exposes backend failures rather than masking them. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Small React/TypeScript client, API contract, and UI/accessibility test notes |
| Pass condition | A basic UI is required by the capstone. React specifically is optional for this self-study Core, while explicit React/TypeScript coverage remains visible in the ITI mapping. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M18 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Advanced frontend design |
| Pausing AI engineering until a complete frontend course is finished |

# M00 — Baseline Assessment and Product Scope

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P0 |
| Prerequisites | None |
| Personal effort | 3–5 focused hours; not official ITI hours |
| Project milestone | [S0](../../project/milestones/s0.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Identify transferable backend skills and specific gaps. |
| O2 | Define users, requirements, failure cases, and acceptance evidence. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N01 | Modern Software Engineering & Git Collaboration | 18 |
| N03 | SDLC & Requirements Engineering | 18 |
| N09 | Software Architecture & System Design | 30 |
| N30 | Effective Communication Skills | 12 |
| N31 | Work Ethics Workshop | 3 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | C1: Planning AI Applications, printed pp. 28–34; The AI Engineering Stack, pp. 35–46. Read selectively. |
| 2 | F2: consult project structures only after the first endpoint; avoid premature architecture. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M00-E1 | Explain a JWT/RBAC flow, Zod validation, and an integration test from CRM. Write a typed JSON cleaner and a test without AI. | Record demonstrated skills and gaps; distinguish prior evidence from assumptions. |
| M00-E2 | Write five user stories and three failure cases: missing evidence, unreadable document, and unauthorized resource access. | Each story has an observable acceptance condition. |
| M00-E3 | Choose a small permitted corpus, specify input/output contracts and three non-goals, and create the first ADR. | A one-page scope and ten initial questions are sufficient to start building. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | baseline.md with links to prior work; project-scope.md and the first ADR |
| Pass condition | Explain the use case and the first deliverable in two minutes. Review only demonstrated gaps rather than restarting backend fundamentals. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M00 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Repeating JavaScript, HTTP, Git, or Docker basics after passing diagnostics |
| Microservices or buying a GPU before a need exists |

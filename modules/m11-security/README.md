# M11 — Security, Authorization, and Responsible AI

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M06](../m06-persistence/README.md), [M08](../m08-rag/README.md) |
| Personal effort | 16–24 focused hours; not official ITI hours |
| Project milestone | [S4](../../project/milestones/s4.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Enforce ownership before retrieval, source viewing, history, memory, and job access. |
| O2 | Constrain untrusted content, tools, uploads, and consumption. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N07 | RESTful API, Backend Architecture & Security | 36 |
| N20 | AI Evaluation, Safety & Responsible AI | 12 |
| N26 | AI Security, Governance & Compliance | 12 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | F8 PDF 338–400: FastAPI authorization implementation; skim familiar JWT concepts. |
| 2 | F9 PDF 401–428; C5 pp. 235–250; C10 pp. 451–455. |
| 3 | OWASP GenAI Prompt Injection: server-enforced permissions and least privilege. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M11-E1 | Build an A/B access matrix across every resource endpoint, source viewer, cache, and job state. | User B cannot retrieve, read, edit, or delete user A data. |
| M11-E2 | Index a passage that tries to change instructions or expose another journal. | Authorization remains independent of the model and document instructions. |
| M11-E3 | Set file/page/token/request/tool/retry limits. | Oversized requests and abuse have bounded, tested failure behavior. |
| M11-E4 | Delete a document and its derived data, memory links, and caches. | Document active deletion and backup retention separately. |
| M11-E5 | Threat-model upload/storage/provider/logs/tools and use synthetic journals. | No secret or sensitive journal content appears in default logs or browser configuration. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Threat model, authorization integration tests, and security matrix; Deletion and retention policy |
| Pass condition | Pass designed isolation tests before public deployment. Passing tests is not proof of universal security; retrieved text does not grant tool privileges. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M11 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| System prompts as authorization controls |
| Unapproved autonomous write tools |

# M12 — Tool Calling, Bounded Agents, and Multi-Agent Decisions

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P1 |
| Prerequisites | [M05](../m05-evaluation/README.md), [M09](../m09-context-memory/README.md), [M11](../m11-security/README.md) |
| Personal effort | 18–28 focused hours; not official ITI hours |
| Project milestone | [S5](../../project/milestones/s5.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Distinguish fixed workflows from model-directed tool loops. |
| O2 | Implement safe tool contracts and evaluate tool/task failures. |
| O3 | Understand sub-agent patterns without assuming they improve the product. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N20 | AI Evaluation, Safety & Responsible AI | 12 |
| N22 | Agentic AI & Multi-Agent Orchestration | 36 |
| N24 | AI Workflow Automation & Business Process Integration | 12 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | G5 printed pp. 102–107 and 122–127; G6 pp. 130–132 for patterns, with implementation examples optional. |
| 2 | C6 Agents pp. 275–299: tools, planning, and failure modes. |
| 3 | Anthropic: JIT context and sub-agent sections, interpreted through project experiments. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M12-E1 | Define read-only search_passages and get_passage tools with bounded outputs. | Validate schemas and enforce authenticated ownership; no generic SQL or shell tool. |
| M12-E2 | Build a small direct-SDK loop with max steps, timeout, and token budget. | Handle unknown tool, invalid arguments, no-tool-needed, and repeated-loop cases. |
| M12-E3 | Compare a fixed workflow and agent on fifteen tasks. | Report success, tool errors, unauthorized attempts, latency, and cost. |
| M12-E4 | Use lightweight references and fetch passages just in time. | Only permitted requested content is loaded; compare against upfront retrieval. |
| M12-E5 | Design a planner/worker experiment and a summary contract. | Implement extra agents only if a measured use case justifies isolation, coordination, and cost. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Tool contracts, bounded agent loop, and evaluation report; Single-agent versus multi-agent ADR |
| Pass condition | A model request is never treated as authorization. Loops stop predictably and you can justify either using an agent or retaining a fixed workflow. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M12 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Framework orchestration before understanding a loop |
| Multi-agent implementation just to check a syllabus keyword |

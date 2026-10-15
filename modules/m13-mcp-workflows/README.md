# M13 — MCP, Enterprise Integration, and AI Workflows

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P2 |
| Prerequisites | [M12](../m12-tools-agents/README.md) |
| Personal effort | 10–16 focused hours; not official ITI hours |
| Project milestone | [S5](../../project/milestones/s5.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Understand MCP host/client/server roles, primitives, transport, and authorization. |
| O2 | Build one bounded integration with explicit failure behavior. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N23 | Model Context Protocol & Enterprise Tool Integration | 12 |
| N24 | AI Workflow Automation & Business Process Integration | 12 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | MCP official architecture and the chosen SDK version; the books are not a sufficient MCP reference. |
| 2 | C10 pp. 472–473: orchestration; G8 conceptual reference only; C6 tool contracts as needed. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M13-E1 | Contrast function calling with an MCP integration diagram. | Identify who manages context and authorization; neither is delegated to the protocol. |
| M13-E2 | Expose get_passage through a local MCP server and call it from one client. | Pin the protocol/SDK version and record successful discovery and invocation. |
| M13-E3 | Test malformed arguments, unauthorized documents, and timeout. | Connection failure does not widen permissions. |
| M13-E4 | Design a reading-summary draft workflow with one simulated save operation. | The application enforces approval, authorization, and duplicate handling for writes; no external message needs to be sent. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Small MCP server/client demo and integration diagram; Version record and permission/timeout tests |
| Pass condition | Demonstrate one real tool invocation through a client and explain where permissions, context, approval, and retries live. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M13 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| Many MCP servers or invented enterprise integrations |
| Production remote authentication before a local protocol demonstration |

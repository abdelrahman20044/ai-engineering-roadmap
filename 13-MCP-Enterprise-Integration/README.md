# L13 · MCP, Enterprise Integration, and AI Workflows

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 10–16 h | 3/5 | P2 | [L12](../12-Tools-Agents/README.md) |

**Outcome:** Understand MCP host/client/server roles, primitives, transport, and authorization. Build one bounded integration with explicit failure behavior.

**Unlocks:** [L16](../16-Capstone-Career/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Client, host, server roles | Official MCP architecture; C10 pp.472–473; [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | [Practice 1](resources.md#practice-and-evidence) |
| Tools, resources, contracts | G5 tool concepts; current MCP docs; [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | [Practice 2](resources.md#practice-and-evidence) |
| Trust boundaries and enterprise adapters | C6 tool failure modes; [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | [Practice 3](resources.md#practice-and-evidence) |
| Workflow orchestration | G8 conceptual reference; C10 pp.472–473; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N23** — Model Context Protocol & Enterprise Tool Integration.
- **N24** — AI Workflow Automation & Business Process Integration.

| ITI topic IDs | Interpretation |
| --- | --- |
| N23, N24 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L13-E1 | Contrast function calling with an MCP integration diagram. | Identify who manages context and authorization; neither is delegated to the protocol. |
| L13-E2 | Expose get_passage through a local MCP server and call it from one client. | Pin the protocol/SDK version and record successful discovery and invocation. |
| L13-E3 | Test malformed arguments, unauthorized documents, and timeout. | Connection failure does not widen permissions. |
| L13-E4 | Design a reading-summary draft workflow with one simulated save operation. | The application enforces approval, authorization, and duplicate handling for writes; no external message needs to be sent. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S5](../project/milestones/s5.md) | Small MCP server/client demo and integration diagram; Version record and permission/timeout tests | Demonstrate one real tool invocation through a client and explain where permissions, context, approval, and retries live. |

## Postpone

| Outside this level |
| --- |
| Many MCP servers or invented enterprise integrations |
| Production remote authentication before a local protocol demonstration |

## Record completion

```bash
python scripts/progress.py set L13 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L12](../12-Tools-Agents/README.md) · Next numbered Level: [L14](../14-LLMOps-Deployment/README.md). Follow the prerequisite table if branches differ.

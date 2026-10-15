# L12 · Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 18–28 h | 4/5 | P1 | [L05](../05-Evaluation/README.md), [L09](../09-Context-Memory/README.md), [L11](../11-Security-Responsible-AI/README.md) |

**Outcome:** Distinguish fixed workflows from model-directed tool loops. Implement safe tool contracts and evaluate tool/task failures. Understand sub-agent patterns without assuming they improve the product.

**Unlocks:** [L13](../13-MCP-Enterprise-Integration/README.md), [L16](../16-Capstone-Career/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Tool schemas and validation | G5 pp.102–107,122–127; C6 pp.275–299; [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | [Practice 1](resources.md#practice-and-evidence) |
| Workflow versus agent | G6 pp.130–132; C6 agents; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 2](resources.md#practice-and-evidence) |
| Stop conditions, budget, errors | C6 agents; F11 behavioral tests; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 3](resources.md#practice-and-evidence) |
| Multi-agent orchestration tradeoffs | G6 patterns; Anthropic sub-agents; [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N20** — AI Evaluation, Safety & Responsible AI.
- **N22** — Agentic AI & Multi-Agent Orchestration.
- **N24** — AI Workflow Automation & Business Process Integration.

| ITI topic IDs | Interpretation |
| --- | --- |
| N20, N22, N24 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

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
| L12-E1 | Define read-only search_passages and get_passage tools with bounded outputs. | Validate schemas and enforce authenticated ownership; no generic SQL or shell tool. |
| L12-E2 | Build a small direct-SDK loop with max steps, timeout, and token budget. | Handle unknown tool, invalid arguments, no-tool-needed, and repeated-loop cases. |
| L12-E3 | Compare a fixed workflow and agent on fifteen tasks. | Report success, tool errors, unauthorized attempts, latency, and cost. |
| L12-E4 | Use lightweight references and fetch passages just in time. | Only permitted requested content is loaded; compare against upfront retrieval. |
| L12-E5 | Design a planner/worker experiment and a summary contract. | Implement extra agents only if a measured use case justifies isolation, coordination, and cost. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S5](../project/milestones/s5.md) | Tool contracts, bounded agent loop, and evaluation report; Single-agent versus multi-agent ADR | A model request is never treated as authorization. Loops stop predictably and you can justify either using an agent or retaining a fixed workflow. |

## Postpone

| Outside this level |
| --- |
| Framework orchestration before understanding a loop |
| Multi-agent implementation just to check a syllabus keyword |

## Record completion

```bash
python scripts/progress.py set L12 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L11](../11-Security-Responsible-AI/README.md) · Next numbered Level: [L13](../13-MCP-Enterprise-Integration/README.md). Follow the prerequisite table if branches differ.

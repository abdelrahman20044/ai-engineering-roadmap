# Technical Details · L12

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **RAG/security readiness:** A caller-scoped search operation exists and rejects unauthorized access.
- **Contract readiness:** Validate tool arguments and distinguish error from empty success.
- **Evaluation readiness:** Measure task completion and tool behavior separately.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Agent anatomy and design choice:** State; model decision; action; observation; workflow alternatives.
- **Tool design and schemas:** Small names; typed inputs; concise outputs; errors; idempotent reads.
- **Bounded execution loop:** Max steps; timeout; token/cost budget; stop/ask-human; error states.
- **Agent evaluation:** Tool choice; arguments; trajectory; task success; final-answer grounding.
- **Memory and context interfaces:** Retrieve only needed state; observation size; provenance; side-effect confirmation.
- **Multi-agent comparison:** Specialist role; independent context; handoff summary; coordination failures.

## Common mistakes and debugging

### Every problem needs an agent

Compare with deterministic routing/workflows first.

### Tool execution trusts model arguments

Validate schema and permission for every call, independent of model compliance.

### Unbounded self-correction

Enforce steps, wall time and token/cost budgets in code.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Workflow versus agent?
2. What is a trajectory failure?
3. When add sub-agents?

<details>
<summary>Answer guide</summary>

**Workflow versus agent?**

The workflow fixes control flow in code; the agent chooses next actions within enforced limits.

**What is a trajectory failure?**

An invalid/unnecessary/repeated tool sequence even if the final prose looks plausible.

**When add sub-agents?**

A separable task and a measured improvement justify coordination, isolation and extra cost.

</details>

## ITI provenance and industry extensions

- **N20:** AI Evaluation, Safety & Responsible AI — official published module title.
- **N22:** Agentic AI & Multi-Agent Orchestration — official published module title.
- **N24:** AI Workflow Automation & Business Process Integration — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Draw a fixed workflow and tool loop for the same journal question; choose a baseline.
- [ ] Expose one owner-scoped search tool; reject malformed and unauthorized arguments.
- [ ] Test repeated calls, unavailable tools, budget exhaustion and terminal behavior.
- [ ] Label five correct and five failed traces; report tool and task metrics separately.
- [ ] Limit tool result size and prove relevant evidence survives the bound.
- [ ] Run one partitioned experiment against the single-agent baseline; record a go/no-go ADR.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

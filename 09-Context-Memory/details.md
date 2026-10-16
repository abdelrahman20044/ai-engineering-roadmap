# Technical Details · L09

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **RAG readiness:** Explain which passages were retrieved and which reached the prompt.
- **State readiness:** Conversations and journals are owner-scoped and deletable.
- **Evaluation readiness:** Have multi-turn cases with expected facts and source evidence.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **Context engineering and context rot:** Prompt versus context; attention budget; irrelevant tokens; position sensitivity.
- **Context budget and selection:** Instructions; schema; evidence; journal; history; output reserve.
- **Just-in-time retrieval:** References versus full content; selective journal search; minimal tool outputs.
- **Conversation history and structured memory:** Working history; durable facts; provenance; conflicts; user edit/delete.
- **Compaction and retained constraints:** Summaries; checkpoints; recoverable sources; lost-detail evaluation.
- **Sub-agent boundary:** Partitionable tasks; narrow context; summary handoff; coordination cost.

## Common mistakes and debugging

### Append all history forever

Allocate a budget and retrieve only relevant state.

### Summary treated as canonical truth

Link memories to sources and preserve correction/deletion behavior.

### Multi-agent complexity for memory alone

Prove a single workflow fails before adding another agent.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Prompt versus context engineering?
2. What is just-in-time retrieval?
3. When is compaction acceptable?

<details>
<summary>Answer guide</summary>

**Prompt versus context engineering?**

Prompt writing is part of choosing and managing all instructions, tools, evidence, history and state available to the model.

**What is just-in-time retrieval?**

Keep lightweight references and fetch detailed information only when the current step needs it.

**When is compaction acceptable?**

After measuring retained facts, lost constraints and future-task performance with recoverable source state.

</details>

## ITI provenance and industry extensions

- **N04:** Prompt / Context Engineering & Structured Outputs — official published module title.
- **N19:** RAG Systems Engineering — official published module title.
- **N22:** Agentic AI & Multi-Agent Orchestration — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Compare focused evidence with the same evidence buried in distractors and report task outcomes.
- [ ] Create a context manifest with token counts, selection reasons and source IDs.
- [ ] Fetch relevant journal records on demand and prove unrelated entries are excluded.
- [ ] Store a user-approved memory with source, timestamp and correction/deletion tests.
- [ ] Summarize a long synthetic conversation and test five facts/constraints before and after.
- [ ] Write an ADR choosing a single workflow unless a bounded comparison demonstrates value.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

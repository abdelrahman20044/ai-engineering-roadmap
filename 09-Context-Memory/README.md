# L09 · Context Engineering, Memory, and Conversations

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 3 · Grounded Retrieval and Context | 14–22 h | 3/5 | P1 | [L08](../08-RAG-Systems/README.md) |

**Unlocks:** [L12](../12-Tools-Agents/README.md), [L16](../16-Capstone-Career/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Budget instructions, evidence, selected journals, history, and memory. Manage memory provenance, correction, deletion, and summarization loss. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| RAG readiness | Explain which passages were retrieved and which reached the prompt. |
| State readiness | Conversations and journals are owner-scoped and deletable. |
| Evaluation readiness | Have multi-turn cases with expected facts and source evidence. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Context engineering and context rot: Compare focused evidence with the same evidence buried in distractors and report task outcomes.
- [ ] Context budget and selection: Create a context manifest with token counts, selection reasons and source IDs.
- [ ] Just-in-time retrieval: Fetch relevant journal records on demand and prove unrelated entries are excluded.
- [ ] Conversation history and structured memory: Store a user-approved memory with source, timestamp and correction/deletion tests.
- [ ] Compaction and retained constraints: Summarize a long synthetic conversation and test five facts/constraints before and after.
- [ ] Sub-agent boundary: Write an ADR choosing a single workflow unless a bounded comparison demonstrates value.

## Recommended learning path

Read Anthropic before agent frameworks → inspect a context trace → budget and retrieve journals → add editable memory → test compaction only when needed.

| Pass | Work to do | Stop condition |
| --- | --- | --- |
| 1 · Orient | Use the assigned book/article focus and one Arabic or English explanation for each unfamiliar topic. | Explain the mechanism in your own words. |
| 2 · Implement | Work through the numbered topic outputs below; integrate them into the assessed exercises. | The specified behavior is reproducible in your own code. |
| 3 · Verify | Run the failure cases, self-check and milestone acceptance contract. | Evidence and remaining limitations are recorded. |

The resource library contains alternatives and optional depth. The effort estimate covers a selected path plus implementation, not watching every listed course. Choose Arabic teaching when it speeds understanding, then consult the English API reference for exact behavior.

## What you learn and exactly where

Each numbered row is a learning unit. **Arabic teaching**, **machine-translated Arabic text**, **English videos**, and **English documentation** are labeled separately. A missing verified Arabic resource is stated explicitly; a loosely related video is not presented as full coverage.

| Topic and required subtopics | Arabic route | English route | Build or verify |
| --- | --- | --- | --- |
| **L09-T01 · Context engineering and context rot**<br>Prompt versus context; attention budget; irrelevant tokens; position sensitivity | [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) (AR machine-translated text) | [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) (EN video) | Compare focused evidence with the same evidence buried in distractors and report task outcomes. |
| **L09-T02 · Context budget and selection**<br>Instructions; schema; evidence; journal; history; output reserve | [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) (AR machine-translated text)<br>[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) (AR machine-translated text) | [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) (EN video) | Create a context manifest with token counts, selection reasons and source IDs. |
| **L09-T03 · Just-in-time retrieval**<br>References versus full content; selective journal search; minimal tool outputs | [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) (AR machine-translated text) | [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) (EN video) | Fetch relevant journal records on demand and prove unrelated entries are excluded. |
| **L09-T04 · Conversation history and structured memory**<br>Working history; durable facts; provenance; conflicts; user edit/delete | [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md) (AR machine-translated text)<br>[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) (AR machine-translated text) | [Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw) (EN video) | Store a user-approved memory with source, timestamp and correction/deletion tests. |
| **L09-T05 · Compaction and retained constraints**<br>Summaries; checkpoints; recoverable sources; lost-detail evaluation | [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) (AR machine-translated text) | [Context engineering: memory, compaction and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) (EN notebook recipe) | Summarize a long synthetic conversation and test five facts/constraints before and after. |
| **L09-T06 · Sub-agent boundary**<br>Partitionable tasks; narrow context; summary handoff; coordination cost | [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) (AR machine-translated text) | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN) | Write an ADR choosing a single workflow unless a bounded comparison demonstrates value. |

**Arabic coverage boundary:** Microsoft provides Arabic translated context/memory lessons. No complete Egyptian video course on context rot, compaction and memory evaluation was verified. The Anthropic article and English lessons are the primary sources for those techniques.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L09-T01 | Anthropic introduction/context-rot sections; C5 pp.218–219 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |
| L09-T02 | C10 Enhance Context p.450; Anthropic context selection | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN)<br>[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) (EN) |
| L09-T03 | Anthropic just-in-time retrieval and tool design | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |
| L09-T04 | C6 Memory pp.300–304 | [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) (EN)<br>[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |
| L09-T05 | Anthropic compaction/structured note-taking sections | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |
| L09-T06 | Anthropic sub-agent section; G6 patterns preview | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN)<br>[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N04 · Prompt / Context Engineering & Structured Outputs | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N19 · RAG Systems Engineering | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N22 · Agentic AI & Multi-Agent Orchestration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L09-E1 | Write a context contract with source priorities and a token budget. | Show how each input is selected, bounded, and truncated. |
| L09-E2 | Compare focused evidence against longer distractor-heavy context. | Use the same tasks and measure effects rather than assuming more context helps. |
| L09-E3 | Add journal CRUD and connect a user-selected entry to source passages. | Clearly separate source claims, journal facts, and assistant suggestions. |
| L09-E4 | Store explicit memory items with owner, source, date, edit, and delete. | Do not infer permanent personality traits automatically; changes affect active context. |
| L09-E5 | Trial compaction on a long synthetic conversation. | Compare required facts before/after and retain source links and covered message ranges; JIT tools arrive in L12. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Append all history forever | Allocate a budget and retrieve only relevant state. |
| Summary treated as canonical truth | Link memories to sources and preserve correction/deletion behavior. |
| Multi-agent complexity for memory alone | Prove a single workflow fails before adding another agent. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Prompt versus context engineering?
2. What is just-in-time retrieval?
3. When is compaction acceptable?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Prompt writing is part of choosing and managing all instructions, tools, evidence, history and state available to the model. |
| 2 | Keep lightweight references and fetch detailed information only when the current step needs it. |
| 3 | After measuring retained facts, lost constraints and future-task performance with recoverable source state. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S4](../project/milestones/s4.md) | Context contract, journal workflow, and editable memory schema; Focused-context and optional compaction experiments | Explain what entered context and why. Deletion is respected and stale summaries are not silently treated as facts. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Explain what entered context and why. Deletion is respected and stale summaries are not silently treated as facts.

## Postpone until justified

- Uneditable automatic memory
- Sub-agents before a working bounded single-agent design

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L09 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L08](../08-RAG-Systems/README.md) · Next numbered Level: [L10](../10-Concurrency-Streaming-Jobs/README.md)

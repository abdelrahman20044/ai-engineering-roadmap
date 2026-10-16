# L09 · Context Engineering, Memory, and Conversations

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 3 · 14–22 focused hours · Difficulty 3/5 · P1**

**You will learn:** Budget instructions, evidence, selected journals, history, and memory. Manage memory provenance, correction, deletion, and summarization loss.

**Before starting:** [L08](../08-RAG-Systems/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Context engineering and context rot

**Learn:** Prompt versus context; attention budget; irrelevant tokens; position sensitivity.

**Required reading:**

- [B30 · C5](../docs/READING_GUIDE.md#b30) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Read the opening distinction between prompt and context engineering, then “Why context engineering is important” on context rot. Save the later techniques for their steps below.

**Practice:** Compare focused evidence with the same evidence buried in distractors and report task outcomes.

**Completion check:** Compare task outcomes with focused versus distractor-heavy context.

[Alternative · AR machine-translated text](resources.md#r-ar-agent-context) (optional)

### 2. Context budget and selection

**Learn:** Instructions; schema; evidence; journal; history; output reserve.

**Required reading:**

- [B29 · C10](../docs/READING_GUIDE.md#b29) — **Read Now**. Printed p.450: Enhance Context. Other C10 sections have later owners.
- [B30 · C5](../docs/READING_GUIDE.md#b30) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Read “The anatomy of effective context” (system prompts, tools, examples and history). Apply its selection principle to your own explicit token-budget manifest; the article does not prescribe numeric budgets.

**Practice:** Create a context manifest with token counts, selection reasons and source IDs.

**Completion check:** A context manifest shows token use, source IDs and selection reasons.

[Alternative · AR machine-translated text](resources.md#r-ar-agent-context) (optional) · [Implementation reference](resources.md#r-hf-token)

### 3. Just-in-time retrieval

**Learn:** References versus full content; selective journal search; minimal tool outputs.

**Required reading:**

- [B29 · C10](../docs/READING_GUIDE.md#b29) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Read “Context retrieval and agentic search”, especially just-in-time loading and progressive discovery. Compare the two retrieval strategies in your own application.

**Practice:** Fetch relevant journal records on demand and prove unrelated entries are excluded.

**Completion check:** An unrelated journal is excluded from the model context.

[Alternative · AR machine-translated text](resources.md#r-ar-agent-context) (optional)

### 4. Conversation history and structured memory

**Learn:** Working history; durable facts; provenance; conflicts; user edit/delete.

**Required reading:**

- [B28 · C6](../docs/READING_GUIDE.md#b28) — **Read Now**. Printed pp.300–304: Memory. Keep agent pp.275–299 for B36.

**Primary · Machine-translated lesson / article:** [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md). Only the linked translated lesson, particularly its sections about Conversation history and structured memory. Its English video/cloud build is an alternative, not an extra requirement.

**Practice:** Store a user-approved memory with source, timestamp and correction/deletion tests.

**Completion check:** Memory can be corrected/deleted and retains its source/version.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-chat) (optional) · [Implementation reference](resources.md#r-sqlalchemy)

### 5. Compaction and retained constraints

**Learn:** Summaries; checkpoints; recoverable sources; lost-detail evaluation.

**Required reading:**

- [B28 · C6](../docs/READING_GUIDE.md#b28) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Read only “Compaction” and “Structured note-taking” under context engineering for long-horizon tasks. Test what your summary loses; do not implement sub-agents here.

**Practice:** Summarize a long synthetic conversation and test five facts/constraints before and after.

**Completion check:** Five constraints/facts are checked before and after compaction.

[Alternative · AR machine-translated text](resources.md#r-ar-agent-context) (optional)

### 6. Sub-agent boundary

**Learn:** Partitionable tasks; narrow context; summary handoff; coordination cost.

**Required reading:**

- [B28 · C6](../docs/READING_GUIDE.md#b28) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Building effective agents](https://www.anthropic.com/research/building-effective-agents). Read the orchestrator-workers pattern and the closing guidance on keeping designs simple. Compare with Anthropic’s context article’s sub-agent discussion; this is a design exercise, not a multi-agent build.

**Practice:** Write an ADR choosing a single workflow unless a bounded comparison demonstrates value.

**Completion check:** The ADR names a measured trigger for adding a sub-agent.

[Alternative · AR machine-translated text](resources.md#r-ar-agent-intro) (optional) · [Implementation reference](resources.md#r-context)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L09-E1:** Write a context contract with source priorities and a token budget.
  - **Pass:** Show how each input is selected, bounded, and truncated.
- [ ] **L09-E2:** Compare focused evidence against longer distractor-heavy context.
  - **Pass:** Use the same tasks and measure effects rather than assuming more context helps.
- [ ] **L09-E3:** Add journal CRUD and connect a user-selected entry to source passages.
  - **Pass:** Clearly separate source claims, journal facts, and assistant suggestions.
- [ ] **L09-E4:** Store explicit memory items with owner, source, date, edit, and delete.
  - **Pass:** Do not infer permanent personality traits automatically; changes affect active context.
- [ ] **L09-E5:** Trial compaction on a long synthetic conversation.
  - **Pass:** Compare required facts before/after and retain source links and covered message ranges; JIT tools arrive in L12.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S4](../project/milestones/s4.md). Explain what entered context and why. Deletion is respected and stale summaries are not silently treated as facts.

**Keep:** Context contract, journal workflow, and editable memory schema; Focused-context and optional compaction experiments.

## What to defer

- Uneditable automatic memory
- Sub-agents before a working bounded single-agent design

## Record progress and choose the next Level

```bash
python scripts/progress.py set L09 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L12](../12-Tools-Agents/README.md), [L16](../16-Capstone-Career/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

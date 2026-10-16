# L12 · Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 4 · 18–28 focused hours · Difficulty 4/5 · P1**

**You will learn:** Distinguish fixed workflows from model-directed tool loops. Implement safe tool contracts and evaluate tool/task failures. Understand sub-agent patterns without assuming they improve the product.

**Before starting:** [L05](../05-Evaluation/README.md), [L09](../09-Context-Memory/README.md), [L11](../11-Security-Responsible-AI/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B36 · G5](../docs/READING_GUIDE.md#b36) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Agent anatomy and design choice

**Learn:** State; model decision; action; observation; workflow alternatives.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B36 · G5](../docs/READING_GUIDE.md#b36) — **Read Now**. Printed pp.102–107 and 122–127: tools, agents and code explanation. Skip repeated travel-app setup.
- [B36a · G6](../docs/READING_GUIDE.md#b36a) — **Read Now**. Printed pp.130–132: patterns first. Remaining implementation pp.133–171 is Optional Advanced after a measured need.

**Primary · Engineering article:** [Building effective agents](https://www.anthropic.com/research/building-effective-agents). Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Agent anatomy and design choice. Multi-agent implementations are not required.

**Practice:** Draw a fixed workflow and tool loop for the same journal question; choose a baseline.

**Completion check:** A workflow baseline and bounded-agent alternative have explicit control-flow diagrams.

### 2. Tool design and schemas

**Learn:** Small names; typed inputs; concise outputs; errors; idempotent reads.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B36b · C6](../docs/READING_GUIDE.md#b36b) — **Read Now**. Printed pp.275–299: tools, planning and agent failure modes. Retrieval/memory slices were B20/B27/B28.

**Primary · Official documentation / tutorial:** [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling). Consult the Small names; typed inputs; concise outputs; errors; idempotent reads sections/examples only. Do not read the entire documentation site.

**Practice:** Expose one owner-scoped search tool; reject malformed and unauthorized arguments.

**Completion check:** Tool arguments and caller permissions are checked before execution.

### 3. Bounded execution loop

**Learn:** Max steps; timeout; token/cost budget; stop/ask-human; error states.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B36b · C6](../docs/READING_GUIDE.md#b36b) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Book section:** [B36b · C6](../docs/READING_GUIDE.md#b36b). Follow the assigned portion above; use the library references during implementation.

**Practice:** Test repeated calls, unavailable tools, budget exhaustion and terminal behavior.

**Completion check:** Repeated calls and budget exhaustion terminate predictably.

### 4. Agent evaluation

**Learn:** Tool choice; arguments; trajectory; task success; final-answer grounding.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B17 · F11](../docs/READING_GUIDE.md#b17) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B36b · C6](../docs/READING_GUIDE.md#b36b) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Documentation: assertions reference:** [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/). The assertion type matching Agent evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Practice:** Label five correct and five failed traces; report tool and task metrics separately.

**Completion check:** Tool/trajectory scores are distinct from final-answer quality.

### 5. Memory and context interfaces

**Learn:** Retrieve only needed state; observation size; provenance; side-effect confirmation.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B28 · C6](../docs/READING_GUIDE.md#b28) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Review only tool design, just-in-time retrieval and sub-agent tradeoffs from L09; no full article reread.

**Practice:** Limit tool result size and prove relevant evidence survives the bound.

**Completion check:** Bounded tool results preserve the relevant evidence with source IDs.

### 6. Multi-agent comparison

**Learn:** Specialist role; independent context; handoff summary; coordination failures.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B36a · G6](../docs/READING_GUIDE.md#b36a) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B36b · C6](../docs/READING_GUIDE.md#b36b) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Engineering article:** [Building effective agents](https://www.anthropic.com/research/building-effective-agents). Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Multi-agent comparison. Multi-agent implementations are not required.

**Practice:** Run one partitioned experiment against the single-agent baseline; record a go/no-go ADR.

**Completion check:** The comparison records any benefit plus coordination cost/failures.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L12-E1:** Define read-only search_passages and get_passage tools with bounded outputs.
  - **Pass:** Validate schemas and enforce authenticated ownership; no generic SQL or shell tool.
- [ ] **L12-E2:** Build a small direct-SDK loop with max steps, timeout, and token budget.
  - **Pass:** Handle unknown tool, invalid arguments, no-tool-needed, and repeated-loop cases.
- [ ] **L12-E3:** Compare a fixed workflow and agent on fifteen tasks.
  - **Pass:** Report success, tool errors, unauthorized attempts, latency, and cost.
- [ ] **L12-E4:** Use lightweight references and fetch passages just in time.
  - **Pass:** Only permitted requested content is loaded; compare against upfront retrieval.
- [ ] **L12-E5:** Design a planner/worker experiment and a summary contract.
  - **Pass:** Implement extra agents only if a measured use case justifies isolation, coordination, and cost.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S5](../project/milestones/s5.md). A model request is never treated as authorization. Loops stop predictably and you can justify either using an agent or retaining a fixed workflow.

**Keep:** Tool contracts, bounded agent loop, and evaluation report; Single-agent versus multi-agent ADR.

## What to defer

- Framework orchestration before understanding a loop
- Multi-agent implementation just to check a syllabus keyword

## Record progress and choose the next Level

```bash
python scripts/progress.py set L12 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L13](../13-MCP-Enterprise-Integration/README.md), [L16](../16-Capstone-Career/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

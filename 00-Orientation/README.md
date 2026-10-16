# L00 · Baseline Assessment and Product Scope

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 1 · 3–5 focused hours · Difficulty 1/5 · P0**

**You will learn:** Identify transferable backend skills and specific gaps. Define users, requirements, failure cases, and acceptance evidence.

**Before starting:** Use your existing backend, Python and SQL experience. Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B01 · G1](../docs/READING_GUIDE.md#b01) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Transfer backend skills

**Learn:** Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B01 · G1](../docs/READING_GUIDE.md#b01) — **Read Now**. Printed pp.1–22: LLM/application intuition. Read once; L03 reviews it.
- [B02 · C1](../docs/READING_GUIDE.md#b02) — **Read Now**. Printed pp.28–34: Planning AI Applications; pp.35–46: The AI Engineering Stack. Skim history.

**Primary · Single video + companion repository:** [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial). Consult the Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries sections/examples only. Do not read the entire documentation site.

**Practice:** Record a comparison with one existing CRM implementation and one Python gap.

**Completion check:** Name one working CRM artifact and one specific Python gap.

### 2. Choose the user problem

**Learn:** Book questions; journal connections; non-goals; permitted document corpus.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B02 · C1](../docs/READING_GUIDE.md#b02) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video (lesson within playlist):** [mini-RAG · What will we build ماذا سنبنى في المشروع](https://www.youtube.com/watch?v=_l5S5CdxE-Q&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=2). Only the linked “What will we build ماذا سنبنى في المشروع” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Write five user stories with acceptance conditions and only one first-release flow.

**Completion check:** Five stories, three non-goals and a single first-release flow exist.

### 3. Define answer contracts

**Learn:** Evidence versus suggestion; no-evidence behavior; ownership.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B03 · C4](../docs/READING_GUIDE.md#b03) — **Skim**. Printed pp.200–207: Design Your Evaluation Pipeline. Preview the workflow; L05 applies it.

**Primary · Machine-translated lesson / article:** [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md). Only the linked translated lesson, particularly its sections about Define answer contracts. Its English video/cloud build is an alternative, not an extra requirement.

**Practice:** Write three response examples: supported, unsupported and unauthorized.

**Completion check:** Supported, unsupported and unauthorized responses are visibly different.

### 4. Plan evaluation evidence

**Learn:** Answerable/unanswerable questions; expected source; fixed synthetic cases.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B03 · C4](../docs/READING_GUIDE.md#b03) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single lecture video + slides:** [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/). Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Plan evaluation evidence. Exact timestamps are not assigned.

**Practice:** Create ten initial questions with source references; label these development cases.

**Completion check:** Ten cases have evidence labels and a stated pass/fail criterion.

### 5. Learn independently

**Learn:** Read → recall → implement → test → explain; AI assistance boundaries.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Course unit: lecture + problem set:** [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/). Week 5 “Unit Tests”: assertions/pytest explanation only; use it to calibrate the diagnostic.

**Practice:** Explain the use case in two minutes and implement a tiny change without AI.

**Completion check:** Explain the product in two minutes and implement a small independent change.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L00-E1:** Explain a JWT/RBAC flow, Zod validation, and an integration test from CRM. Write a typed JSON cleaner and a test without AI.
  - **Pass:** Record demonstrated skills and gaps; distinguish prior evidence from assumptions.
- [ ] **L00-E2:** Write five user stories and three failure cases: missing evidence, unreadable document, and unauthorized resource access.
  - **Pass:** Each story has an observable acceptance condition.
- [ ] **L00-E3:** Choose a small permitted corpus, specify input/output contracts and three non-goals, and create the first ADR.
  - **Pass:** A one-page scope and ten initial questions are sufficient to start building.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S0](../project/milestones/s0.md). Explain the use case and the first deliverable in two minutes. Review only demonstrated gaps rather than restarting backend fundamentals.

**Keep:** baseline.md with links to prior work; project-scope.md and the first ADR.

## What to defer

- Repeating JavaScript, HTTP, Git, or Docker basics after passing diagnostics
- Microservices or buying a GPU before a need exists

## Record progress and choose the next Level

```bash
python scripts/progress.py set L00 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L01](../01-Python-FastAPI/README.md), [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

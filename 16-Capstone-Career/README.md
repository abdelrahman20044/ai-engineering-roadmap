# L16 · Capstone Release, Technical Defense, and Career Evidence

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 5 · 12–18 focused hours · Difficulty 4/5 · P2**

**You will learn:** Demonstrate a usable AI application with evaluation and operating evidence. Explain and modify the implementation independently and communicate honest limitations.

**Before starting:** [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md), [L08](../08-RAG-Systems/README.md), [L09](../09-Context-Memory/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md), [L11](../11-Security-Responsible-AI/README.md), [L12](../12-Tools-Agents/README.md), [L13](../13-MCP-Enterprise-Integration/README.md), [L14](../14-LLMOps-Deployment/README.md), [L15](../15-Model-Selection-Optimization/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Reproducible capstone release

**Learn:** Setup; seed corpus; secrets template; migrations; version manifest.

**Required reading:**

- [B38 · F11](../docs/READING_GUIDE.md#b38) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B39 · F12](../docs/READING_GUIDE.md#b39) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Documentation article:** [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes). Consult the Setup; seed corpus; secrets template; migrations; version manifest sections/examples only. Do not read the entire documentation site.

**Practice:** A reviewer runs the release on synthetic data from a clean checkout.

**Completion check:** A reviewer can run the release with synthetic data from a clean checkout.

[Alternative · AR video](resources.md#r-ar-mini-4) (optional) · [Implementation reference](resources.md#r-releases)

### 2. Final evaluation and limitations

**Learn:** Untouched holdout; raw counts; source/citation results; failure taxonomy.

**Required reading:**

- [B44 · C4](../docs/READING_GUIDE.md#b44) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Documentation: assertions reference:** [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/). The assertion type matching Final evaluation and limitations; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Practice:** Freeze the config, run holdout once for release assessment and analyze three failures.

**Completion check:** The frozen holdout report discloses raw counts and three major failures.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-lifecycle) (optional)

### 3. Architecture and technical defense

**Learn:** ERD; request trace; ADR; provider boundary; agent/no-agent rationale.

**Required reading:**

- [B02 · C1](../docs/READING_GUIDE.md#b02) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Template / reference repository:** [Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record). Consult the ERD; request trace; ADR; provider boundary; agent/no-agent rationale sections/examples only. Do not read the entire documentation site.

**Practice:** Present a 5-minute demo and a deeper 20-minute walkthrough with one rejected option.

**Completion check:** The short demo and deeper defense explain one rejected design.

[Alternative · AR video](resources.md#r-ar-mini-4) (optional) · [Implementation reference](resources.md#r-technical-writing)

### 4. AI fundamentals interview bridge

**Learn:** ML leakage; gradients; tokens; embeddings; retrieval; sampling.

**Required reading:**

- [B01 · G1](../docs/READING_GUIDE.md#b01) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B15 · C3](../docs/READING_GUIDE.md#b15) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html). Consult the ML leakage; gradients; tokens; embeddings; retrieval; sampling sections/examples only. Do not read the entire documentation site.

**Practice:** Answer conceptual questions using your own experiment or failure example.

**Completion check:** Fundamental answers use the learner’s own experiments and failures.

[Alternative · AR video](resources.md#r-ar-sklearn) (optional) · [Implementation reference](resources.md#r-st-eval)

### 5. Backend and operations defense

**Learn:** Auth; SQL; transaction; async; worker; deployment; trace diagnosis.

**Required reading:**

- [B06 · F11](../docs/READING_GUIDE.md#b06) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html). Consult the Auth; SQL; transaction; async; worker; deployment; trace diagnosis sections/examples only. Do not read the entire documentation site.

**Practice:** Write an endpoint, query and test independently; diagnose a supplied failing trace.

**Completion check:** An endpoint, query and test can be written without generated code.

[Alternative · AR video](resources.md#r-ar-mini-20) (optional) · [Implementation reference](resources.md#r-asyncio)

### 6. Career evidence and communication

**Learn:** Role-specific CV; scoped proposal; ethical claims; status reporting.

**Required reading:**

- [B43 · C10](../docs/READING_GUIDE.md#b43) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Written course + exercises:** [Technical Writing One](https://developers.google.com/tech-writing/one). Technical Writing One: audience, organization and concise sentences; do one writing exercise using the project README/proposal.

**Practice:** Write three evidence-backed CV bullets and a scoped delivery proposal with assumptions and acceptance criteria.

**Completion check:** CV/proposal claims link to measured evidence and scoped acceptance criteria.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-ux) (optional)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L16-E1:** Demonstrate upload → question → source → journal connection → conversation → deletion through a basic UI.
  - **Pass:** Include failure paths and cross-user access tests.
- [ ] **L16-E2:** Freeze configuration and run the final independent holdout.
  - **Pass:** Analyze three major failures and disclose remaining limitations.
- [ ] **L16-E3:** Publish application setup docs, ERD/architecture, ADRs, runbook, and a 3–5-minute demo.
  - **Pass:** A reviewer can reproduce the demo with synthetic data.
- [ ] **L16-E4:** Run a mock defense: write an endpoint, query, and test without AI; diagnose a trace.
  - **Pass:** Explain framework, model, retrieval, and single-agent decisions.
- [ ] **L16-E5:** Draft evidence-based CV claims and a scoped freelance proposal.
  - **Pass:** Only measured figures are used; discuss data ethics, delivery scope, and communication.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S7](../project/milestones/s7.md). Run, explain, modify, and evaluate the system. This is a self-study gate, not an ITI credential or hiring guarantee. L17/L18 remain optional.

**Keep:** Versioned release, demo, evaluation report/dashboard, and defense notes.

## What to defer

- Waiting for every advanced topic before applying
- Inflated metrics or unsupported production-ready claims

## Record progress and choose the next Level

```bash
python scripts/progress.py set L16 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** No further required Level; return to the capstone or role checklist.

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

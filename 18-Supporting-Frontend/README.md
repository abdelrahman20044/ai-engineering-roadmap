# L18 · Supporting TypeScript and React UI

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 6 · 12–20 focused hours · Difficulty 2/5 · P3 · Optional Level**

**You will learn:** Build a small accessible client for API errors, streaming, and evidence display. Distinguish product UI needs from a complete React/TypeScript curriculum.

**Before starting:** [L01](../01-Python-FastAPI/README.md), [L04](../04-LLM-Applications-Prompts/README.md), [L11](../11-Security-Responsible-AI/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. TypeScript bridge

**Learn:** Interfaces; unions; narrowing; request/response types.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Official documentation / tutorial:** [React with TypeScript](https://react.dev/learn/typescript). Consult the Interfaces; unions; narrowing; request/response types sections/examples only. Do not read the entire documentation site.

**Practice:** Type API success/error responses and remove unsafe any usage from the request layer.

**Completion check:** API success/error types are explicit and unsafe any is removed from the request layer.

### 2. React state and components

**Learn:** Upload state; chat turns; journal form; component boundaries.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.

**Primary · Official documentation / tutorial:** [React Learn](https://react.dev/learn). Consult the Upload state; chat turns; journal form; component boundaries sections/examples only. Do not read the entire documentation site.

**Practice:** Build a small UI with explicit loading, error and empty states.

**Completion check:** Upload/chat/journal views expose loading, error and empty states.

### 3. Authenticated API client

**Learn:** Fetch; cookies/headers; expired sessions; server errors.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B33 · F8](../docs/READING_GUIDE.md#b33) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). Consult the Fetch; cookies/headers; expired sessions; server errors sections/examples only. Do not read the entire documentation site.

**Practice:** Handle expired sessions and forbidden source requests without exposing stale private data.

**Completion check:** Expired/forbidden responses cannot reveal stale private state.

### 4. Streaming and cancellation

**Learn:** ReadableStream; event framing; abort; partial completion.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B48 · F6](../docs/READING_GUIDE.md#b48) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). Consult the ReadableStream; event framing; abort; partial completion sections/examples only. Do not read the entire documentation site.

**Practice:** Render partial text, cancel a response and display terminal error/completion states.

**Completion check:** Partial text, cancellation and terminal failures are handled.

### 5. Evidence and reflection UX

**Learn:** Source/page view; book claim versus suggestion; uncertainty; memory controls.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B43 · C10](../docs/READING_GUIDE.md#b43) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Machine-translated lesson / article:** [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md). Only the linked translated lesson, particularly its sections about Evidence and reflection UX. Its English video/cloud build is an alternative, not an extra requirement.

**Practice:** Click a citation to an authorized passage and allow memory correction/deletion.

**Completion check:** Authorized citations open and memory correction/deletion is usable.

### 6. Accessibility and end-to-end tests

**Learn:** Keyboard; focus; labels; errors; upload→ask→source→delete.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B38 · F11](../docs/READING_GUIDE.md#b38) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Playwright writing tests](https://playwright.dev/docs/writing-tests). Consult the Keyboard; focus; labels; errors; upload→ask→source→delete sections/examples only. Do not read the entire documentation site.

**Practice:** Automate the main happy/error paths and manually test keyboard navigation.

**Completion check:** The happy/error paths pass browser tests and keyboard navigation is checked.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L18-E1:** Type requests, responses, and citations; add upload/question/journal forms.
  - **Pass:** Handle loading, empty, and failure states.
- [ ] **L18-E2:** Display source snippets and pages using server metadata.
  - **Pass:** Test keyboard navigation, long text, and RTL if supported by the product.
- [ ] **L18-E3:** Integrate authentication and streaming without browser secrets.
  - **Pass:** Document cookie/bearer/CORS/CSRF choices for the client.
- [ ] **L18-E4:** Test a normal UI journey and unauthorized access.
  - **Pass:** The UI exposes backend failures rather than masking them.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S7](../project/milestones/s7.md). A basic UI is required by the capstone. React specifically is optional for this self-study Core, while explicit React/TypeScript coverage remains visible in the ITI mapping.

**Keep:** Small React/TypeScript client, API contract, and UI/accessibility test notes.

## What to defer

- Advanced frontend design
- Pausing AI engineering until a complete frontend course is finished

## Record progress and choose the next Level

```bash
python scripts/progress.py set L18 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** No further required Level; return to the capstone or role checklist.

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

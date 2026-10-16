# L18 · Supporting TypeScript and React UI

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 6 · Optional Specialization and Supporting UI | 12–20 h | 2/5 | P3 · optional | [L01](../01-Python-FastAPI/README.md), [L04](../04-LLM-Applications-Prompts/README.md), [L11](../11-Security-Responsible-AI/README.md) |

**Unlocks:** No further required Level; use the evidence to apply or specialize.

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Build a small accessible client for API errors, streaming, and evidence display. Distinguish product UI needs from a complete React/TypeScript curriculum. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| JavaScript transfer | Use promises, modules and HTTP requests without a full JS course. |
| Backend readiness | Stable auth, upload, question and source endpoints exist. |
| Product contract | Define streaming events and the citation response schema. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] TypeScript bridge: Type API success/error responses and remove unsafe any usage from the request layer.
- [ ] React state and components: Build a small UI with explicit loading, error and empty states.
- [ ] Authenticated API client: Handle expired sessions and forbidden source requests without exposing stale private data.
- [ ] Streaming and cancellation: Render partial text, cancel a response and display terminal error/completion states.
- [ ] Evidence and reflection UX: Click a citation to an authorized passage and allow memory correction/deletion.
- [ ] Accessibility and end-to-end tests: Automate the main happy/error paths and manually test keyboard navigation.

## Recommended learning path

Optional supporting UI: Elzero TypeScript gaps → React official quick path → fetch/abort → source display and browser tests. A minimal client is sufficient.

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
| **L18-T01 · TypeScript bridge**<br>Interfaces; unions; narrowing; request/response types | [TypeScript study plan](https://elzero.org/study/typescript-study-plan/) (AR video + assignments) | [React with TypeScript](https://react.dev/learn/typescript) (EN) | Type API success/error responses and remove unsafe any usage from the request layer. |
| **L18-T02 · React state and components**<br>Upload state; chat turns; journal form; component boundaries | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text)<br>**Scope:** AI UX design context; React implementation is covered by the English tutorial. | [React Learn](https://react.dev/learn) (EN) | Build a small UI with explicit loading, error and empty states. |
| **L18-T03 · Authenticated API client**<br>Fetch; cookies/headers; expired sessions; server errors | [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) (AR video + code)<br>**Scope:** HTTP/API introduction; authenticated browser contracts use F8/Fetch docs. | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Handle expired sessions and forbidden source requests without exposing stale private data. |
| **L18-T04 · Streaming and cancellation**<br>ReadableStream; event framing; abort; partial completion | [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) (AR machine-translated text)<br>**Scope:** Conversation-app context; ReadableStream/abort implementation uses English docs. | [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) (EN)<br>[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) (EN) | Render partial text, cancel a response and display terminal error/completion states. |
| **L18-T05 · Evidence and reflection UX**<br>Source/page view; book claim versus suggestion; uncertainty; memory controls | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text)<br>[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) (EN video + slides) | Click a citation to an authorized passage and allow memory correction/deletion. |
| **L18-T06 · Accessibility and end-to-end tests**<br>Keyboard; focus; labels; errors; upload→ask→source→delete | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text)<br>**Scope:** UX principles only; accessible client/browser tests use English resources. | [Playwright writing tests](https://playwright.dev/docs/writing-tests) (EN) | Automate the main happy/error paths and manually test keyboard navigation. |

**Arabic coverage boundary:** Elzero provides Arabic TypeScript teaching. This Level uses English React/MDN docs for current React, stream consumption and accessibility; a React-specific Arabic playlist was not verified in this pass.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L18-T01 | No TypeScript coverage in the three AI books; official React/TypeScript tutorial fills the gap | [React with TypeScript](https://react.dev/learn/typescript) (EN) |
| L18-T02 | Official React Learn is primary; F6 is backend contract reference | [React Learn](https://react.dev/learn) (EN) |
| L18-T03 | F8 auth contract review | [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) (EN) |
| L18-T04 | F6 communication reference | [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) (EN)<br>[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) (EN) |
| L18-T05 | C10 feedback and C4 criteria; UI implementation is additional | [React Learn](https://react.dev/learn) (EN) |
| L18-T06 | F11 E2E principles | [Playwright writing tests](https://playwright.dev/docs/writing-tests) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N05 · Software Testing & Full-Stack Debugging | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N08 · Frontend TypeScript & React | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L18-E1 | Type requests, responses, and citations; add upload/question/journal forms. | Handle loading, empty, and failure states. |
| L18-E2 | Display source snippets and pages using server metadata. | Test keyboard navigation, long text, and RTL if supported by the product. |
| L18-E3 | Integrate authentication and streaming without browser secrets. | Document cookie/bearer/CORS/CSRF choices for the client. |
| L18-E4 | Test a normal UI journey and unauthorized access. | The UI exposes backend failures rather than masking them. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Full frontend specialization | Implement only the capstone user flows. |
| Client guards replace backend auth | Server ownership tests remain mandatory. |
| Render model output as arbitrary HTML | Use safe rendering and explicit source links; avoid unsanitized HTML. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Why a discriminated union for API results?
2. Why AbortController?
3. What proves usable citations?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | It forces success/error/stream states to be handled explicitly. |
| 2 | It cancels a fetch/stream and lets the UI stop unnecessary work. |
| 3 | Keyboard-accessible source links resolve to authorized passages with page/context and clear loading/error states. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S7](../project/milestones/s7.md) | Small React/TypeScript client, API contract, and UI/accessibility test notes | A basic UI is required by the capstone. React specifically is optional for this self-study Core, while explicit React/TypeScript coverage remains visible in the ITI mapping. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

A basic UI is required by the capstone. React specifically is optional for this self-study Core, while explicit React/TypeScript coverage remains visible in the ITI mapping.

## Postpone until justified

- Advanced frontend design
- Pausing AI engineering until a complete frontend course is finished

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L18 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L17](../17-Fine-Tuning-Advanced-Serving/README.md) · Return to the capstone and role checklist.

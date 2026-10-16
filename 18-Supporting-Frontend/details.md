# Technical Details · L18

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **JavaScript transfer:** Use promises, modules and HTTP requests without a full JS course.
- **Backend readiness:** Stable auth, upload, question and source endpoints exist.
- **Product contract:** Define streaming events and the citation response schema.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **TypeScript bridge:** Interfaces; unions; narrowing; request/response types.
- **React state and components:** Upload state; chat turns; journal form; component boundaries.
- **Authenticated API client:** Fetch; cookies/headers; expired sessions; server errors.
- **Streaming and cancellation:** ReadableStream; event framing; abort; partial completion.
- **Evidence and reflection UX:** Source/page view; book claim versus suggestion; uncertainty; memory controls.
- **Accessibility and end-to-end tests:** Keyboard; focus; labels; errors; upload→ask→source→delete.

## Common mistakes and debugging

### Full frontend specialization

Implement only the capstone user flows.

### Client guards replace backend auth

Server ownership tests remain mandatory.

### Render model output as arbitrary HTML

Use safe rendering and explicit source links; avoid unsanitized HTML.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Why a discriminated union for API results?
2. Why AbortController?
3. What proves usable citations?

<details>
<summary>Answer guide</summary>

**Why a discriminated union for API results?**

It forces success/error/stream states to be handled explicitly.

**Why AbortController?**

It cancels a fetch/stream and lets the UI stop unnecessary work.

**What proves usable citations?**

Keyboard-accessible source links resolve to authorized passages with page/context and clear loading/error states.

</details>

## ITI provenance and industry extensions

- **N05:** Software Testing & Full-Stack Debugging — official published module title.
- **N08:** Frontend TypeScript & React — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Type API success/error responses and remove unsafe any usage from the request layer.
- [ ] Build a small UI with explicit loading, error and empty states.
- [ ] Handle expired sessions and forbidden source requests without exposing stale private data.
- [ ] Render partial text, cancel a response and display terminal error/completion states.
- [ ] Click a citation to an authorized passage and allow memory correction/deletion.
- [ ] Automate the main happy/error paths and manually test keyboard navigation.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

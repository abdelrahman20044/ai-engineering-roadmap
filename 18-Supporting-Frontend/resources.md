# Resource Library · L18 — Supporting TypeScript and React UI

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Elzero provides Arabic TypeScript teaching. This Level uses English React/MDN docs for current React, stream consumption and accessibility; a React-specific Arabic playlist was not verified in this pass.

## Topic navigation

1. [TypeScript bridge](#unit-01)
2. [React state and components](#unit-02)
3. [Authenticated API client](#unit-03)
4. [Streaming and cancellation](#unit-04)
5. [Evidence and reflection UX](#unit-05)
6. [Accessibility and end-to-end tests](#unit-06)

<a id="unit-01"></a>

## 1. TypeScript bridge

[Return to README Step 1](README.md#1-typescript-bridge)

**Topic/subtopics:** Interfaces; unions; narrowing; request/response types.

**Required sequence:** `react`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-typescript-bridge) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `react` · [React with TypeScript](https://react.dev/learn/typescript)<br>React · EN | Documentation / tutorial | Primary | Typing props, hooks and events. | Consult the Interfaces; unions; narrowing; request/response types… [bounds](#unit-01-react) |
| `ar-ts` · [TypeScript study plan](https://elzero.org/study/typescript-study-plan/)<br>Osama Elzero · Egypt · AR video + assignments | Full Course / study-plan index | Complementary (as needed) | Interfaces, unions, narrowing and generics for the small… | #22–26 interfaces and #34–37 generics. Review only missing TypeScript… [bounds](#unit-01-ar-ts) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-react"></a>

**`react` — selected portion:** Consult the Interfaces; unions; narrowing; request/response types sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-ts"></a>

**`ar-ts` — selected portion:** #22–26 interfaces and #34–37 generics. Review only missing TypeScript concepts before typing the small React client.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-02"></a>

## 2. React state and components

[Return to README Step 2](README.md#2-react-state-and-components)

**Topic/subtopics:** Upload state; chat turns; journal form; component boundaries.

**Required sequence:** `react-learn`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-react-state-and-components) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `react-learn` · [React Learn](https://react.dev/learn)<br>React · EN | Documentation / tutorial | Primary | State, effects and component boundaries. | Consult the Upload state; chat turns; journal form; component boundaries… [bounds](#unit-02-react-learn) |
| `ar-gen-ux` · [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Communicating limitations, feedback and human control. | Only the linked translated lesson: Communicating limitations, feedback and… [bounds](#unit-02-ar-gen-ux) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-react-learn"></a>

**`react-learn` — selected portion:** Consult the Upload state; chat turns; journal form; component boundaries sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-gen-ux"></a>

**`ar-gen-ux` — selected portion:** Only the linked translated lesson: Communicating limitations, feedback and human control. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: AI UX design context; React implementation is covered by the English tutorial.

</details>

<a id="unit-03"></a>

## 3. Authenticated API client

[Return to README Step 3](README.md#3-authenticated-api-client)

**Topic/subtopics:** Fetch; cookies/headers; expired sessions; server errors.

**Required sequence:** `fetch`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-authenticated-api-client) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B33 · F8](../docs/READING_GUIDE.md#b33)<br>Alireza Parandeh · EN | Book Section | Reference | Authenticated API client | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b33) |
| `fetch` · [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)<br>MDN · EN | Documentation / tutorial | Primary | HTTP errors, response bodies, streaming and abort signals. | Consult the Fetch; cookies/headers; expired sessions; server errors… [bounds](#unit-03-fetch) |
| `ar-api` · [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)<br>Pythonation · Arabic Python community · AR video + code | Single Video + companion repository | Complementary (as needed) | Turn Python functions into validated HTTP endpoints and… | Consult the relevant example for Turn Python functions into validated HTTP… [bounds](#unit-03-ar-api) |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Complementary (as needed) | Authenticated API client (selected course unit) | Section 8 login/token examples for API contract review; browser Fetch handling comes from MDN. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-fetch"></a>

**`fetch` — selected portion:** Consult the Fetch; cookies/headers; expired sessions; server errors sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-api"></a>

**`ar-api` — selected portion:** Consult the relevant example for Turn Python functions into validated HTTP endpoints and inspect the companion app. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: HTTP/API introduction; authenticated browser contracts use F8/Fetch docs.

<a id="unit-03-fcc-api"></a>

**`fcc-api` — selected portion:** Section 8 login/token examples for API contract review; browser Fetch handling comes from MDN.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-04"></a>

## 4. Streaming and cancellation

[Return to README Step 4](README.md#4-streaming-and-cancellation)

**Topic/subtopics:** ReadableStream; event framing; abort; partial completion.

**Required sequence:** `fetch`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `stream`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-streaming-and-cancellation) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B48 · F6](../docs/READING_GUIDE.md#b48)<br>Alireza Parandeh · EN | Book Section | Reference | Streaming and cancellation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b48) |
| `fetch` · [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)<br>MDN · EN | Documentation / tutorial | Primary | HTTP errors, response bodies, streaming and abort signals. | Consult the ReadableStream; event framing; abort; partial completion… [bounds](#unit-04-fetch) |
| `ar-gen-chat` · [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Conversation state and token/context constraints. | Only the linked translated lesson: Conversation state and token/context… [bounds](#unit-04-ar-gen-chat) |
| `stream` · [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)<br>FastAPI · EN | Documentation / tutorial | Reference | StreamingResponse and generator behavior; frame your own… | Consult the relevant example for StreamingResponse and generator behavior;… [bounds](#unit-04-stream) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-fetch"></a>

**`fetch` — selected portion:** Consult the ReadableStream; event framing; abort; partial completion sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-gen-chat"></a>

**`ar-gen-chat` — selected portion:** Only the linked translated lesson: Conversation state and token/context constraints. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Conversation-app context; ReadableStream/abort implementation uses English docs.

<a id="unit-04-stream"></a>

**`stream` — selected portion:** Consult the relevant example for StreamingResponse and generator behavior; frame your own event stream correctly. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Evidence and reflection UX

[Return to README Step 5](README.md#5-evidence-and-reflection-ux)

**Topic/subtopics:** Source/page view; book claim versus suggestion; uncertainty; memory controls.

**Required sequence (default route):** `ar-gen-ux`. Stop each source at the stated portion.

**Choose ONE explanation for uncertainty and source/answer UX:** default `ar-gen-ux` **OR** `fsdl-ux`. Keep accessibility and evidence-navigation acceptance criteria. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `react-learn`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-evidence-and-reflection-ux) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B43 · C10](../docs/READING_GUIDE.md#b43)<br>Chip Huyen · EN | Book Section | Reference | Evidence and reflection UX | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b43) |
| `ar-gen-ux` · [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Primary | Communicating limitations, feedback and human control. | Only the linked translated lesson, particularly its sections about… [bounds](#unit-05-ar-gen-ux) |
| `ar-gen-responsible` · [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Fairness, reliability and accountable use. | Only the linked translated lesson: Fairness, reliability and accountable… [bounds](#unit-05-ar-gen-responsible) |
| `fsdl-ux` · [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Alternative | Uncertainty, interaction design and feedback. | Topic bounds; lesson IDs not verified — [details](#unit-05-fsdl-ux) |
| `react-learn` · [React Learn](https://react.dev/learn)<br>React · EN | Documentation / tutorial | Reference | State, effects and component boundaries. | Consult the relevant example for State, effects and component boundaries.… [bounds](#unit-05-react-learn) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-ar-gen-ux"></a>

**`ar-gen-ux` — selected portion:** Only the linked translated lesson, particularly its sections about Evidence and reflection UX. Its English video/cloud build is an alternative, not an extra requirement.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-gen-responsible"></a>

**`ar-gen-responsible` — selected portion:** Only the linked translated lesson: Fairness, reliability and accountable use. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-fsdl-ux"></a>

**`fsdl-ux` — selected portion:** Only the linked lesson on Uncertainty, interaction design and feedback. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for uncertainty and source/answer UX. Keep accessibility and evidence-navigation acceptance criteria.

<a id="unit-05-react-learn"></a>

**`react-learn` — selected portion:** Consult the relevant example for State, effects and component boundaries. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Accessibility and end-to-end tests

[Return to README Step 6](README.md#6-accessibility-and-end-to-end-tests)

**Topic/subtopics:** Keyboard; focus; labels; errors; upload→ask→source→delete.

**Required sequence:** `playwright`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-accessibility-and-end-to-end-tests) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B38 · F11](../docs/READING_GUIDE.md#b38)<br>Alireza Parandeh · EN | Book Section | Reference | Accessibility and end-to-end tests | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b38) |
| `playwright` · [Playwright writing tests](https://playwright.dev/docs/writing-tests)<br>Playwright · EN | Documentation / tutorial | Primary | Browser-level tests for login, chat, errors and citation… | Consult the Keyboard; focus; labels; errors; upload→ask→source→delete… [bounds](#unit-06-playwright) |
| `ar-gen-ux` · [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Communicating limitations, feedback and human control. | Only the linked translated lesson: Communicating limitations, feedback and… [bounds](#unit-06-ar-gen-ux) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-playwright"></a>

**`playwright` — selected portion:** Consult the Keyboard; focus; labels; errors; upload→ask→source→delete sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-gen-ux"></a>

**`ar-gen-ux` — selected portion:** Only the linked translated lesson: Communicating limitations, feedback and human control. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: UX principles only; accessible client/browser tests use English resources.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-ts"></a>

<details>
<summary>ar-ts · TypeScript study plan — access, scope and verification</summary>

[TypeScript study plan](https://elzero.org/study/typescript-study-plan/) · Osama Elzero · Egypt · AR video + assignments

- **Resource Type:** Full Course / study-plan index.
- **Access:** Free.
- **Catalog scope:** Interfaces, unions, narrowing and generics for the small client.
- **Scope/version limits:** Select unfamiliar typing topics; skip JavaScript basics.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** TypeScript bridge.
- **Retained broad selection notes (lookup only):** Only Elzero lessons 22–26 (interfaces) and 34–37 (generics) where needed; verify the topic title in the study plan. Skip already-known JS material.

</details>

<a id="r-react"></a>

<details>
<summary>react · React with TypeScript — access, scope and verification</summary>

[React with TypeScript](https://react.dev/learn/typescript) · React · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Typing props, hooks and events.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** TypeScript bridge.
- **Retained broad selection notes (lookup only):** Consult the Interfaces; unions; narrowing; request/response types sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-ux"></a>

<details>
<summary>ar-gen-ux · AI user experience · Arabic — access, scope and verification</summary>

[AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Communicating limitations, feedback and human control.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** React state and components; Evidence and reflection UX; Accessibility and end-to-end tests.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Evidence and reflection UX. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-react-learn"></a>

<details>
<summary>react-learn · React Learn — access, scope and verification</summary>

[React Learn](https://react.dev/learn) · React · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** State, effects and component boundaries.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** React state and components; Evidence and reflection UX.
- **Retained broad selection notes (lookup only):** Consult the Upload state; chat turns; journal form; component boundaries sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-api"></a>

<details>
<summary>ar-api · Pythonation FastAPI tutorial and companion code — access, scope and verification</summary>

[Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) · Pythonation · Arabic Python community · AR video + code

- **Resource Type:** Single Video + companion repository.
- **Access:** Free.
- **Catalog scope:** Turn Python functions into validated HTTP endpoints and inspect the companion app.
- **Scope/version limits:** Introductory; lifecycle, production security and async depth need the official docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Authenticated API client.
- **Retained broad selection notes (lookup only):** Consult the Fetch; cookies/headers; expired sessions; server errors sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-fcc-api"></a>

<details>
<summary>fcc-api · Creating APIs with Python · course index — access, scope and verification</summary>

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) · Sanjeev Thiyagarajan · freeCodeCamp · EN video

- **Resource Type:** Full Course (19 hours; selected sections only).
- **Access:** Free.
- **Catalog scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Scope/version limits:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Authenticated API client.
- **Retained broad selection notes (lookup only):** Section 8 authentication is backend contract review; it does not teach React or streaming clients.

</details>

<a id="r-fetch"></a>

<details>
<summary>fetch · Using Fetch — access, scope and verification</summary>

[Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) · MDN · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** HTTP errors, response bodies, streaming and abort signals.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Authenticated API client; Streaming and cancellation.
- **Retained broad selection notes (lookup only):** Consult the Fetch; cookies/headers; expired sessions; server errors sections/examples only. Do not read the entire documentation site. Consult the ReadableStream; event framing; abort; partial completion sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-chat"></a>

<details>
<summary>ar-gen-chat · Chat applications · Arabic — access, scope and verification</summary>

[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Conversation state and token/context constraints.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Streaming and cancellation.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Streaming and cancellation. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-stream"></a>

<details>
<summary>stream · FastAPI custom responses — access, scope and verification</summary>

[FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** StreamingResponse and generator behavior; frame your own event stream correctly.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Streaming and cancellation.
- **Retained broad selection notes (lookup only):** Consult the ReadableStream; event framing; abort; partial completion sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-responsible"></a>

<details>
<summary>ar-gen-responsible · Responsible generative AI · Arabic — access, scope and verification</summary>

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Fairness, reliability and accountable use.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Evidence and reflection UX.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Evidence and reflection UX. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-fsdl-ux"></a>

<details>
<summary>fsdl-ux · UX for Language User Interfaces — access, scope and verification</summary>

[UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Uncertainty, interaction design and feedback.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Evidence and reflection UX.
- **Retained broad selection notes (lookup only):** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Evidence and reflection UX. Exact timestamps are not assigned.

</details>

<a id="r-playwright"></a>

<details>
<summary>playwright · Playwright writing tests — access, scope and verification</summary>

[Playwright writing tests](https://playwright.dev/docs/writing-tests) · Playwright · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Browser-level tests for login, chat, errors and citation navigation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Accessibility and end-to-end tests.
- **Retained broad selection notes (lookup only):** Consult the Keyboard; focus; labels; errors; upload→ask→source→delete sections/examples only. Do not read the entire documentation site.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

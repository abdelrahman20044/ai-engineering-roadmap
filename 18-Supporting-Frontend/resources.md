# Resource Library · L18 — Supporting TypeScript and React UI

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Optional supporting UI: Elzero TypeScript gaps → React official quick path → fetch/abort → source display and browser tests. A minimal client is sufficient.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Elzero provides Arabic TypeScript teaching. This Level uses English React/MDN docs for current React, stream consumption and accessibility; a React-specific Arabic playlist was not verified in this pass.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [TypeScript study plan](https://elzero.org/study/typescript-study-plan/) | Osama Elzero · Egypt<br>AR video + assignments<br>Free | L18-T01 · TypeScript bridge | Interfaces, unions, narrowing and generics for the small client. **Boundary:** Select unfamiliar typing topics; skip JavaScript basics. |
| [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L18-T02 · React state and components; L18-T05 · Evidence and reflection UX; L18-T06 · Accessibility and end-to-end tests | Communicating limitations, feedback and human control. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) | Pythonation · Arabic Python community<br>AR video + code<br>Free | L18-T03 · Authenticated API client | Turn Python functions into validated HTTP endpoints and inspect the companion app. **Boundary:** Introductory; lifecycle, production security and async depth need the official docs. |
| [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L18-T04 · Streaming and cancellation | Conversation state and token/context constraints. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) | Microsoft<br>AR machine-translated text<br>Free | L18-T05 · Evidence and reflection UX | Fairness, reliability and accountable use. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L18-T03 · Authenticated API client | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |
| [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L18-T05 · Evidence and reflection UX | Uncertainty, interaction design and feedback. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| React official Using TypeScript and Learn: a necessary gap resource if choosing React. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F6 client/streaming and F8 authentication contracts as references. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L18-T01 | Type API success/error responses and remove unsafe any usage from the request layer. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L18-T02 | Build a small UI with explicit loading, error and empty states. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L18-T03 | Handle expired sessions and forbidden source requests without exposing stale private data. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L18-T04 | Render partial text, cancel a response and display terminal error/completion states. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L18-T05 | Click a citation to an authorized passage and allow memory correction/deletion. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L18-T06 | Automate the main happy/error paths and manually test keyboard navigation. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [React with TypeScript](https://react.dev/learn/typescript) | React<br>EN<br>Free | L18-T01 · TypeScript bridge | Typing props, hooks and events. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [React Learn](https://react.dev/learn) | React<br>EN<br>Free | L18-T02 · React state and components; L18-T05 · Evidence and reflection UX | State, effects and component boundaries. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | MDN<br>EN<br>Free | L18-T03 · Authenticated API client; L18-T04 · Streaming and cancellation | HTTP errors, response bodies, streaming and abort signals. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/) | FastAPI<br>EN<br>Free | L18-T04 · Streaming and cancellation | StreamingResponse and generator behavior; frame your own event stream correctly. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Playwright writing tests](https://playwright.dev/docs/writing-tests) | Playwright<br>EN<br>Free | L18-T06 · Accessibility and end-to-end tests | Browser-level tests for login, chat, errors and citation navigation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

# Resource Library · L11 — Security, Authorization, and Responsible AI

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Port your known auth concepts using F8 → test object ownership at every boundary → malicious-document fixtures → upload/rate/privacy controls.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Arabic translated security material introduces risks. No Arabic hands-on equivalent to the selected LLM security labs was verified; use the English labs for attack/defense practice.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) | Pythonation · Arabic Python community<br>AR video + code<br>Free | L11-T01 · FastAPI authentication | Turn Python functions into validated HTTP endpoints and inspect the companion app. **Boundary:** Introductory; lifecycle, production security and async depth need the official docs. |
| [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L11-T02 · Object-level authorization; L11-T03 · Prompt injection and excessive agency | Threats and mitigations around a model-backed app. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) | Microsoft<br>AR machine-translated text<br>Free | L11-T03 · Prompt injection and excessive agency | Trust boundaries, human control and reliability. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L11-T04 · Upload and parser security | Uploading a File in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) | Microsoft<br>AR machine-translated text<br>Free | L11-T05 · Privacy, deletion and observability; L11-T06 · Responsible answer behavior | Fairness, reliability and accountable use. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L11-T06 · Responsible answer behavior | Communicating limitations, feedback and human control. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L11-T01 · FastAPI authentication; L11-T02 · Object-level authorization | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |
| [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L11-T06 · Responsible answer behavior | Uncertainty, interaction design and feedback. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) | Eric Roby and Chad Darby<br>EN video<br>Paid · variable regional/subscription pricing | Optional support for this Level’s assessed exercises | Alternative guided backend course for validation, persistence, auth and tests. **Boundary:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python. |

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| F8 PDF338–400: FastAPI authorization implementation; skim familiar JWT concepts. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F9 PDF401–428; C5 pp.235–250; C10 pp.451–455. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| OWASP GenAI Prompt Injection: server-enforced permissions and least privilege. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Web LLM attacks learning path](https://portswigger.net/web-security/llm-attacks) | PortSwigger Web Security Academy<br>EN hands-on labs<br>Free | L11-T03 · Prompt injection and excessive agency | Indirect prompt injection, unsafe tool behavior and trust boundaries in hosted labs. **Boundary:** Practice only in the authorized labs; adapt the failure classes to synthetic project fixtures. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L11-T01 | Test invalid, expired and missing tokens and define the client session contract. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L11-T02 | Build a two-user access matrix and test direct object reads and indirect retrieval. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L11-T03 | Place hostile instructions in a PDF fixture and test backend-enforced tool/data restrictions. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L11-T04 | Reject oversized/invalid files and prevent user-supplied path writes. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L11-T05 | Delete a document/journal and prove it disappears from retrieval, memory and permitted logs. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L11-T06 | Test unsupported advice, conflicting text and correction requests with a documented response rubric. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) | FastAPI<br>EN<br>Free | L11-T01 · FastAPI authentication | Password hashing, token verification and dependency-based auth. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP<br>EN<br>Free | L11-T02 · Object-level authorization; L11-T05 · Privacy, deletion and observability | Deny-by-default object authorization and least privilege. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | SQLAlchemy<br>EN<br>Free | L11-T02 · Object-level authorization | One session per concurrent task; explicit database I/O. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | OWASP GenAI<br>EN<br>Free | L11-T03 · Prompt injection and excessive agency | Direct/indirect injection and layered mitigations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/) | OWASP GenAI<br>EN<br>Free | L11-T03 · Prompt injection and excessive agency; L11-T05 · Privacy, deletion and observability | Sensitive information, excessive agency, poisoning and resource consumption. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | OWASP<br>EN<br>Free | L11-T04 · Upload and parser security | Filename, file type, size, storage and untrusted parser boundaries. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L11-T06 · Responsible answer behavior | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

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

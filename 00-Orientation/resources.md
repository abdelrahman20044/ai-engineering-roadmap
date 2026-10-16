# Resource Library · L00 — Baseline Assessment and Product Scope

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

C1 planning → mini-RAG orientation → your scope and diagnostic. Spend hours defining a testable first slice, not choosing a framework.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) | Pythonation · Arabic Python community<br>AR video + code<br>Free | L00-T01 · Transfer backend skills | Turn Python functions into validated HTTP endpoints and inspect the companion app. **Boundary:** Introductory; lifecycle, production security and async depth need the official docs. |
| [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) | Osama Elzero · Egypt<br>AR video + assignments<br>Free | L00-T01 · Transfer backend skills | Functions, OOP, modules, generators and exceptions: select only diagnostic gaps. **Boundary:** Skip the beginner sequence after passing L00. |
| [mini-RAG · About the Course ماذا ولمـــاذا](https://www.youtube.com/watch?v=Vv6e2Rb1Q6w&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L00-T02 · Choose the user problem | About the Course ماذا ولمـــاذا in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · What will we build ماذا سنبنى في المشروع](https://www.youtube.com/watch?v=_l5S5CdxE-Q&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=2) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L00-T02 · Choose the user problem | What will we build ماذا سنبنى في المشروع in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L00-T03 · Define answer contracts | Communicating limitations, feedback and human control. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) | Microsoft<br>AR machine-translated text<br>Free | L00-T04 · Plan evaluation evidence | Evaluation, versioning and operational stages. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L00-T05 · Learn independently | Project Architecture in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) | Harvard · David Malan<br>EN video + problem sets<br>Free | L00-T01 · Transfer backend skills; L00-T05 · Learn independently | pytest, assertions and test-driven reasoning; do the associated exercises. **Boundary:** Skip unrelated beginner lectures. |
| [Launch an LLM App in One Hour](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/launch-an-llm-app-in-one-hour/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L00-T02 · Choose the user problem | Scope a small model-backed application and trace its implementation. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L00-T03 · Define answer contracts | Uncertainty, interaction design and feedback. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L00-T04 · Plan evaluation evidence | Evaluation, production behavior and operational iteration. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| C1: Planning AI Applications, printed pp.28–34; The AI Engineering Stack, pp.35–46. Read selectively. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F2: consult project structures only after the first endpoint; avoid premature architecture. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [PostgreSQL Exercises](https://pgexercises.com/) | PGExercises<br>EN interactive exercises<br>Free | Optional support for this Level’s assessed exercises | Selected joins, aggregation and window exercises for SQL diagnostics. **Boundary:** Prior SQL knowledge means a short diagnostic, not a full SQL track. |
| [Exercism Python track](https://exercism.org/tracks/python) | Exercism<br>EN<br>Free | Optional support for this Level’s assessed exercises | Small Python exercises with automated tests and community feedback. **Boundary:** Choose typing, iteration and error-handling gaps, not hundreds of exercises. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L00-T01 | Record a comparison with one existing CRM implementation and one Python gap. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L00-T02 | Write five user stories with acceptance conditions and only one first-release flow. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L00-T03 | Write three response examples: supported, unsupported and unauthorized. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L00-T04 | Create ten initial questions with source references; label these development cases. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L00-T05 | Explain the use case in two minutes and implement a tiny change without AI. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | FastAPI<br>EN<br>Free | L00-T01 · Transfer backend skills | Request/response models and routing. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record) | Joel Parker Henderson<br>EN<br>Free | L00-T02 · Choose the user problem | Options, decision drivers and consequences. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP<br>EN<br>Free | L00-T03 · Define answer contracts | Deny-by-default object authorization and least privilege. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L00-T04 · Plan evaluation evidence | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Technical Writing One](https://developers.google.com/tech-writing/one) | Google<br>EN<br>Free | L00-T05 · Learn independently | Structure, audience, concise explanations and exercises. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | GitHub<br>EN<br>Free | Optional support for this Level’s assessed exercises | Reproducible setup, navigation and reader expectations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

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

# Resource Library · L16 — Capstone Release, Technical Defense, and Career Evidence

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

No new large course: assemble the evidence, run an untouched holdout, ship a reproducible release and defend the decisions. Apply while improving documented gaps.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Arabic project orientation and UX/lifecycle lessons support presentation. A verified Arabic AI-engineering interview bank was not found. The Level self-checks and mock defense are recommendations, not official ITI interview questions.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L16-T01 · Reproducible capstone release; L16-T03 · Architecture and technical defense | Project Architecture in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L16-T01 · Reproducible capstone release | App Deployments 1/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) | Microsoft<br>AR machine-translated text<br>Free | L16-T02 · Final evaluation and limitations | Evaluation, versioning and operational stages. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) | Microsoft<br>AR machine-translated text<br>Free | L16-T03 · Architecture and technical defense | When agent autonomy adds value. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Art of Machine Learning · scikit-learn](https://www.youtube.com/playlist?list=PL6-3IRz2XF5X_9JeJh1xeciAbkijvc09k) | Hesham Asem · Egypt<br>AR video<br>Free | L16-T04 · AI fundamentals interview bridge | Practical model fitting and metrics; update older APIs. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |
| [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) | Hesham Asem · Egypt<br>AR video<br>Free | L16-T04 · AI fundamentals interview bridge | Layers, activations and learning intuition. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |
| [mini-RAG · From Mongo to Postgres + SQLAlchemy & Alembic](https://www.youtube.com/watch?v=BVOq7Ek2Up0) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L16-T05 · Backend and operations defense | From Mongo to Postgres + SQLAlchemy & Alembic in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Celery Workers 1/2](https://www.youtube.com/watch?v=pX-iWWT2TJo) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L16-T05 · Backend and operations defense | Celery Workers 1/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L16-T06 · Career evidence and communication | Communicating limitations, feedback and human control. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) | Microsoft<br>AR machine-translated text<br>Free | L16-T06 · Career evidence and communication | Fairness, reliability and accountable use. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L16-T01 · Reproducible capstone release; L16-T05 · Backend and operations defense | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |
| [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | DeepLearning.AI · LlamaIndex/TruEra<br>EN video + notebooks<br>Limited-time free access advertised; account/terms may change | L16-T02 · Final evaluation and limitations | Advanced retrieval and structured evaluation experiments. **Boundary:** Framework-specific lab; reimplement one comparison using your existing retrieval interface. |
| [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L16-T03 · Architecture and technical defense; L16-T06 · Career evidence and communication | Evaluation, production behavior and operational iteration. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Hugging Face<br>EN course + videos + quizzes<br>Free | L16-T04 · AI fundamentals interview bridge | Transformer families, tokenization and using pretrained models. **Boundary:** Read targeted sections; training an LLM is optional. |
| [Next-Level Concurrent Programming in Python with Asyncio](https://www.youtube.com/watch?v=GpqAQxH1Afc) | ArjanCodes<br>EN video<br>Free | L16-T05 · Backend and operations defense | I/O concurrency, async generators and architecture tradeoffs. **Boundary:** Older video; use current asyncio TaskGroup/timeout semantics for new code. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| Review C1 milestones/maintenance, C4 evaluation, F11 E2E, and C10 feedback only where needed. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| No large new chapter; close real gaps in the evidence. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Agent fundamentals quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz) | Hugging Face<br>EN interactive quiz<br>Free | Optional support for this Level’s assessed exercises | Independent concept check for tools, observations and agent behavior. **Boundary:** A quiz pass does not replace implementation tests; login may be needed to submit. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L16-T01 | A reviewer runs the release on synthetic data from a clean checkout. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L16-T02 | Freeze the config, run holdout once for release assessment and analyze three failures. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L16-T03 | Present a 5-minute demo and a deeper 20-minute walkthrough with one rejected option. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L16-T04 | Answer conceptual questions using your own experiment or failure example. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L16-T05 | Write an endpoint, query and test independently; diagnose a supplied failing trace. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L16-T06 | Write three evidence-backed CV bullets and a scoped delivery proposal with assumptions and acceptance criteria. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | GitHub<br>EN<br>Free | L16-T01 · Reproducible capstone release | Reproducible setup, navigation and reader expectations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) | GitHub<br>EN<br>Free | L16-T01 · Reproducible capstone release | Versioned deliverables, release notes and assets. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L16-T02 · Final evaluation and limitations | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record) | Joel Parker Henderson<br>EN<br>Free | L16-T03 · Architecture and technical defense | Options, decision drivers and consequences. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Technical Writing One](https://developers.google.com/tech-writing/one) | Google<br>EN<br>Free | L16-T03 · Architecture and technical defense; L16-T06 · Career evidence and communication | Structure, audience, concise explanations and exercises. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Common ML pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | scikit-learn<br>EN<br>Free | L16-T04 · AI fundamentals interview bridge | Splitting, preprocessing and leakage prevention. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) | Sentence Transformers<br>EN<br>Free | L16-T04 · AI fundamentals interview bridge | MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) | SQLAlchemy<br>EN<br>Free | L16-T05 · Backend and operations defense | One session per concurrent task; explicit database I/O. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) | Python<br>EN<br>Free | L16-T05 · Backend and operations defense | Task groups, cancellation, timeouts and concurrency. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Postmortem culture](https://sre.google/sre-book/postmortem-culture/) | Google SRE<br>EN chapter<br>Free | Optional support for this Level’s assessed exercises | Blameless failure analysis and actionable follow-up. **Boundary:** Write one from a real injected failure in your app. |

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

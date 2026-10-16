# Resource Library · L14 — MLOps, LLMOps, Architecture, and Deployment

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

F12 selective Docker → mini-RAG deployment lessons → CI + immutable version metadata → trace one request → backup/restore and rollback drill.

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
| [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L14-T01 · Containers and service topology; L14-T02 · CI and evaluation gates; L14-T05 · Deployment and safe operation | App Deployments 1/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L14-T01 · Containers and service topology; L14-T02 · CI and evaluation gates; L14-T04 · Tracing and metrics; L14-T05 · Deployment and safe operation; L14-T06 · Recovery and incident handling | App Deployments 2/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) | Microsoft<br>AR machine-translated text<br>Free | L14-T03 · Version and release metadata | Evaluation, versioning and operational stages. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L14-T01 · Containers and service topology; L14-T02 · CI and evaluation gates; L14-T05 · Deployment and safe operation | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |
| [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L14-T01 · Containers and service topology; L14-T03 · Version and release metadata; L14-T04 · Tracing and metrics | Evaluation, production behavior and operational iteration. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag) | Abu Bakr Soliman<br>AR explanations / Python code<br>Free | Optional support for this Level’s assessed exercises | Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. **Boundary:** Educational reference, not a security or correctness certification. |

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| F12 PDF536–594: Dockerfile, storage, networking, Compose, and image optimization; skim familiar Docker basics. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F11 E2E; C10 Monitoring and Observability pp.465–473. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F3 serving strategies and C9 performance metrics; GPU optimization remains optional. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Test with Actions](https://github.com/skills/test-with-actions) | GitHub Skills<br>EN guided exercise<br>Free | Optional support for this Level’s assessed exercises | Create a working CI test workflow in a practice repository. **Boundary:** Avoid duplicate CI tutorials if you can already create one independently. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L14-T01 | Start the stack from a clean checkout and preserve uploaded documents/database state across restarts. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L14-T02 | Fail a PR/commit check on a deliberately broken ownership test and retain the report. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L14-T03 | Attach a version manifest to a demo/evaluation result so it can be reproduced. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L14-T04 | Trace upload and question flows; create a dashboard or query for errors, latency and usage. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L14-T05 | Deploy one small environment and document startup, migration and dependency-outage behavior. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L14-T06 | Restore a backup into a fresh DB and write a short incident report for an induced failure. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Docker workshop](https://docs.docker.com/get-started/workshop/) | Docker<br>EN<br>Free | L14-T01 · Containers and service topology; L14-T05 · Deployment and safe operation | Images, Compose, networks, storage and repeatable local deployment. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | GitHub<br>EN<br>Free | L14-T02 · CI and evaluation gates; L14-T05 · Deployment and safe operation | Dependency install, test jobs and retained artifacts. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) | GitHub<br>EN<br>Free | L14-T03 · Version and release metadata | Versioned deliverables, release notes and assets. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | OpenTelemetry<br>EN<br>Free | L14-T04 · Tracing and metrics | Spans, attributes, context and exporting telemetry. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/) | Prometheus<br>EN<br>Free | L14-T04 · Tracing and metrics | Scrape and query operational metrics. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) | PostgreSQL<br>EN<br>Free | L14-T06 · Recovery and incident handling | Logical backup and restore procedure; verify by restoring. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Postmortem culture](https://sre.google/sre-book/postmortem-culture/) | Google SRE<br>EN chapter<br>Free | L14-T06 · Recovery and incident handling | Blameless failure analysis and actionable follow-up. **Boundary:** Write one from a real injected failure in your app. |
| [Implementing SLOs](https://sre.google/workbook/implementing-slos/) | Google SRE<br>EN worked chapter<br>Free | Optional support for this Level’s assessed exercises | Availability/latency indicators, objectives and error budgets. **Boundary:** Use modest application-level targets; do not copy enterprise numbers. |

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

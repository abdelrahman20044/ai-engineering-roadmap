# Resource Library · L14 — MLOps, LLMOps, Architecture, and Deployment

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

## Topic navigation

1. [Containers and service topology](#unit-01)
2. [CI and evaluation gates](#unit-02)
3. [Version and release metadata](#unit-03)
4. [Tracing and metrics](#unit-04)
5. [Deployment and safe operation](#unit-05)
6. [Recovery and incident handling](#unit-06)

<a id="unit-01"></a>

## 1. Containers and service topology

[Return to README Step 1](README.md#1-containers-and-service-topology)

**Topic/subtopics:** API/worker/db; images; networks; volumes; configuration; health.

**Required sequence (default route):** the assigned book slice [B39 · F12](../docs/READING_GUIDE.md#b39) **THEN** `docker`. Stop each source at the stated portion.

**Choose ONE explanation for container/image/Compose fundamentals:** default `docker` **OR** `fcc-api`. Keep the API/worker/database topology and readiness tests. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-containers-and-service-topology) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B39 · F12](../docs/READING_GUIDE.md#b39)<br>Alireza Parandeh · EN | Book Section | Complementary | Containers and service topology | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b39) |
| `docker` · [Docker workshop](https://docs.docker.com/get-started/workshop/)<br>Docker · EN | Documentation / tutorial | Primary | Images, Compose, networks, storage and repeatable local… | Consult the API/worker/db; images; networks; volumes; configuration;… [bounds](#unit-01-docker) |
| `ar-mini-22` · [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-23` · [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | Containers and service topology (selected course unit) | Section 15: Docker. |
| `fsdl-ops` · [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Complementary (as needed) | Evaluation, production behavior and operational iteration. | Topic bounds; lesson IDs not verified — [details](#unit-01-fsdl-ops) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-docker"></a>

**`docker` — selected portion:** Consult the API/worker/db; images; networks; volumes; configuration; health sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-mini-22"></a>

**`ar-mini-22` — selected portion:** Only the linked “App Deployments 1/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-ar-mini-23"></a>

**`ar-mini-23` — selected portion:** Only the linked “App Deployments 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-fcc-api"></a>

**`fcc-api` — selected portion:** Section 15: Docker.

**Relationship:** Substitute only for container/image/Compose fundamentals. Keep the API/worker/database topology and readiness tests.

<a id="unit-01-fsdl-ops"></a>

**`fsdl-ops` — selected portion:** Only the linked lesson on Evaluation, production behavior and operational iteration. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-02"></a>

## 2. CI and evaluation gates

[Return to README Step 2](README.md#2-ci-and-evaluation-gates)

**Topic/subtopics:** Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts.

**Required sequence (default route):** the assigned book slice [B38 · F11](../docs/READING_GUIDE.md#b38) **THEN** `ci`. Stop each source at the stated portion.

**Choose ONE explanation for GitHub Actions workflow basics:** default `ci` **OR** `fcc-api`. AI evaluation gates/artifact versions are your application-specific addition, not an extra whole course. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-ci-and-evaluation-gates) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B38 · F11](../docs/READING_GUIDE.md#b38)<br>Alireza Parandeh · EN | Book Section | Complementary | CI and evaluation gates | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b38) |
| `ci` · [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)<br>GitHub · EN | Documentation / tutorial | Primary | Dependency install, test jobs and retained artifacts. | Consult the Install pinned deps; lint/types if adopted; tests; fixed eval;… [bounds](#unit-02-ci) |
| `ar-mini-22` · [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-23` · [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | CI and evaluation gates (selected course unit) | Section 17: CI/CD. |
| `github-skills` · [Test with Actions](https://github.com/skills/test-with-actions)<br>GitHub Skills · EN guided exercise | Guided hands-on lab repository | Complementary (as needed) | Create a working CI test workflow in a practice repository. | One matching lab/notebook for the stated topic; do not complete the whole platform. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-ci"></a>

**`ci` — selected portion:** Consult the Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mini-22"></a>

**`ar-mini-22` — selected portion:** Only the linked “App Deployments 1/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-ar-mini-23"></a>

**`ar-mini-23` — selected portion:** Only the linked “App Deployments 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-fcc-api"></a>

**`fcc-api` — selected portion:** Section 17: CI/CD.

**Relationship:** Substitute only for GitHub Actions workflow basics. AI evaluation gates/artifact versions are your application-specific addition, not an extra whole course.

<a id="unit-02-github-skills"></a>

**`github-skills` — selected portion:** One matching lab/notebook for the stated topic; do not complete the whole platform.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-03"></a>

## 3. Version and release metadata

[Return to README Step 3](README.md#3-version-and-release-metadata)

**Topic/subtopics:** Code/model/prompt/corpus/index/eval identifiers; config diff.

**Required sequence:** `releases`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-version-and-release-metadata) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B37 · C10](../docs/READING_GUIDE.md#b37)<br>Chip Huyen · EN | Book Section | Reference | Version and release metadata | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b37) |
| [B39 · F12](../docs/READING_GUIDE.md#b39)<br>Alireza Parandeh · EN | Book Section | Reference | Version and release metadata | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b39) |
| `releases` · [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)<br>GitHub · EN | Documentation tutorial | Primary | Versioned deliverables, release notes and assets. | Read Creating a release, Editing a release and Comparing releases. Attach… [bounds](#unit-03-releases) |
| `ar-gen-lifecycle` · [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation, versioning and operational stages. | Only the linked translated lesson: Evaluation, versioning and operational… [bounds](#unit-03-ar-gen-lifecycle) |
| `fsdl-ops` · [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Complementary (as needed) | Evaluation, production behavior and operational iteration. | Topic bounds; lesson IDs not verified — [details](#unit-03-fsdl-ops) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-releases"></a>

**`releases` — selected portion:** Read Creating a release, Editing a release and Comparing releases. Attach your own prompt/model/corpus/evaluation manifest; GitHub release documentation does not define AI artifact versioning.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-gen-lifecycle"></a>

**`ar-gen-lifecycle` — selected portion:** Only the linked translated lesson: Evaluation, versioning and operational stages. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-fsdl-ops"></a>

**`fsdl-ops` — selected portion:** Only the linked lesson on Evaluation, production behavior and operational iteration. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-04"></a>

## 4. Tracing and metrics

[Return to README Step 4](README.md#4-tracing-and-metrics)

**Topic/subtopics:** Spans; retrieval latency; provider timing; errors; token use; redaction.

**Required sequence:** the assigned book slice [B39a · C10](../docs/READING_GUIDE.md#b39a) **THEN** `otel`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `prometheus`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-tracing-and-metrics) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B39a · C10](../docs/READING_GUIDE.md#b39a)<br>Chip Huyen · EN | Book Section | Complementary | Tracing and metrics | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b39a) |
| `otel` · [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)<br>OpenTelemetry · EN | Documentation / tutorial | Primary | Spans, attributes, context and exporting telemetry. | Consult the Spans; retrieval latency; provider timing; errors; token use;… [bounds](#unit-04-otel) |
| `ar-mini-23` · [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `fsdl-ops` · [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Complementary (as needed) | Evaluation, production behavior and operational iteration. | Topic bounds; lesson IDs not verified — [details](#unit-04-fsdl-ops) |
| `prometheus` · [Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)<br>Prometheus · EN | Documentation / tutorial | Reference | Scrape and query operational metrics. | Consult the relevant example for Scrape and query operational metrics.… [bounds](#unit-04-prometheus) |
| `sre-slos` · [Implementing SLOs](https://sre.google/workbook/implementing-slos/)<br>Google SRE · EN worked chapter | Worked book chapter (free online) | Optional Advanced | Availability/latency indicators, objectives and error… | Consult the relevant example for Availability/latency indicators,… [bounds](#unit-04-sre-slos) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-otel"></a>

**`otel` — selected portion:** Consult the Spans; retrieval latency; provider timing; errors; token use; redaction sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-mini-23"></a>

**`ar-mini-23` — selected portion:** Only the linked “App Deployments 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Deployment/monitoring context; detailed span instrumentation uses OpenTelemetry.

<a id="unit-04-fsdl-ops"></a>

**`fsdl-ops` — selected portion:** Only the linked lesson on Evaluation, production behavior and operational iteration. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-prometheus"></a>

**`prometheus` — selected portion:** Consult the relevant example for Scrape and query operational metrics. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-04-sre-slos"></a>

**`sre-slos` — selected portion:** Consult the relevant example for Availability/latency indicators, objectives and error budgets. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-05"></a>

## 5. Deployment and safe operation

[Return to README Step 5](README.md#5-deployment-and-safe-operation)

**Topic/subtopics:** Health/readiness; migration order; worker limits; secret injection.

**Required sequence (default route):** `ar-mini-22`. Stop each source at the stated portion.

**Choose ONE explanation for a basic service deployment:** default `ar-mini-22` **OR** `fcc-api`. Retain worker/database recovery and private-secret configuration checks. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `docker`, `ci`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-deployment-and-safe-operation) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B39 · F12](../docs/READING_GUIDE.md#b39)<br>Alireza Parandeh · EN | Book Section | Reference | Deployment and safe operation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b39) |
| `ar-mini-22` · [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | App Deployments 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-23` · [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | Deployment and safe operation (selected course unit) | Section 14: Ubuntu Deployment; Section 15: Docker as needed. |
| `docker` · [Docker workshop](https://docs.docker.com/get-started/workshop/)<br>Docker · EN | Documentation / tutorial | Reference | Images, Compose, networks, storage and repeatable local… | Consult the relevant example for Images, Compose, networks, storage and… [bounds](#unit-05-docker) |
| `ci` · [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)<br>GitHub · EN | Documentation / tutorial | Reference | Dependency install, test jobs and retained artifacts. | Consult the relevant example for Dependency install, test jobs and… [bounds](#unit-05-ci) |
| `mini-code` · [mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)<br>Abu Bakr Soliman · AR explanations / Python code | Course repository / lesson index | Optional Advanced | Match each lesson to its tutorial branch; compare… | Only the branch corresponding to this topic’s named mini-RAG lesson.… [bounds](#unit-05-mini-code) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-ar-mini-22"></a>

**`ar-mini-22` — selected portion:** Only the linked “App Deployments 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-23"></a>

**`ar-mini-23` — selected portion:** Only the linked “App Deployments 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-fcc-api"></a>

**`fcc-api` — selected portion:** Section 14: Ubuntu Deployment; Section 15: Docker as needed.

**Relationship:** Substitute only for a basic service deployment. Retain worker/database recovery and private-secret configuration checks.

<a id="unit-05-docker"></a>

**`docker` — selected portion:** Consult the relevant example for Images, Compose, networks, storage and repeatable local deployment. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-ci"></a>

**`ci` — selected portion:** Consult the relevant example for Dependency install, test jobs and retained artifacts. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-mini-code"></a>

**`mini-code` — selected portion:** Only the branch corresponding to this topic’s named mini-RAG lesson. Inspect after writing your own implementation.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-06"></a>

## 6. Recovery and incident handling

[Return to README Step 6](README.md#6-recovery-and-incident-handling)

**Topic/subtopics:** Restore; release rollback; runbook; retention; injected failure.

**Required sequence:** `pgbackup`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-recovery-and-incident-handling) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B39a · C10](../docs/READING_GUIDE.md#b39a)<br>Chip Huyen · EN | Book Section | Reference | Recovery and incident handling | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b39a) |
| `pgbackup` · [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html)<br>PostgreSQL · EN | Documentation / tutorial | Primary | Logical backup and restore procedure; verify by restoring. | Read pg_dump, restoring the dump, and handling large databases only as… [bounds](#unit-06-pgbackup) |
| `ar-mini-23` · [mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 2/2 in a working RAG backend. | The linked video only; not its playlist. |
| `sre-postmortem` · [Postmortem culture](https://sre.google/sre-book/postmortem-culture/)<br>Google SRE · EN chapter | Book chapter (free online) | Optional Advanced | Blameless failure analysis and actionable follow-up. | Consult the relevant example for Blameless failure analysis and actionable… [bounds](#unit-06-sre-postmortem) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-pgbackup"></a>

**`pgbackup` — selected portion:** Read pg_dump, restoring the dump, and handling large databases only as needed. Perform a database restore drill; application rollback/runbook policies are your own operational exercise.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-mini-23"></a>

**`ar-mini-23` — selected portion:** Only the linked “App Deployments 2/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-sre-postmortem"></a>

**`sre-postmortem` — selected portion:** Consult the relevant example for Blameless failure analysis and actionable follow-up. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-mini-22"></a>

<details>
<summary>ar-mini-22 · mini-RAG · App Deployments 1/2 — access, scope and verification</summary>

[mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** App Deployments 1/2 in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Containers and service topology; CI and evaluation gates; Deployment and safe operation.
- **Retained broad selection notes (lookup only):** Only the linked “App Deployments 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-mini-23"></a>

<details>
<summary>ar-mini-23 · mini-RAG · App Deployments 2/2 — access, scope and verification</summary>

[mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** App Deployments 2/2 in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Containers and service topology; CI and evaluation gates; Tracing and metrics; Deployment and safe operation; Recovery and incident handling.
- **Retained broad selection notes (lookup only):** Only the linked “App Deployments 2/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

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
- **Retained Level-wide topic association:** Containers and service topology; CI and evaluation gates; Deployment and safe operation.
- **Retained broad selection notes (lookup only):** Sections 14 (Ubuntu deployment), 15 (Docker), 17 (CI/CD). Select only the platform you use; Heroku Section 13 is optional historical material.

</details>

<a id="r-fsdl-ops"></a>

<details>
<summary>fsdl-ops · LLMOps — access, scope and verification</summary>

[LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Evaluation, production behavior and operational iteration.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Containers and service topology; Version and release metadata; Tracing and metrics.
- **Retained broad selection notes (lookup only):** Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Containers and service topology. Exact timestamps are not assigned.

</details>

<a id="r-docker"></a>

<details>
<summary>docker · Docker workshop — access, scope and verification</summary>

[Docker workshop](https://docs.docker.com/get-started/workshop/) · Docker · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Images, Compose, networks, storage and repeatable local deployment.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Containers and service topology; Deployment and safe operation.
- **Retained broad selection notes (lookup only):** Consult the API/worker/db; images; networks; volumes; configuration; health sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ci"></a>

<details>
<summary>ci · Build and test Python in GitHub Actions — access, scope and verification</summary>

[Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) · GitHub · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Dependency install, test jobs and retained artifacts.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** CI and evaluation gates; Deployment and safe operation.
- **Retained broad selection notes (lookup only):** Consult the Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-lifecycle"></a>

<details>
<summary>ar-gen-lifecycle · Generative AI lifecycle · Arabic — access, scope and verification</summary>

[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Evaluation, versioning and operational stages.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Version and release metadata.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Version and release metadata. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-releases"></a>

<details>
<summary>releases · Managing releases — access, scope and verification</summary>

[Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) · GitHub · EN

- **Resource Type:** Documentation tutorial.
- **Access:** Free.
- **Catalog scope:** Versioned deliverables, release notes and assets.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Version and release metadata.
- **Retained broad selection notes (lookup only):** Read Creating a release, Editing a release and Comparing releases. Attach your own prompt/model/corpus/evaluation manifest; GitHub release documentation does not define AI artifact versioning.

</details>

<a id="r-otel"></a>

<details>
<summary>otel · Python instrumentation — access, scope and verification</summary>

[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) · OpenTelemetry · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Spans, attributes, context and exporting telemetry.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tracing and metrics.
- **Retained broad selection notes (lookup only):** Consult the Spans; retrieval latency; provider timing; errors; token use; redaction sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-prometheus"></a>

<details>
<summary>prometheus · Prometheus getting started — access, scope and verification</summary>

[Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/) · Prometheus · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Scrape and query operational metrics.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tracing and metrics.
- **Retained broad selection notes (lookup only):** Consult the Spans; retrieval latency; provider timing; errors; token use; redaction sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-sre-postmortem"></a>

<details>
<summary>sre-postmortem · Postmortem culture — access, scope and verification</summary>

[Postmortem culture](https://sre.google/sre-book/postmortem-culture/) · Google SRE · EN chapter

- **Resource Type:** Book chapter (free online).
- **Access:** Free.
- **Catalog scope:** Blameless failure analysis and actionable follow-up.
- **Scope/version limits:** Write one from a real injected failure in your app.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Recovery and incident handling.
- **Retained broad selection notes (lookup only):** Blameless failure analysis and actionable follow-up. Optional lookup; implement only the portion that addresses the named gap.

</details>

<a id="r-pgbackup"></a>

<details>
<summary>pgbackup · PostgreSQL backup and restore — access, scope and verification</summary>

[PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html) · PostgreSQL · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Logical backup and restore procedure; verify by restoring.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Recovery and incident handling.
- **Retained broad selection notes (lookup only):** Read pg_dump, restoring the dump, and handling large databases only as needed. Perform a database restore drill; application rollback/runbook policies are your own operational exercise.

</details>

<a id="r-github-skills"></a>

<details>
<summary>github-skills · Test with Actions — access, scope and verification</summary>

[Test with Actions](https://github.com/skills/test-with-actions) · GitHub Skills · EN guided exercise

- **Resource Type:** Guided hands-on lab repository.
- **Access:** Free.
- **Catalog scope:** Create a working CI test workflow in a practice repository.
- **Scope/version limits:** Avoid duplicate CI tutorials if you can already create one independently.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** The Test with Actions guided exercise only if you cannot build the CI gate independently.

</details>

<a id="r-sre-slos"></a>

<details>
<summary>sre-slos · Implementing SLOs — access, scope and verification</summary>

[Implementing SLOs](https://sre.google/workbook/implementing-slos/) · Google SRE · EN worked chapter

- **Resource Type:** Worked book chapter (free online).
- **Access:** Free.
- **Catalog scope:** Availability/latency indicators, objectives and error budgets.
- **Scope/version limits:** Use modest application-level targets; do not copy enterprise numbers.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Availability/latency indicators, objectives and error budgets. Optional lookup; implement only the portion that addresses the named gap.

</details>

<a id="r-mini-code"></a>

<details>
<summary>mini-code · mini-RAG lesson index and source branches — access, scope and verification</summary>

[mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag) · Abu Bakr Soliman · AR explanations / Python code

- **Resource Type:** Course repository / lesson index.
- **Access:** Free.
- **Catalog scope:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers.
- **Scope/version limits:** Educational reference, not a security or correctness certification.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. Optional lookup; implement only the portion that addresses the named gap.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

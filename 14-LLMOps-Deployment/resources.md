# Resource Library · L14 — MLOps, LLMOps, Architecture, and Deployment

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

## Book references

Assigned reading is authoritative in [the master order for L14](../docs/READING_GUIDE.md#l14). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B39 · F12](../docs/READING_GUIDE.md#b39), [B38 · F11](../docs/READING_GUIDE.md#b38), [B39a · C10](../docs/READING_GUIDE.md#b39a).

**Previously covered / lookup only:** [B06 · F11](../docs/READING_GUIDE.md#b06), [B26 · F11](../docs/READING_GUIDE.md#b26), [B37 · C10](../docs/READING_GUIDE.md#b37). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-mini-22"></a>

### mini-RAG · App Deployments 1/2

[mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Primary. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Containers and service topology; CI and evaluation gates; Deployment and safe operation.
- **Assigned portion:** Only the linked “App Deployments 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** App Deployments 1/2 in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

<a id="r-ar-mini-23"></a>

### mini-RAG · App Deployments 2/2

[mini-RAG · App Deployments 2/2](https://www.youtube.com/watch?v=qJ5Hdyc4hDc)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Containers and service topology; CI and evaluation gates; Tracing and metrics; Deployment and safe operation; Recovery and incident handling.
- **Assigned portion:** Only the linked “App Deployments 2/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** App Deployments 2/2 in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Deployment/monitoring context; detailed span instrumentation uses OpenTelemetry.

<a id="r-ar-gen-lifecycle"></a>

### Generative AI lifecycle · Arabic

[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Version and release metadata.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Version and release metadata. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Evaluation, versioning and operational stages.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-fcc-api"></a>

### Creating APIs with Python · course index

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)

- **Resource Type:** Full video course (19 hours; selected sections only).
- **Role:** Alternative. **Language:** EN video. **By:** Sanjeev Thiyagarajan · freeCodeCamp.
- **Access:** Free.
- **Use for:** Containers and service topology; CI and evaluation gates; Deployment and safe operation.
- **Assigned portion:** Sections 14 (Ubuntu deployment), 15 (Docker), 17 (CI/CD). Select only the platform you use; Heroku Section 13 is optional historical material.
- **Scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Limit:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.

<a id="r-fsdl-ops"></a>

### LLMOps

[LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)

- **Resource Type:** Single lecture video + slides.
- **Role:** Alternative. **Language:** EN video + slides. **By:** Full Stack Deep Learning.
- **Access:** Free.
- **Use for:** Containers and service topology; Version and release metadata; Tracing and metrics.
- **Assigned portion:** Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Containers and service topology. Exact timestamps are not assigned.
- **Scope:** Evaluation, production behavior and operational iteration.
- **Limit:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.

## Slides, notebooks and repositories

<a id="r-mini-code"></a>

### mini-RAG lesson index and source branches

[mini-RAG lesson index and source branches](https://github.com/bakrianoo/mini-rag)

- **Resource Type:** Course repository / lesson index.
- **Role:** Reference. **Language:** AR explanations / Python code. **By:** Abu Bakr Soliman.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Match each lesson to its tutorial branch; compare architecture, parsing, providers, database migrations and workers.
- **Limit:** Educational reference, not a security or correctness certification.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

<a id="r-github-skills"></a>

### Test with Actions

[Test with Actions](https://github.com/skills/test-with-actions)

- **Resource Type:** Guided hands-on lab repository.
- **Role:** Alternative. **Language:** EN guided exercise. **By:** GitHub Skills.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** The Test with Actions guided exercise only if you cannot build the CI gate independently.
- **Scope:** Create a working CI test workflow in a practice repository.
- **Limit:** Avoid duplicate CI tutorials if you can already create one independently.

## Official documentation and engineering articles

<a id="r-docker"></a>

### Docker workshop

[Docker workshop](https://docs.docker.com/get-started/workshop/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Docker.
- **Access:** Free.
- **Use for:** Containers and service topology; Deployment and safe operation.
- **Assigned portion:** Consult the API/worker/db; images; networks; volumes; configuration; health sections/examples only. Do not read the entire documentation site.
- **Scope:** Images, Compose, networks, storage and repeatable local deployment.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ci"></a>

### Build and test Python in GitHub Actions

[Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** GitHub.
- **Access:** Free.
- **Use for:** CI and evaluation gates; Deployment and safe operation.
- **Assigned portion:** Consult the Install pinned deps; lint/types if adopted; tests; fixed eval; artifacts sections/examples only. Do not read the entire documentation site.
- **Scope:** Dependency install, test jobs and retained artifacts.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-releases"></a>

### Managing releases

[Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

- **Resource Type:** Documentation tutorial.
- **Role:** Primary. **Language:** EN. **By:** GitHub.
- **Access:** Free.
- **Use for:** Version and release metadata.
- **Assigned portion:** Read Creating a release, Editing a release and Comparing releases. Attach your own prompt/model/corpus/evaluation manifest; GitHub release documentation does not define AI artifact versioning.
- **Scope:** Versioned deliverables, release notes and assets.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-otel"></a>

### Python instrumentation

[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OpenTelemetry.
- **Access:** Free.
- **Use for:** Tracing and metrics.
- **Assigned portion:** Consult the Spans; retrieval latency; provider timing; errors; token use; redaction sections/examples only. Do not read the entire documentation site.
- **Scope:** Spans, attributes, context and exporting telemetry.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-prometheus"></a>

### Prometheus getting started

[Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Prometheus.
- **Access:** Free.
- **Use for:** Tracing and metrics.
- **Assigned portion:** Consult the Spans; retrieval latency; provider timing; errors; token use; redaction sections/examples only. Do not read the entire documentation site.
- **Scope:** Scrape and query operational metrics.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pgbackup"></a>

### PostgreSQL backup and restore

[PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup-dump.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** PostgreSQL.
- **Access:** Free.
- **Use for:** Recovery and incident handling.
- **Assigned portion:** Read pg_dump, restoring the dump, and handling large databases only as needed. Perform a database restore drill; application rollback/runbook policies are your own operational exercise.
- **Scope:** Logical backup and restore procedure; verify by restoring.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

<a id="r-sre-postmortem"></a>

### Postmortem culture

[Postmortem culture](https://sre.google/sre-book/postmortem-culture/)

- **Resource Type:** Book chapter (free online).
- **Role:** Optional Advanced. **Language:** EN chapter. **By:** Google SRE.
- **Access:** Free.
- **Use for:** Recovery and incident handling.
- **Assigned portion:** Blameless failure analysis and actionable follow-up. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Blameless failure analysis and actionable follow-up.
- **Limit:** Write one from a real injected failure in your app.

<a id="r-sre-slos"></a>

### Implementing SLOs

[Implementing SLOs](https://sre.google/workbook/implementing-slos/)

- **Resource Type:** Worked book chapter (free online).
- **Role:** Optional Advanced. **Language:** EN worked chapter. **By:** Google SRE.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Availability/latency indicators, objectives and error budgets. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Availability/latency indicators, objectives and error budgets.
- **Limit:** Use modest application-level targets; do not copy enterprise numbers.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

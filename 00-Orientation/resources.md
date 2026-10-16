# Resource Library · L00 — Baseline Assessment and Product Scope

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

1. [Transfer backend skills](#unit-01)
2. [Choose the user problem](#unit-02)
3. [Define answer contracts](#unit-03)
4. [Plan evaluation evidence](#unit-04)
5. [Learn independently](#unit-05)

<a id="unit-01"></a>

## 1. Transfer backend skills

[Return to README Step 1](README.md#1-transfer-backend-skills)

**Topic/subtopics:** Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries.

**Required sequence:** the assigned book slices [B01 · G1](../docs/READING_GUIDE.md#b01), [B02 · C1](../docs/READING_GUIDE.md#b02) **THEN** `ar-api`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `fastapi`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-transfer-backend-skills) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B01 · G1](../docs/READING_GUIDE.md#b01)<br>Andrea De Mauro · EN | Book Section | Complementary | Transfer backend skills | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b01) |
| [B02 · C1](../docs/READING_GUIDE.md#b02)<br>Chip Huyen · EN | Book Section | Complementary | Transfer backend skills | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b02) |
| `ar-api` · [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)<br>Pythonation · Arabic Python community · AR video + code | Single Video + companion repository | Primary | Turn Python functions into validated HTTP endpoints and… | Consult the Express handlers → FastAPI routes; Zod → Pydantic; Jest →… [bounds](#unit-01-ar-api) |
| `ar-python` · [Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/)<br>Osama Elzero · Egypt · AR video + assignments | Full Course / study-plan index | Complementary (as needed) | Functions, OOP, modules, generators and exceptions: select… | Diagnostic gaps only: #094 Type Hinting; #103–116 OOP if needed. |
| `cs50-tests` · [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)<br>Harvard · David Malan · EN video + problem sets | Course unit: lecture + problem set | Complementary (as needed) | pytest, assertions and test-driven reasoning; do the… | Consult the relevant example for pytest, assertions and test-driven… [bounds](#unit-01-cs50-tests) |
| `fastapi` · [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)<br>FastAPI · EN | Documentation / tutorial | Reference | Request/response models and routing. | Consult the relevant example for Request/response models and routing.… [bounds](#unit-01-fastapi) |
| `pg-exercises` · [PostgreSQL Exercises](https://pgexercises.com/)<br>PGExercises · EN interactive exercises | Interactive SQL practice platform | Complementary (as needed) | Selected joins, aggregation and window exercises for SQL… | Selected joins/aggregation/window exercises only for a demonstrated SQL… [bounds](#unit-01-pg-exercises) |
| `exercism` · [Exercism Python track](https://exercism.org/tracks/python)<br>Exercism · EN | Practice platform / automated exercises | Complementary (as needed) | Small Python exercises with automated tests and community… | One Python exercise matching the diagnostic gap; complete its tests and explain the solution. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-api"></a>

**`ar-api` — selected portion:** Consult the Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-python"></a>

**`ar-python` — selected portion:** Diagnostic gaps only: #094 Type Hinting; #103–116 OOP if needed.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-cs50-tests"></a>

**`cs50-tests` — selected portion:** Consult the relevant example for pytest, assertions and test-driven reasoning; do the associated exercises. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Different or partially overlapping concepts; as-needed support, not a substitute for the required route.

<a id="unit-01-fastapi"></a>

**`fastapi` — selected portion:** Consult the relevant example for Request/response models and routing. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-01-pg-exercises"></a>

**`pg-exercises` — selected portion:** Selected joins/aggregation/window exercises only for a demonstrated SQL gap; no full SQL restart.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-exercism"></a>

**`exercism` — selected portion:** One Python exercise matching the diagnostic gap; complete its tests and explain the solution.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-02"></a>

## 2. Choose the user problem

[Return to README Step 2](README.md#2-choose-the-user-problem)

**Topic/subtopics:** Book questions; journal connections; non-goals; permitted document corpus.

**Required sequence (default route):** `ar-mini-2`. Stop each source at the stated portion.

**Choose ONE explanation for scoping a small LLM application:** default `ar-mini-2` **OR** `fsdl-launch`. The named book planning slice and your product contract remain required. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `adr`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-choose-the-user-problem) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B02 · C1](../docs/READING_GUIDE.md#b02)<br>Chip Huyen · EN | Book Section | Reference | Choose the user problem | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b02) |
| `ar-mini-2` · [mini-RAG · What will we build ماذا سنبنى في المشروع](https://www.youtube.com/watch?v=_l5S5CdxE-Q&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=2)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | What will we build ماذا سنبنى في المشروع in a working RAG… | The linked video only; not its playlist. |
| `ar-mini-1` · [mini-RAG · About the Course ماذا ولمـــاذا](https://www.youtube.com/watch?v=Vv6e2Rb1Q6w&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | About the Course ماذا ولمـــاذا in a working RAG backend. | The linked video only; not its playlist. |
| `fsdl-launch` · [Launch an LLM App in One Hour](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/launch-an-llm-app-in-one-hour/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Alternative | Scope a small model-backed application and trace its… | Topic bounds; lesson IDs not verified — [details](#unit-02-fsdl-launch) |
| `adr` · [Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record)<br>Joel Parker Henderson · EN | Template / reference repository | Reference | Options, decision drivers and consequences. | Consult the relevant example for Options, decision drivers and… [bounds](#unit-02-adr) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-ar-mini-2"></a>

**`ar-mini-2` — selected portion:** Only the linked “What will we build ماذا سنبنى في المشروع” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mini-1"></a>

**`ar-mini-1` — selected portion:** Only the linked “About the Course ماذا ولمـــاذا” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-fsdl-launch"></a>

**`fsdl-launch` — selected portion:** Only the linked lesson on Scope a small model-backed application and trace its implementation. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for scoping a small LLM application. The named book planning slice and your product contract remain required.

<a id="unit-02-adr"></a>

**`adr` — selected portion:** Consult the relevant example for Options, decision drivers and consequences. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Define answer contracts

[Return to README Step 3](README.md#3-define-answer-contracts)

**Topic/subtopics:** Evidence versus suggestion; no-evidence behavior; ownership.

**Required sequence (default route):** the assigned book slice [B03 · C4](../docs/READING_GUIDE.md#b03) **THEN** `ar-gen-ux`. Stop each source at the stated portion.

**Choose ONE explanation for communicating uncertainty and user control:** default `ar-gen-ux` **OR** `fsdl-ux`. Implement the same answer contract whichever explanation you choose. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `authz`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-define-answer-contracts) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B03 · C4](../docs/READING_GUIDE.md#b03)<br>Chip Huyen · EN | Book Section | Complementary | Define answer contracts | [Skim: exact assigned slice](../docs/READING_GUIDE.md#b03) |
| `ar-gen-ux` · [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Primary | Communicating limitations, feedback and human control. | Only the linked translated lesson, particularly its sections about Define… [bounds](#unit-03-ar-gen-ux) |
| `fsdl-ux` · [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Alternative | Uncertainty, interaction design and feedback. | Topic bounds; lesson IDs not verified — [details](#unit-03-fsdl-ux) |
| `authz` · [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Reference | Deny-by-default object authorization and least privilege. | Consult the relevant example for Deny-by-default object authorization and… [bounds](#unit-03-authz) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-ar-gen-ux"></a>

**`ar-gen-ux` — selected portion:** Only the linked translated lesson, particularly its sections about Define answer contracts. Its English video/cloud build is an alternative, not an extra requirement.

**Relationship:** Default selected route for this topic.

<a id="unit-03-fsdl-ux"></a>

**`fsdl-ux` — selected portion:** Only the linked lesson on Uncertainty, interaction design and feedback. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for communicating uncertainty and user control. Implement the same answer contract whichever explanation you choose.

<a id="unit-03-authz"></a>

**`authz` — selected portion:** Consult the relevant example for Deny-by-default object authorization and least privilege. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Plan evaluation evidence

[Return to README Step 4](README.md#4-plan-evaluation-evidence)

**Topic/subtopics:** Answerable/unanswerable questions; expected source; fixed synthetic cases.

**Required sequence:** `fsdl-ops`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-plan-evaluation-evidence) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B03 · C4](../docs/READING_GUIDE.md#b03)<br>Chip Huyen · EN | Book Section | Reference | Plan evaluation evidence | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b03) |
| `fsdl-ops` · [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Primary | Evaluation, production behavior and operational iteration. | Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the… [bounds](#unit-04-fsdl-ops) |
| `ar-gen-lifecycle` · [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation, versioning and operational stages. | Only the linked translated lesson: Evaluation, versioning and operational… [bounds](#unit-04-ar-gen-lifecycle) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-04-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-fsdl-ops"></a>

**`fsdl-ops` — selected portion:** Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Plan evaluation evidence. Exact timestamps are not assigned.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-gen-lifecycle"></a>

**`ar-gen-lifecycle` — selected portion:** Only the linked translated lesson: Evaluation, versioning and operational stages. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Learn independently

[Return to README Step 5](README.md#5-learn-independently)

**Topic/subtopics:** Read → recall → implement → test → explain; AI assistance boundaries.

**Required sequence:** `cs50-tests`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `technical-writing`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-learn-independently) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| `cs50-tests` · [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)<br>Harvard · David Malan · EN video + problem sets | Course unit: lecture + problem set | Primary | pytest, assertions and test-driven reasoning; do the… | Week 5 “Unit Tests”: assertions/pytest explanation only; use it to calibrate the diagnostic. |
| `ar-mini-4` · [mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Project Architecture in a working RAG backend. | The linked video only; not its playlist. |
| `technical-writing` · [Technical Writing One](https://developers.google.com/tech-writing/one)<br>Google · EN | Written course + exercises | Reference | Structure, audience, concise explanations and exercises. | Consult the relevant example for Structure, audience, concise explanations… [bounds](#unit-05-technical-writing) |
| `readme` · [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)<br>GitHub · EN | Documentation article | Optional Advanced | Reproducible setup, navigation and reader expectations. | Consult the relevant example for Reproducible setup, navigation and reader… [bounds](#unit-05-readme) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-cs50-tests"></a>

**`cs50-tests` — selected portion:** Week 5 “Unit Tests”: assertions/pytest explanation only; use it to calibrate the diagnostic.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-4"></a>

**`ar-mini-4` — selected portion:** Only the linked “Project Architecture” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-technical-writing"></a>

**`technical-writing` — selected portion:** Consult the relevant example for Structure, audience, concise explanations and exercises. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-05-readme"></a>

**`readme` — selected portion:** Consult the relevant example for Reproducible setup, navigation and reader expectations. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-api"></a>

<details>
<summary>ar-api · Pythonation FastAPI tutorial and companion code — access, scope and verification</summary>

[Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) · Pythonation · Arabic Python community · AR video + code

- **Resource Type:** Single Video + companion repository.
- **Access:** Free.
- **Catalog scope:** Turn Python functions into validated HTTP endpoints and inspect the companion app.
- **Scope/version limits:** Introductory; lifecycle, production security and async depth need the official docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Transfer backend skills.
- **Retained broad selection notes (lookup only):** Consult the Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-python"></a>

<details>
<summary>ar-python · Mastering Python study plan — access, scope and verification</summary>

[Mastering Python study plan](https://elzero.org/study/mastering-python-study-plan/) · Osama Elzero · Egypt · AR video + assignments

- **Resource Type:** Full Course / study-plan index.
- **Access:** Free.
- **Catalog scope:** Functions, OOP, modules, generators and exceptions: select only diagnostic gaps.
- **Scope/version limits:** Skip the beginner sequence after passing L00.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Transfer backend skills.
- **Retained broad selection notes (lookup only):** Consult the Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-cs50-tests"></a>

<details>
<summary>cs50-tests · CS50P · Unit Tests — access, scope and verification</summary>

[CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) · Harvard · David Malan · EN video + problem sets

- **Resource Type:** Course unit: lecture + problem set.
- **Access:** Free.
- **Catalog scope:** pytest, assertions and test-driven reasoning; do the associated exercises.
- **Scope/version limits:** Skip unrelated beginner lectures.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Transfer backend skills; Learn independently.
- **Retained broad selection notes (lookup only):** Week 5 “Unit Tests”: assertions/pytest explanation only; use it to calibrate the diagnostic.

</details>

<a id="r-fastapi"></a>

<details>
<summary>fastapi · FastAPI tutorial — access, scope and verification</summary>

[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Request/response models and routing.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Transfer backend skills.
- **Retained broad selection notes (lookup only):** Consult the Express handlers → FastAPI routes; Zod → Pydantic; Jest → pytest; Mongoose → ORM boundaries sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-1"></a>

<details>
<summary>ar-mini-1 · mini-RAG · About the Course ماذا ولمـــاذا — access, scope and verification</summary>

[mini-RAG · About the Course ماذا ولمـــاذا](https://www.youtube.com/watch?v=Vv6e2Rb1Q6w&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** About the Course ماذا ولمـــاذا in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Choose the user problem.
- **Retained broad selection notes (lookup only):** Only the linked “About the Course ماذا ولمـــاذا” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-mini-2"></a>

<details>
<summary>ar-mini-2 · mini-RAG · What will we build ماذا سنبنى في المشروع — access, scope and verification</summary>

[mini-RAG · What will we build ماذا سنبنى في المشروع](https://www.youtube.com/watch?v=_l5S5CdxE-Q&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=2) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** What will we build ماذا سنبنى في المشروع in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Choose the user problem.
- **Retained broad selection notes (lookup only):** Only the linked “What will we build ماذا سنبنى في المشروع” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-fsdl-launch"></a>

<details>
<summary>fsdl-launch · Launch an LLM App in One Hour — access, scope and verification</summary>

[Launch an LLM App in One Hour](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/launch-an-llm-app-in-one-hour/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Scope a small model-backed application and trace its implementation.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Choose the user problem.
- **Retained broad selection notes (lookup only):** Only the linked “Launch an LLM App in One Hour” lecture; not the complete LLM Bootcamp. Use the parts relevant to Choose the user problem. Exact timestamps are not assigned.

</details>

<a id="r-adr"></a>

<details>
<summary>adr · Architecture decision record templates — access, scope and verification</summary>

[Architecture decision record templates](https://github.com/joelparkerhenderson/architecture-decision-record) · Joel Parker Henderson · EN

- **Resource Type:** Template / reference repository.
- **Access:** Free.
- **Catalog scope:** Options, decision drivers and consequences.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Choose the user problem.
- **Retained broad selection notes (lookup only):** Consult the Book questions; journal connections; non-goals; permitted document corpus sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Define answer contracts.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Define answer contracts. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Define answer contracts.
- **Retained broad selection notes (lookup only):** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Define answer contracts. Exact timestamps are not assigned.

</details>

<a id="r-authz"></a>

<details>
<summary>authz · Authorization cheat sheet — access, scope and verification</summary>

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · OWASP · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Deny-by-default object authorization and least privilege.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Define answer contracts.
- **Retained broad selection notes (lookup only):** Consult the Evidence versus suggestion; no-evidence behavior; ownership sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Plan evaluation evidence.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Plan evaluation evidence. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Plan evaluation evidence.
- **Retained broad selection notes (lookup only):** Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Plan evaluation evidence. Exact timestamps are not assigned.

</details>

<a id="r-promptfoo"></a>

<details>
<summary>promptfoo · Assertions and metrics — access, scope and verification</summary>

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) · Promptfoo · EN

- **Resource Type:** Documentation: assertions reference.
- **Access:** Free.
- **Catalog scope:** Deterministic checks, model judges and eval assertions.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Plan evaluation evidence.
- **Retained broad selection notes (lookup only):** The assertion type matching Plan evaluation evidence; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

</details>

<a id="r-ar-mini-4"></a>

<details>
<summary>ar-mini-4 · mini-RAG · Project Architecture — access, scope and verification</summary>

[mini-RAG · Project Architecture](https://www.youtube.com/watch?v=Ei_nBwBbFUQ&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=4) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Project Architecture in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Learn independently.
- **Retained broad selection notes (lookup only):** Only the linked “Project Architecture” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-technical-writing"></a>

<details>
<summary>technical-writing · Technical Writing One — access, scope and verification</summary>

[Technical Writing One](https://developers.google.com/tech-writing/one) · Google · EN

- **Resource Type:** Written course + exercises.
- **Access:** Free.
- **Catalog scope:** Structure, audience, concise explanations and exercises.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Learn independently.
- **Retained broad selection notes (lookup only):** Technical Writing One: audience, organization and concise sentences; do one writing exercise using the project README/proposal.

</details>

<a id="r-readme"></a>

<details>
<summary>readme · About repository READMEs — access, scope and verification</summary>

[About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) · GitHub · EN

- **Resource Type:** Documentation article.
- **Access:** Free.
- **Catalog scope:** Reproducible setup, navigation and reader expectations.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Consult the Reproducible setup, navigation and reader expectations. sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-pg-exercises"></a>

<details>
<summary>pg-exercises · PostgreSQL Exercises — access, scope and verification</summary>

[PostgreSQL Exercises](https://pgexercises.com/) · PGExercises · EN interactive exercises

- **Resource Type:** Interactive SQL practice platform.
- **Access:** Free.
- **Catalog scope:** Selected joins, aggregation and window exercises for SQL diagnostics.
- **Scope/version limits:** Prior SQL knowledge means a short diagnostic, not a full SQL track.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** A short join/aggregate/window diagnostic, then stop when the relevant query works. No complete SQL track.

</details>

<a id="r-exercism"></a>

<details>
<summary>exercism · Exercism Python track — access, scope and verification</summary>

[Exercism Python track](https://exercism.org/tracks/python) · Exercism · EN

- **Resource Type:** Practice platform / automated exercises.
- **Access:** Free.
- **Catalog scope:** Small Python exercises with automated tests and community feedback.
- **Scope/version limits:** Choose typing, iteration and error-handling gaps, not hundreds of exercises.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Choose one iteration/error-handling exercise matching the failed Python diagnostic. No full-track requirement.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

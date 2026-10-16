# Resource Library · L11 — Security, Authorization, and Responsible AI

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Arabic translated security material introduces risks. No Arabic hands-on equivalent to the selected LLM security labs was verified; use the English labs for attack/defense practice.

## Topic navigation

1. [FastAPI authentication](#unit-01)
2. [Object-level authorization](#unit-02)
3. [Prompt injection and excessive agency](#unit-03)
4. [Upload and parser security](#unit-04)
5. [Privacy, deletion and observability](#unit-05)
6. [Responsible answer behavior](#unit-06)

<a id="unit-01"></a>

## 1. FastAPI authentication

[Return to README Step 1](README.md#1-fastapi-authentication)

**Topic/subtopics:** Hashing; token verification; expiry; dependencies; cookie/header choice.

**Required sequence (default route):** the assigned book slice [B33 · F8](../docs/READING_GUIDE.md#b33) **THEN** `jwt`. Stop each source at the stated portion.

**Choose ONE explanation for JWT authentication implementation:** default `jwt` **OR** `fcc-api`. Use current FastAPI/JWT dependencies and retain the existing password/token tests. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-fastapi-authentication) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B33 · F8](../docs/READING_GUIDE.md#b33)<br>Alireza Parandeh · EN | Book Section | Complementary | FastAPI authentication | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b33) |
| `jwt` · [OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)<br>FastAPI · EN | Documentation / tutorial | Primary | Password hashing, token verification and dependency-based… | Consult the Hashing; token verification; expiry; dependencies;… [bounds](#unit-01-jwt) |
| `ar-api` · [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)<br>Pythonation · Arabic Python community · AR video + code | Single Video + companion repository | Complementary (as needed) | Turn Python functions into validated HTTP endpoints and… | Consult the relevant example for Turn Python functions into validated HTTP… [bounds](#unit-01-ar-api) |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Alternative | FastAPI authentication (selected course unit) | Section 8: Authentication and Users (passwords, login, token verification). |
| `roby` · [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)<br>Eric Roby and Chad Darby · EN video | Full Course (paid) | Optional Advanced | Alternative guided backend course for validation,… | Topic bounds; lesson IDs not verified — [details](#unit-01-roby) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-jwt"></a>

**`jwt` — selected portion:** Consult the Hashing; token verification; expiry; dependencies; cookie/header choice sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-api"></a>

**`ar-api` — selected portion:** Consult the relevant example for Turn Python functions into validated HTTP endpoints and inspect the companion app. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: API introduction only; secure token/cookie implementation uses F8/FastAPI.

<a id="unit-01-fcc-api"></a>

**`fcc-api` — selected portion:** Section 8: Authentication and Users (passwords, login, token verification).

**Relationship:** Substitute only for JWT authentication implementation. Use current FastAPI/JWT dependencies and retain the existing password/token tests.

<a id="unit-01-roby"></a>

**`roby` — selected portion:** Optional purchase only: use the topic-specific FastAPI section for a demonstrated gap. Individual current lesson IDs/access not verified; no whole-course requirement.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-02"></a>

## 2. Object-level authorization

[Return to README Step 2](README.md#2-object-level-authorization)

**Topic/subtopics:** Owner predicates; chunks; sources; messages; memories; jobs.

**Required sequence:** `authz`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `sqlasync`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-object-level-authorization) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B33 · F8](../docs/READING_GUIDE.md#b33)<br>Alireza Parandeh · EN | Book Section | Reference | Object-level authorization | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b33) |
| `authz` · [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Primary | Deny-by-default object authorization and least privilege. | Consult the Owner predicates; chunks; sources; messages; memories; jobs… [bounds](#unit-02-authz) |
| `ar-gen-security` · [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Threats and mitigations around a model-backed app. | Only the linked translated lesson: Threats and mitigations around a… [bounds](#unit-02-ar-gen-security) |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Complementary (as needed) | Object-level authorization (selected course unit) | Ownership/token-protected route examples in Sections 8–9; retain the OWASP… [bounds](#unit-02-fcc-api) |
| `sqlasync` · [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)<br>SQLAlchemy · EN | Documentation / tutorial | Reference | One session per concurrent task; explicit database I/O. | Consult the relevant example for One session per concurrent task; explicit… [bounds](#unit-02-sqlasync) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-authz"></a>

**`authz` — selected portion:** Consult the Owner predicates; chunks; sources; messages; memories; jobs sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-gen-security"></a>

**`ar-gen-security` — selected portion:** Only the linked translated lesson: Threats and mitigations around a model-backed app. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-fcc-api"></a>

**`fcc-api` — selected portion:** Ownership/token-protected route examples in Sections 8–9; retain the OWASP object-authorization design.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-sqlasync"></a>

**`sqlasync` — selected portion:** Consult the relevant example for One session per concurrent task; explicit database I/O. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Prompt injection and excessive agency

[Return to README Step 3](README.md#3-prompt-injection-and-excessive-agency)

**Topic/subtopics:** Malicious documents; tool output instructions; least privilege.

**Required sequence:** the assigned book slices [B34 · F9](../docs/READING_GUIDE.md#b34), [B35 · C5](../docs/READING_GUIDE.md#b35) **THEN** `owasp`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `llm-top10`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-prompt-injection-and-excessive-agency) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B34 · F9](../docs/READING_GUIDE.md#b34)<br>Alireza Parandeh · EN | Book Section | Complementary | Prompt injection and excessive agency | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b34) |
| [B35 · C5](../docs/READING_GUIDE.md#b35)<br>Chip Huyen · EN | Book Section | Complementary | Prompt injection and excessive agency | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b35) |
| `owasp` · [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)<br>OWASP GenAI · EN | Documentation / tutorial | Primary | Direct/indirect injection and layered mitigations. | Consult the Malicious documents; tool output instructions; least privilege… [bounds](#unit-03-owasp) |
| `ar-gen-security` · [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Threats and mitigations around a model-backed app. | Only the linked translated lesson: Threats and mitigations around a… [bounds](#unit-03-ar-gen-security) |
| `ar-agent-trust` · [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Trust boundaries, human control and reliability. | Only the linked translated lesson: Trust boundaries, human control and… [bounds](#unit-03-ar-agent-trust) |
| `portswigger` · [Web LLM attacks learning path](https://portswigger.net/web-security/llm-attacks)<br>PortSwigger Web Security Academy · EN hands-on labs | Learning path + hosted security labs | Complementary (as needed) | Indirect prompt injection, unsafe tool behavior and trust… | One prompt-injection/tool-boundary lab matching your threat case; an… [bounds](#unit-03-portswigger) |
| `llm-top10` · [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)<br>OWASP GenAI · EN | Documentation / tutorial | Reference | Sensitive information, excessive agency, poisoning and… | Consult the relevant example for Sensitive information, excessive agency,… [bounds](#unit-03-llm-top10) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-owasp"></a>

**`owasp` — selected portion:** Consult the Malicious documents; tool output instructions; least privilege sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-gen-security"></a>

**`ar-gen-security` — selected portion:** Only the linked translated lesson: Threats and mitigations around a model-backed app. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-ar-agent-trust"></a>

**`ar-agent-trust` — selected portion:** Only the linked translated lesson: Trust boundaries, human control and reliability. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-portswigger"></a>

**`portswigger` — selected portion:** One prompt-injection/tool-boundary lab matching your threat case; an exploit lab complements, not replaces, the mitigation reference.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-llm-top10"></a>

**`llm-top10` — selected portion:** Consult the relevant example for Sensitive information, excessive agency, poisoning and resource consumption. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Upload and parser security

[Return to README Step 4](README.md#4-upload-and-parser-security)

**Topic/subtopics:** Size/type limits; path traversal; storage names; resource limits.

**Required sequence:** `fileupload`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-upload-and-parser-security) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B34 · F9](../docs/READING_GUIDE.md#b34)<br>Alireza Parandeh · EN | Book Section | Reference | Upload and parser security | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b34) |
| `fileupload` · [File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Primary | Filename, file type, size, storage and untrusted parser… | Consult the Size/type limits; path traversal; storage names; resource… [bounds](#unit-04-fileupload) |
| `ar-mini-7` · [mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Uploading a File in a working RAG backend. | The linked video only; not its playlist. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-fileupload"></a>

**`fileupload` — selected portion:** Consult the Size/type limits; path traversal; storage names; resource limits sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-mini-7"></a>

**`ar-mini-7` — selected portion:** Only the linked “Uploading a File” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-05"></a>

## 5. Privacy, deletion and observability

[Return to README Step 5](README.md#5-privacy-deletion-and-observability)

**Topic/subtopics:** Journal sensitivity; consent; redaction; retention; cache/vector cleanup.

**Required sequence:** the assigned book slice [B35a · C10](../docs/READING_GUIDE.md#b35a) **THEN** `llm-top10`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `authz`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-privacy-deletion-and-observability) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B35a · C10](../docs/READING_GUIDE.md#b35a)<br>Chip Huyen · EN | Book Section | Complementary | Privacy, deletion and observability | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b35a) |
| `llm-top10` · [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)<br>OWASP GenAI · EN | Documentation / tutorial | Primary | Sensitive information, excessive agency, poisoning and… | Consult the Journal sensitivity; consent; redaction; retention;… [bounds](#unit-05-llm-top10) |
| `ar-gen-responsible` · [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Fairness, reliability and accountable use. | Only the linked translated lesson: Fairness, reliability and accountable… [bounds](#unit-05-ar-gen-responsible) |
| `authz` · [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Reference | Deny-by-default object authorization and least privilege. | Consult the relevant example for Deny-by-default object authorization and… [bounds](#unit-05-authz) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-llm-top10"></a>

**`llm-top10` — selected portion:** Consult the Journal sensitivity; consent; redaction; retention; cache/vector cleanup sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-gen-responsible"></a>

**`ar-gen-responsible` — selected portion:** Only the linked translated lesson: Fairness, reliability and accountable use. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-authz"></a>

**`authz` — selected portion:** Consult the relevant example for Deny-by-default object authorization and least privilege. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Responsible answer behavior

[Return to README Step 6](README.md#6-responsible-answer-behavior)

**Topic/subtopics:** Attribution; uncertainty; book claim versus suggestion; feedback/appeal.

**Required sequence (default route):** `ar-gen-ux`. Stop each source at the stated portion.

**Choose ONE explanation for uncertainty, feedback and human control:** default `ar-gen-ux` **OR** `fsdl-ux`. Keep the responsible-answer contract and evaluation cases. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-responsible-answer-behavior) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B16 · C4](../docs/READING_GUIDE.md#b16)<br>Chip Huyen · EN | Book Section | Reference | Responsible answer behavior | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b16) |
| [B35a · C10](../docs/READING_GUIDE.md#b35a)<br>Chip Huyen · EN | Book Section | Reference | Responsible answer behavior | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b35a) |
| `ar-gen-ux` · [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Primary | Communicating limitations, feedback and human control. | Only the linked translated lesson, particularly its sections about… [bounds](#unit-06-ar-gen-ux) |
| `ar-gen-responsible` · [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Fairness, reliability and accountable use. | Only the linked translated lesson: Fairness, reliability and accountable… [bounds](#unit-06-ar-gen-responsible) |
| `fsdl-ux` · [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Alternative | Uncertainty, interaction design and feedback. | Topic bounds; lesson IDs not verified — [details](#unit-06-fsdl-ux) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-06-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-ar-gen-ux"></a>

**`ar-gen-ux` — selected portion:** Only the linked translated lesson, particularly its sections about Responsible answer behavior. Its English video/cloud build is an alternative, not an extra requirement.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-gen-responsible"></a>

**`ar-gen-responsible` — selected portion:** Only the linked translated lesson: Fairness, reliability and accountable use. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-fsdl-ux"></a>

**`fsdl-ux` — selected portion:** Only the linked lesson on Uncertainty, interaction design and feedback. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for uncertainty, feedback and human control. Keep the responsible-answer contract and evaluation cases.

<a id="unit-06-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

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
- **Retained Level-wide topic association:** FastAPI authentication.
- **Retained broad selection notes (lookup only):** Consult the Hashing; token verification; expiry; dependencies; cookie/header choice sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** FastAPI authentication; Object-level authorization.
- **Retained broad selection notes (lookup only):** Section 8: token verification/protected routes; Section 9: ownership restrictions; Section 16: failed login/unauthorized reads.

</details>

<a id="r-jwt"></a>

<details>
<summary>jwt · OAuth2 with JWT — access, scope and verification</summary>

[OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Password hashing, token verification and dependency-based auth.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** FastAPI authentication.
- **Retained broad selection notes (lookup only):** Consult the Hashing; token verification; expiry; dependencies; cookie/header choice sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-security"></a>

<details>
<summary>ar-gen-security · Securing AI applications · Arabic — access, scope and verification</summary>

[Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Threats and mitigations around a model-backed app.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Object-level authorization; Prompt injection and excessive agency.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Object-level authorization. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Object-level authorization; Privacy, deletion and observability.
- **Retained broad selection notes (lookup only):** Consult the Owner predicates; chunks; sources; messages; memories; jobs sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-sqlasync"></a>

<details>
<summary>sqlasync · SQLAlchemy asyncio — access, scope and verification</summary>

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** One session per concurrent task; explicit database I/O.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Object-level authorization.
- **Retained broad selection notes (lookup only):** Consult the Owner predicates; chunks; sources; messages; memories; jobs sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-agent-trust"></a>

<details>
<summary>ar-agent-trust · Trustworthy agents · Arabic — access, scope and verification</summary>

[Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Trust boundaries, human control and reliability.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Prompt injection and excessive agency.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Prompt injection and excessive agency. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-portswigger"></a>

<details>
<summary>portswigger · Web LLM attacks learning path — access, scope and verification</summary>

[Web LLM attacks learning path](https://portswigger.net/web-security/llm-attacks) · PortSwigger Web Security Academy · EN hands-on labs

- **Resource Type:** Learning path + hosted security labs.
- **Access:** Free.
- **Catalog scope:** Indirect prompt injection, unsafe tool behavior and trust boundaries in hosted labs.
- **Scope/version limits:** Practice only in the authorized labs; adapt the failure classes to synthetic project fixtures.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Prompt injection and excessive agency.
- **Retained broad selection notes (lookup only):** Web LLM attacks introduction and one available indirect-injection/tool-abuse lab relevant to your synthetic fixture; this is not a general penetration-testing curriculum.

</details>

<a id="r-owasp"></a>

<details>
<summary>owasp · LLM prompt injection — access, scope and verification</summary>

[LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) · OWASP GenAI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Direct/indirect injection and layered mitigations.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Prompt injection and excessive agency.
- **Retained broad selection notes (lookup only):** Consult the Malicious documents; tool output instructions; least privilege sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-llm-top10"></a>

<details>
<summary>llm-top10 · OWASP GenAI risks — access, scope and verification</summary>

[OWASP GenAI risks](https://genai.owasp.org/llm-top-10/) · OWASP GenAI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Sensitive information, excessive agency, poisoning and resource consumption.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Prompt injection and excessive agency; Privacy, deletion and observability.
- **Retained broad selection notes (lookup only):** Consult the Journal sensitivity; consent; redaction; retention; cache/vector cleanup sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-7"></a>

<details>
<summary>ar-mini-7 · mini-RAG · Uploading a File — access, scope and verification</summary>

[mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Uploading a File in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Upload and parser security.
- **Retained broad selection notes (lookup only):** Only the linked “Uploading a File” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-fileupload"></a>

<details>
<summary>fileupload · File upload cheat sheet — access, scope and verification</summary>

[File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) · OWASP · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Filename, file type, size, storage and untrusted parser boundaries.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Upload and parser security.
- **Retained broad selection notes (lookup only):** Consult the Size/type limits; path traversal; storage names; resource limits sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Privacy, deletion and observability; Responsible answer behavior.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Privacy, deletion and observability. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Responsible answer behavior.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Responsible answer behavior. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Responsible answer behavior.
- **Retained broad selection notes (lookup only):** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Responsible answer behavior. Exact timestamps are not assigned.

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
- **Retained Level-wide topic association:** Responsible answer behavior.
- **Retained broad selection notes (lookup only):** The assertion type matching Responsible answer behavior; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

</details>

<a id="r-roby"></a>

<details>
<summary>roby · FastAPI — The Complete Course — access, scope and verification</summary>

[FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) · Eric Roby and Chad Darby · EN video

- **Resource Type:** Full Course (paid).
- **Access:** Paid · variable regional/subscription pricing.
- **Catalog scope:** Alternative guided backend course for validation, persistence, auth and tests.
- **Scope/version limits:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Alternative only: JWT/auth and authorization implementation. Exact current lesson numbers not verified.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

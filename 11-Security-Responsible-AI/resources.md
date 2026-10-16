# Resource Library · L11 — Security, Authorization, and Responsible AI

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** Arabic translated security material introduces risks. No Arabic hands-on equivalent to the selected LLM security labs was verified; use the English labs for attack/defense practice.

## Book references

Assigned reading is authoritative in [the master order for L11](../docs/READING_GUIDE.md#l11). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B33 · F8](../docs/READING_GUIDE.md#b33), [B34 · F9](../docs/READING_GUIDE.md#b34), [B35 · C5](../docs/READING_GUIDE.md#b35), [B35a · C10](../docs/READING_GUIDE.md#b35a).

**Previously covered / lookup only:** [B16 · C4](../docs/READING_GUIDE.md#b16). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-api"></a>

### Pythonation FastAPI tutorial and companion code

[Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)

- **Resource Type:** Single video + companion repository.
- **Role:** Alternative. **Language:** AR video + code. **By:** Pythonation · Arabic Python community.
- **Access:** Free.
- **Use for:** FastAPI authentication.
- **Assigned portion:** Consult the Hashing; token verification; expiry; dependencies; cookie/header choice sections/examples only. Do not read the entire documentation site.
- **Scope:** Turn Python functions into validated HTTP endpoints and inspect the companion app.
- **Limit:** Introductory; lifecycle, production security and async depth need the official docs.

**Arabic scope note:** API introduction only; secure token/cookie implementation uses F8/FastAPI.

<a id="r-ar-gen-security"></a>

### Securing AI applications · Arabic

[Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Object-level authorization; Prompt injection and excessive agency.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Object-level authorization. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Threats and mitigations around a model-backed app.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-agent-trust"></a>

### Trustworthy agents · Arabic

[Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Prompt injection and excessive agency.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Prompt injection and excessive agency. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Trust boundaries, human control and reliability.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-mini-7"></a>

### mini-RAG · Uploading a File

[mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Upload and parser security.
- **Assigned portion:** Only the linked “Uploading a File” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Uploading a File in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

<a id="r-ar-gen-responsible"></a>

### Responsible generative AI · Arabic

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Privacy, deletion and observability; Responsible answer behavior.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Privacy, deletion and observability. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Fairness, reliability and accountable use.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-ux"></a>

### AI user experience · Arabic

[AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Primary. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Responsible answer behavior.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Responsible answer behavior. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Communicating limitations, feedback and human control.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-fcc-api"></a>

### Creating APIs with Python · course index

[Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)

- **Resource Type:** Full video course (19 hours; selected sections only).
- **Role:** Alternative. **Language:** EN video. **By:** Sanjeev Thiyagarajan · freeCodeCamp.
- **Access:** Free.
- **Use for:** FastAPI authentication; Object-level authorization.
- **Assigned portion:** Section 8: token verification/protected routes; Section 9: ownership restrictions; Section 16: failed login/unauthorized reads.
- **Scope:** Select the database, auth, testing and deployment chapters from the published course outline.
- **Limit:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours.

<a id="r-fsdl-ux"></a>

### UX for Language User Interfaces

[UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/)

- **Resource Type:** Single lecture video + slides.
- **Role:** Alternative. **Language:** EN video + slides. **By:** Full Stack Deep Learning.
- **Access:** Free.
- **Use for:** Responsible answer behavior.
- **Assigned portion:** Only the linked “UX for Language User Interfaces” lecture; not the complete LLM Bootcamp. Use the parts relevant to Responsible answer behavior. Exact timestamps are not assigned.
- **Scope:** Uncertainty, interaction design and feedback.
- **Limit:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

<a id="r-roby"></a>

### FastAPI — The Complete Course

[FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)

- **Resource Type:** Paid full video course.
- **Role:** Optional Advanced. **Language:** EN video. **By:** Eric Roby and Chad Darby.
- **Access:** Paid · variable regional/subscription pricing.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Alternative only: JWT/auth and authorization implementation. Exact current lesson numbers not verified.
- **Scope:** Alternative guided backend course for validation, persistence, auth and tests.
- **Limit:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python.

## Practice, labs and quizzes

<a id="r-portswigger"></a>

### Web LLM attacks learning path

[Web LLM attacks learning path](https://portswigger.net/web-security/llm-attacks)

- **Resource Type:** Learning path + hosted security labs.
- **Role:** Alternative. **Language:** EN hands-on labs. **By:** PortSwigger Web Security Academy.
- **Access:** Free.
- **Use for:** Prompt injection and excessive agency.
- **Assigned portion:** Web LLM attacks introduction and one available indirect-injection/tool-abuse lab relevant to your synthetic fixture; this is not a general penetration-testing curriculum.
- **Scope:** Indirect prompt injection, unsafe tool behavior and trust boundaries in hosted labs.
- **Limit:** Practice only in the authorized labs; adapt the failure classes to synthetic project fixtures.

## Official documentation and engineering articles

<a id="r-jwt"></a>

### OAuth2 with JWT

[OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** FastAPI.
- **Access:** Free.
- **Use for:** FastAPI authentication.
- **Assigned portion:** Consult the Hashing; token verification; expiry; dependencies; cookie/header choice sections/examples only. Do not read the entire documentation site.
- **Scope:** Password hashing, token verification and dependency-based auth.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-authz"></a>

### Authorization cheat sheet

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OWASP.
- **Access:** Free.
- **Use for:** Object-level authorization; Privacy, deletion and observability.
- **Assigned portion:** Consult the Owner predicates; chunks; sources; messages; memories; jobs sections/examples only. Do not read the entire documentation site.
- **Scope:** Deny-by-default object authorization and least privilege.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-sqlasync"></a>

### SQLAlchemy asyncio

[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** SQLAlchemy.
- **Access:** Free.
- **Use for:** Object-level authorization.
- **Assigned portion:** Consult the Owner predicates; chunks; sources; messages; memories; jobs sections/examples only. Do not read the entire documentation site.
- **Scope:** One session per concurrent task; explicit database I/O.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-owasp"></a>

### LLM prompt injection

[LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OWASP GenAI.
- **Access:** Free.
- **Use for:** Prompt injection and excessive agency.
- **Assigned portion:** Consult the Malicious documents; tool output instructions; least privilege sections/examples only. Do not read the entire documentation site.
- **Scope:** Direct/indirect injection and layered mitigations.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-llm-top10"></a>

### OWASP GenAI risks

[OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OWASP GenAI.
- **Access:** Free.
- **Use for:** Prompt injection and excessive agency; Privacy, deletion and observability.
- **Assigned portion:** Consult the Journal sensitivity; consent; redaction; retention; cache/vector cleanup sections/examples only. Do not read the entire documentation site.
- **Scope:** Sensitive information, excessive agency, poisoning and resource consumption.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-fileupload"></a>

### File upload cheat sheet

[File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OWASP.
- **Access:** Free.
- **Use for:** Upload and parser security.
- **Assigned portion:** Consult the Size/type limits; path traversal; storage names; resource limits sections/examples only. Do not read the entire documentation site.
- **Scope:** Filename, file type, size, storage and untrusted parser boundaries.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-promptfoo"></a>

### Assertions and metrics

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

- **Resource Type:** Documentation: assertions reference.
- **Role:** Reference. **Language:** EN. **By:** Promptfoo.
- **Access:** Free.
- **Use for:** Responsible answer behavior.
- **Assigned portion:** The assertion type matching Responsible answer behavior; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.
- **Scope:** Deterministic checks, model judges and eval assertions.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

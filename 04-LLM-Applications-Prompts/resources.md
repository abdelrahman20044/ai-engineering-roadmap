# Resource Library · L04 — Prompt Engineering, Structured Outputs, and LLM Integration

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

1. [Instructions and examples](#unit-01)
2. [Prompt lifecycle](#unit-02)
3. [Provider integration](#unit-03)
4. [Structured output validation](#unit-04)
5. [Untrusted input boundaries](#unit-05)
6. [Small AI endpoint](#unit-06)

<a id="unit-01"></a>

## 1. Instructions and examples

[Return to README Step 1](README.md#1-instructions-and-examples)

**Topic/subtopics:** Task; role; delimiters; few-shot examples; output constraints.

**Required sequence (default route):** the assigned book slices [B10 · G2](../docs/READING_GUIDE.md#b10), [B11 · G3](../docs/READING_GUIDE.md#b11) **THEN** `prompt-lab`. Stop each source at the stated portion.

**Choose ONE explanation for instruction and example design:** default `prompt-lab` **OR** `fsdl-prompt`. Run the prompt-lab exercises whichever explanation you choose. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-instructions-and-examples) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B10 · G2](../docs/READING_GUIDE.md#b10)<br>Andrea De Mauro · EN | Book Section | Complementary | Instructions and examples | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b10) |
| [B11 · G3](../docs/READING_GUIDE.md#b11)<br>Andrea De Mauro · EN | Book Section | Complementary | Instructions and examples | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b11) |
| `prompt-lab` · [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)<br>Anthropic · EN | Interactive tutorial / notebook exercises | Primary | Exercises with expected behaviors for prompts and… | Consult the Task; role; delimiters; few-shot examples; output constraints… [bounds](#unit-01-prompt-lab) |
| `ar-gen-prompt` · [Prompt engineering fundamentals · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/04-prompt-engineering-fundamentals/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Instructions, examples, prompting techniques and exercises. | Only the linked translated lesson: Instructions, examples, prompting… [bounds](#unit-01-ar-gen-prompt) |
| `fsdl-prompt` · [Learn to Spell: Prompt Engineering](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/prompt-engineering/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Alternative | Prompt iteration and practical prompt design. | Topic bounds; lesson IDs not verified — [details](#unit-01-fsdl-prompt) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-prompt-lab"></a>

**`prompt-lab` — selected portion:** Consult the Task; role; delimiters; few-shot examples; output constraints sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-gen-prompt"></a>

**`ar-gen-prompt` — selected portion:** Only the linked translated lesson: Instructions, examples, prompting techniques and exercises. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-fsdl-prompt"></a>

**`fsdl-prompt` — selected portion:** Only the linked lesson on Prompt iteration and practical prompt design. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for instruction and example design. Run the prompt-lab exercises whichever explanation you choose.

</details>

<a id="unit-02"></a>

## 2. Prompt lifecycle

[Return to README Step 2](README.md#2-prompt-lifecycle)

**Topic/subtopics:** Template variables; version control; config; regression cases.

**Required sequence:** the assigned book slice [B14 · C5](../docs/READING_GUIDE.md#b14) **THEN** `promptfoo`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-prompt-lifecycle) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B14 · C5](../docs/READING_GUIDE.md#b14)<br>Chip Huyen · EN | Book Section | Complementary | Prompt lifecycle | [Skim: exact assigned slice](../docs/READING_GUIDE.md#b14) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Primary | Deterministic checks, model judges and eval assertions. | The assertion type matching Prompt lifecycle; start with deterministic… [bounds](#unit-02-promptfoo) |
| `ar-gen-advancedprompt` · [Advanced prompts · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/05-advanced-prompts/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Prompt iteration and task decomposition. | Only the linked translated lesson: Prompt iteration and task… [bounds](#unit-02-ar-gen-advancedprompt) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-promptfoo"></a>

**`promptfoo` — selected portion:** The assertion type matching Prompt lifecycle; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-gen-advancedprompt"></a>

**`ar-gen-advancedprompt` — selected portion:** Only the linked translated lesson: Prompt iteration and task decomposition. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-03"></a>

## 3. Provider integration

[Return to README Step 3](README.md#3-provider-integration)

**Topic/subtopics:** SDK/HTTP boundary; errors; credentials via environment; limits.

**Required sequence:** the assigned book slices [B12 · F3](../docs/READING_GUIDE.md#b12), [B13 · F5](../docs/READING_GUIDE.md#b13) **THEN** `ar-mini-14`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `httpx`, `ollama`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-provider-integration) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B12 · F3](../docs/READING_GUIDE.md#b12)<br>Alireza Parandeh · EN | Book Section | Complementary | Provider integration | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b12) |
| [B13 · F5](../docs/READING_GUIDE.md#b13)<br>Alireza Parandeh · EN | Book Section | Complementary | Provider integration | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b13) |
| `ar-mini-14` · [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | LLM Factory in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-19` · [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Ollama Local LLM Server in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Complementary (as needed) | Provider integration (selected course unit) | Section 3 request/response and handler examples only; the separate LLM adapter comes from F3/F5. |
| `httpx` · [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/)<br>HTTPX · EN | Documentation / tutorial | Reference | Connect/read/write/pool timeouts for provider calls. | Consult the relevant example for Connect/read/write/pool timeouts for… [bounds](#unit-03-httpx) |
| `ollama` · [Ollama API introduction](https://docs.ollama.com/api/introduction)<br>Ollama · EN | Documentation / tutorial | Reference | Local inference endpoint contracts; local operation uses… | Consult the relevant example for Local inference endpoint contracts; local… [bounds](#unit-03-ollama) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-ar-mini-14"></a>

**`ar-mini-14` — selected portion:** Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-mini-19"></a>

**`ar-mini-19` — selected portion:** Only the linked “Ollama Local LLM Server” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-fcc-api"></a>

**`fcc-api` — selected portion:** Section 3 request/response and handler examples only; the separate LLM adapter comes from F3/F5.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-httpx"></a>

**`httpx` — selected portion:** Consult the relevant example for Connect/read/write/pool timeouts for provider calls. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-03-ollama"></a>

**`ollama` — selected portion:** Consult the relevant example for Local inference endpoint contracts; local operation uses your hardware. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Structured output validation

[Return to README Step 4](README.md#4-structured-output-validation)

**Topic/subtopics:** Schema; enum/constraints; invalid JSON; refusal; repair boundary.

**Required sequence:** `ollama-structured`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `pydantic`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-structured-output-validation) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B05 · F4](../docs/READING_GUIDE.md#b05)<br>Alireza Parandeh · EN | Book Section | Reference | Structured output validation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b05) |
| [B08 · C2](../docs/READING_GUIDE.md#b08)<br>Chip Huyen · EN | Book Section | Reference | Structured output validation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b08) |
| `ollama-structured` · [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs)<br>Ollama · EN | Documentation / tutorial | Primary | Schema-constrained output and validation. | Consult the Schema; enum/constraints; invalid JSON; refusal; repair… [bounds](#unit-04-ollama-structured) |
| `ar-api` · [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial)<br>Pythonation · Arabic Python community · AR video + code | Single Video + companion repository | Complementary (as needed) | Turn Python functions into validated HTTP endpoints and… | Consult the relevant example for Turn Python functions into validated HTTP… [bounds](#unit-04-ar-api) |
| `pydantic` · [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)<br>Pydantic · EN | Documentation / tutorial | Reference | Validation, coercion, strictness and serialization. | Consult the relevant example for Validation, coercion, strictness and… [bounds](#unit-04-pydantic) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-ollama-structured"></a>

**`ollama-structured` — selected portion:** Consult the Schema; enum/constraints; invalid JSON; refusal; repair boundary sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-api"></a>

**`ar-api` — selected portion:** Consult the relevant example for Turn Python functions into validated HTTP endpoints and inspect the companion app. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Pydantic/API validation orientation; model-constrained output requires the English reference.

<a id="unit-04-pydantic"></a>

**`pydantic` — selected portion:** Consult the relevant example for Validation, coercion, strictness and serialization. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Untrusted input boundaries

[Return to README Step 5](README.md#5-untrusted-input-boundaries)

**Topic/subtopics:** Document text versus instructions; evidence labels; tool output trust.

**Required sequence:** `owasp`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-untrusted-input-boundaries) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B14 · C5](../docs/READING_GUIDE.md#b14)<br>Chip Huyen · EN | Book Section | Reference | Untrusted input boundaries | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b14) |
| `owasp` · [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)<br>OWASP GenAI · EN | Documentation / tutorial | Primary | Direct/indirect injection and layered mitigations. | Consult the Document text versus instructions; evidence labels; tool… [bounds](#unit-05-owasp) |
| `ar-gen-security` · [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Threats and mitigations around a model-backed app. | Only the linked translated lesson: Threats and mitigations around a… [bounds](#unit-05-ar-gen-security) |
| `hf-agents` · [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction)<br>Hugging Face · EN course + videos + exercises | Course unit: text, videos and exercises | Complementary (as needed) | Tools, thought-action-observation and the minimal agent… | Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe… [bounds](#unit-05-hf-agents) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-owasp"></a>

**`owasp` — selected portion:** Consult the Document text versus instructions; evidence labels; tool output trust sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-gen-security"></a>

**`ar-gen-security` — selected portion:** Only the linked translated lesson: Threats and mitigations around a model-backed app. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-hf-agents"></a>

**`hf-agents` — selected portion:** Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe cycle. Select the subsection matching this group; no framework completion requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-06"></a>

## 6. Small AI endpoint

[Return to README Step 6](README.md#6-small-ai-endpoint)

**Topic/subtopics:** One call; request IDs; output contract; no low-code dependency.

**Required sequence:** `ar-mini-5`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `fastapi-testing`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-small-ai-endpoint) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B10 · G2](../docs/READING_GUIDE.md#b10)<br>Andrea De Mauro · EN | Book Section | Reference | Small AI endpoint | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b10) |
| `ar-mini-5` · [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | Welcome to FastAPI in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-14` · [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | LLM Factory in a working RAG backend. | The linked video only; not its playlist. |
| `fcc-api` · [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)<br>Sanjeev Thiyagarajan · freeCodeCamp · EN video | Full Course (19 hours; selected sections only) | Complementary (as needed) | Small AI endpoint (selected course unit) | Section 3: Starting FastAPI; Path operations. |
| `fastapi-testing` · [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/)<br>FastAPI · EN | Documentation / tutorial | Reference | Swap provider implementations in API tests. | Consult the relevant example for Swap provider implementations in API… [bounds](#unit-06-fastapi-testing) |
| `roby` · [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/)<br>Eric Roby and Chad Darby · EN video | Full Course (paid) | Optional Advanced | Alternative guided backend course for validation,… | Topic bounds; lesson IDs not verified — [details](#unit-06-roby) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-ar-mini-5"></a>

**`ar-mini-5` — selected portion:** Only the linked “Welcome to FastAPI” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-mini-14"></a>

**`ar-mini-14` — selected portion:** Only the linked “LLM Factory” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-fcc-api"></a>

**`fcc-api` — selected portion:** Section 3: Starting FastAPI; Path operations.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-fastapi-testing"></a>

**`fastapi-testing` — selected portion:** Consult the relevant example for Swap provider implementations in API tests. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-06-roby"></a>

**`roby` — selected portion:** Optional purchase only: use the topic-specific FastAPI section for a demonstrated gap. Individual current lesson IDs/access not verified; no whole-course requirement.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-gen-prompt"></a>

<details>
<summary>ar-gen-prompt · Prompt engineering fundamentals · Arabic — access, scope and verification</summary>

[Prompt engineering fundamentals · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/04-prompt-engineering-fundamentals/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Instructions, examples, prompting techniques and exercises.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Instructions and examples.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Instructions and examples. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-fsdl-prompt"></a>

<details>
<summary>fsdl-prompt · Learn to Spell: Prompt Engineering — access, scope and verification</summary>

[Learn to Spell: Prompt Engineering](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/prompt-engineering/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Prompt iteration and practical prompt design.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Instructions and examples.
- **Retained broad selection notes (lookup only):** Only the linked “Learn to Spell: Prompt Engineering” lecture; not the complete LLM Bootcamp. Use the parts relevant to Instructions and examples. Exact timestamps are not assigned.

</details>

<a id="r-prompt-lab"></a>

<details>
<summary>prompt-lab · Interactive prompt engineering tutorial — access, scope and verification</summary>

[Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) · Anthropic · EN

- **Resource Type:** Interactive tutorial / notebook exercises.
- **Access:** Free.
- **Catalog scope:** Exercises with expected behaviors for prompts and formatting.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Instructions and examples.
- **Retained broad selection notes (lookup only):** Consult the Task; role; delimiters; few-shot examples; output constraints sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-advancedprompt"></a>

<details>
<summary>ar-gen-advancedprompt · Advanced prompts · Arabic — access, scope and verification</summary>

[Advanced prompts · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/05-advanced-prompts/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Prompt iteration and task decomposition.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Prompt lifecycle.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Prompt lifecycle. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Prompt lifecycle.
- **Retained broad selection notes (lookup only):** The assertion type matching Prompt lifecycle; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

</details>

<a id="r-ar-mini-14"></a>

<details>
<summary>ar-mini-14 · mini-RAG · LLM Factory — access, scope and verification</summary>

[mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** LLM Factory in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Provider integration; Small AI endpoint.
- **Retained broad selection notes (lookup only):** Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ar-mini-19"></a>

<details>
<summary>ar-mini-19 · mini-RAG · Ollama Local LLM Server — access, scope and verification</summary>

[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Ollama Local LLM Server in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Provider integration.
- **Retained broad selection notes (lookup only):** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

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
- **Retained Level-wide topic association:** Provider integration; Small AI endpoint.
- **Retained broad selection notes (lookup only):** Section 3: Path operations and Schema Validation; Section 7: Response Model. These are API mechanics, not LLM-specific provider teaching.

</details>

<a id="r-httpx"></a>

<details>
<summary>httpx · HTTPX timeouts — access, scope and verification</summary>

[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) · HTTPX · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Connect/read/write/pool timeouts for provider calls.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Provider integration.
- **Retained broad selection notes (lookup only):** Consult the SDK/HTTP boundary; errors; credentials via environment; limits sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ollama"></a>

<details>
<summary>ollama · Ollama API introduction — access, scope and verification</summary>

[Ollama API introduction](https://docs.ollama.com/api/introduction) · Ollama · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Local inference endpoint contracts; local operation uses your hardware.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Provider integration.
- **Retained broad selection notes (lookup only):** Consult the SDK/HTTP boundary; errors; credentials via environment; limits sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-api"></a>

<details>
<summary>ar-api · Pythonation FastAPI tutorial and companion code — access, scope and verification</summary>

[Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) · Pythonation · Arabic Python community · AR video + code

- **Resource Type:** Single Video + companion repository.
- **Access:** Free.
- **Catalog scope:** Turn Python functions into validated HTTP endpoints and inspect the companion app.
- **Scope/version limits:** Introductory; lifecycle, production security and async depth need the official docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Structured output validation.
- **Retained broad selection notes (lookup only):** Consult the Schema; enum/constraints; invalid JSON; refusal; repair boundary sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ollama-structured"></a>

<details>
<summary>ollama-structured · Ollama structured outputs — access, scope and verification</summary>

[Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs) · Ollama · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Schema-constrained output and validation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Structured output validation.
- **Retained broad selection notes (lookup only):** Consult the Schema; enum/constraints; invalid JSON; refusal; repair boundary sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-pydantic"></a>

<details>
<summary>pydantic · Pydantic models — access, scope and verification</summary>

[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) · Pydantic · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Validation, coercion, strictness and serialization.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Structured output validation.
- **Retained broad selection notes (lookup only):** Consult the Schema; enum/constraints; invalid JSON; refusal; repair boundary sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Untrusted input boundaries.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Untrusted input boundaries. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-hf-agents"></a>

<details>
<summary>hf-agents · Agents course · Unit 1 — access, scope and verification</summary>

[Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) · Hugging Face · EN course + videos + exercises

- **Resource Type:** Course unit: text, videos and exercises.
- **Access:** Free.
- **Catalog scope:** Tools, thought-action-observation and the minimal agent loop.
- **Scope/version limits:** Learn the loop before adopting smolagents or another framework.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Untrusted input boundaries.
- **Retained broad selection notes (lookup only):** Unit 1 “Tools” concepts are orientation only; the current Level does not require an agent build.

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
- **Retained Level-wide topic association:** Untrusted input boundaries.
- **Retained broad selection notes (lookup only):** Consult the Document text versus instructions; evidence labels; tool output trust sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-5"></a>

<details>
<summary>ar-mini-5 · mini-RAG · Welcome to FastAPI — access, scope and verification</summary>

[mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Welcome to FastAPI in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Small AI endpoint.
- **Retained broad selection notes (lookup only):** Only the linked “Welcome to FastAPI” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-fastapi-testing"></a>

<details>
<summary>fastapi-testing · Testing dependencies with overrides — access, scope and verification</summary>

[Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) · FastAPI · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Swap provider implementations in API tests.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Small AI endpoint.
- **Retained broad selection notes (lookup only):** Consult the One call; request IDs; output contract; no low-code dependency sections/examples only. Do not read the entire documentation site.

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
- **Retained broad selection notes (lookup only):** Optional alternative for a diagnosed gap only. Exact current lesson identifiers were not verified; no full-course requirement.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

# Resource Library · L12 — Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Arabic translated agent lessons provide structured text. A complete Arabic course covering bounded loops plus trajectory evaluation was not verified; pair them with the English agent course and assessment labs.

## Topic navigation

1. [Agent anatomy and design choice](#unit-01)
2. [Tool design and schemas](#unit-02)
3. [Bounded execution loop](#unit-03)
4. [Agent evaluation](#unit-04)
5. [Memory and context interfaces](#unit-05)
6. [Multi-agent comparison](#unit-06)

<a id="unit-01"></a>

## 1. Agent anatomy and design choice

[Return to README Step 1](README.md#1-agent-anatomy-and-design-choice)

**Topic/subtopics:** State; model decision; action; observation; workflow alternatives.

**Required sequence (default route):** the assigned book slices [B36 · G5](../docs/READING_GUIDE.md#b36), [B36a · G6](../docs/READING_GUIDE.md#b36a) **THEN** `agents`. Stop each source at the stated portion.

**Choose ONE explanation for workflow versus agent fundamentals:** default `agents` **OR** `hf-agents`. Anthropic’s simple-pattern decision remains the architectural check, not a mandatory framework migration. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-agent-anatomy-and-design-choice) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B36 · G5](../docs/READING_GUIDE.md#b36)<br>Andrea De Mauro · EN | Book Section | Complementary | Agent anatomy and design choice | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b36) |
| [B36a · G6](../docs/READING_GUIDE.md#b36a)<br>Andrea De Mauro · EN | Book Section | Complementary | Agent anatomy and design choice | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b36a) |
| `agents` · [Building effective agents](https://www.anthropic.com/research/building-effective-agents)<br>Anthropic · EN | Engineering article | Primary | Workflow patterns versus autonomous agents and tool… | Read the “workflows versus agents” distinction and the pattern/tool-design… [bounds](#unit-01-agents) |
| `ar-agent-intro` · [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When agent autonomy adds value. | Only the linked translated lesson: When agent autonomy adds value. Arabic… [bounds](#unit-01-ar-agent-intro) |
| `hf-agents` · [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction)<br>Hugging Face · EN course + videos + exercises | Course unit: text, videos and exercises | Alternative | Tools, thought-action-observation and the minimal agent… | Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe… [bounds](#unit-01-hf-agents) |
| `hf-quiz` · [Agent fundamentals quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz)<br>Hugging Face · EN interactive quiz | Interactive quiz | Complementary (as needed) | Independent concept check for tools, observations and… | One matching quiz/exercise set for the stated topic; do not complete the whole platform. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-agents"></a>

**`agents` — selected portion:** Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Agent anatomy and design choice. Multi-agent implementations are not required.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-agent-intro"></a>

**`ar-agent-intro` — selected portion:** Only the linked translated lesson: When agent autonomy adds value. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-hf-agents"></a>

**`hf-agents` — selected portion:** Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe cycle. Select the subsection matching this group; no framework completion requirement.

**Relationship:** Substitute only for workflow versus agent fundamentals. Anthropic’s simple-pattern decision remains the architectural check, not a mandatory framework migration.

<a id="unit-01-hf-quiz"></a>

**`hf-quiz` — selected portion:** One matching quiz/exercise set for the stated topic; do not complete the whole platform.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-02"></a>

## 2. Tool design and schemas

[Return to README Step 2](README.md#2-tool-design-and-schemas)

**Topic/subtopics:** Small names; typed inputs; concise outputs; errors; idempotent reads.

**Required sequence:** the assigned book slice [B36b · C6](../docs/READING_GUIDE.md#b36b) **THEN** `ollama-tools`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `pydantic`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-tool-design-and-schemas) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B36b · C6](../docs/READING_GUIDE.md#b36b)<br>Chip Huyen · EN | Book Section | Complementary | Tool design and schemas | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b36b) |
| `ollama-tools` · [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling)<br>Ollama · EN | Documentation / tutorial | Primary | Tool definitions and execution loop; support varies by… | Consult the Small names; typed inputs; concise outputs; errors; idempotent… [bounds](#unit-02-ollama-tools) |
| `ar-agent-intro` · [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When agent autonomy adds value. | Only the linked translated lesson: When agent autonomy adds value. Arabic… [bounds](#unit-02-ar-agent-intro) |
| `ar-mini-14` · [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | LLM Factory in a working RAG backend. | The linked video only; not its playlist. |
| `hf-agents` · [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction)<br>Hugging Face · EN course + videos + exercises | Course unit: text, videos and exercises | Complementary (as needed) | Tools, thought-action-observation and the minimal agent… | Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe… [bounds](#unit-02-hf-agents) |
| `pydantic` · [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)<br>Pydantic · EN | Documentation / tutorial | Reference | Validation, coercion, strictness and serialization. | Consult the relevant example for Validation, coercion, strictness and… [bounds](#unit-02-pydantic) |
| `prompt-lab` · [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)<br>Anthropic · EN | Interactive tutorial / notebook exercises | Complementary (as needed) | Exercises with expected behaviors for prompts and… | Consult the relevant example for Exercises with expected behaviors for… [bounds](#unit-02-prompt-lab) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-ollama-tools"></a>

**`ollama-tools` — selected portion:** Consult the Small names; typed inputs; concise outputs; errors; idempotent reads sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-agent-intro"></a>

**`ar-agent-intro` — selected portion:** Only the linked translated lesson: When agent autonomy adds value. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-ar-mini-14"></a>

**`ar-mini-14` — selected portion:** Only the linked “LLM Factory” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-hf-agents"></a>

**`hf-agents` — selected portion:** Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe cycle. Select the subsection matching this group; no framework completion requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-pydantic"></a>

**`pydantic` — selected portion:** Consult the relevant example for Validation, coercion, strictness and serialization. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-02-prompt-lab"></a>

**`prompt-lab` — selected portion:** Consult the relevant example for Exercises with expected behaviors for prompts and formatting. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-03"></a>

## 3. Bounded execution loop

[Return to README Step 3](README.md#3-bounded-execution-loop)

**Topic/subtopics:** Max steps; timeout; token/cost budget; stop/ask-human; error states.

**Required sequence:** review only [B36b · C6](../docs/READING_GUIDE.md#b36b) for this task. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `asyncio`, `agents`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-bounded-execution-loop) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B36b · C6](../docs/READING_GUIDE.md#b36b)<br>Chip Huyen · EN | Book Section | Primary | Bounded execution loop | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b36b) |
| `ar-agent-trust` · [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Trust boundaries, human control and reliability. | Only the linked translated lesson: Trust boundaries, human control and… [bounds](#unit-03-ar-agent-trust) |
| `hf-agents` · [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction)<br>Hugging Face · EN course + videos + exercises | Course unit: text, videos and exercises | Complementary (as needed) | Tools, thought-action-observation and the minimal agent… | Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe… [bounds](#unit-03-hf-agents) |
| `asyncio` · [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)<br>Python · EN | Documentation / tutorial | Reference | Task groups, cancellation, timeouts and concurrency. | Consult the relevant example for Task groups, cancellation, timeouts and… [bounds](#unit-03-asyncio) |
| `agents` · [Building effective agents](https://www.anthropic.com/research/building-effective-agents)<br>Anthropic · EN | Engineering article | Reference | Workflow patterns versus autonomous agents and tool… | Read only workflows versus agents and the pattern/tool-design section… [bounds](#unit-03-agents) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-ar-agent-trust"></a>

**`ar-agent-trust` — selected portion:** Only the linked translated lesson: Trust boundaries, human control and reliability. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-hf-agents"></a>

**`hf-agents` — selected portion:** Unit 1: What are Agents?, What are Tools?, and the Think → Act → Observe cycle. Select the subsection matching this group; no framework completion requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-asyncio"></a>

**`asyncio` — selected portion:** Consult the relevant example for Task groups, cancellation, timeouts and concurrency. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-03-agents"></a>

**`agents` — selected portion:** Read only workflows versus agents and the pattern/tool-design section relevant to this decision. A multi-agent implementation is not implied.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Agent evaluation

[Return to README Step 4](README.md#4-agent-evaluation)

**Topic/subtopics:** Tool choice; arguments; trajectory; task success; final-answer grounding.

**Required sequence:** `promptfoo`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-agent-evaluation) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B17 · F11](../docs/READING_GUIDE.md#b17)<br>Alireza Parandeh · EN | Book Section | Reference | Agent evaluation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b17) |
| [B36b · C6](../docs/READING_GUIDE.md#b36b)<br>Chip Huyen · EN | Book Section | Reference | Agent evaluation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b36b) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Primary | Deterministic checks, model judges and eval assertions. | The assertion type matching Agent evaluation; start with deterministic… [bounds](#unit-04-promptfoo) |
| `ar-agent-production` · [Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation and deployment concerns. | Only the linked translated lesson: Evaluation and deployment concerns.… [bounds](#unit-04-ar-agent-production) |
| `dla-eval` · [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)<br>DeepLearning.AI · Arize AI · EN video + labs | Short Course + labs | Complementary (as needed) | Trace, router, skill and trajectory evaluation. | Improving your LLM-as-a-judge for judge design; Adding router and skill… [bounds](#unit-04-dla-eval) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-promptfoo"></a>

**`promptfoo` — selected portion:** The assertion type matching Agent evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-agent-production"></a>

**`ar-agent-production` — selected portion:** Only the linked translated lesson: Evaluation and deployment concerns. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-dla-eval"></a>

**`dla-eval` — selected portion:** Improving your LLM-as-a-judge for judge design; Adding router and skill evaluations / Lab 3; Adding trajectory evaluations / Lab 4 for the bounded agent.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-05"></a>

## 5. Memory and context interfaces

[Return to README Step 5](README.md#5-memory-and-context-interfaces)

**Topic/subtopics:** Retrieve only needed state; observation size; provenance; side-effect confirmation.

**Required sequence (default route):** `context`. Stop each source at the stated portion.

**Choose ONE explanation for context-interface orientation:** default `context` **OR** `context-video`. Review only the named L09 concepts; memory persistence remains a distinct concern. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-memory-and-context-interfaces) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B28 · C6](../docs/READING_GUIDE.md#b28)<br>Chip Huyen · EN | Book Section | Reference | Memory and context interfaces | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b28) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Primary | Selection, context rot, just-in-time retrieval,… | Review only tool design, just-in-time retrieval and sub-agent tradeoffs… [bounds](#unit-05-context) |
| `ar-agent-memory` · [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Short/long-term state and memory lifecycle. | Only the linked translated lesson: Short/long-term state and memory… [bounds](#unit-05-ar-agent-memory) |
| `ar-agent-context` · [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Selecting and organizing information for agents. | Only the linked translated lesson: Selecting and organizing information… [bounds](#unit-05-ar-agent-context) |
| `context-video` · [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag)<br>Microsoft AI Agents for Beginners · EN video | Single Video (course lesson) | Alternative | Context selection, organization and agent context design. | Topic bounds; lesson IDs not verified — [details](#unit-05-context-video) |
| `memory-video` · [Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw)<br>Microsoft AI Agents for Beginners · EN video | Single Video (course lesson) | Complementary (as needed) | Agent memory concepts and persistence boundaries. | Topic bounds; lesson IDs not verified — [details](#unit-05-memory-video) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-context"></a>

**`context` — selected portion:** Review only tool design, just-in-time retrieval and sub-agent tradeoffs from L09; no full article reread.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-agent-memory"></a>

**`ar-agent-memory` — selected portion:** Only the linked translated lesson: Short/long-term state and memory lifecycle. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-ar-agent-context"></a>

**`ar-agent-context` — selected portion:** Only the linked translated lesson: Selecting and organizing information for agents. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-context-video"></a>

**`context-video` — selected portion:** Only the linked lesson on Context selection, organization and agent context design. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for context-interface orientation. Review only the named L09 concepts; memory persistence remains a distinct concern.

<a id="unit-05-memory-video"></a>

**`memory-video` — selected portion:** Only the linked lesson on Agent memory concepts and persistence boundaries. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-06"></a>

## 6. Multi-agent comparison

[Return to README Step 6](README.md#6-multi-agent-comparison)

**Topic/subtopics:** Specialist role; independent context; handoff summary; coordination failures.

**Required sequence:** `agents`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `context`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-multi-agent-comparison) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B36a · G6](../docs/READING_GUIDE.md#b36a)<br>Andrea De Mauro · EN | Book Section | Reference | Multi-agent comparison | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b36a) |
| [B36b · C6](../docs/READING_GUIDE.md#b36b)<br>Chip Huyen · EN | Book Section | Reference | Multi-agent comparison | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b36b) |
| `agents` · [Building effective agents](https://www.anthropic.com/research/building-effective-agents)<br>Anthropic · EN | Engineering article | Primary | Workflow patterns versus autonomous agents and tool… | Read the “workflows versus agents” distinction and the pattern/tool-design… [bounds](#unit-06-agents) |
| `ar-agent-intro` · [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When agent autonomy adds value. | Only the linked translated lesson: When agent autonomy adds value. Arabic… [bounds](#unit-06-ar-agent-intro) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Reference | Selection, context rot, just-in-time retrieval,… | Review only the context-selection, JIT retrieval, compaction or sub-agent… [bounds](#unit-06-context) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-agents"></a>

**`agents` — selected portion:** Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Multi-agent comparison. Multi-agent implementations are not required.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-agent-intro"></a>

**`ar-agent-intro` — selected portion:** Only the linked translated lesson: When agent autonomy adds value. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-context"></a>

**`context` — selected portion:** Review only the context-selection, JIT retrieval, compaction or sub-agent subsection relevant to this group; follow the named step scope, not a full reread.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-agent-intro"></a>

<details>
<summary>ar-agent-intro · Agent use cases · Arabic — access, scope and verification</summary>

[Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** When agent autonomy adds value.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Agent anatomy and design choice; Tool design and schemas; Multi-agent comparison.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Agent anatomy and design choice. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Agent anatomy and design choice; Tool design and schemas; Bounded execution loop.
- **Retained broad selection notes (lookup only):** Unit 1: what is an agent, tools, actions/observations, the dummy-agent loop and final quiz. Framework-specific builds are alternatives.

</details>

<a id="r-agents"></a>

<details>
<summary>agents · Building effective agents — access, scope and verification</summary>

[Building effective agents](https://www.anthropic.com/research/building-effective-agents) · Anthropic · EN

- **Resource Type:** Engineering article.
- **Access:** Free.
- **Catalog scope:** Workflow patterns versus autonomous agents and tool interface design.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Agent anatomy and design choice; Bounded execution loop; Multi-agent comparison.
- **Retained broad selection notes (lookup only):** Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Agent anatomy and design choice. Multi-agent implementations are not required. Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Multi-agent comparison. Multi-agent implementations are not required.

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
- **Retained Level-wide topic association:** Tool design and schemas.
- **Retained broad selection notes (lookup only):** Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-ollama-tools"></a>

<details>
<summary>ollama-tools · Ollama tool calling — access, scope and verification</summary>

[Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling) · Ollama · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Tool definitions and execution loop; support varies by model.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tool design and schemas.
- **Retained broad selection notes (lookup only):** Consult the Small names; typed inputs; concise outputs; errors; idempotent reads sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Tool design and schemas.
- **Retained broad selection notes (lookup only):** Consult the Small names; typed inputs; concise outputs; errors; idempotent reads sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Bounded execution loop.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Bounded execution loop. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-asyncio"></a>

<details>
<summary>asyncio · asyncio tasks — access, scope and verification</summary>

[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) · Python · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Task groups, cancellation, timeouts and concurrency.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Bounded execution loop.
- **Retained broad selection notes (lookup only):** Consult the Max steps; timeout; token/cost budget; stop/ask-human; error states sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-agent-production"></a>

<details>
<summary>ar-agent-production · Agents in production · Arabic — access, scope and verification</summary>

[Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Evaluation and deployment concerns.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Agent evaluation.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Agent evaluation. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-dla-eval"></a>

<details>
<summary>dla-eval · Evaluating AI Agents — access, scope and verification</summary>

[Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) · DeepLearning.AI · Arize AI · EN video + labs

- **Resource Type:** Short Course + labs.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Catalog scope:** Trace, router, skill and trajectory evaluation.
- **Scope/version limits:** Use after a bounded agent exists; simpler output evals come first.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Agent evaluation.
- **Retained broad selection notes (lookup only):** “Adding router and skill evaluations” with Lab 3; “Adding trajectory evaluations” with Lab 4. Review tracing only as needed.

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
- **Retained Level-wide topic association:** Agent evaluation.
- **Retained broad selection notes (lookup only):** The assertion type matching Agent evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

</details>

<a id="r-ar-agent-memory"></a>

<details>
<summary>ar-agent-memory · Agent memory · Arabic — access, scope and verification</summary>

[Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Short/long-term state and memory lifecycle.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Memory and context interfaces.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Memory and context interfaces. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-ar-agent-context"></a>

<details>
<summary>ar-agent-context · Context engineering · Arabic — access, scope and verification</summary>

[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Selecting and organizing information for agents.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Memory and context interfaces.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Memory and context interfaces. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-context-video"></a>

<details>
<summary>context-video · Context Engineering for AI Agents · lesson — access, scope and verification</summary>

[Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) · Microsoft AI Agents for Beginners · EN video

- **Resource Type:** Single Video (course lesson).
- **Access:** Free.
- **Catalog scope:** Context selection, organization and agent context design.
- **Scope/version limits:** Use Anthropic as the primary assigned article; framework examples are supplementary.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Memory and context interfaces.
- **Retained broad selection notes (lookup only):** The single linked video. No other channel/playlist content is assigned.

</details>

<a id="r-memory-video"></a>

<details>
<summary>memory-video · Managing Agentic Memory · lesson — access, scope and verification</summary>

[Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw) · Microsoft AI Agents for Beginners · EN video

- **Resource Type:** Single Video (course lesson).
- **Access:** Free.
- **Catalog scope:** Agent memory concepts and persistence boundaries.
- **Scope/version limits:** Provenance, erasure and compaction tests still need your own project implementation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Memory and context interfaces.
- **Retained broad selection notes (lookup only):** The single linked video. No other channel/playlist content is assigned.

</details>

<a id="r-context"></a>

<details>
<summary>context · Effective context engineering for AI agents — access, scope and verification</summary>

[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · Anthropic · EN

- **Resource Type:** Engineering article.
- **Access:** Free.
- **Catalog scope:** Selection, context rot, just-in-time retrieval, compaction, memory and sub-agents.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Memory and context interfaces; Multi-agent comparison.
- **Retained broad selection notes (lookup only):** Review only tool design, just-in-time retrieval and sub-agent tradeoffs from L09; no full article reread.

</details>

<a id="r-hf-quiz"></a>

<details>
<summary>hf-quiz · Agent fundamentals quiz — access, scope and verification</summary>

[Agent fundamentals quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz) · Hugging Face · EN interactive quiz

- **Resource Type:** Interactive quiz.
- **Access:** Free.
- **Catalog scope:** Independent concept check for tools, observations and agent behavior.
- **Scope/version limits:** A quiz pass does not replace implementation tests; login may be needed to submit.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Unit 1 final quiz only; record missed concepts, then return to the bounded-agent exercise.

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
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Consult the Exercises with expected behaviors for prompts and formatting. sections/examples only. Do not read the entire documentation site.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

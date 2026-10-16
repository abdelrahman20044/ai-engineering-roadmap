# Resource Library · L09 — Context Engineering, Memory, and Conversations

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Microsoft provides Arabic translated context/memory lessons. No complete Egyptian video course on context rot, compaction and memory evaluation was verified. The Anthropic article and English lessons are the primary sources for those techniques.

## Topic navigation

1. [Context engineering and context rot](#unit-01)
2. [Context budget and selection](#unit-02)
3. [Just-in-time retrieval](#unit-03)
4. [Conversation history and structured memory](#unit-04)
5. [Compaction and retained constraints](#unit-05)
6. [Sub-agent boundary](#unit-06)

<a id="unit-01"></a>

## 1. Context engineering and context rot

[Return to README Step 1](README.md#1-context-engineering-and-context-rot)

**Topic/subtopics:** Prompt versus context; attention budget; irrelevant tokens; position sensitivity.

**Required sequence (default route):** `context`. Stop each source at the stated portion.

**Choose ONE explanation for context-selection orientation:** default `context` **OR** `context-video`. The specific Anthropic context-rot discussion and your distractor experiment remain required. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-context-engineering-and-context-rot) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B30 · C5](../docs/READING_GUIDE.md#b30)<br>Chip Huyen · EN | Book Section | Reference | Context engineering and context rot | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b30) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Primary | Selection, context rot, just-in-time retrieval,… | Read the opening distinction between prompt and context engineering, then… [bounds](#unit-01-context) |
| `ar-agent-context` · [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Selecting and organizing information for agents. | Only the linked translated lesson: Selecting and organizing information… [bounds](#unit-01-ar-agent-context) |
| `context-video` · [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag)<br>Microsoft AI Agents for Beginners · EN video | Single Video (course lesson) | Alternative | Context selection, organization and agent context design. | Topic bounds; lesson IDs not verified — [details](#unit-01-context-video) |
| `lost-middle` · [Lost in the Middle](https://arxiv.org/abs/2307.03172)<br>Liu et al. · EN research paper | Research paper | Optional Advanced | Evidence about long-context position sensitivity. | Problem statement and architecture/results relevant to this topic;… [bounds](#unit-01-lost-middle) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-context"></a>

**`context` — selected portion:** Read the opening distinction between prompt and context engineering, then “Why context engineering is important” on context rot. Save the later techniques for their steps below.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-agent-context"></a>

**`ar-agent-context` — selected portion:** Only the linked translated lesson: Selecting and organizing information for agents. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-context-video"></a>

**`context-video` — selected portion:** Only the linked lesson on Context selection, organization and agent context design. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for context-selection orientation. The specific Anthropic context-rot discussion and your distractor experiment remain required.

<a id="unit-01-lost-middle"></a>

**`lost-middle` — selected portion:** Problem statement and architecture/results relevant to this topic; optional depth, not paper-wide implementation homework.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-02"></a>

## 2. Context budget and selection

[Return to README Step 2](README.md#2-context-budget-and-selection)

**Topic/subtopics:** Instructions; schema; evidence; journal; history; output reserve.

**Required sequence:** the assigned book slice [B29 · C10](../docs/READING_GUIDE.md#b29) **THEN** `context`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `hf-token`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-context-budget-and-selection) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B29 · C10](../docs/READING_GUIDE.md#b29)<br>Chip Huyen · EN | Book Section | Complementary | Context budget and selection | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b29) |
| [B30 · C5](../docs/READING_GUIDE.md#b30)<br>Chip Huyen · EN | Book Section | Reference | Context budget and selection | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b30) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Primary | Selection, context rot, just-in-time retrieval,… | Read “The anatomy of effective context” (system prompts, tools, examples… [bounds](#unit-02-context) |
| `ar-agent-context` · [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Selecting and organizing information for agents. | Only the linked translated lesson: Selecting and organizing information… [bounds](#unit-02-ar-agent-context) |
| `ar-gen-chat` · [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Conversation state and token/context constraints. | Only the linked translated lesson: Conversation state and token/context… [bounds](#unit-02-ar-gen-chat) |
| `context-video` · [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag)<br>Microsoft AI Agents for Beginners · EN video | Single Video (course lesson) | Complementary (as needed) | Context selection, organization and agent context design. | Topic bounds; lesson IDs not verified — [details](#unit-02-context-video) |
| `hf-token` · [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)<br>Hugging Face · EN | Documentation / tutorial | Reference | Subword tokenization and language-dependent token counts. | Chapter 6 introduction to tokenization; selected tokenizer/model example… [bounds](#unit-02-hf-token) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-context"></a>

**`context` — selected portion:** Read “The anatomy of effective context” (system prompts, tools, examples and history). Apply its selection principle to your own explicit token-budget manifest; the article does not prescribe numeric budgets.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-agent-context"></a>

**`ar-agent-context` — selected portion:** Only the linked translated lesson: Selecting and organizing information for agents. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-ar-gen-chat"></a>

**`ar-gen-chat` — selected portion:** Only the linked translated lesson: Conversation state and token/context constraints. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-context-video"></a>

**`context-video` — selected portion:** Only the linked lesson on Context selection, organization and agent context design. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-hf-token"></a>

**`hf-token` — selected portion:** Chapter 6 introduction to tokenization; selected tokenizer/model example only. Reuse for token counting, not a course restart.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Just-in-time retrieval

[Return to README Step 3](README.md#3-just-in-time-retrieval)

**Topic/subtopics:** References versus full content; selective journal search; minimal tool outputs.

**Required sequence:** `context`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-just-in-time-retrieval) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B29 · C10](../docs/READING_GUIDE.md#b29)<br>Chip Huyen · EN | Book Section | Reference | Just-in-time retrieval | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b29) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Primary | Selection, context rot, just-in-time retrieval,… | Read “Context retrieval and agentic search”, especially just-in-time… [bounds](#unit-03-context) |
| `ar-agent-context` · [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Selecting and organizing information for agents. | Only the linked translated lesson: Selecting and organizing information… [bounds](#unit-03-ar-agent-context) |
| `context-video` · [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag)<br>Microsoft AI Agents for Beginners · EN video | Single Video (course lesson) | Complementary (as needed) | Context selection, organization and agent context design. | Topic bounds; lesson IDs not verified — [details](#unit-03-context-video) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-context"></a>

**`context` — selected portion:** Read “Context retrieval and agentic search”, especially just-in-time loading and progressive discovery. Compare the two retrieval strategies in your own application.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-agent-context"></a>

**`ar-agent-context` — selected portion:** Only the linked translated lesson: Selecting and organizing information for agents. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-context-video"></a>

**`context-video` — selected portion:** Only the linked lesson on Context selection, organization and agent context design. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-04"></a>

## 4. Conversation history and structured memory

[Return to README Step 4](README.md#4-conversation-history-and-structured-memory)

**Topic/subtopics:** Working history; durable facts; provenance; conflicts; user edit/delete.

**Required sequence (default route):** the assigned book slice [B28 · C6](../docs/READING_GUIDE.md#b28) **THEN** `ar-agent-memory`. Stop each source at the stated portion.

**Choose ONE explanation for memory concepts and lifecycle:** default `ar-agent-memory` **OR** `memory-video`. Keep the assigned C6 memory slice and application-specific correction/deletion tests. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `sqlalchemy`, `context`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-conversation-history-and-structured-memory) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B28 · C6](../docs/READING_GUIDE.md#b28)<br>Chip Huyen · EN | Book Section | Complementary | Conversation history and structured memory | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b28) |
| `ar-agent-memory` · [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Primary | Short/long-term state and memory lifecycle. | Only the linked translated lesson, particularly its sections about… [bounds](#unit-04-ar-agent-memory) |
| `ar-gen-chat` · [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Conversation state and token/context constraints. | Only the linked translated lesson: Conversation state and token/context… [bounds](#unit-04-ar-gen-chat) |
| `memory-video` · [Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw)<br>Microsoft AI Agents for Beginners · EN video | Single Video (course lesson) | Alternative | Agent memory concepts and persistence boundaries. | Topic bounds; lesson IDs not verified — [details](#unit-04-memory-video) |
| `sqlalchemy` · [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)<br>SQLAlchemy · EN | Documentation / tutorial | Reference | Mapped classes, relationships, selects and unit of work. | Consult the relevant example for Mapped classes, relationships, selects… [bounds](#unit-04-sqlalchemy) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Reference | Selection, context rot, just-in-time retrieval,… | Review only the context-selection, JIT retrieval, compaction or sub-agent… [bounds](#unit-04-context) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-ar-agent-memory"></a>

**`ar-agent-memory` — selected portion:** Only the linked translated lesson, particularly its sections about Conversation history and structured memory. Its English video/cloud build is an alternative, not an extra requirement.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-gen-chat"></a>

**`ar-gen-chat` — selected portion:** Only the linked translated lesson: Conversation state and token/context constraints. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-memory-video"></a>

**`memory-video` — selected portion:** Only the linked lesson on Agent memory concepts and persistence boundaries. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Substitute only for memory concepts and lifecycle. Keep the assigned C6 memory slice and application-specific correction/deletion tests.

<a id="unit-04-sqlalchemy"></a>

**`sqlalchemy` — selected portion:** Consult the relevant example for Mapped classes, relationships, selects and unit of work. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-04-context"></a>

**`context` — selected portion:** Review only the context-selection, JIT retrieval, compaction or sub-agent subsection relevant to this group; follow the named step scope, not a full reread.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Compaction and retained constraints

[Return to README Step 5](README.md#5-compaction-and-retained-constraints)

**Topic/subtopics:** Summaries; checkpoints; recoverable sources; lost-detail evaluation.

**Required sequence:** `context`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-compaction-and-retained-constraints) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B28 · C6](../docs/READING_GUIDE.md#b28)<br>Chip Huyen · EN | Book Section | Reference | Compaction and retained constraints | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b28) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Primary | Selection, context rot, just-in-time retrieval,… | Read only “Compaction” and “Structured note-taking” under context… [bounds](#unit-05-context) |
| `ar-agent-context` · [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Selecting and organizing information for agents. | Only the linked translated lesson: Selecting and organizing information… [bounds](#unit-05-ar-agent-context) |
| `context-cookbook` · [Context engineering: memory, compaction and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)<br>Anthropic · EN notebook recipe | Notebook / practical recipe | Complementary (as needed) | Inspect memory and context-management experiments after… | One memory/compaction/tool-clearing notebook matching an observed context… [bounds](#unit-05-context-cookbook) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-context"></a>

**`context` — selected portion:** Read only “Compaction” and “Structured note-taking” under context engineering for long-horizon tasks. Test what your summary loses; do not implement sub-agents here.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-agent-context"></a>

**`ar-agent-context` — selected portion:** Only the linked translated lesson: Selecting and organizing information for agents. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-context-cookbook"></a>

**`context-cookbook` — selected portion:** One memory/compaction/tool-clearing notebook matching an observed context failure; provider-specific APIs are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-06"></a>

## 6. Sub-agent boundary

[Return to README Step 6](README.md#6-sub-agent-boundary)

**Topic/subtopics:** Partitionable tasks; narrow context; summary handoff; coordination cost.

**Required sequence:** `agents`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `context`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-sub-agent-boundary) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B28 · C6](../docs/READING_GUIDE.md#b28)<br>Chip Huyen · EN | Book Section | Reference | Sub-agent boundary | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b28) |
| `agents` · [Building effective agents](https://www.anthropic.com/research/building-effective-agents)<br>Anthropic · EN | Engineering article | Primary | Workflow patterns versus autonomous agents and tool… | Read the orchestrator-workers pattern and the closing guidance on keeping… [bounds](#unit-06-agents) |
| `ar-agent-intro` · [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When agent autonomy adds value. | Only the linked translated lesson: When agent autonomy adds value. Arabic… [bounds](#unit-06-ar-agent-intro) |
| `context` · [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)<br>Anthropic · EN | Engineering article | Reference | Selection, context rot, just-in-time retrieval,… | Review only the context-selection, JIT retrieval, compaction or sub-agent… [bounds](#unit-06-context) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-agents"></a>

**`agents` — selected portion:** Read the orchestrator-workers pattern and the closing guidance on keeping designs simple. Compare with Anthropic’s context article’s sub-agent discussion; this is a design exercise, not a multi-agent build.

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

<a id="r-ar-agent-context"></a>

<details>
<summary>ar-agent-context · Context engineering · Arabic — access, scope and verification</summary>

[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Selecting and organizing information for agents.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Context engineering and context rot; Context budget and selection; Just-in-time retrieval; Compaction and retained constraints.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Context engineering and context rot. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Context engineering and context rot; Context budget and selection; Just-in-time retrieval.
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
- **Retained Level-wide topic association:** Context engineering and context rot; Context budget and selection; Just-in-time retrieval; Conversation history and structured memory; Compaction and retained constraints; Sub-agent boundary.
- **Retained broad selection notes (lookup only):** Read the opening distinction between prompt and context engineering, then “Why context engineering is important” on context rot. Save the later techniques for their steps below. Read “The anatomy of effective context” (system prompts, tools, examples and history). Apply its selection principle to your own explicit token-budget manifest; the article does not prescribe numeric budgets. Read “Context retrieval and agentic search”, especially just-in-time loading and progressive discovery. Compare the two retrieval strategies in your own application. Read only “Compaction” and “Structured note-taking” under context engineering for long-horizon tasks. Test what your summary loses; do not implement sub-agents here.

</details>

<a id="r-ar-gen-chat"></a>

<details>
<summary>ar-gen-chat · Chat applications · Arabic — access, scope and verification</summary>

[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Conversation state and token/context constraints.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Context budget and selection; Conversation history and structured memory.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Context budget and selection. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-hf-token"></a>

<details>
<summary>hf-token · Tokenizers — access, scope and verification</summary>

[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) · Hugging Face · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Subword tokenization and language-dependent token counts.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Context budget and selection.
- **Retained broad selection notes (lookup only):** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.

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
- **Retained Level-wide topic association:** Conversation history and structured memory.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Conversation history and structured memory. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Conversation history and structured memory.
- **Retained broad selection notes (lookup only):** The single linked video. No other channel/playlist content is assigned.

</details>

<a id="r-sqlalchemy"></a>

<details>
<summary>sqlalchemy · SQLAlchemy Unified Tutorial — access, scope and verification</summary>

[SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) · SQLAlchemy · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Mapped classes, relationships, selects and unit of work.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Conversation history and structured memory.
- **Retained broad selection notes (lookup only):** Consult the Working history; durable facts; provenance; conflicts; user edit/delete sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-context-cookbook"></a>

<details>
<summary>context-cookbook · Context engineering: memory, compaction and tool clearing — access, scope and verification</summary>

[Context engineering: memory, compaction and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) · Anthropic · EN notebook recipe

- **Resource Type:** Notebook / practical recipe.
- **Access:** Free.
- **Catalog scope:** Inspect memory and context-management experiments after implementing a provider-independent baseline.
- **Scope/version limits:** Claude-specific optional experiment; provider API usage may incur cost.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Compaction and retained constraints.
- **Retained broad selection notes (lookup only):** Only the memory/compaction/tool-clearing recipe after the provider-independent L09 baseline; API calls may cost money.

</details>

<a id="r-ar-agent-intro"></a>

<details>
<summary>ar-agent-intro · Agent use cases · Arabic — access, scope and verification</summary>

[Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** When agent autonomy adds value.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Sub-agent boundary.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Sub-agent boundary. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Sub-agent boundary.
- **Retained broad selection notes (lookup only):** Read the orchestrator-workers pattern and the closing guidance on keeping designs simple. Compare with Anthropic’s context article’s sub-agent discussion; this is a design exercise, not a multi-agent build.

</details>

<a id="r-lost-middle"></a>

<details>
<summary>lost-middle · Lost in the Middle — access, scope and verification</summary>

[Lost in the Middle](https://arxiv.org/abs/2307.03172) · Liu et al. · EN research paper

- **Resource Type:** Research paper.
- **Access:** Free.
- **Catalog scope:** Evidence about long-context position sensitivity.
- **Scope/version limits:** Findings are experimental, not a universal score for every current model.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Evidence about long-context position sensitivity. Optional lookup; implement only the portion that addresses the named gap.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

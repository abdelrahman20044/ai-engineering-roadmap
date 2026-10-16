# Resource Library · L09 — Context Engineering, Memory, and Conversations

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** Microsoft provides Arabic translated context/memory lessons. No complete Egyptian video course on context rot, compaction and memory evaluation was verified. The Anthropic article and English lessons are the primary sources for those techniques.

## Book references

Assigned reading is authoritative in [the master order for L09](../docs/READING_GUIDE.md#l09). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B30 · C5](../docs/READING_GUIDE.md#b30), [B29 · C10](../docs/READING_GUIDE.md#b29), [B28 · C6](../docs/READING_GUIDE.md#b28).

**Previously covered / lookup only:** [B14 · C5](../docs/READING_GUIDE.md#b14). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-agent-context"></a>

### Context engineering · Arabic

[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Context engineering and context rot; Context budget and selection; Just-in-time retrieval; Compaction and retained constraints.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Context engineering and context rot. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Selecting and organizing information for agents.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-chat"></a>

### Chat applications · Arabic

[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Context budget and selection; Conversation history and structured memory.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Context budget and selection. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Conversation state and token/context constraints.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-agent-memory"></a>

### Agent memory · Arabic

[Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Primary. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Conversation history and structured memory.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Conversation history and structured memory. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Short/long-term state and memory lifecycle.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-agent-intro"></a>

### Agent use cases · Arabic

[Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Sub-agent boundary.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Sub-agent boundary. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** When agent autonomy adds value.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-context-video"></a>

### Context Engineering for AI Agents · lesson

[Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag)

- **Resource Type:** Single course video.
- **Role:** Alternative. **Language:** EN video. **By:** Microsoft AI Agents for Beginners.
- **Access:** Free.
- **Use for:** Context engineering and context rot; Context budget and selection; Just-in-time retrieval.
- **Assigned portion:** The single linked video. No other channel/playlist content is assigned.
- **Scope:** Context selection, organization and agent context design.
- **Limit:** Use Anthropic as the primary assigned article; framework examples are supplementary.

<a id="r-memory-video"></a>

### Managing Agentic Memory · lesson

[Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw)

- **Resource Type:** Single course video.
- **Role:** Alternative. **Language:** EN video. **By:** Microsoft AI Agents for Beginners.
- **Access:** Free.
- **Use for:** Conversation history and structured memory.
- **Assigned portion:** The single linked video. No other channel/playlist content is assigned.
- **Scope:** Agent memory concepts and persistence boundaries.
- **Limit:** Provenance, erasure and compaction tests still need your own project implementation.

## Slides, notebooks and repositories

<a id="r-context-cookbook"></a>

### Context engineering: memory, compaction and tool clearing

[Context engineering: memory, compaction and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)

- **Resource Type:** Notebook / practical recipe.
- **Role:** Optional Advanced. **Language:** EN notebook recipe. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Compaction and retained constraints.
- **Assigned portion:** Only the memory/compaction/tool-clearing recipe after the provider-independent L09 baseline; API calls may cost money.
- **Scope:** Inspect memory and context-management experiments after implementing a provider-independent baseline.
- **Limit:** Claude-specific optional experiment; provider API usage may incur cost.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Official documentation and engineering articles

<a id="r-context"></a>

### Effective context engineering for AI agents

[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

- **Resource Type:** Engineering article.
- **Role:** Primary. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Context engineering and context rot; Context budget and selection; Just-in-time retrieval; Conversation history and structured memory; Compaction and retained constraints; Sub-agent boundary.
- **Assigned portion:** Read the opening distinction between prompt and context engineering, then “Why context engineering is important” on context rot. Save the later techniques for their steps below. Read “The anatomy of effective context” (system prompts, tools, examples and history). Apply its selection principle to your own explicit token-budget manifest; the article does not prescribe numeric budgets. Read “Context retrieval and agentic search”, especially just-in-time loading and progressive discovery. Compare the two retrieval strategies in your own application. Read only “Compaction” and “Structured note-taking” under context engineering for long-horizon tasks. Test what your summary loses; do not implement sub-agents here.
- **Scope:** Selection, context rot, just-in-time retrieval, compaction, memory and sub-agents.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-hf-token"></a>

### Tokenizers

[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Context budget and selection.
- **Assigned portion:** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.
- **Scope:** Subword tokenization and language-dependent token counts.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-sqlalchemy"></a>

### SQLAlchemy Unified Tutorial

[SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** SQLAlchemy.
- **Access:** Free.
- **Use for:** Conversation history and structured memory.
- **Assigned portion:** Consult the Working history; durable facts; provenance; conflicts; user edit/delete sections/examples only. Do not read the entire documentation site.
- **Scope:** Mapped classes, relationships, selects and unit of work.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-agents"></a>

### Building effective agents

[Building effective agents](https://www.anthropic.com/research/building-effective-agents)

- **Resource Type:** Engineering article.
- **Role:** Primary. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Sub-agent boundary.
- **Assigned portion:** Read the orchestrator-workers pattern and the closing guidance on keeping designs simple. Compare with Anthropic’s context article’s sub-agent discussion; this is a design exercise, not a multi-agent build.
- **Scope:** Workflow patterns versus autonomous agents and tool interface design.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

<a id="r-lost-middle"></a>

### Lost in the Middle

[Lost in the Middle](https://arxiv.org/abs/2307.03172)

- **Resource Type:** Research paper.
- **Role:** Optional Advanced. **Language:** EN research paper. **By:** Liu et al..
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Evidence about long-context position sensitivity. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Evidence about long-context position sensitivity.
- **Limit:** Findings are experimental, not a universal score for every current model.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

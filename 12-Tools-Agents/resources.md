# Resource Library · L12 — Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** Arabic translated agent lessons provide structured text. A complete Arabic course covering bounded loops plus trajectory evaluation was not verified; pair them with the English agent course and assessment labs.

## Book references

Assigned reading is authoritative in [the master order for L12](../docs/READING_GUIDE.md#l12). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B36 · G5](../docs/READING_GUIDE.md#b36), [B36a · G6](../docs/READING_GUIDE.md#b36a), [B36b · C6](../docs/READING_GUIDE.md#b36b).

**Previously covered / lookup only:** [B17 · F11](../docs/READING_GUIDE.md#b17), [B28 · C6](../docs/READING_GUIDE.md#b28). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-agent-intro"></a>

### Agent use cases · Arabic

[Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Agent anatomy and design choice; Tool design and schemas; Multi-agent comparison.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Agent anatomy and design choice. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** When agent autonomy adds value.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-mini-14"></a>

### mini-RAG · LLM Factory

[mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Tool design and schemas.
- **Assigned portion:** Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** LLM Factory in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

<a id="r-ar-agent-trust"></a>

### Trustworthy agents · Arabic

[Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Bounded execution loop.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Bounded execution loop. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Trust boundaries, human control and reliability.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-agent-production"></a>

### Agents in production · Arabic

[Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Agent evaluation.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Agent evaluation. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Evaluation and deployment concerns.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-agent-memory"></a>

### Agent memory · Arabic

[Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Memory and context interfaces.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Memory and context interfaces. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Short/long-term state and memory lifecycle.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-agent-context"></a>

### Context engineering · Arabic

[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Memory and context interfaces.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Memory and context interfaces. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Selecting and organizing information for agents.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-hf-agents"></a>

### Agents course · Unit 1

[Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction)

- **Resource Type:** Course unit: text, videos and exercises.
- **Role:** Alternative. **Language:** EN course + videos + exercises. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Agent anatomy and design choice; Tool design and schemas; Bounded execution loop.
- **Assigned portion:** Unit 1: what is an agent, tools, actions/observations, the dummy-agent loop and final quiz. Framework-specific builds are alternatives.
- **Scope:** Tools, thought-action-observation and the minimal agent loop.
- **Limit:** Learn the loop before adopting smolagents or another framework.

<a id="r-dla-eval"></a>

### Evaluating AI Agents

[Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)

- **Resource Type:** Short video course + labs.
- **Role:** Alternative. **Language:** EN video + labs. **By:** DeepLearning.AI · Arize AI.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** Agent evaluation.
- **Assigned portion:** “Adding router and skill evaluations” with Lab 3; “Adding trajectory evaluations” with Lab 4. Review tracing only as needed.
- **Scope:** Trace, router, skill and trajectory evaluation.
- **Limit:** Use after a bounded agent exists; simpler output evals come first.

<a id="r-context-video"></a>

### Context Engineering for AI Agents · lesson

[Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag)

- **Resource Type:** Single course video.
- **Role:** Alternative. **Language:** EN video. **By:** Microsoft AI Agents for Beginners.
- **Access:** Free.
- **Use for:** Memory and context interfaces.
- **Assigned portion:** The single linked video. No other channel/playlist content is assigned.
- **Scope:** Context selection, organization and agent context design.
- **Limit:** Use Anthropic as the primary assigned article; framework examples are supplementary.

<a id="r-memory-video"></a>

### Managing Agentic Memory · lesson

[Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw)

- **Resource Type:** Single course video.
- **Role:** Alternative. **Language:** EN video. **By:** Microsoft AI Agents for Beginners.
- **Access:** Free.
- **Use for:** Memory and context interfaces.
- **Assigned portion:** The single linked video. No other channel/playlist content is assigned.
- **Scope:** Agent memory concepts and persistence boundaries.
- **Limit:** Provenance, erasure and compaction tests still need your own project implementation.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

<a id="r-hf-quiz"></a>

### Agent fundamentals quiz

[Agent fundamentals quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz)

- **Resource Type:** Interactive quiz.
- **Role:** Alternative. **Language:** EN interactive quiz. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Unit 1 final quiz only; record missed concepts, then return to the bounded-agent exercise.
- **Scope:** Independent concept check for tools, observations and agent behavior.
- **Limit:** A quiz pass does not replace implementation tests; login may be needed to submit.

<a id="r-prompt-lab"></a>

### Interactive prompt engineering tutorial

[Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)

- **Resource Type:** Interactive tutorial / notebook exercises.
- **Role:** Alternative. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Consult the Exercises with expected behaviors for prompts and formatting. sections/examples only. Do not read the entire documentation site.
- **Scope:** Exercises with expected behaviors for prompts and formatting.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Official documentation and engineering articles

<a id="r-agents"></a>

### Building effective agents

[Building effective agents](https://www.anthropic.com/research/building-effective-agents)

- **Resource Type:** Engineering article.
- **Role:** Primary. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Agent anatomy and design choice; Bounded execution loop; Multi-agent comparison.
- **Assigned portion:** Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Agent anatomy and design choice. Multi-agent implementations are not required. Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Multi-agent comparison. Multi-agent implementations are not required.
- **Scope:** Workflow patterns versus autonomous agents and tool interface design.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ollama-tools"></a>

### Ollama tool calling

[Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Ollama.
- **Access:** Free.
- **Use for:** Tool design and schemas.
- **Assigned portion:** Consult the Small names; typed inputs; concise outputs; errors; idempotent reads sections/examples only. Do not read the entire documentation site.
- **Scope:** Tool definitions and execution loop; support varies by model.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pydantic"></a>

### Pydantic models

[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Pydantic.
- **Access:** Free.
- **Use for:** Tool design and schemas.
- **Assigned portion:** Consult the Small names; typed inputs; concise outputs; errors; idempotent reads sections/examples only. Do not read the entire documentation site.
- **Scope:** Validation, coercion, strictness and serialization.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-asyncio"></a>

### asyncio tasks

[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Python.
- **Access:** Free.
- **Use for:** Bounded execution loop.
- **Assigned portion:** Consult the Max steps; timeout; token/cost budget; stop/ask-human; error states sections/examples only. Do not read the entire documentation site.
- **Scope:** Task groups, cancellation, timeouts and concurrency.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-promptfoo"></a>

### Assertions and metrics

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

- **Resource Type:** Documentation: assertions reference.
- **Role:** Primary. **Language:** EN. **By:** Promptfoo.
- **Access:** Free.
- **Use for:** Agent evaluation.
- **Assigned portion:** The assertion type matching Agent evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.
- **Scope:** Deterministic checks, model judges and eval assertions.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-context"></a>

### Effective context engineering for AI agents

[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

- **Resource Type:** Engineering article.
- **Role:** Primary. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Memory and context interfaces; Multi-agent comparison.
- **Assigned portion:** Review only tool design, just-in-time retrieval and sub-agent tradeoffs from L09; no full article reread.
- **Scope:** Selection, context rot, just-in-time retrieval, compaction, memory and sub-agents.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

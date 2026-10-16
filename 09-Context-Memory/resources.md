# Resource Library · L09 — Context Engineering, Memory, and Conversations

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Read Anthropic before agent frameworks → inspect a context trace → budget and retrieve journals → add editable memory → test compaction only when needed.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Microsoft provides Arabic translated context/memory lessons. No complete Egyptian video course on context rot, compaction and memory evaluation was verified. The Anthropic article and English lessons are the primary sources for those techniques.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) | Microsoft<br>AR machine-translated text<br>Free | L09-T01 · Context engineering and context rot; L09-T02 · Context budget and selection; L09-T03 · Just-in-time retrieval; L09-T05 · Compaction and retained constraints | Selecting and organizing information for agents. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L09-T02 · Context budget and selection; L09-T04 · Conversation history and structured memory | Conversation state and token/context constraints. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md) | Microsoft<br>AR machine-translated text<br>Free | L09-T04 · Conversation history and structured memory | Short/long-term state and memory lifecycle. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) | Microsoft<br>AR machine-translated text<br>Free | L09-T06 · Sub-agent boundary | When agent autonomy adds value. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) | Microsoft AI Agents for Beginners<br>EN video<br>Free | L09-T01 · Context engineering and context rot; L09-T02 · Context budget and selection; L09-T03 · Just-in-time retrieval | Context selection, organization and agent context design. **Boundary:** Use Anthropic as the primary assigned article; framework examples are supplementary. |
| [Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw) | Microsoft AI Agents for Beginners<br>EN video<br>Free | L09-T04 · Conversation history and structured memory | Agent memory concepts and persistence boundaries. **Boundary:** Provenance, erasure and compaction tests still need your own project implementation. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Context engineering: memory, compaction and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) | Anthropic<br>EN notebook recipe<br>Free | L09-T05 · Compaction and retained constraints | Inspect memory and context-management experiments after implementing a provider-independent baseline. **Boundary:** Claude-specific optional experiment; provider API usage may incur cost. |

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| Anthropic: context selection/retrieval and long-horizon sections. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C5 pp.218–219; C6 Memory pp.300–304; C10 Enhance Context p.450. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L09-T01 | Compare focused evidence with the same evidence buried in distractors and report task outcomes. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L09-T02 | Create a context manifest with token counts, selection reasons and source IDs. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L09-T03 | Fetch relevant journal records on demand and prove unrelated entries are excluded. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L09-T04 | Store a user-approved memory with source, timestamp and correction/deletion tests. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L09-T05 | Summarize a long synthetic conversation and test five facts/constraints before and after. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L09-T06 | Write an ADR choosing a single workflow unless a bounded comparison demonstrates value. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic<br>EN<br>Free | L09-T01 · Context engineering and context rot; L09-T02 · Context budget and selection; L09-T03 · Just-in-time retrieval; L09-T04 · Conversation history and structured memory; L09-T05 · Compaction and retained constraints; L09-T06 · Sub-agent boundary | Selection, context rot, just-in-time retrieval, compaction, memory and sub-agents. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) | Hugging Face<br>EN<br>Free | L09-T02 · Context budget and selection | Subword tokenization and language-dependent token counts. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) | SQLAlchemy<br>EN<br>Free | L09-T04 · Conversation history and structured memory | Mapped classes, relationships, selects and unit of work. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Anthropic<br>EN<br>Free | L09-T06 · Sub-agent boundary | Workflow patterns versus autonomous agents and tool interface design. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) | Liu et al.<br>EN research paper<br>Free | Optional support for this Level’s assessed exercises | Evidence about long-context position sensitivity. **Boundary:** Findings are experimental, not a universal score for every current model. |

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

# Resource Library · L12 — Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

G5 tool concepts → Anthropic workflow patterns → one read-only tool → bounded loop → trajectory evaluation. Keep multi-agent work conditional.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Arabic translated agent lessons provide structured text. A complete Arabic course covering bounded loops plus trajectory evaluation was not verified; pair them with the English agent course and assessment labs.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) | Microsoft<br>AR machine-translated text<br>Free | L12-T01 · Agent anatomy and design choice; L12-T02 · Tool design and schemas; L12-T06 · Multi-agent comparison | When agent autonomy adds value. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L12-T02 · Tool design and schemas | LLM Factory in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) | Microsoft<br>AR machine-translated text<br>Free | L12-T03 · Bounded execution loop | Trust boundaries, human control and reliability. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md) | Microsoft<br>AR machine-translated text<br>Free | L12-T04 · Agent evaluation | Evaluation and deployment concerns. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md) | Microsoft<br>AR machine-translated text<br>Free | L12-T05 · Memory and context interfaces | Short/long-term state and memory lifecycle. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) | Microsoft<br>AR machine-translated text<br>Free | L12-T05 · Memory and context interfaces | Selecting and organizing information for agents. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) | Hugging Face<br>EN course + videos + exercises<br>Free | L12-T01 · Agent anatomy and design choice; L12-T02 · Tool design and schemas; L12-T03 · Bounded execution loop | Tools, thought-action-observation and the minimal agent loop. **Boundary:** Learn the loop before adopting smolagents or another framework. |
| [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) | DeepLearning.AI · Arize AI<br>EN video + labs<br>Limited-time free access advertised; account/terms may change | L12-T04 · Agent evaluation | Trace, router, skill and trajectory evaluation. **Boundary:** Use after a bounded agent exists; simpler output evals come first. |
| [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) | Microsoft AI Agents for Beginners<br>EN video<br>Free | L12-T05 · Memory and context interfaces | Context selection, organization and agent context design. **Boundary:** Use Anthropic as the primary assigned article; framework examples are supplementary. |
| [Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw) | Microsoft AI Agents for Beginners<br>EN video<br>Free | L12-T05 · Memory and context interfaces | Agent memory concepts and persistence boundaries. **Boundary:** Provenance, erasure and compaction tests still need your own project implementation. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| G5 printed pp.102–107 and 122–127; G6 pp.130–132 for patterns, with implementation examples optional. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C6 Agents pp.275–299: tools, planning, and failure modes. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| Anthropic: JIT context and sub-agent sections, interpreted through project experiments. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Agent fundamentals quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz) | Hugging Face<br>EN interactive quiz<br>Free | Optional support for this Level’s assessed exercises | Independent concept check for tools, observations and agent behavior. **Boundary:** A quiz pass does not replace implementation tests; login may be needed to submit. |
| [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic<br>EN<br>Free | Optional support for this Level’s assessed exercises | Exercises with expected behaviors for prompts and formatting. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L12-T01 | Draw a fixed workflow and tool loop for the same journal question; choose a baseline. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L12-T02 | Expose one owner-scoped search tool; reject malformed and unauthorized arguments. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L12-T03 | Test repeated calls, unavailable tools, budget exhaustion and terminal behavior. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L12-T04 | Label five correct and five failed traces; report tool and task metrics separately. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L12-T05 | Limit tool result size and prove relevant evidence survives the bound. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L12-T06 | Run one partitioned experiment against the single-agent baseline; record a go/no-go ADR. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Anthropic<br>EN<br>Free | L12-T01 · Agent anatomy and design choice; L12-T03 · Bounded execution loop; L12-T06 · Multi-agent comparison | Workflow patterns versus autonomous agents and tool interface design. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling) | Ollama<br>EN<br>Free | L12-T02 · Tool design and schemas | Tool definitions and execution loop; support varies by model. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | Pydantic<br>EN<br>Free | L12-T02 · Tool design and schemas | Validation, coercion, strictness and serialization. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) | Python<br>EN<br>Free | L12-T03 · Bounded execution loop | Task groups, cancellation, timeouts and concurrency. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L12-T04 · Agent evaluation | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic<br>EN<br>Free | L12-T05 · Memory and context interfaces; L12-T06 · Multi-agent comparison | Selection, context rot, just-in-time retrieval, compaction, memory and sub-agents. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

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

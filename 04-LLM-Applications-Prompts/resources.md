# Resource Library · L04 — Prompt Engineering, Structured Outputs, and LLM Integration

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

G2 code section + G3 → one provider adapter → validated output → a fixed prompt comparison. Read C5 for failure analysis after the first call.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Prompt engineering fundamentals · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/04-prompt-engineering-fundamentals/README.md) | Microsoft<br>AR machine-translated text<br>Free | L04-T01 · Instructions and examples | Instructions, examples, prompting techniques and exercises. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Advanced prompts · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/05-advanced-prompts/README.md) | Microsoft<br>AR machine-translated text<br>Free | L04-T02 · Prompt lifecycle | Prompt iteration and task decomposition. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L04-T03 · Provider integration; L04-T06 · Small AI endpoint | LLM Factory in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L04-T03 · Provider integration | Ollama Local LLM Server in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) | Pythonation · Arabic Python community<br>AR video + code<br>Free | L04-T04 · Structured output validation | Turn Python functions into validated HTTP endpoints and inspect the companion app. **Boundary:** Introductory; lifecycle, production security and async depth need the official docs. |
| [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L04-T05 · Untrusted input boundaries | Threats and mitigations around a model-backed app. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Welcome to FastAPI](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L04-T06 · Small AI endpoint | Welcome to FastAPI in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Learn to Spell: Prompt Engineering](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/prompt-engineering/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L04-T01 · Instructions and examples | Prompt iteration and practical prompt design. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) | Sanjeev Thiyagarajan · freeCodeCamp<br>EN video<br>Free | L04-T03 · Provider integration; L04-T06 · Small AI endpoint | Select the database, auth, testing and deployment chapters from the published course outline. **Boundary:** 2021-era Pydantic/SQLAlchemy syntax requires adaptation; do not watch all 19 hours. |
| [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) | Hugging Face<br>EN course + videos + exercises<br>Free | L04-T05 · Untrusted input boundaries | Tools, thought-action-observation and the minimal agent loop. **Boundary:** Learn the loop before adopting smolagents or another framework. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [FastAPI — The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) | Eric Roby and Chad Darby<br>EN video<br>Paid · variable regional/subscription pricing | Optional support for this Level’s assessed exercises | Alternative guided backend course for validation, persistence, auth and tests. **Boundary:** Buy only if the owned FastAPI book plus free teaching do not close your specific gap; skip beginner Python. |

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| G2: What if we coded it?, printed pp.42–45; skip Langflow setup. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| G3 pp.48–56 and 68–72: prompt quality, techniques, and the coding explanation. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F3 external serving, F4 validation, and F5 PDF203–208 provider APIs. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C5 pp.218–234: context efficiency and prompt versioning; C2 structured outputs as needed. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic<br>EN<br>Free | L04-T01 · Instructions and examples | Exercises with expected behaviors for prompts and formatting. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L04-T01 | Compare a baseline and revised prompt on ten fixed examples. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L04-T02 | Store prompt v1/v2 and record the exact configuration and changed failures. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L04-T03 | Implement a real adapter with connect/read timeout and a fake equivalent. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L04-T04 | Reject invalid schema output and distinguish provider refusal from parse failure. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L04-T05 | Test a journal entry that tries to override system behavior and record the failure. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L04-T06 | Ship /reflect with explicit error behavior and a reproducible curl example. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L04-T02 · Prompt lifecycle | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) | HTTPX<br>EN<br>Free | L04-T03 · Provider integration | Connect/read/write/pool timeouts for provider calls. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ollama API introduction](https://docs.ollama.com/api/introduction) | Ollama<br>EN<br>Free | L04-T03 · Provider integration | Local inference endpoint contracts; local operation uses your hardware. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs) | Ollama<br>EN<br>Free | L04-T04 · Structured output validation | Schema-constrained output and validation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) | Pydantic<br>EN<br>Free | L04-T04 · Structured output validation | Validation, coercion, strictness and serialization. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | OWASP GenAI<br>EN<br>Free | L04-T05 · Untrusted input boundaries | Direct/indirect injection and layered mitigations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) | FastAPI<br>EN<br>Free | L04-T06 · Small AI endpoint | Swap provider implementations in API tests. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

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

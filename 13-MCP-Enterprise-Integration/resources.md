# Resource Library · L13 — MCP, Enterprise Integration, and AI Workflows

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Official MCP architecture + Arabic translated index → Python SDK server/client → permission boundary → failure/reconnect tests. Use a single local integration first.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

The verified Arabic MCP resource is a translated curriculum with code links. No comparable Egyptian video course was verified; use the Anthropic course plus official SDK examples for implementation.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md) | Microsoft<br>AR translated curriculum<br>Free | L13-T01 · MCP architecture and lifecycle; L13-T02 · Tools and resources; L13-T03 · Client and transport; L13-T04 · Authorization and trust | Navigate introduction, core concepts, first server/client, security and hands-on Python material. **Boundary:** Arabic text with linked multilingual code, not an Arabic video course; cross-check protocol details against the current specification. |
| [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) | Microsoft<br>AR machine-translated text<br>Free | L13-T04 · Authorization and trust | Trust boundaries, human control and reliability. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L13-T05 · Enterprise adapter contracts | LLM Factory in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md) | Microsoft<br>AR machine-translated text<br>Free | L13-T06 · Orchestration and observability | Evaluation and deployment concerns. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) | DeepLearning.AI · Anthropic<br>EN video + labs<br>Limited-time free access advertised; account/terms may change | L13-T01 · MCP architecture and lifecycle; L13-T02 · Tools and resources; L13-T03 · Client and transport; L13-T04 · Authorization and trust | Implement MCP servers and clients and inspect tools/resources. **Boundary:** Course transports or SDK examples may differ from the current protocol. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| MCP official architecture and the chosen SDK version; the books are not a sufficient MCP reference. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C10 pp.472–473: orchestration; G8 conceptual reference only; C6 tool contracts as needed. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L13-T01 | Diagram one connection and identify the boundary that owns user authorization. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L13-T02 | Implement one read-only document search capability with explicit response limits. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L13-T03 | Run a client-server integration test with pinned versions and deterministic fixtures. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L13-T04 | Test cross-user queries and a tool result containing instruction-like text. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L13-T05 | Fake an upstream outage and incompatible schema; preserve explicit failure status. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L13-T06 | Trace one MCP call end-to-end and test shutdown/reconnection without duplicate effects. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | MCP project<br>EN<br>Free | L13-T01 · MCP architecture and lifecycle | Host/client/server roles, primitives and lifecycle. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) | MCP project<br>EN<br>Free | L13-T02 · Tools and resources | Python server and tool/resource implementation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | MCP project<br>EN<br>Free | L13-T02 · Tools and resources; L13-T03 · Client and transport; L13-T05 · Enterprise adapter contracts; L13-T06 · Orchestration and observability | Runnable SDK examples; pin the SDK and compatible protocol version. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client) | MCP project<br>EN<br>Free | L13-T03 · Client and transport | Connect, discover tools and route requests. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) | MCP project<br>EN<br>Free | L13-T04 · Authorization and trust | Token passthrough, trust and confused-deputy risks; draft is explicitly version-sensitive. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | OWASP<br>EN<br>Free | L13-T04 · Authorization and trust | Deny-by-default object authorization and least privilege. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) | HTTPX<br>EN<br>Free | L13-T05 · Enterprise adapter contracts | Connect/read/write/pool timeouts for provider calls. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) | OpenTelemetry<br>EN<br>Free | L13-T06 · Orchestration and observability | Spans, attributes, context and exporting telemetry. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Anthropic<br>EN<br>Free | L13-T06 · Orchestration and observability | Workflow patterns versus autonomous agents and tool interface design. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

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

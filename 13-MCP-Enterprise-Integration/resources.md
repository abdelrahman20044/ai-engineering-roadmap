# Resource Library · L13 — MCP, Enterprise Integration, and AI Workflows

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** The verified Arabic MCP resource is a translated curriculum with code links. No comparable Egyptian video course was verified; use the Anthropic course plus official SDK examples for implementation.

## Topic navigation

1. [MCP architecture and lifecycle](#unit-01)
2. [Tools and resources](#unit-02)
3. [Client and transport](#unit-03)
4. [Authorization and trust](#unit-04)
5. [Enterprise adapter contracts](#unit-05)
6. [Orchestration and observability](#unit-06)

<a id="unit-01"></a>

## 1. MCP architecture and lifecycle

[Return to README Step 1](README.md#1-mcp-architecture-and-lifecycle)

**Topic/subtopics:** Host; client; server; initialization; capability discovery.

**Required sequence (default route):** the assigned book slice [B37 · C10](../docs/READING_GUIDE.md#b37) **THEN** `mcp`. Stop each source at the stated portion.

**Choose ONE explanation for MCP host/client/server orientation:** default `mcp` **OR** `dla-mcp`. Use the current protocol architecture page as the implementation reference in either route. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-mcp-architecture-and-lifecycle) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B37 · C10](../docs/READING_GUIDE.md#b37)<br>Chip Huyen · EN | Book Section | Complementary | MCP architecture and lifecycle | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b37) |
| `mcp` · [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)<br>MCP project · EN | Documentation / tutorial | Primary | Host/client/server roles, primitives and lifecycle. | Consult the Host; client; server; initialization; capability discovery… [bounds](#unit-01-mcp) |
| `ar-mcp` · [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md)<br>Microsoft · AR translated curriculum | Translated curriculum index | Complementary (as needed) | Navigate introduction, core concepts, first server/client,… | Introduction and Core Concepts from the Arabic curriculum index. |
| `dla-mcp` · [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic)<br>DeepLearning.AI · Anthropic · EN video + labs | Short Course + labs | Alternative | Implement MCP servers and clients and inspect… | Introduction and first architecture/server orientation; server/client… [bounds](#unit-01-dla-mcp) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-mcp"></a>

**`mcp` — selected portion:** Consult the Host; client; server; initialization; capability discovery sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-mcp"></a>

**`ar-mcp` — selected portion:** Introduction and Core Concepts from the Arabic curriculum index.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-dla-mcp"></a>

**`dla-mcp` — selected portion:** Introduction and first architecture/server orientation; server/client terminology matches the current official architecture reference.

**Relationship:** Substitute only for MCP host/client/server orientation. Use the current protocol architecture page as the implementation reference in either route.

</details>

<a id="unit-02"></a>

## 2. Tools and resources

[Return to README Step 2](README.md#2-tools-and-resources)

**Topic/subtopics:** Input/output schemas; resource URIs; errors; prompt templates.

**Required sequence (default route):** `mcp-server` **THEN** `mcp-sdk` (a different required capability). Stop each source at the stated portion.

**Choose ONE explanation for first MCP server and tool:** default `mcp-server` **OR** `dla-mcp`. Resource/prompt primitives still require the named SDK examples; they are complementary. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-tools-and-resources) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B36b · C6](../docs/READING_GUIDE.md#b36b)<br>Chip Huyen · EN | Book Section | Reference | Tools and resources | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b36b) |
| `mcp-server` · [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server)<br>MCP project · EN | Documentation / tutorial | Primary | Python server and tool/resource implementation. | Consult the Input/output schemas; resource URIs; errors; prompt templates… [bounds](#unit-02-mcp-server) |
| `ar-mcp` · [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md)<br>Microsoft · AR translated curriculum | Translated curriculum index | Complementary (as needed) | Navigate introduction, core concepts, first server/client,… | First Python server and tools/resources examples from the Arabic index. |
| `dla-mcp` · [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic)<br>DeepLearning.AI · Anthropic · EN video + labs | Short Course + labs | Alternative | Implement MCP servers and clients and inspect… | Creating an MCP Server; Adding Prompt and Resource Features for distinct primitives. |
| `mcp-sdk` · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)<br>MCP project · EN | Official SDK repository / examples | Complementary (required) | Runnable SDK examples; pin the SDK and compatible protocol… | Python SDK server/client examples; for Tools and resources add resource… [bounds](#unit-02-mcp-sdk) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-mcp-server"></a>

**`mcp-server` — selected portion:** Consult the Input/output schemas; resource URIs; errors; prompt templates sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-mcp"></a>

**`ar-mcp` — selected portion:** First Python server and tools/resources examples from the Arabic index.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-dla-mcp"></a>

**`dla-mcp` — selected portion:** Creating an MCP Server; Adding Prompt and Resource Features for distinct primitives.

**Relationship:** Substitute only for first MCP server and tool. Resource/prompt primitives still require the named SDK examples; they are complementary.

<a id="unit-02-mcp-sdk"></a>

**`mcp-sdk` — selected portion:** Python SDK server/client examples; for Tools and resources add resource and prompt examples. Pin the compatible SDK/protocol version.

**Relationship:** Required after the primary: a distinct capability, not a replacement.

</details>

<a id="unit-03"></a>

## 3. Client and transport

[Return to README Step 3](README.md#3-client-and-transport)

**Topic/subtopics:** stdio first; remote transport when justified; discovery/call; cleanup.

**Required sequence (default route):** `mcp-client`. Stop each source at the stated portion.

**Choose ONE explanation for first MCP client:** default `mcp-client` **OR** `dla-mcp`. Use current SDK/transport examples when the course differs in protocol version. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `mcp-sdk`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-client-and-transport) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B37 · C10](../docs/READING_GUIDE.md#b37)<br>Chip Huyen · EN | Book Section | Reference | Client and transport | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b37) |
| `mcp-client` · [Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client)<br>MCP project · EN | Documentation / tutorial | Primary | Connect, discover tools and route requests. | Consult the stdio first; remote transport when justified; discovery/call;… [bounds](#unit-03-mcp-client) |
| `ar-mcp` · [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md)<br>Microsoft · AR translated curriculum | Translated curriculum index | Complementary (as needed) | Navigate introduction, core concepts, first server/client,… | First Python client/transport example from the Arabic index. |
| `dla-mcp` · [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic)<br>DeepLearning.AI · Anthropic · EN video + labs | Short Course + labs | Alternative | Implement MCP servers and clients and inspect… | Creating an MCP Client. |
| `mcp-sdk` · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)<br>MCP project · EN | Official SDK repository / examples | Reference | Runnable SDK examples; pin the SDK and compatible protocol… | Python SDK server/client examples; for Tools and resources add resource… [bounds](#unit-03-mcp-sdk) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-mcp-client"></a>

**`mcp-client` — selected portion:** Consult the stdio first; remote transport when justified; discovery/call; cleanup sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-mcp"></a>

**`ar-mcp` — selected portion:** First Python client/transport example from the Arabic index.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-dla-mcp"></a>

**`dla-mcp` — selected portion:** Creating an MCP Client.

**Relationship:** Substitute only for first MCP client. Use current SDK/transport examples when the course differs in protocol version.

<a id="unit-03-mcp-sdk"></a>

**`mcp-sdk` — selected portion:** Python SDK server/client examples; for Tools and resources add resource and prompt examples. Pin the compatible SDK/protocol version.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Authorization and trust

[Return to README Step 4](README.md#4-authorization-and-trust)

**Topic/subtopics:** Caller context; least privilege; token audience; no token passthrough.

**Required sequence:** `mcp-security`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `authz`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-authorization-and-trust) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B35 · C5](../docs/READING_GUIDE.md#b35)<br>Chip Huyen · EN | Book Section | Reference | Authorization and trust | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b35) |
| `mcp-security` · [MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)<br>MCP project · EN | Documentation / tutorial | Primary | Token passthrough, trust and confused-deputy risks; draft… | Consult the Caller context; least privilege; token audience; no token… [bounds](#unit-04-mcp-security) |
| `ar-mcp` · [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md)<br>Microsoft · AR translated curriculum | Translated curriculum index | Complementary (as needed) | Navigate introduction, core concepts, first server/client,… | Security material from the Arabic index; current English specification… [bounds](#unit-04-ar-mcp) |
| `ar-agent-trust` · [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Trust boundaries, human control and reliability. | Only the linked translated lesson: Trust boundaries, human control and… [bounds](#unit-04-ar-agent-trust) |
| `dla-mcp` · [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic)<br>DeepLearning.AI · Anthropic · EN video + labs | Short Course + labs | Complementary (as needed) | Implement MCP servers and clients and inspect… | Security discussion only as background. No verified lesson title/number… [bounds](#unit-04-dla-mcp) |
| `authz` · [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)<br>OWASP · EN | Documentation / tutorial | Reference | Deny-by-default object authorization and least privilege. | Consult the relevant example for Deny-by-default object authorization and… [bounds](#unit-04-authz) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-mcp-security"></a>

**`mcp-security` — selected portion:** Consult the Caller context; least privilege; token audience; no token passthrough sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-mcp"></a>

**`ar-mcp` — selected portion:** Security material from the Arabic index; current English specification resolves protocol details.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-ar-agent-trust"></a>

**`ar-agent-trust` — selected portion:** Only the linked translated lesson: Trust boundaries, human control and reliability. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-dla-mcp"></a>

**`dla-mcp` — selected portion:** Security discussion only as background. No verified lesson title/number for complete protocol authorization; use the current security specification.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-authz"></a>

**`authz` — selected portion:** Consult the relevant example for Deny-by-default object authorization and least privilege. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Enterprise adapter contracts

[Return to README Step 5](README.md#5-enterprise-adapter-contracts)

**Topic/subtopics:** Timeout; retries; schema drift; pagination; safe error handling.

**Required sequence:** `httpx`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `mcp-sdk`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-enterprise-adapter-contracts) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B36b · C6](../docs/READING_GUIDE.md#b36b)<br>Chip Huyen · EN | Book Section | Reference | Enterprise adapter contracts | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b36b) |
| `httpx` · [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/)<br>HTTPX · EN | Documentation / tutorial | Primary | Connect/read/write/pool timeouts for provider calls. | Read HTTPX’s connect/read/write/pool timeouts and Timeout configuration… [bounds](#unit-05-httpx) |
| `ar-mini-14` · [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | LLM Factory in a working RAG backend. | The linked video only; not its playlist. |
| `mcp-sdk` · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)<br>MCP project · EN | Official SDK repository / examples | Reference | Runnable SDK examples; pin the SDK and compatible protocol… | Python SDK server/client examples; for Tools and resources add resource… [bounds](#unit-05-mcp-sdk) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-httpx"></a>

**`httpx` — selected portion:** Read HTTPX’s connect/read/write/pool timeouts and Timeout configuration example. Apply them to a narrow enterprise adapter; authorization and adapter schemas remain your design work from L11/L12.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-14"></a>

**`ar-mini-14` — selected portion:** Only the linked “LLM Factory” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Adapter/factory pattern context; enterprise failure contracts use HTTPX/MCP docs.

<a id="unit-05-mcp-sdk"></a>

**`mcp-sdk` — selected portion:** Python SDK server/client examples; for Tools and resources add resource and prompt examples. Pin the compatible SDK/protocol version.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Orchestration and observability

[Return to README Step 6](README.md#6-orchestration-and-observability)

**Topic/subtopics:** Business workflow versus protocol; tracing; audit; disconnect/reconnect.

**Required sequence:** `otel`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `mcp-sdk`, `agents`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-orchestration-and-observability) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B37 · C10](../docs/READING_GUIDE.md#b37)<br>Chip Huyen · EN | Book Section | Reference | Orchestration and observability | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b37) |
| `otel` · [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)<br>OpenTelemetry · EN | Documentation / tutorial | Primary | Spans, attributes, context and exporting telemetry. | Consult the Business workflow versus protocol; tracing; audit;… [bounds](#unit-06-otel) |
| `ar-agent-production` · [Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation and deployment concerns. | Only the linked translated lesson: Evaluation and deployment concerns.… [bounds](#unit-06-ar-agent-production) |
| `mcp-sdk` · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)<br>MCP project · EN | Official SDK repository / examples | Reference | Runnable SDK examples; pin the SDK and compatible protocol… | Python SDK server/client examples; for Tools and resources add resource… [bounds](#unit-06-mcp-sdk) |
| `agents` · [Building effective agents](https://www.anthropic.com/research/building-effective-agents)<br>Anthropic · EN | Engineering article | Reference | Workflow patterns versus autonomous agents and tool… | Read only workflows versus agents and the pattern/tool-design section… [bounds](#unit-06-agents) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-otel"></a>

**`otel` — selected portion:** Consult the Business workflow versus protocol; tracing; audit; disconnect/reconnect sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-agent-production"></a>

**`ar-agent-production` — selected portion:** Only the linked translated lesson: Evaluation and deployment concerns. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-mcp-sdk"></a>

**`mcp-sdk` — selected portion:** Python SDK server/client examples; for Tools and resources add resource and prompt examples. Pin the compatible SDK/protocol version.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-06-agents"></a>

**`agents` — selected portion:** Read only workflows versus agents and the pattern/tool-design section relevant to this decision. A multi-agent implementation is not implied.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-mcp"></a>

<details>
<summary>ar-mcp · MCP for Beginners · Arabic course index — access, scope and verification</summary>

[MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md) · Microsoft · AR translated curriculum

- **Resource Type:** Translated curriculum index.
- **Access:** Free.
- **Catalog scope:** Navigate introduction, core concepts, first server/client, security and hands-on Python material.
- **Scope/version limits:** Arabic text with linked multilingual code, not an Arabic video course; cross-check protocol details against the current specification.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** MCP architecture and lifecycle; Tools and resources; Client and transport; Authorization and trust.
- **Retained broad selection notes (lookup only):** From the Arabic index open Introduction, Core Concepts, first Python server/client and Security. No entire curriculum requirement; English protocol docs are authoritative.

</details>

<a id="r-dla-mcp"></a>

<details>
<summary>dla-mcp · MCP: Build Rich-Context AI Apps with Anthropic — access, scope and verification</summary>

[MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) · DeepLearning.AI · Anthropic · EN video + labs

- **Resource Type:** Short Course + labs.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Catalog scope:** Implement MCP servers and clients and inspect tools/resources.
- **Scope/version limits:** Course transports or SDK examples may differ from the current protocol.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** MCP architecture and lifecycle; Tools and resources; Client and transport; Authorization and trust.
- **Retained broad selection notes (lookup only):** Select “Creating an MCP Server”, “Creating an MCP Client” and “Adding Prompt and Resource Features”. Remote deployments are optional after local tests.

</details>

<a id="r-mcp"></a>

<details>
<summary>mcp · MCP architecture — access, scope and verification</summary>

[MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) · MCP project · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Host/client/server roles, primitives and lifecycle.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** MCP architecture and lifecycle.
- **Retained broad selection notes (lookup only):** Consult the Host; client; server; initialization; capability discovery sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-mcp-server"></a>

<details>
<summary>mcp-server · Build an MCP server — access, scope and verification</summary>

[Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) · MCP project · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Python server and tool/resource implementation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tools and resources.
- **Retained broad selection notes (lookup only):** Consult the Input/output schemas; resource URIs; errors; prompt templates sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-mcp-sdk"></a>

<details>
<summary>mcp-sdk · MCP Python SDK — access, scope and verification</summary>

[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) · MCP project · EN

- **Resource Type:** Official SDK repository / examples.
- **Access:** Free.
- **Catalog scope:** Runnable SDK examples; pin the SDK and compatible protocol version.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tools and resources; Client and transport; Enterprise adapter contracts; Orchestration and observability.
- **Retained broad selection notes (lookup only):** Consult the Input/output schemas; resource URIs; errors; prompt templates sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-mcp-client"></a>

<details>
<summary>mcp-client · Build an MCP client — access, scope and verification</summary>

[Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client) · MCP project · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Connect, discover tools and route requests.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Client and transport.
- **Retained broad selection notes (lookup only):** Consult the stdio first; remote transport when justified; discovery/call; cleanup sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Authorization and trust.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Authorization and trust. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-mcp-security"></a>

<details>
<summary>mcp-security · MCP security best practices — access, scope and verification</summary>

[MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) · MCP project · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Token passthrough, trust and confused-deputy risks; draft is explicitly version-sensitive.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Authorization and trust.
- **Retained broad selection notes (lookup only):** Consult the Caller context; least privilege; token audience; no token passthrough sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-authz"></a>

<details>
<summary>authz · Authorization cheat sheet — access, scope and verification</summary>

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · OWASP · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Deny-by-default object authorization and least privilege.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Authorization and trust.
- **Retained broad selection notes (lookup only):** Consult the Caller context; least privilege; token audience; no token passthrough sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Enterprise adapter contracts.
- **Retained broad selection notes (lookup only):** Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

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
- **Retained Level-wide topic association:** Enterprise adapter contracts.
- **Retained broad selection notes (lookup only):** Read HTTPX’s connect/read/write/pool timeouts and Timeout configuration example. Apply them to a narrow enterprise adapter; authorization and adapter schemas remain your design work from L11/L12.

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
- **Retained Level-wide topic association:** Orchestration and observability.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Orchestration and observability. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-otel"></a>

<details>
<summary>otel · Python instrumentation — access, scope and verification</summary>

[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) · OpenTelemetry · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Spans, attributes, context and exporting telemetry.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Orchestration and observability.
- **Retained broad selection notes (lookup only):** Consult the Business workflow versus protocol; tracing; audit; disconnect/reconnect sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Orchestration and observability.
- **Retained broad selection notes (lookup only):** Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Orchestration and observability. Multi-agent implementations are not required.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

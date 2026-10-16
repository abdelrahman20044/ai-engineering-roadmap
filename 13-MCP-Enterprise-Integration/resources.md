# Resource Library · L13 — MCP, Enterprise Integration, and AI Workflows

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** The verified Arabic MCP resource is a translated curriculum with code links. No comparable Egyptian video course was verified; use the Anthropic course plus official SDK examples for implementation.

## Book references

Assigned reading is authoritative in [the master order for L13](../docs/READING_GUIDE.md#l13). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B37 · C10](../docs/READING_GUIDE.md#b37).

**Previously covered / lookup only:** [B35 · C5](../docs/READING_GUIDE.md#b35), [B36b · C6](../docs/READING_GUIDE.md#b36b). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-mcp"></a>

### MCP for Beginners · Arabic course index

[MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md)

- **Resource Type:** Translated curriculum index.
- **Role:** Alternative. **Language:** AR translated curriculum. **By:** Microsoft.
- **Access:** Free.
- **Use for:** MCP architecture and lifecycle; Tools and resources; Client and transport; Authorization and trust.
- **Assigned portion:** From the Arabic index open Introduction, Core Concepts, first Python server/client and Security. No entire curriculum requirement; English protocol docs are authoritative.
- **Scope:** Navigate introduction, core concepts, first server/client, security and hands-on Python material.
- **Limit:** Arabic text with linked multilingual code, not an Arabic video course; cross-check protocol details against the current specification.

<a id="r-ar-agent-trust"></a>

### Trustworthy agents · Arabic

[Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Authorization and trust.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Authorization and trust. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Trust boundaries, human control and reliability.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-mini-14"></a>

### mini-RAG · LLM Factory

[mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Enterprise adapter contracts.
- **Assigned portion:** Only the linked “LLM Factory” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** LLM Factory in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Adapter/factory pattern context; enterprise failure contracts use HTTPX/MCP docs.

<a id="r-ar-agent-production"></a>

### Agents in production · Arabic

[Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Orchestration and observability.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Orchestration and observability. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Evaluation and deployment concerns.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

## English video and guided courses

<a id="r-dla-mcp"></a>

### MCP: Build Rich-Context AI Apps with Anthropic

[MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic)

- **Resource Type:** Short video course + labs.
- **Role:** Alternative. **Language:** EN video + labs. **By:** DeepLearning.AI · Anthropic.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** MCP architecture and lifecycle; Tools and resources; Client and transport; Authorization and trust.
- **Assigned portion:** Select “Creating an MCP Server”, “Creating an MCP Client” and “Adding Prompt and Resource Features”. Remote deployments are optional after local tests.
- **Scope:** Implement MCP servers and clients and inspect tools/resources.
- **Limit:** Course transports or SDK examples may differ from the current protocol.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Official documentation and engineering articles

<a id="r-mcp"></a>

### MCP architecture

[MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** MCP project.
- **Access:** Free.
- **Use for:** MCP architecture and lifecycle.
- **Assigned portion:** Consult the Host; client; server; initialization; capability discovery sections/examples only. Do not read the entire documentation site.
- **Scope:** Host/client/server roles, primitives and lifecycle.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-mcp-server"></a>

### Build an MCP server

[Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** MCP project.
- **Access:** Free.
- **Use for:** Tools and resources.
- **Assigned portion:** Consult the Input/output schemas; resource URIs; errors; prompt templates sections/examples only. Do not read the entire documentation site.
- **Scope:** Python server and tool/resource implementation.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-mcp-sdk"></a>

### MCP Python SDK

[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

- **Resource Type:** Official SDK repository / examples.
- **Role:** Reference. **Language:** EN. **By:** MCP project.
- **Access:** Free.
- **Use for:** Tools and resources; Client and transport; Enterprise adapter contracts; Orchestration and observability.
- **Assigned portion:** Consult the Input/output schemas; resource URIs; errors; prompt templates sections/examples only. Do not read the entire documentation site.
- **Scope:** Runnable SDK examples; pin the SDK and compatible protocol version.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-mcp-client"></a>

### Build an MCP client

[Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** MCP project.
- **Access:** Free.
- **Use for:** Client and transport.
- **Assigned portion:** Consult the stdio first; remote transport when justified; discovery/call; cleanup sections/examples only. Do not read the entire documentation site.
- **Scope:** Connect, discover tools and route requests.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-mcp-security"></a>

### MCP security best practices

[MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** MCP project.
- **Access:** Free.
- **Use for:** Authorization and trust.
- **Assigned portion:** Consult the Caller context; least privilege; token audience; no token passthrough sections/examples only. Do not read the entire documentation site.
- **Scope:** Token passthrough, trust and confused-deputy risks; draft is explicitly version-sensitive.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-authz"></a>

### Authorization cheat sheet

[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** OWASP.
- **Access:** Free.
- **Use for:** Authorization and trust.
- **Assigned portion:** Consult the Caller context; least privilege; token audience; no token passthrough sections/examples only. Do not read the entire documentation site.
- **Scope:** Deny-by-default object authorization and least privilege.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-httpx"></a>

### HTTPX timeouts

[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** HTTPX.
- **Access:** Free.
- **Use for:** Enterprise adapter contracts.
- **Assigned portion:** Read HTTPX’s connect/read/write/pool timeouts and Timeout configuration example. Apply them to a narrow enterprise adapter; authorization and adapter schemas remain your design work from L11/L12.
- **Scope:** Connect/read/write/pool timeouts for provider calls.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-otel"></a>

### Python instrumentation

[Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** OpenTelemetry.
- **Access:** Free.
- **Use for:** Orchestration and observability.
- **Assigned portion:** Consult the Business workflow versus protocol; tracing; audit; disconnect/reconnect sections/examples only. Do not read the entire documentation site.
- **Scope:** Spans, attributes, context and exporting telemetry.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-agents"></a>

### Building effective agents

[Building effective agents](https://www.anthropic.com/research/building-effective-agents)

- **Resource Type:** Engineering article.
- **Role:** Reference. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Orchestration and observability.
- **Assigned portion:** Read the “workflows versus agents” distinction and the pattern/tool-design portion matching Orchestration and observability. Multi-agent implementations are not required.
- **Scope:** Workflow patterns versus autonomous agents and tool interface design.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

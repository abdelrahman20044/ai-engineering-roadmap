# L13 · MCP, Enterprise Integration, and AI Workflows

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 10–16 h | 3/5 | P2 | [L12](../12-Tools-Agents/README.md) |

**Unlocks:** [L16](../16-Capstone-Career/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Understand MCP host/client/server roles, primitives, transport, and authorization. Build one bounded integration with explicit failure behavior. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Tool prerequisites | A typed read-only operation already works without MCP. |
| Security prerequisites | Caller identity and tool/data permissions are explicit. |
| Protocol reasoning | Distinguish app orchestration, transport and model behavior. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] MCP architecture and lifecycle: Diagram one connection and identify the boundary that owns user authorization.
- [ ] Tools and resources: Implement one read-only document search capability with explicit response limits.
- [ ] Client and transport: Run a client-server integration test with pinned versions and deterministic fixtures.
- [ ] Authorization and trust: Test cross-user queries and a tool result containing instruction-like text.
- [ ] Enterprise adapter contracts: Fake an upstream outage and incompatible schema; preserve explicit failure status.
- [ ] Orchestration and observability: Trace one MCP call end-to-end and test shutdown/reconnection without duplicate effects.

## Recommended learning path

Official MCP architecture + Arabic translated index → Python SDK server/client → permission boundary → failure/reconnect tests. Use a single local integration first.

| Pass | Work to do | Stop condition |
| --- | --- | --- |
| 1 · Orient | Use the assigned book/article focus and one Arabic or English explanation for each unfamiliar topic. | Explain the mechanism in your own words. |
| 2 · Implement | Work through the numbered topic outputs below; integrate them into the assessed exercises. | The specified behavior is reproducible in your own code. |
| 3 · Verify | Run the failure cases, self-check and milestone acceptance contract. | Evidence and remaining limitations are recorded. |

The resource library contains alternatives and optional depth. The effort estimate covers a selected path plus implementation, not watching every listed course. Choose Arabic teaching when it speeds understanding, then consult the English API reference for exact behavior.

## What you learn and exactly where

Each numbered row is a learning unit. **Arabic teaching**, **machine-translated Arabic text**, **English videos**, and **English documentation** are labeled separately. A missing verified Arabic resource is stated explicitly; a loosely related video is not presented as full coverage.

| Topic and required subtopics | Arabic route | English route | Build or verify |
| --- | --- | --- | --- |
| **L13-T01 · MCP architecture and lifecycle**<br>Host; client; server; initialization; capability discovery | [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md) (AR translated curriculum) | [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) (EN video + labs) | Diagram one connection and identify the boundary that owns user authorization. |
| **L13-T02 · Tools and resources**<br>Input/output schemas; resource URIs; errors; prompt templates | [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md) (AR translated curriculum) | [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) (EN video + labs) | Implement one read-only document search capability with explicit response limits. |
| **L13-T03 · Client and transport**<br>stdio first; remote transport when justified; discovery/call; cleanup | [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md) (AR translated curriculum) | [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) (EN video + labs) | Run a client-server integration test with pinned versions and deterministic fixtures. |
| **L13-T04 · Authorization and trust**<br>Caller context; least privilege; token audience; no token passthrough | [MCP for Beginners · Arabic course index](https://github.com/microsoft/mcp-for-beginners/blob/main/translations/ar/README.md) (AR translated curriculum)<br>[Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) (AR machine-translated text) | [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) (EN video + labs) | Test cross-user queries and a tool result containing instruction-like text. |
| **L13-T05 · Enterprise adapter contracts**<br>Timeout; retries; schema drift; pagination; safe error handling | [mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) (AR video)<br>**Scope:** Adapter/factory pattern context; enterprise failure contracts use HTTPX/MCP docs. | [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) (EN) | Fake an upstream outage and incompatible schema; preserve explicit failure status. |
| **L13-T06 · Orchestration and observability**<br>Business workflow versus protocol; tracing; audit; disconnect/reconnect | [Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md) (AR machine-translated text) | [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN)<br>[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (EN) | Trace one MCP call end-to-end and test shutdown/reconnection without duplicate effects. |

**Arabic coverage boundary:** The verified Arabic MCP resource is a translated curriculum with code links. No comparable Egyptian video course was verified; use the Anthropic course plus official SDK examples for implementation.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L13-T01 | No sufficient MCP chapter in the books; official docs are primary | [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) (EN) |
| L13-T02 | G5 tool concepts only; do not label it an MCP reference | [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) (EN)<br>[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (EN) |
| L13-T03 | Current protocol/SDK gap resource | [Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client) (EN)<br>[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (EN) |
| L13-T04 | F8/C6 principles; official MCP security details are additional depth | [MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) (EN)<br>[Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN) |
| L13-T05 | C6 tool failure modes; C10 pp.472–473 orchestration | [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) (EN)<br>[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (EN) |
| L13-T06 | C10 pp.472–473; G8 conceptual reference only | [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) (EN)<br>[Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N23 · Model Context Protocol & Enterprise Tool Integration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N24 · AI Workflow Automation & Business Process Integration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L13-E1 | Contrast function calling with an MCP integration diagram. | Identify who manages context and authorization; neither is delegated to the protocol. |
| L13-E2 | Expose get_passage through a local MCP server and call it from one client. | Pin the protocol/SDK version and record successful discovery and invocation. |
| L13-E3 | Test malformed arguments, unauthorized documents, and timeout. | Connection failure does not widen permissions. |
| L13-E4 | Design a reading-summary draft workflow with one simulated save operation. | The application enforces approval, authorization, and duplicate handling for writes; no external message needs to be sent. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| MCP grants permission automatically | Protocol interoperability is separate from authorization. |
| SDK example without version pin | Pin SDK/protocol and document transport compatibility. |
| Remote server output becomes trusted instructions | Validate and scope results; keep business decisions in application code. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Host/client/server?
2. Tools versus resources?
3. Why not add MCP everywhere?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | The host application manages model interaction, the client maintains a server connection, and the server exposes capabilities. |
| 2 | Tools perform callable operations; resources expose addressable context. Neither bypasses permissions. |
| 3 | Use it for interoperable external integrations; direct internal calls can be simpler. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S5](../project/milestones/s5.md) | Small MCP server/client demo and integration diagram; Version record and permission/timeout tests | Demonstrate one real tool invocation through a client and explain where permissions, context, approval, and retries live. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Demonstrate one real tool invocation through a client and explain where permissions, context, approval, and retries live.

## Postpone until justified

- Many MCP servers or invented enterprise integrations
- Production remote authentication before a local protocol demonstration

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L13 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L12](../12-Tools-Agents/README.md) · Next numbered Level: [L14](../14-LLMOps-Deployment/README.md)

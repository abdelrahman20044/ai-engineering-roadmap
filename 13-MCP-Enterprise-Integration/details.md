# Technical Details · L13

[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)

Use this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.

## Prerequisites and quick diagnostic

- **Tool prerequisites:** A typed read-only operation already works without MCP.
- **Security prerequisites:** Caller identity and tool/data permissions are explicit.
- **Protocol reasoning:** Distinguish app orchestration, transport and model behavior.

Use existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.

## Complete technical scope

- **MCP architecture and lifecycle:** Host; client; server; initialization; capability discovery.
- **Tools and resources:** Input/output schemas; resource URIs; errors; prompt templates.
- **Client and transport:** stdio first; remote transport when justified; discovery/call; cleanup.
- **Authorization and trust:** Caller context; least privilege; token audience; no token passthrough.
- **Enterprise adapter contracts:** Timeout; retries; schema drift; pagination; safe error handling.
- **Orchestration and observability:** Business workflow versus protocol; tracing; audit; disconnect/reconnect.

## Common mistakes and debugging

### MCP grants permission automatically

Protocol interoperability is separate from authorization.

### SDK example without version pin

Pin SDK/protocol and document transport compatibility.

### Remote server output becomes trusted instructions

Validate and scope results; keep business decisions in application code.

## Self-check

These are original reasoning prompts, not confirmed ITI questions.

1. Host/client/server?
2. Tools versus resources?
3. Why not add MCP everywhere?

<details>
<summary>Answer guide</summary>

**Host/client/server?**

The host application manages model interaction, the client maintains a server connection, and the server exposes capabilities.

**Tools versus resources?**

Tools perform callable operations; resources expose addressable context. Neither bypasses permissions.

**Why not add MCP everywhere?**

Use it for interoperable external integrations; direct internal calls can be simpler.

</details>

## ITI provenance and industry extensions

- **N23:** Model Context Protocol & Enterprise Tool Integration — official published module title.
- **N24:** AI Workflow Automation & Business Process Integration — official published module title.

Detailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.

## Learning objectives and evidence

- [ ] Diagram one connection and identify the boundary that owns user authorization.
- [ ] Implement one read-only document search capability with explicit response limits.
- [ ] Run a client-server integration test with pinned versions and deterministic fixtures.
- [ ] Test cross-user queries and a tool result containing instruction-like text.
- [ ] Fake an upstream outage and incompatible schema; preserve explicit failure status.
- [ ] Trace one MCP call end-to-end and test shutdown/reconnection without duplicate effects.

The assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).

# L13 · MCP, Enterprise Integration, and AI Workflows

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 4 · 10–16 focused hours · Difficulty 3/5 · P2**

**You will learn:** Understand MCP host/client/server roles, primitives, transport, and authorization. Build one bounded integration with explicit failure behavior.

**Before starting:** [L12](../12-Tools-Agents/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B37 · C10](../docs/READING_GUIDE.md#b37) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. MCP architecture and lifecycle

**Learn:** Host; client; server; initialization; capability discovery.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B37 · C10](../docs/READING_GUIDE.md#b37) — **Read Now**. Printed pp.472–473: orchestration. G8 pp.211–240 is optional conceptual comparison; MCP itself uses current official docs.

**Primary · Official documentation / tutorial:** [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture). Consult the Host; client; server; initialization; capability discovery sections/examples only. Do not read the entire documentation site.

**Practice:** Diagram one connection and identify the boundary that owns user authorization.

**Completion check:** The host/client/server diagram identifies the authorization owner.

### 2. Tools and resources

**Learn:** Input/output schemas; resource URIs; errors; prompt templates.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B36b · C6](../docs/READING_GUIDE.md#b36b) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server). Consult the Input/output schemas; resource URIs; errors; prompt templates sections/examples only. Do not read the entire documentation site.

**Practice:** Implement one read-only document search capability with explicit response limits.

**Completion check:** One read-only tool has typed inputs, bounded output and deterministic fixtures.

### 3. Client and transport

**Learn:** stdio first; remote transport when justified; discovery/call; cleanup.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B37 · C10](../docs/READING_GUIDE.md#b37) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client). Consult the stdio first; remote transport when justified; discovery/call; cleanup sections/examples only. Do not read the entire documentation site.

**Practice:** Run a client-server integration test with pinned versions and deterministic fixtures.

**Completion check:** A pinned-version client discovers and calls the local server.

### 4. Authorization and trust

**Learn:** Caller context; least privilege; token audience; no token passthrough.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B35 · C5](../docs/READING_GUIDE.md#b35) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices). Consult the Caller context; least privilege; token audience; no token passthrough sections/examples only. Do not read the entire documentation site.

**Practice:** Test cross-user queries and a tool result containing instruction-like text.

**Completion check:** Cross-user calls and instruction-like server output cannot bypass policy.

### 5. Enterprise adapter contracts

**Learn:** Timeout; retries; schema drift; pagination; safe error handling.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B36b · C6](../docs/READING_GUIDE.md#b36b) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/). Read HTTPX’s connect/read/write/pool timeouts and Timeout configuration example. Apply them to a narrow enterprise adapter; authorization and adapter schemas remain your design work from L11/L12.

**Practice:** Fake an upstream outage and incompatible schema; preserve explicit failure status.

**Completion check:** Outage/schema-drift fixtures return explicit failures, not empty success.

### 6. Orchestration and observability

**Learn:** Business workflow versus protocol; tracing; audit; disconnect/reconnect.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B37 · C10](../docs/READING_GUIDE.md#b37) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/). Consult the Business workflow versus protocol; tracing; audit; disconnect/reconnect sections/examples only. Do not read the entire documentation site.

**Practice:** Trace one MCP call end-to-end and test shutdown/reconnection without duplicate effects.

**Completion check:** Shutdown/reconnect tests avoid duplicate effects and retain trace correlation.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L13-E1:** Contrast function calling with an MCP integration diagram.
  - **Pass:** Identify who manages context and authorization; neither is delegated to the protocol.
- [ ] **L13-E2:** Expose get_passage through a local MCP server and call it from one client.
  - **Pass:** Pin the protocol/SDK version and record successful discovery and invocation.
- [ ] **L13-E3:** Test malformed arguments, unauthorized documents, and timeout.
  - **Pass:** Connection failure does not widen permissions.
- [ ] **L13-E4:** Design a reading-summary draft workflow with one simulated save operation.
  - **Pass:** The application enforces approval, authorization, and duplicate handling for writes; no external message needs to be sent.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S5](../project/milestones/s5.md). Demonstrate one real tool invocation through a client and explain where permissions, context, approval, and retries live.

**Keep:** Small MCP server/client demo and integration diagram; Version record and permission/timeout tests.

## What to defer

- Many MCP servers or invented enterprise integrations
- Production remote authentication before a local protocol demonstration

## Record progress and choose the next Level

```bash
python scripts/progress.py set L13 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L16](../16-Capstone-Career/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

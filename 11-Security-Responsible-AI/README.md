# L11 · Security, Authorization, and Responsible AI

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 4 · 16–24 focused hours · Difficulty 3/5 · P1**

**You will learn:** Enforce ownership before retrieval, source viewing, history, memory, and job access. Constrain untrusted content, tools, uploads, and consumption.

**Before starting:** [L06](../06-Application-State/README.md), [L08](../08-RAG-Systems/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B33 · F8](../docs/READING_GUIDE.md#b33) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. FastAPI authentication

**Learn:** Hashing; token verification; expiry; dependencies; cookie/header choice.

**Choose resources:** [Unit 01 — topic table and study choices](resources.md#unit-01).

**Required reading:**

- [B33 · F8](../docs/READING_GUIDE.md#b33) — **Read Now**. PDF pp.338–400: FastAPI implementation, dependencies and ownership. Skim JWT/RBAC theory already demonstrated in CRM.

**Primary · Official documentation / tutorial:** [OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/). Consult the Hashing; token verification; expiry; dependencies; cookie/header choice sections/examples only. Do not read the entire documentation site.

**Practice:** Test invalid, expired and missing tokens and define the client session contract.

**Completion check:** Missing/invalid/expired token cases follow the documented contract.

### 2. Object-level authorization

**Learn:** Owner predicates; chunks; sources; messages; memories; jobs.

**Choose resources:** [Unit 02 — topic table and study choices](resources.md#unit-02).

**Required reading:**

- [B33 · F8](../docs/READING_GUIDE.md#b33) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Consult the Owner predicates; chunks; sources; messages; memories; jobs sections/examples only. Do not read the entire documentation site.

**Practice:** Build a two-user access matrix and test direct object reads and indirect retrieval.

**Completion check:** The two-user access matrix passes for retrieval, sources, memory, history and jobs.

### 3. Prompt injection and excessive agency

**Learn:** Malicious documents; tool output instructions; least privilege.

**Choose resources:** [Unit 03 — topic table and study choices](resources.md#unit-03).

**Required reading:**

- [B34 · F9](../docs/READING_GUIDE.md#b34) — **Read Now**. PDF pp.401–428: abuse controls and AI-service security. Cross-check current OWASP guidance.
- [B35 · C5](../docs/READING_GUIDE.md#b35) — **Read Now**. Printed pp.235–250: defensive prompting, prompt attacks and their limits. Earlier prompt basics are review.

**Primary · Official documentation / tutorial:** [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). Consult the Malicious documents; tool output instructions; least privilege sections/examples only. Do not read the entire documentation site.

**Practice:** Place hostile instructions in a PDF fixture and test backend-enforced tool/data restrictions.

**Completion check:** Malicious retrieved instructions cannot bypass tool/data authorization.

### 4. Upload and parser security

**Learn:** Size/type limits; path traversal; storage names; resource limits.

**Choose resources:** [Unit 04 — topic table and study choices](resources.md#unit-04).

**Required reading:**

- [B34 · F9](../docs/READING_GUIDE.md#b34) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html). Consult the Size/type limits; path traversal; storage names; resource limits sections/examples only. Do not read the entire documentation site.

**Practice:** Reject oversized/invalid files and prevent user-supplied path writes.

**Completion check:** Size/type/path manipulation fixtures are rejected.

### 5. Privacy, deletion and observability

**Learn:** Journal sensitivity; consent; redaction; retention; cache/vector cleanup.

**Choose resources:** [Unit 05 — topic table and study choices](resources.md#unit-05).

**Required reading:**

- [B35a · C10](../docs/READING_GUIDE.md#b35a) — **Read Now**. Printed pp.451–455: guardrails and limits. p.450 was B29.

**Primary · Official documentation / tutorial:** [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/). Consult the Journal sensitivity; consent; redaction; retention; cache/vector cleanup sections/examples only. Do not read the entire documentation site.

**Practice:** Delete a document/journal and prove it disappears from retrieval, memory and permitted logs.

**Completion check:** Deleted private content is absent from retrieval, memory and permitted logging paths.

### 6. Responsible answer behavior

**Learn:** Attribution; uncertainty; book claim versus suggestion; feedback/appeal.

**Choose resources:** [Unit 06 — topic table and study choices](resources.md#unit-06).

**Required reading:**

- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B35a · C10](../docs/READING_GUIDE.md#b35a) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Machine-translated lesson / article:** [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md). Only the linked translated lesson, particularly its sections about Responsible answer behavior. Its English video/cloud build is an alternative, not an extra requirement.

**Practice:** Test unsupported advice, conflicting text and correction requests with a documented response rubric.

**Completion check:** The rubric distinguishes source claims, journal facts and generated suggestions.

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L11-E1:** Build an A/B access matrix across every resource endpoint, source viewer, cache, and job state.
  - **Pass:** User B cannot retrieve, read, edit, or delete user A data.
- [ ] **L11-E2:** Index a passage that tries to change instructions or expose another journal.
  - **Pass:** Authorization remains independent of the model and document instructions.
- [ ] **L11-E3:** Set file/page/token/request/tool/retry limits.
  - **Pass:** Oversized requests and abuse have bounded, tested failure behavior.
- [ ] **L11-E4:** Delete a document and its derived data, memory links, and caches.
  - **Pass:** Document active deletion and backup retention separately.
- [ ] **L11-E5:** Threat-model upload/storage/provider/logs/tools and use synthetic journals.
  - **Pass:** No secret or sensitive journal content appears in default logs or browser configuration.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S4](../project/milestones/s4.md). Pass designed isolation tests before public deployment. Passing tests is not proof of universal security; retrieved text does not grant tool privileges.

**Keep:** Threat model, authorization integration tests, and security matrix; Deletion and retention policy.

## What to defer

- System prompts as authorization controls
- Unapproved autonomous write tools

## Record progress and choose the next Level

```bash
python scripts/progress.py set L11 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L12](../12-Tools-Agents/README.md), [L14](../14-LLMOps-Deployment/README.md), [L16](../16-Capstone-Career/README.md), [L18](../18-Supporting-Frontend/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

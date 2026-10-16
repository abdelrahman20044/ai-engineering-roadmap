# L11 · Security, Authorization, and Responsible AI

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 16–24 h | 3/5 | P1 | [L06](../06-Application-State/README.md), [L08](../08-RAG-Systems/README.md) |

**Unlocks:** [L12](../12-Tools-Agents/README.md), [L14](../14-LLMOps-Deployment/README.md), [L16](../16-Capstone-Career/README.md), [L18](../18-Supporting-Frontend/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Enforce ownership before retrieval, source viewing, history, memory, and job access. Constrain untrusted content, tools, uploads, and consumption. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Auth transfer | Explain JWT validation and role versus object permission. |
| RAG readiness | Document retrieval and source display are separate access paths. |
| Job readiness | Job IDs and state can be tied to a caller. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] FastAPI authentication: Test invalid, expired and missing tokens and define the client session contract.
- [ ] Object-level authorization: Build a two-user access matrix and test direct object reads and indirect retrieval.
- [ ] Prompt injection and excessive agency: Place hostile instructions in a PDF fixture and test backend-enforced tool/data restrictions.
- [ ] Upload and parser security: Reject oversized/invalid files and prevent user-supplied path writes.
- [ ] Privacy, deletion and observability: Delete a document/journal and prove it disappears from retrieval, memory and permitted logs.
- [ ] Responsible answer behavior: Test unsupported advice, conflicting text and correction requests with a documented response rubric.

## Recommended learning path

Port your known auth concepts using F8 → test object ownership at every boundary → malicious-document fixtures → upload/rate/privacy controls.

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
| **L11-T01 · FastAPI authentication**<br>Hashing; token verification; expiry; dependencies; cookie/header choice | [Pythonation FastAPI tutorial and companion code](https://github.com/Pythonation/FastAPI_Tutorial) (AR video + code)<br>**Scope:** API introduction only; secure token/cookie implementation uses F8/FastAPI. | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Test invalid, expired and missing tokens and define the client session contract. |
| **L11-T02 · Object-level authorization**<br>Owner predicates; chunks; sources; messages; memories; jobs | [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md) (AR machine-translated text) | [Creating APIs with Python · course index](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/) (EN video) | Build a two-user access matrix and test direct object reads and indirect retrieval. |
| **L11-T03 · Prompt injection and excessive agency**<br>Malicious documents; tool output instructions; least privilege | [Securing AI applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/13-securing-ai-applications/README.md) (AR machine-translated text)<br>[Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) (AR machine-translated text) | [Web LLM attacks learning path](https://portswigger.net/web-security/llm-attacks) (EN hands-on labs) | Place hostile instructions in a PDF fixture and test backend-enforced tool/data restrictions. |
| **L11-T04 · Upload and parser security**<br>Size/type limits; path traversal; storage names; resource limits | [mini-RAG · Uploading a File](https://www.youtube.com/watch?v=5alMKCbFqWs&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=7) (AR video) | [File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) (EN) | Reject oversized/invalid files and prevent user-supplied path writes. |
| **L11-T05 · Privacy, deletion and observability**<br>Journal sensitivity; consent; redaction; retention; cache/vector cleanup | [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN) | Delete a document/journal and prove it disappears from retrieval, memory and permitted logs. |
| **L11-T06 · Responsible answer behavior**<br>Attribution; uncertainty; book claim versus suggestion; feedback/appeal | [AI user experience · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/12-designing-ux-for-ai-applications/README.md) (AR machine-translated text)<br>[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [UX for Language User Interfaces](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/ux-for-luis/) (EN video + slides) | Test unsupported advice, conflicting text and correction requests with a documented response rubric. |

**Arabic coverage boundary:** Arabic translated security material introduces risks. No Arabic hands-on equivalent to the selected LLM security labs was verified; use the English labs for attack/defense practice.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L11-T01 | F8 PDF338–400; skim JWT theory already known | [OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) (EN) |
| L11-T02 | F8 implementation, thorough | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN)<br>[SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) (EN) |
| L11-T03 | C5 pp.235–250; F9 PDF401–428 | [LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (EN)<br>[OWASP GenAI risks](https://genai.owasp.org/llm-top-10/) (EN) |
| L11-T04 | F9 security; parser-specific rules are an industry extension | [File upload cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) (EN) |
| L11-T05 | C10 pp.451–455; F9 | [Authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (EN)<br>[OWASP GenAI risks](https://genai.owasp.org/llm-top-10/) (EN) |
| L11-T06 | C4 task criteria; C10 guardrails | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N07 · RESTful API, Backend Architecture & Security | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N20 · AI Evaluation, Safety & Responsible AI | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N26 · AI Security, Governance & Compliance | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L11-E1 | Build an A/B access matrix across every resource endpoint, source viewer, cache, and job state. | User B cannot retrieve, read, edit, or delete user A data. |
| L11-E2 | Index a passage that tries to change instructions or expose another journal. | Authorization remains independent of the model and document instructions. |
| L11-E3 | Set file/page/token/request/tool/retry limits. | Oversized requests and abuse have bounded, tested failure behavior. |
| L11-E4 | Delete a document and its derived data, memory links, and caches. | Document active deletion and backup retention separately. |
| L11-E5 | Threat-model upload/storage/provider/logs/tools and use synthetic journals. | No secret or sensitive journal content appears in default logs or browser configuration. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Prompt as an access-control system | Permission checks execute in backend code before data/tools are exposed. |
| Sanitize then trust everything | Treat retrieved text/tool output as untrusted throughout execution. |
| Log all prompts for debugging | Redact sensitive fields and define retention/erasure behavior. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Authentication versus authorization?
2. Why indirect prompt injection?
3. What is a safe reflection boundary?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Identity verification versus permission to perform a specific action on a specific object. |
| 2 | A document or tool result can carry instructions even when the user query is benign. |
| 3 | Separate cited book content, personal journal facts and generated suggestions; avoid unsupported clinical claims. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S4](../project/milestones/s4.md) | Threat model, authorization integration tests, and security matrix; Deletion and retention policy | Pass designed isolation tests before public deployment. Passing tests is not proof of universal security; retrieved text does not grant tool privileges. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Pass designed isolation tests before public deployment. Passing tests is not proof of universal security; retrieved text does not grant tool privileges.

## Postpone until justified

- System prompts as authorization controls
- Unapproved autonomous write tools

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L11 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L10](../10-Concurrency-Streaming-Jobs/README.md) · Next numbered Level: [L12](../12-Tools-Agents/README.md)

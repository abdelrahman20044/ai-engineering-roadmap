# Sources and Verification

[Home](../README.md) · [ITI coverage](ITI_COVERAGE.md) · [Reading guide](READING_GUIDE.md)

Sources checked on 15 October 2026. Existing research was reused, with **ITI Native AI Developer as the only official curriculum governing this roadmap**. Module structure, hard prerequisites, personal hours, exercises, and gates are recommendations.

| Primary source | Verification and limitations |
|---|---|
| [ITI Native AI Developer2026/2027](https://rgateway.iti.gov.eg/Resources/Resources/GetResourceFileForPublicUsers?PublicId=5f2565dc-2a2f-4347-8240-eed7e16d7953) | Read all five pages. Page 2 states678 hours/about five months; listed items on pages4–5 sum to696. Discrepancy unresolved. This is an overview brochure, not lecture-level descriptions. |
| G — Andrea De Mauro, Grokking AI Applications, Manning ©2026 | Checked supplied PDF contents, PDF 7–10, and relevant chapter excerpts. Printed page numbers used. |
| F — Alireza Parandeh, Building Generative AI Services with FastAPI, O’Reilly, April 2025 | Checked supplied structure and relevant excerpts. Viewer pages: F2=43, F3=83, F4=153, F5=187, F6=258, F7=302, F8=338, F9=401, F10=429, F11=477, F12=536–594. |
| C — Chip Huyen, AI Engineering: Building Applications with Foundation Models | Checked supplied contents and relevant excerpts. Printed page numbers used; in the supplied body, viewer page is printed page +24. |
| [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),29 September 2025 | Read the article. Timing and project applications are proposed teaching decisions. |

The books were not claimed to have been read cover to cover and are not included in the ZIP. Check pagination if using another edition.

| Official gap resource | Use it when |
|---|---|
| [FastAPI async](https://fastapi.tiangolo.com/async/), [background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/), [tutorial](https://fastapi.tiangolo.com/tutorial/) | M01/M10: framework behavior |
| [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html), [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | M06: lifecycle and migrations |
| [pgvector](https://github.com/pgvector/pgvector) | M07/M08: exact/ANN/filtering/hybrid |
| [scikit-learn pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | M02: preprocessing and leakage |
| [PyTorch tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html), [autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) | M03: tiny CPU lab |
| [Celery tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html) | M10: retry/acknowledgment/idempotency semantics |
| [OWASP Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | M11: threat boundaries |
| [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | M13: current protocol and SDK |
| [React TypeScript](https://react.dev/learn/typescript) | Optional M18 |
| [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | Focused testing reference |

This is a small set of gap references, not a parallel course list. Use each resource to answer a current implementation question.

| Prior project evidence | Scope |
|---|---|
| [CRM](https://github.com/abdelrahman20044/CRM), tree3318e4ac1e2711ec543c88e516ff5311ab5b4f1c | Read package, authorization middleware, validation, auth controller, contact tests, and README. JWT/RBAC, Zod, and Jest/Supertest were observed. No modification or test execution; not a full audit. |

| Claim type | Confidence boundary |
|---|---|
| Official titles/hours | Verified in the brochure; total conflict remains explicit |
| Book assignments | Grounded in supplied contents/excerpts |
| Tools and sequence | Our implementation recommendations, not official ITI tool mandates |
| Current APIs/prices | Recheck documentation at implementation time; no assumed current prices |
| Interviews/jobs | Practice inferences and evidence guidance; no confirmed question bank or hiring guarantee |

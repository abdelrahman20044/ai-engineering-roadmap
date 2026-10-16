# Master Book Reading Order

[Roadmap](../README.md) · [Chapter-to-Level map](CHAPTER_MAP.md) · [Progress](../progress/PROGRESS.md)

**Use this page to decide what to read next.** Follow the numbered queue below with the Level you are working on. Use the chapter map only to find a section or understand a split. An assignment has one first-reading Level; later appearances are review, not new homework.

## Reading status

- **Read Now:** first purposeful reading when you reach the stated Level.
- **Read Later:** any assignment whose Level/prerequisites you have not reached. Do not front-load it.
- **Skim:** read the named ideas selectively; skip familiar setup/theory.
- **Previously Covered / Review Only:** look up a specific uncertainty or apply an earlier section; no restart.
- **Optional Advanced:** outside the core completion path.

G = Andrea De Mauro, *Grokking AI Applications*; F = Alireza Parandeh, *Building Generative AI Services with FastAPI*; C = Chip Huyen, *AI Engineering*. **G/C page numbers are printed pages; F numbers are PDF viewer positions starting at 1.** The supplied PDFs remain the verified source; the files are not redistributed.

## How the original sequence changed

The baseline was G1–4 → F2–5 → G5–6 → F6–7 → C3–4 → F8–12 → C5–6/C10. The selected chapters remain represented, with these practical changes:

1. G1 remains early. Selected C1 planning and C4 evaluation-pipeline orientation move to L00 so the project starts with a scope and evidence contract. Neither entire Chip chapter is a prerequisite to coding.
2. F2/F4 and the pytest slice of F11 move before G2–4 are finished: existing Express experience transfers directly into a small Python API. F3/F5 are split by implementation need rather than read as one block.
3. C3/C4 evaluation comes before retrieval improvements and agents. G4 and C6 retrieval are read when document search is built, not during a long introductory reading phase.
4. F7 persistence precedes F6 streaming because ownership, documents and conversation state support RAG. F5 concurrency is expanded when jobs/streaming make it necessary.
5. Context Engineering and memory precede G5/G6 agent implementation. G5/G6 then follow a working, evaluated RAG service. Fine-tuning and the rest of inference optimization stay optional.
6. F8/F9 security is applied before tool autonomy; F12 deployment and F10 optimization follow measured behavior. C5/C6/C10 sections are introduced once at their practical decision point and reviewed later only as needed.

## Chronological queue

The queue is a sensible default traversal of the prerequisite graph, not a weekly schedule. You can take unlocked branches in a different order; keep the same first-reading/review rules. **Only the first new book use in a Level is a reading task; repeated step references mean reuse.**

<a id="l00"></a>

### L00 · Baseline Assessment and Product Scope

[Open this Level](../00-Orientation/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b01"></a>

1. **B01 · G1 — Peeking inside the black box · Read Now**

   Printed pp.1–22: LLM/application intuition. Read once; L03 reviews it.

   **Purpose:** Start with the accessible introduction from the original plan.

<a id="b02"></a>

2. **B02 · C1 — Introduction · Read Now**

   Printed pp.28–34: Planning AI Applications; pp.35–46: The AI Engineering Stack. Skim history.

   **Purpose:** Adds product scope before implementation, without reading all of C1.

<a id="b03"></a>

3. **B03 · C4 — Evaluate AI Systems · Skim**

   Printed pp.200–207: Design Your Evaluation Pipeline. Preview the workflow; L05 applies it.

   **Purpose:** Define evidence before the demo grows.

<a id="l01"></a>

### L01 · Python, FastAPI, and Service Testing

[Open this Level](../01-Python-FastAPI/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b04"></a>

4. **B04 · F2 — Getting Started with FastAPI · Read Now**

   PDF pp.43–82: server setup, Depends, lifespan and project boundaries. Skim familiar HTTP/framework comparisons.

   **Purpose:** Build a tested endpoint before finishing the conceptual books.

<a id="b05"></a>

5. **B05 · F4 — Implementing Type-Safe AI Services · Read Now**

   PDF pp.153–186: annotations, Annotated, Pydantic constraints/serialization/settings. Skim primitive Python types.

   **Purpose:** Python-specific validation is a genuine transfer gap.

<a id="b06"></a>

6. **B06 · F11 — Testing AI Services · Read Now**

   PDF pp.501–518: unit tests, pytest fixtures/parametrization, async tests and doubles. Other Chapter 11 sections are later assignments.

   **Purpose:** Move only the needed testing portion forward.

<a id="l02"></a>

### L02 · Practical Mathematics, ML, and Data Preparation

[Open this Level](../02-Mathematics-ML/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b07"></a>

7. **B07 · C8 — Dataset Engineering · Skim**

   Printed pp.368–371: data quality. Use as motivation; scikit-learn teaches the actual foundation lab.

   **Purpose:** A short quality lens, not a new data-science curriculum.

<a id="l03"></a>

### L03 · Deep Learning, Foundation Models, and Serving

[Open this Level](../03-Deep-Learning-Foundation-Models/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b08"></a>

8. **B08 · C2 — Understanding Foundation Models · Read Now**

   Printed pp.49–87: model architecture/training orientation; pp.88–105: sampling and structured-output concepts. Avoid research derivations.

   **Purpose:** Understand the model interface and behavior before relying on it.

<a id="b09"></a>

9. **B09 · F3 — AI Integration and Model Serving · Read Now**

   PDF pp.83–105: language-model integration; pp.137–142: serving/lifespan boundaries. Defer other modalities.

   **Purpose:** Separate inference integration from training.

**Previously Covered / Review Only:** [B01](#b01). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l04"></a>

### L04 · Prompt Engineering, Structured Outputs, and LLM Integration

[Open this Level](../04-LLM-Applications-Prompts/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b10"></a>

10. **B10 · G2 — Building your first GenAI app · Read Now**

   Printed pp.42–45: What if we coded it? Skim pp.23–41 only for orientation; no Langflow setup requirement.

   **Purpose:** Preserves the original introduction while avoiding low-code detours.

<a id="b11"></a>

11. **B11 · G3 — Writing the right prompt · Read Now**

   Printed pp.48–56 and 68–72: prompt techniques and their implementation. Skim repeated UI examples.

   **Purpose:** Primary prompt explanation; C5 supplies only missing engineering details.

<a id="b14"></a>

12. **B14 · C5 — Prompt Engineering · Skim**

   Printed pp.218–234: context efficiency, prompt construction/versioning. Skim prompt techniques already learned in B11.

   **Purpose:** First pass includes context basics; L09 revisits pp.218–219 rather than reassigning them.

<a id="b12"></a>

13. **B12 · F3 — AI Integration and Model Serving · Read Now**

   PDF pp.142–147: external serving/API boundary. The overlap page 142 is a section transition, not a chapter restart.

   **Purpose:** Later slice of F3 after its serving concepts in B09.

<a id="b13"></a>

14. **B13 · F5 — Achieving Concurrency in AI Workloads · Read Now**

   PDF pp.211–212: async handler/provider call example. Use current HTTP client docs; full concurrency theory is B31.

   **Purpose:** The provider API example is here; pp.203–208 teach async concepts rather than a separate provider chapter.

**Previously Covered / Review Only:** [B05](#b05), [B08](#b08). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l05"></a>

### L05 · Evaluation Engineering

[Open this Level](../05-Evaluation/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b16"></a>

15. **B16 · C4 — Evaluate AI Systems · Read Now**

   Printed pp.160–178: task criteria and operational criteria. pp.200–207 were previewed in B03; review/apply, do not restart.

   **Purpose:** Model-selection pp.179–200 remain B40.

<a id="b15"></a>

16. **B15 · C3 — Evaluation Methodology · Read Now**

   Printed pp.114–117 and 125–147: challenges, exact measures, similarity and AI judges. Defer entropy derivations.

   **Purpose:** Evaluation moves before agents and retrieval optimization.

<a id="b17"></a>

17. **B17 · F11 — Testing AI Services · Read Now**

   PDF pp.495–500: model-testing challenges; pp.523–528: behavioral tests. Reuse pytest knowledge from B06.

   **Purpose:** Different sections from the first pytest pass; retrieval/E2E are B26/B38.

**Previously Covered / Review Only:** [B03](#b03), [B06](#b06). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l06"></a>

### L06 · PostgreSQL, ORM, and AI Application State

[Open this Level](../06-Application-State/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b18"></a>

18. **B18 · F7 — Integrating Databases into AI Services · Read Now**

   PDF pp.302–337: SQLAlchemy models, engine/session, CRUD, Alembic. Skim DB comparisons, known SQL and Prisma.

   **Purpose:** Persistence precedes RAG and durable state, so F7 comes before F6.

<a id="l07"></a>

### L07 · RAG Document Preparation, Embeddings, and Semantic Search

[Open this Level](../07-Embeddings-Semantic-Search/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b21"></a>

19. **B21 · F5 — Achieving Concurrency in AI Workloads · Read Now**

   PDF pp.219–236: document preparation, upload, extraction, chunking, embeddings and vector storage. Web scraping pp.213–218 is optional.

   **Purpose:** This is the ingestion slice; generation pp.237–239 is B25.

<a id="b22"></a>

20. **B22 · C8 — Dataset Engineering · Skim**

   Printed pp.396–402: processing principles applied to the document corpus. B07 quality is review only.

   **Purpose:** Separate processing from optional training-dataset engineering.

<a id="b19"></a>

21. **B19 · G4 — Augmenting LLMs with your own documents · Read Now**

   Printed pp.74–82: retrieval, embeddings and grounding intuition. The improvement/code slice is B24.

   **Purpose:** Split G4 at the point its techniques become useful.

<a id="b20"></a>

22. **B20 · C6 — RAG and Agents · Read Now**

   Printed pp.253–266: retrieval foundations. No agent/memory reading yet.

   **Purpose:** Retrieval now; agents and memory have distinct later slices.

<a id="b23"></a>

23. **B23 · C3 — Evaluation Methodology · Previously Covered / Review Only**

   Printed pp.125–135: similarity/embedding context already covered in B15. Consult only if cosine/semantic interpretation is unclear.

   **Purpose:** No fresh mandatory chapter assignment.

**Previously Covered / Review Only:** [B07](#b07). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l08"></a>

### L08 · RAG Systems, Citations, and Retrieval Improvement

[Open this Level](../08-RAG-Systems/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b24"></a>

24. **B24 · G4 — Augmenting LLMs with your own documents · Read Now**

   Printed pp.94–100: improvement ideas and code explanation. Do not restart pp.74–82.

   **Purpose:** Completes the selected G4 route.

<a id="b25"></a>

25. **B25 · F5 — Achieving Concurrency in AI Workloads · Read Now**

   PDF pp.237–239: retrieval into generation and the integrated RAG answer flow. Reuse B21 ingestion code.

   **Purpose:** Completes the application slice of F5; no full chapter reread.

<a id="b26"></a>

26. **B26 · F11 — Testing AI Services · Read Now**

   PDF pp.519–522: integration tests, particularly retrieval/vector-database boundaries. Behavioral testing pp.523–528 is B17 review.

   **Purpose:** Precise retrieval slice replaces the old overlapping 519–527 assignment.

<a id="b27"></a>

27. **B27 · C6 — RAG and Agents · Read Now**

   Printed pp.267–274: retrieval improvements and tradeoffs. pp.253–266 are B20 review.

   **Purpose:** Optimization follows a measured baseline.

**Previously Covered / Review Only:** [B15](#b15), [B16](#b16), [B17](#b17), [B19](#b19), [B20](#b20), [B21](#b21). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l09"></a>

### L09 · Context Engineering, Memory, and Conversations

[Open this Level](../09-Context-Memory/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b30"></a>

28. **B30 · C5 — Prompt Engineering · Previously Covered / Review Only**

   Printed pp.218–219: context efficiency from B14; consult while implementing budgets.

   **Purpose:** Not a second first-reading assignment.

<a id="b29"></a>

29. **B29 · C10 — AI Engineering Architecture and User Feedback · Read Now**

   Printed p.450: Enhance Context. Other C10 sections have later owners.

   **Purpose:** Use architecture context alongside the assigned Anthropic article.

<a id="b28"></a>

30. **B28 · C6 — RAG and Agents · Read Now**

   Printed pp.300–304: Memory. Keep agent pp.275–299 for B36.

   **Purpose:** Context/memory comes before agent autonomy.

**Previously Covered / Review Only:** [B14](#b14). Consult only for the current implementation/failure; do not read those chapters again.

**Assigned article:** Anthropic’s [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Read selection/rot/JIT retrieval before budgets, memory/compaction before long-history experiments, and sub-agents only as a decision boundary. L12 reviews the relevant sections.

<a id="l10"></a>

### L10 · Concurrency, Streaming, and Long-Running Jobs

[Open this Level](../10-Concurrency-Streaming-Jobs/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b31"></a>

31. **B31 · F5 — Achieving Concurrency in AI Workloads · Read Now**

   PDF pp.187–210: concurrency/async foundations; pp.253–256: background work/summary. pp.211–212 were B13; pp.240–252 advanced inference is optional in L17.

   **Purpose:** Read the deferred concurrency slice when implementing streaming/jobs.

<a id="b32"></a>

32. **B32 · F6 — Real-Time Communication with Generative Models · Read Now**

   PDF pp.258–269: protocol choice/polling/SSE; pp.278–290: stream/SSE server and client. Skim comparison pp.270–277; WebSocket build pp.291–301 is optional.

   **Purpose:** The actual stream behavior is needed now, after an API/RAG service exists.

**Previously Covered / Review Only:** [B06](#b06), [B13](#b13). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l11"></a>

### L11 · Security, Authorization, and Responsible AI

[Open this Level](../11-Security-Responsible-AI/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b33"></a>

33. **B33 · F8 — Authentication and Authorization · Read Now**

   PDF pp.338–400: FastAPI implementation, dependencies and ownership. Skim JWT/RBAC theory already demonstrated in CRM.

   **Purpose:** Port known backend concepts and verify object boundaries.

<a id="b34"></a>

34. **B34 · F9 — Securing AI Services · Read Now**

   PDF pp.401–428: abuse controls and AI-service security. Cross-check current OWASP guidance.

   **Purpose:** Security is evaluated against a real application.

<a id="b35"></a>

35. **B35 · C5 — Prompt Engineering · Read Now**

   Printed pp.235–250: defensive prompting, prompt attacks and their limits. Earlier prompt basics are review.

   **Purpose:** Security slice of C5, not another complete prompt chapter.

<a id="b35a"></a>

36. **B35a · C10 — AI Engineering Architecture and User Feedback · Read Now**

   Printed pp.451–455: guardrails and limits. p.450 was B29.

   **Purpose:** Separate guardrails from authorization and operating metrics.

**Previously Covered / Review Only:** [B16](#b16). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l12"></a>

### L12 · Tool Calling, Bounded Agents, and Multi-Agent Decisions

[Open this Level](../12-Tools-Agents/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b36"></a>

37. **B36 · G5 — Tools and agents · Read Now**

   Printed pp.102–107 and 122–127: tools, agents and code explanation. Skip repeated travel-app setup.

   **Purpose:** Tools follow RAG, context and security foundations.

<a id="b36a"></a>

38. **B36a · G6 — Implementing agentic structures · Read Now**

   Printed pp.130–132: patterns first. Remaining implementation pp.133–171 is Optional Advanced after a measured need.

   **Purpose:** Learn patterns without requiring a multi-agent build.

<a id="b36b"></a>

39. **B36b · C6 — RAG and Agents · Read Now**

   Printed pp.275–299: tools, planning and agent failure modes. Retrieval/memory slices were B20/B27/B28.

   **Purpose:** Agent slice has one first-reading owner.

**Previously Covered / Review Only:** [B17](#b17), [B28](#b28). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l13"></a>

### L13 · MCP, Enterprise Integration, and AI Workflows

[Open this Level](../13-MCP-Enterprise-Integration/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b37"></a>

40. **B37 · C10 — AI Engineering Architecture and User Feedback · Read Now**

   Printed pp.472–473: orchestration. G8 pp.211–240 is optional conceptual comparison; MCP itself uses current official docs.

   **Purpose:** No book is claimed to be an MCP protocol reference.

**Previously Covered / Review Only:** [B35](#b35), [B36b](#b36b). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l14"></a>

### L14 · MLOps, LLMOps, Architecture, and Deployment

[Open this Level](../14-LLMOps-Deployment/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b39"></a>

41. **B39 · F12 — Deployment of AI Services · Read Now**

   PDF pp.536–594: images, persistence, networks, Compose and deployment. Skim familiar Docker basics.

   **Purpose:** Deploy the tested product rather than an isolated demo.

<a id="b38"></a>

42. **B38 · F11 — Testing AI Services · Read Now**

   PDF pp.529–534: end-to-end test boundaries and vertical/horizontal scenarios. Unit, behavioral and retrieval tests are review.

   **Purpose:** The E2E slice closes the production evidence chain.

<a id="b39a"></a>

43. **B39a · C10 — AI Engineering Architecture and User Feedback · Read Now**

   Printed pp.465–471: monitoring/observability. Orchestration pp.472–473 was B37 and is review only.

   **Purpose:** Avoid overlapping a fresh assignment across L13/L14.

**Previously Covered / Review Only:** [B06](#b06), [B26](#b26), [B37](#b37). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l15"></a>

### L15 · Model Selection, Cost, Latency, and User Feedback

[Open this Level](../15-Model-Selection-Optimization/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b40"></a>

44. **B40 · C4 — Evaluate AI Systems · Read Now**

   Printed pp.179–200: model selection. Cost/latency pp.177–178 are B16 review.

   **Purpose:** Model selection follows evaluation and measurements.

<a id="b42"></a>

45. **B42 · C9 — Inference Optimization · Read Now**

   Printed pp.412–418: performance metrics. Rest of C9 is Optional Advanced in L17.

   **Purpose:** Measure before considering GPU-serving complexity.

<a id="b41"></a>

46. **B41 · F10 — Optimizing AI Services · Read Now**

   PDF pp.429–476: choose caching/performance sections addressing your measured bottleneck; do not implement every technique.

   **Purpose:** Optimization becomes a constrained experiment.

<a id="b43"></a>

47. **B43 · C10 — AI Engineering Architecture and User Feedback · Read Now**

   Printed pp.480–491: feedback design and limitations. Do not restart architecture/observability sections.

   **Purpose:** Feedback belongs after a usable, observable product exists.

**Previously Covered / Review Only:** [B16](#b16), [B39a](#b39a). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l16"></a>

### L16 · Capstone Release, Technical Defense, and Career Evidence

[Open this Level](../16-Capstone-Career/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b44"></a>

48. **B44 · C4 — Evaluate AI Systems · Previously Covered / Review Only**

   Review B03/B16/B40 only for the final release report; no new chapter.

   **Purpose:** Finish evidence and apply, rather than add another reading block.

**Previously Covered / Review Only:** [B02](#b02), [B06](#b06), [B15](#b15), [B16](#b16), [B38](#b38), [B39](#b39), [B43](#b43). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l17"></a>

### L17 · Fine-Tuning, Dataset Engineering, and Advanced Serving

[Open this Level](../17-Fine-Tuning-Advanced-Serving/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b45"></a>

49. **B45 · C7 — Finetuning · Optional Advanced**

   Printed pp.311–318: When to Finetune first; select remaining tactics only for a justified adapter experiment.

   **Purpose:** This Level is outside the core application path.

<a id="b46"></a>

50. **B46 · C8 — Dataset Engineering · Optional Advanced**

   Training-data curation sections within printed pp.363–403 as needed; pp.368–371 and 396–402 are B07/B22 review.

   **Purpose:** No duplicate mandatory processing assignment.

<a id="b47"></a>

51. **B47 · C9 — Inference Optimization · Optional Advanced**

   Selected serving/optimization sections within printed pp.405–447 beyond the B42 metrics slice. F5 PDF240–252 is an optional companion for batching/KV/paged attention.

   **Purpose:** Use only for an identified serving bottleneck.

**Previously Covered / Review Only:** [B07](#b07), [B22](#b22), [B42](#b42). Consult only for the current implementation/failure; do not read those chapters again.

<a id="l18"></a>

### L18 · Supporting TypeScript and React UI

[Open this Level](../18-Supporting-Frontend/README.md). Before reaching it, its new reading is **Read Later**.

<a id="b48"></a>

52. **B48 · F6 — Real-Time Communication with Generative Models · Previously Covered / Review Only**

   Review B32 client/SSE examples PDF pp.281–290; consult F8 for the existing auth contract. No new required book chapter.

   **Purpose:** React/TypeScript needs official tutorials, not invented AI-book coverage.

**Previously Covered / Review Only:** [B33](#b33). Consult only for the current implementation/failure; do not read those chapters again.

## Books you do not need to finish

- **G7:** KNIME/data-ecosystem setup is optional background; it is not a Data Engineering specialization or a core prerequisite.
- **G8:** deployment/orchestration overview is optional at L13/L14; F12 and current MCP docs are the primary implementation references.
- **F1:** optional orientation. F3 other modalities, F5 advanced serving and F6 WebSocket implementation remain deferred unless the product needs them.
- **C1 history, C3 entropy derivations and C7–9 advanced training/serving:** selective or Optional Advanced. Finish the application evidence before expanding them.

The machine-readable source is `reading_plan.json`. Run `python scripts/audit_level_content.py` after changing assignments; it checks first owners, step IDs and generated-document consistency.

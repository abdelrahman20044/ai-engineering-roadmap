# L12 · Tool Calling, Bounded Agents, and Multi-Agent Decisions

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 4 · Production Behavior and Tool Use | 18–28 h | 4/5 | P1 | [L05](../05-Evaluation/README.md), [L09](../09-Context-Memory/README.md), [L11](../11-Security-Responsible-AI/README.md) |

**Unlocks:** [L13](../13-MCP-Enterprise-Integration/README.md), [L16](../16-Capstone-Career/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Distinguish fixed workflows from model-directed tool loops. Implement safe tool contracts and evaluate tool/task failures. Understand sub-agent patterns without assuming they improve the product. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| RAG/security readiness | A caller-scoped search operation exists and rejects unauthorized access. |
| Contract readiness | Validate tool arguments and distinguish error from empty success. |
| Evaluation readiness | Measure task completion and tool behavior separately. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Agent anatomy and design choice: Draw a fixed workflow and tool loop for the same journal question; choose a baseline.
- [ ] Tool design and schemas: Expose one owner-scoped search tool; reject malformed and unauthorized arguments.
- [ ] Bounded execution loop: Test repeated calls, unavailable tools, budget exhaustion and terminal behavior.
- [ ] Agent evaluation: Label five correct and five failed traces; report tool and task metrics separately.
- [ ] Memory and context interfaces: Limit tool result size and prove relevant evidence survives the bound.
- [ ] Multi-agent comparison: Run one partitioned experiment against the single-agent baseline; record a go/no-go ADR.

## Recommended learning path

G5 tool concepts → Anthropic workflow patterns → one read-only tool → bounded loop → trajectory evaluation. Keep multi-agent work conditional.

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
| **L12-T01 · Agent anatomy and design choice**<br>State; model decision; action; observation; workflow alternatives | [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) (AR machine-translated text) | [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) (EN course + videos + exercises) | Draw a fixed workflow and tool loop for the same journal question; choose a baseline. |
| **L12-T02 · Tool design and schemas**<br>Small names; typed inputs; concise outputs; errors; idempotent reads | [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) (AR machine-translated text)<br>[mini-RAG · LLM Factory](https://www.youtube.com/watch?v=5TKRIFtIQAY) (AR video) | [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) (EN course + videos + exercises) | Expose one owner-scoped search tool; reject malformed and unauthorized arguments. |
| **L12-T03 · Bounded execution loop**<br>Max steps; timeout; token/cost budget; stop/ask-human; error states | [Trustworthy agents · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/06-building-trustworthy-agents/README.md) (AR machine-translated text) | [Agents course · Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction) (EN course + videos + exercises)<br>[asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN) | Test repeated calls, unavailable tools, budget exhaustion and terminal behavior. |
| **L12-T04 · Agent evaluation**<br>Tool choice; arguments; trajectory; task success; final-answer grounding | [Agents in production · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/10-ai-agents-production/README.md) (AR machine-translated text) | [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) (EN video + labs) | Label five correct and five failed traces; report tool and task metrics separately. |
| **L12-T05 · Memory and context interfaces**<br>Retrieve only needed state; observation size; provenance; side-effect confirmation | [Agent memory · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/13-agent-memory/README.md) (AR machine-translated text)<br>[Context engineering · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/12-context-engineering/README.md) (AR machine-translated text) | [Context Engineering for AI Agents · lesson](https://youtu.be/F5zqRV7gEag) (EN video)<br>[Managing Agentic Memory · lesson](https://youtu.be/QrYbHesIxpw) (EN video) | Limit tool result size and prove relevant evidence survives the bound. |
| **L12-T06 · Multi-agent comparison**<br>Specialist role; independent context; handoff summary; coordination failures | [Agent use cases · Arabic](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/ar/01-intro-to-ai-agents/README.md) (AR machine-translated text) | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN) | Run one partitioned experiment against the single-agent baseline; record a go/no-go ADR. |

**Arabic coverage boundary:** Arabic translated agent lessons provide structured text. A complete Arabic course covering bounded loops plus trajectory evaluation was not verified; pair them with the English agent course and assessment labs.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L12-T01 | G5 pp.102–107 and 122–127; G6 pp.130–132 | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN) |
| L12-T02 | C6 pp.275–299; Anthropic tool design | [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling) (EN)<br>[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) (EN) |
| L12-T03 | C6 agent planning/failure modes | [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) (EN)<br>[Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN) |
| L12-T04 | F11 behavioral testing; C6 failure modes | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L12-T05 | C6 pp.300–304 review; Anthropic JIT selection | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |
| L12-T06 | G6 patterns; Anthropic sub-agents, optional implementation | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (EN)<br>[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N20 · AI Evaluation, Safety & Responsible AI | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N22 · Agentic AI & Multi-Agent Orchestration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N24 · AI Workflow Automation & Business Process Integration | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L12-E1 | Define read-only search_passages and get_passage tools with bounded outputs. | Validate schemas and enforce authenticated ownership; no generic SQL or shell tool. |
| L12-E2 | Build a small direct-SDK loop with max steps, timeout, and token budget. | Handle unknown tool, invalid arguments, no-tool-needed, and repeated-loop cases. |
| L12-E3 | Compare a fixed workflow and agent on fifteen tasks. | Report success, tool errors, unauthorized attempts, latency, and cost. |
| L12-E4 | Use lightweight references and fetch passages just in time. | Only permitted requested content is loaded; compare against upfront retrieval. |
| L12-E5 | Design a planner/worker experiment and a summary contract. | Implement extra agents only if a measured use case justifies isolation, coordination, and cost. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| Every problem needs an agent | Compare with deterministic routing/workflows first. |
| Tool execution trusts model arguments | Validate schema and permission for every call, independent of model compliance. |
| Unbounded self-correction | Enforce steps, wall time and token/cost budgets in code. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. Workflow versus agent?
2. What is a trajectory failure?
3. When add sub-agents?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | The workflow fixes control flow in code; the agent chooses next actions within enforced limits. |
| 2 | An invalid/unnecessary/repeated tool sequence even if the final prose looks plausible. |
| 3 | A separable task and a measured improvement justify coordination, isolation and extra cost. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S5](../project/milestones/s5.md) | Tool contracts, bounded agent loop, and evaluation report; Single-agent versus multi-agent ADR | A model request is never treated as authorization. Loops stop predictably and you can justify either using an agent or retaining a fixed workflow. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

A model request is never treated as authorization. Loops stop predictably and you can justify either using an agent or retaining a fixed workflow.

## Postpone until justified

- Framework orchestration before understanding a loop
- Multi-agent implementation just to check a syllabus keyword

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L12 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L11](../11-Security-Responsible-AI/README.md) · Next numbered Level: [L13](../13-MCP-Enterprise-Integration/README.md)

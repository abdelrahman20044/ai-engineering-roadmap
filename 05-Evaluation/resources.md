# Resource Library · L05 — Evaluation Engineering

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Arabic lifecycle material provides orientation. A complete Arabic course covering judge calibration, retrieval metrics and release-gate statistics was not verified; use C3/C4 and the English evaluation labs for those parts.

## Topic navigation

1. [Task criteria and failure taxonomy](#unit-01)
2. [Evaluation dataset design](#unit-02)
3. [Deterministic component checks](#unit-03)
4. [Human review and AI judges](#unit-04)
5. [Retrieval versus answer metrics](#unit-05)
6. [Regression gates and uncertainty](#unit-06)

<a id="unit-01"></a>

## 1. Task criteria and failure taxonomy

[Return to README Step 1](README.md#1-task-criteria-and-failure-taxonomy)

**Topic/subtopics:** Correctness; groundedness; abstention; privacy; severity.

**Required sequence:** the assigned book slice [B16 · C4](../docs/READING_GUIDE.md#b16). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-task-criteria-and-failure-taxonomy) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B16 · C4](../docs/READING_GUIDE.md#b16)<br>Chip Huyen · EN | Book Section | Primary | Task criteria and failure taxonomy | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b16) |
| `ar-gen-lifecycle` · [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation, versioning and operational stages. | Only the linked translated lesson: Evaluation, versioning and operational… [bounds](#unit-01-ar-gen-lifecycle) |
| `ar-gen-responsible` · [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Fairness, reliability and accountable use. | Only the linked translated lesson: Fairness, reliability and accountable… [bounds](#unit-01-ar-gen-responsible) |
| `fsdl-ops` · [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Complementary (as needed) | Evaluation, production behavior and operational iteration. | Topic bounds; lesson IDs not verified — [details](#unit-01-fsdl-ops) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-01-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-gen-lifecycle"></a>

**`ar-gen-lifecycle` — selected portion:** Only the linked translated lesson: Evaluation, versioning and operational stages. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-ar-gen-responsible"></a>

**`ar-gen-responsible` — selected portion:** Only the linked translated lesson: Fairness, reliability and accountable use. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-fsdl-ops"></a>

**`fsdl-ops` — selected portion:** Only the linked lesson on Evaluation, production behavior and operational iteration. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-02"></a>

## 2. Evaluation dataset design

[Return to README Step 2](README.md#2-evaluation-dataset-design)

**Topic/subtopics:** Question strata; reference evidence; train/dev/holdout; versions.

**Required sequence:** review only [B03 · C4](../docs/READING_GUIDE.md#b03) for this task. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `ragas`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-evaluation-dataset-design) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B03 · C4](../docs/READING_GUIDE.md#b03)<br>Chip Huyen · EN | Book Section | Primary | Evaluation dataset design | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b03) |
| [B16 · C4](../docs/READING_GUIDE.md#b16)<br>Chip Huyen · EN | Book Section | Reference | Evaluation dataset design | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b16) |
| `ar-gen-lifecycle` · [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Evaluation, versioning and operational stages. | Only the linked translated lesson: Evaluation, versioning and operational… [bounds](#unit-02-ar-gen-lifecycle) |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt… [bounds](#unit-02-dla-rag) |
| `ragas` · [Ragas evaluation documentation](https://docs.ragas.io/en/stable/)<br>Ragas · EN | Documentation / evaluation tutorials | Reference | Reference/context/answer metrics and experiment workflow;… | Consult the relevant example for Reference/context/answer metrics and… [bounds](#unit-02-ragas) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-ar-gen-lifecycle"></a>

**`ar-gen-lifecycle` — selected portion:** Only the linked translated lesson: Evaluation, versioning and operational stages. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-dla-rag"></a>

**`dla-rag` — selected portion:** RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt metrics to your own rubric.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-ragas"></a>

**`ragas` — selected portion:** Consult the relevant example for Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. Deterministic component checks

[Return to README Step 3](README.md#3-deterministic-component-checks)

**Topic/subtopics:** JSON schema; source IDs; ownership; parser contracts; golden fixtures.

**Required sequence (default route):** the assigned book slice [B15 · C3](../docs/READING_GUIDE.md#b15) **THEN** `pytest`. Stop each source at the stated portion.

**Choose ONE explanation for pytest fixtures/assertion basics:** default `pytest` **OR** `cs50-tests`. Apply them to the Level-specific component failures; the course is not a RAG evaluation tutorial. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-deterministic-component-checks) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B06 · F11](../docs/READING_GUIDE.md#b06)<br>Alireza Parandeh · EN | Book Section | Reference | Deterministic component checks | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b06) |
| [B15 · C3](../docs/READING_GUIDE.md#b15)<br>Chip Huyen · EN | Book Section | Complementary | Deterministic component checks | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b15) |
| `pytest` · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)<br>pytest · EN | Documentation / tutorial | Primary | Fixtures, scope, teardown and dependency isolation. | Read pytest’s fixtures introduction, fixture scope and teardown sections.… [bounds](#unit-03-pytest) |
| `cs50-tests` · [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)<br>Harvard · David Malan · EN video + problem sets | Course unit: lecture + problem set | Alternative | pytest, assertions and test-driven reasoning; do the… | Consult the relevant example for pytest, assertions and test-driven… [bounds](#unit-03-cs50-tests) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-03-promptfoo) |
| `prompt-lab` · [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)<br>Anthropic · EN | Interactive tutorial / notebook exercises | Complementary (as needed) | Exercises with expected behaviors for prompts and… | Consult the relevant example for Exercises with expected behaviors for… [bounds](#unit-03-prompt-lab) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-pytest"></a>

**`pytest` — selected portion:** Read pytest’s fixtures introduction, fixture scope and teardown sections. Reuse L01 tests; design deterministic component assertions for your own failure cases.

**Relationship:** Default selected route for this topic.

<a id="unit-03-cs50-tests"></a>

**`cs50-tests` — selected portion:** Consult the relevant example for pytest, assertions and test-driven reasoning; do the associated exercises. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Substitute only for pytest fixtures/assertion basics. Apply them to the Level-specific component failures; the course is not a RAG evaluation tutorial.

<a id="unit-03-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-03-prompt-lab"></a>

**`prompt-lab` — selected portion:** Consult the relevant example for Exercises with expected behaviors for prompts and formatting. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

</details>

<a id="unit-04"></a>

## 4. Human review and AI judges

[Return to README Step 4](README.md#4-human-review-and-ai-judges)

**Topic/subtopics:** Rubric anchors; blind labels; disagreement; bias; judge prompts.

**Required sequence:** the assigned book slice [B17 · F11](../docs/READING_GUIDE.md#b17) **THEN** review only [B15 · C3](../docs/READING_GUIDE.md#b15) for this task. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `ragas`, `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-human-review-and-ai-judges) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B15 · C3](../docs/READING_GUIDE.md#b15)<br>Chip Huyen · EN | Book Section | Primary | Human review and AI judges | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b15) |
| [B17 · F11](../docs/READING_GUIDE.md#b17)<br>Alireza Parandeh · EN | Book Section | Complementary | Human review and AI judges | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b17) |
| `dla-eval` · [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)<br>DeepLearning.AI · Arize AI · EN video + labs | Short Course + labs | Complementary (as needed) | Trace, router, skill and trajectory evaluation. | Improving your LLM-as-a-judge for judge design; the judge section only;… [bounds](#unit-04-dla-eval) |
| `ragas` · [Ragas evaluation documentation](https://docs.ragas.io/en/stable/)<br>Ragas · EN | Documentation / evaluation tutorials | Reference | Reference/context/answer metrics and experiment workflow;… | Consult the relevant example for Reference/context/answer metrics and… [bounds](#unit-04-ragas) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-04-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-dla-eval"></a>

**`dla-eval` — selected portion:** Improving your LLM-as-a-judge for judge design; the judge section only; agent router/trajectory labs wait for L12.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-ragas"></a>

**`ragas` — selected portion:** Consult the relevant example for Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-04-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Retrieval versus answer metrics

[Return to README Step 5](README.md#5-retrieval-versus-answer-metrics)

**Topic/subtopics:** Recall@k; MRR; faithfulness; answer relevance; no-evidence behavior.

**Required sequence:** `st-eval`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `ragas`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-retrieval-versus-answer-metrics) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B15 · C3](../docs/READING_GUIDE.md#b15)<br>Chip Huyen · EN | Book Section | Reference | Retrieval versus answer metrics | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b15) |
| [B16 · C4](../docs/READING_GUIDE.md#b16)<br>Chip Huyen · EN | Book Section | Reference | Retrieval versus answer metrics | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b16) |
| `st-eval` · [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html)<br>Sentence Transformers · EN | Documentation / tutorial | Primary | MRR, NDCG, accuracy, precision/recall and MAP; select the… | InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and… [bounds](#unit-05-st-eval) |
| `ar-gen-rag` · [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Retrieval architecture and grounding. | Only the linked translated lesson: Retrieval architecture and grounding.… [bounds](#unit-05-ar-gen-rag) |
| `dla-rag` · [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)<br>DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks | Short Course + notebooks | Complementary (as needed) | Advanced retrieval and structured evaluation experiments. | RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt… [bounds](#unit-05-dla-rag) |
| `ragas` · [Ragas evaluation documentation](https://docs.ragas.io/en/stable/)<br>Ragas · EN | Documentation / evaluation tutorials | Reference | Reference/context/answer metrics and experiment workflow;… | Consult the relevant example for Reference/context/answer metrics and… [bounds](#unit-05-ragas) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-st-eval"></a>

**`st-eval` — selected portion:** InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-gen-rag"></a>

**`ar-gen-rag` — selected portion:** Only the linked translated lesson: Retrieval architecture and grounding. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: RAG orientation only; ranking formulas and judge calibration use the English sources.

<a id="unit-05-dla-rag"></a>

**`dla-rag` — selected portion:** RAG Triad of metrics lesson. Use its retrieval/answer distinction; adapt metrics to your own rubric.

**Relationship:** Different or partially overlapping concepts; as-needed support, not a substitute for the required route.

<a id="unit-05-ragas"></a>

**`ragas` — selected portion:** Consult the relevant example for Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Regression gates and uncertainty

[Return to README Step 6](README.md#6-regression-gates-and-uncertainty)

**Topic/subtopics:** Counts; confidence caveats; stochastic repeats; release decision.

**Required sequence:** `ci`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `promptfoo`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-regression-gates-and-uncertainty) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B03 · C4](../docs/READING_GUIDE.md#b03)<br>Chip Huyen · EN | Book Section | Reference | Regression gates and uncertainty | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b03) |
| [B17 · F11](../docs/READING_GUIDE.md#b17)<br>Alireza Parandeh · EN | Book Section | Reference | Regression gates and uncertainty | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b17) |
| `ci` · [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)<br>GitHub · EN | Documentation / tutorial | Primary | Dependency install, test jobs and retained artifacts. | Consult the Counts; confidence caveats; stochastic repeats; release… [bounds](#unit-06-ci) |
| `cs50-tests` · [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)<br>Harvard · David Malan · EN video + problem sets | Course unit: lecture + problem set | Complementary (as needed) | pytest, assertions and test-driven reasoning; do the… | Consult the relevant example for pytest, assertions and test-driven… [bounds](#unit-06-cs50-tests) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Reference | Deterministic checks, model judges and eval assertions. | Consult the relevant example for Deterministic checks, model judges and… [bounds](#unit-06-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-ci"></a>

**`ci` — selected portion:** Consult the Counts; confidence caveats; stochastic repeats; release decision sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-cs50-tests"></a>

**`cs50-tests` — selected portion:** Consult the relevant example for pytest, assertions and test-driven reasoning; do the associated exercises. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-06-promptfoo"></a>

**`promptfoo` — selected portion:** Consult the relevant example for Deterministic checks, model judges and eval assertions. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-gen-lifecycle"></a>

<details>
<summary>ar-gen-lifecycle · Generative AI lifecycle · Arabic — access, scope and verification</summary>

[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Evaluation, versioning and operational stages.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Task criteria and failure taxonomy; Evaluation dataset design.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Task criteria and failure taxonomy. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-ar-gen-responsible"></a>

<details>
<summary>ar-gen-responsible · Responsible generative AI · Arabic — access, scope and verification</summary>

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Fairness, reliability and accountable use.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Task criteria and failure taxonomy.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Task criteria and failure taxonomy. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-fsdl-ops"></a>

<details>
<summary>fsdl-ops · LLMOps — access, scope and verification</summary>

[LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Evaluation, production behavior and operational iteration.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Task criteria and failure taxonomy.
- **Retained broad selection notes (lookup only):** Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Task criteria and failure taxonomy. Exact timestamps are not assigned.

</details>

<a id="r-promptfoo"></a>

<details>
<summary>promptfoo · Assertions and metrics — access, scope and verification</summary>

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) · Promptfoo · EN

- **Resource Type:** Documentation: assertions reference.
- **Access:** Free.
- **Catalog scope:** Deterministic checks, model judges and eval assertions.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Task criteria and failure taxonomy; Deterministic component checks; Human review and AI judges; Regression gates and uncertainty.
- **Retained broad selection notes (lookup only):** The assertion type matching Task criteria and failure taxonomy; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

</details>

<a id="r-dla-rag"></a>

<details>
<summary>dla-rag · Building and Evaluating Advanced RAG — access, scope and verification</summary>

[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) · DeepLearning.AI · LlamaIndex/TruEra · EN video + notebooks

- **Resource Type:** Short Course + notebooks.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Catalog scope:** Advanced retrieval and structured evaluation experiments.
- **Scope/version limits:** Framework-specific lab; reimplement one comparison using your existing retrieval interface.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Evaluation dataset design; Retrieval versus answer metrics.
- **Retained broad selection notes (lookup only):** “RAG Triad of Metrics” and the evaluation portions of “Advanced RAG Pipeline”. Advanced retrieval builds are Read Later in L08.

</details>

<a id="r-ragas"></a>

<details>
<summary>ragas · Ragas evaluation documentation — access, scope and verification</summary>

[Ragas evaluation documentation](https://docs.ragas.io/en/stable/) · Ragas · EN

- **Resource Type:** Documentation / evaluation tutorials.
- **Access:** Free.
- **Catalog scope:** Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Evaluation dataset design; Human review and AI judges; Retrieval versus answer metrics.
- **Retained broad selection notes (lookup only):** Consult the Question strata; reference evidence; train/dev/holdout; versions sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-cs50-tests"></a>

<details>
<summary>cs50-tests · CS50P · Unit Tests — access, scope and verification</summary>

[CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) · Harvard · David Malan · EN video + problem sets

- **Resource Type:** Course unit: lecture + problem set.
- **Access:** Free.
- **Catalog scope:** pytest, assertions and test-driven reasoning; do the associated exercises.
- **Scope/version limits:** Skip unrelated beginner lectures.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Deterministic component checks; Regression gates and uncertainty.
- **Retained broad selection notes (lookup only):** Week 5 assert/pytest material is review only; no second lecture assignment.

</details>

<a id="r-pytest"></a>

<details>
<summary>pytest · pytest fixtures — access, scope and verification</summary>

[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · pytest · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Fixtures, scope, teardown and dependency isolation.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Deterministic component checks.
- **Retained broad selection notes (lookup only):** Read pytest’s fixtures introduction, fixture scope and teardown sections. Reuse L01 tests; design deterministic component assertions for your own failure cases.

</details>

<a id="r-dla-eval"></a>

<details>
<summary>dla-eval · Evaluating AI Agents — access, scope and verification</summary>

[Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) · DeepLearning.AI · Arize AI · EN video + labs

- **Resource Type:** Short Course + labs.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Catalog scope:** Trace, router, skill and trajectory evaluation.
- **Scope/version limits:** Use after a bounded agent exists; simpler output evals come first.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Human review and AI judges.
- **Retained broad selection notes (lookup only):** “Improving your LLM-as-a-judge” only if judge calibration remains unclear. Agent-building and trajectory labs are Read Later in L12.

</details>

<a id="r-ar-gen-rag"></a>

<details>
<summary>ar-gen-rag · RAG and vector databases · Arabic — access, scope and verification</summary>

[RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Retrieval architecture and grounding.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Retrieval versus answer metrics.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Retrieval versus answer metrics. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-st-eval"></a>

<details>
<summary>st-eval · InformationRetrievalEvaluator — access, scope and verification</summary>

[InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) · Sentence Transformers · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Retrieval versus answer metrics.
- **Retained broad selection notes (lookup only):** InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.

</details>

<a id="r-ci"></a>

<details>
<summary>ci · Build and test Python in GitHub Actions — access, scope and verification</summary>

[Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) · GitHub · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Dependency install, test jobs and retained artifacts.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Regression gates and uncertainty.
- **Retained broad selection notes (lookup only):** Consult the Counts; confidence caveats; stochastic repeats; release decision sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-prompt-lab"></a>

<details>
<summary>prompt-lab · Interactive prompt engineering tutorial — access, scope and verification</summary>

[Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) · Anthropic · EN

- **Resource Type:** Interactive tutorial / notebook exercises.
- **Access:** Free.
- **Catalog scope:** Exercises with expected behaviors for prompts and formatting.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Consult the Exercises with expected behaviors for prompts and formatting. sections/examples only. Do not read the entire documentation site.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

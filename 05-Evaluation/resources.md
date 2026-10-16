# Resource Library · L05 — Evaluation Engineering

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** Arabic lifecycle material provides orientation. A complete Arabic course covering judge calibration, retrieval metrics and release-gate statistics was not verified; use C3/C4 and the English evaluation labs for those parts.

## Book references

Assigned reading is authoritative in [the master order for L05](../docs/READING_GUIDE.md#l05). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B16 · C4](../docs/READING_GUIDE.md#b16), [B15 · C3](../docs/READING_GUIDE.md#b15), [B17 · F11](../docs/READING_GUIDE.md#b17).

**Previously covered / lookup only:** [B03 · C4](../docs/READING_GUIDE.md#b03), [B06 · F11](../docs/READING_GUIDE.md#b06). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-gen-lifecycle"></a>

### Generative AI lifecycle · Arabic

[Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Task criteria and failure taxonomy; Evaluation dataset design.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Task criteria and failure taxonomy. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Evaluation, versioning and operational stages.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-responsible"></a>

### Responsible generative AI · Arabic

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Task criteria and failure taxonomy.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Task criteria and failure taxonomy. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Fairness, reliability and accountable use.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-rag"></a>

### RAG and vector databases · Arabic

[RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Retrieval versus answer metrics.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Retrieval versus answer metrics. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Retrieval architecture and grounding.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

**Arabic scope note:** RAG orientation only; ranking formulas and judge calibration use the English sources.

## English video and guided courses

<a id="r-fsdl-ops"></a>

### LLMOps

[LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)

- **Resource Type:** Single lecture video + slides.
- **Role:** Alternative. **Language:** EN video + slides. **By:** Full Stack Deep Learning.
- **Access:** Free.
- **Use for:** Task criteria and failure taxonomy.
- **Assigned portion:** Only the linked “LLMOps” lecture; not the complete LLM Bootcamp. Use the parts relevant to Task criteria and failure taxonomy. Exact timestamps are not assigned.
- **Scope:** Evaluation, production behavior and operational iteration.
- **Limit:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.

<a id="r-dla-rag"></a>

### Building and Evaluating Advanced RAG

[Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)

- **Resource Type:** Short video course + notebooks.
- **Role:** Alternative. **Language:** EN video + notebooks. **By:** DeepLearning.AI · LlamaIndex/TruEra.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** Evaluation dataset design; Retrieval versus answer metrics.
- **Assigned portion:** “RAG Triad of Metrics” and the evaluation portions of “Advanced RAG Pipeline”. Advanced retrieval builds are Read Later in L08.
- **Scope:** Advanced retrieval and structured evaluation experiments.
- **Limit:** Framework-specific lab; reimplement one comparison using your existing retrieval interface.

<a id="r-cs50-tests"></a>

### CS50P · Unit Tests

[CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/)

- **Resource Type:** Course unit: lecture + problem set.
- **Role:** Alternative. **Language:** EN video + problem sets. **By:** Harvard · David Malan.
- **Access:** Free.
- **Use for:** Deterministic component checks; Regression gates and uncertainty.
- **Assigned portion:** Week 5 assert/pytest material is review only; no second lecture assignment.
- **Scope:** pytest, assertions and test-driven reasoning; do the associated exercises.
- **Limit:** Skip unrelated beginner lectures.

<a id="r-dla-eval"></a>

### Evaluating AI Agents

[Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)

- **Resource Type:** Short video course + labs.
- **Role:** Alternative. **Language:** EN video + labs. **By:** DeepLearning.AI · Arize AI.
- **Access:** Limited-time free access advertised; account/terms may change.
- **Use for:** Human review and AI judges.
- **Assigned portion:** “Improving your LLM-as-a-judge” only if judge calibration remains unclear. Agent-building and trajectory labs are Read Later in L12.
- **Scope:** Trace, router, skill and trajectory evaluation.
- **Limit:** Use after a bounded agent exists; simpler output evals come first.

## Slides, notebooks and repositories

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

<a id="r-prompt-lab"></a>

### Interactive prompt engineering tutorial

[Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)

- **Resource Type:** Interactive tutorial / notebook exercises.
- **Role:** Alternative. **Language:** EN. **By:** Anthropic.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Consult the Exercises with expected behaviors for prompts and formatting. sections/examples only. Do not read the entire documentation site.
- **Scope:** Exercises with expected behaviors for prompts and formatting.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Official documentation and engineering articles

<a id="r-promptfoo"></a>

### Assertions and metrics

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

- **Resource Type:** Documentation: assertions reference.
- **Role:** Reference. **Language:** EN. **By:** Promptfoo.
- **Access:** Free.
- **Use for:** Task criteria and failure taxonomy; Deterministic component checks; Human review and AI judges; Regression gates and uncertainty.
- **Assigned portion:** The assertion type matching Task criteria and failure taxonomy; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.
- **Scope:** Deterministic checks, model judges and eval assertions.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ragas"></a>

### Ragas evaluation documentation

[Ragas evaluation documentation](https://docs.ragas.io/en/stable/)

- **Resource Type:** Documentation / evaluation tutorials.
- **Role:** Reference. **Language:** EN. **By:** Ragas.
- **Access:** Free.
- **Use for:** Evaluation dataset design; Human review and AI judges; Retrieval versus answer metrics.
- **Assigned portion:** Consult the Question strata; reference evidence; train/dev/holdout; versions sections/examples only. Do not read the entire documentation site.
- **Scope:** Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-pytest"></a>

### pytest fixtures

[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** pytest.
- **Access:** Free.
- **Use for:** Deterministic component checks.
- **Assigned portion:** Read pytest’s fixtures introduction, fixture scope and teardown sections. Reuse L01 tests; design deterministic component assertions for your own failure cases.
- **Scope:** Fixtures, scope, teardown and dependency isolation.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-st-eval"></a>

### InformationRetrievalEvaluator

[InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Sentence Transformers.
- **Access:** Free.
- **Use for:** Retrieval versus answer metrics.
- **Assigned portion:** InformationRetrievalEvaluator section: Recall@k, MRR/NDCG and relevance-label inputs. Other evaluator classes are reference only.
- **Scope:** MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ci"></a>

### Build and test Python in GitHub Actions

[Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** GitHub.
- **Access:** Free.
- **Use for:** Regression gates and uncertainty.
- **Assigned portion:** Consult the Counts; confidence caveats; stochastic repeats; release decision sections/examples only. Do not read the entire documentation site.
- **Scope:** Dependency install, test jobs and retained artifacts.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

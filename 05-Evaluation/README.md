# L05 · Evaluation Engineering

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Focused effort | Difficulty | Priority | Required before starting |
| --- | --- | --- | --- | --- |
| 2 · Reliable LLM Application Basics | 14–22 h | 3/5 | P0 | [L04](../04-LLM-Applications-Prompts/README.md) |

**Unlocks:** [L08](../08-RAG-Systems/README.md), [L12](../12-Tools-Agents/README.md), [L15](../15-Model-Selection-Optimization/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[Start path](#recommended-learning-path) · [Topics](#what-you-learn-and-exactly-where) · [Books](#book-and-article-focus-by-topic) · [Practice](#practical-exercises) · [Completion gate](#completion-criteria)

## Why this Level matters

Define datasets and rubrics before expanding the application. Distinguish deterministic tests, component evaluation, and end-to-end quality. The output contributes to the same Book-Grounded Reflection Assistant; build the implementation yourself in a separate application repository.

## Prerequisites and quick diagnostic

| Check | Demonstrate before starting |
| --- | --- |
| Working endpoint | Run the same request repeatedly and capture output/config. |
| Test separation | Distinguish HTTP correctness from answer usefulness. |
| Dataset hygiene | Keep development examples apart from release holdout. |

Use existing CRM work as evidence where applicable. If a check fails, use the targeted remedial resource; a full beginner course is unnecessary when you can demonstrate the skill.

## Learning objectives

- [ ] Task criteria and failure taxonomy: Write a rubric with anchored pass/fail examples and name five failure classes.
- [ ] Evaluation dataset design: Version development cases and a separate holdout with source labels.
- [ ] Deterministic component checks: Add exact checks that catch a valid-looking answer with an invalid citation.
- [ ] Human review and AI judges: Label a small sample twice and compare judge/human disagreements by category.
- [ ] Retrieval versus answer metrics: Report retrieval and generation failures as separate tables.
- [ ] Regression gates and uncertainty: Run a fixed eval suite and retain model/prompt/corpus versions with the results.

## Recommended learning path

C4 evaluation pipeline → handwritten cases/rubric → deterministic checks → small human calibration sample → judge experiment. Evaluate before agent complexity.

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
| **L05-T01 · Task criteria and failure taxonomy**<br>Correctness; groundedness; abstention; privacy; severity | [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text)<br>[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) (AR machine-translated text) | [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) (EN video + slides) | Write a rubric with anchored pass/fail examples and name five failure classes. |
| **L05-T02 · Evaluation dataset design**<br>Question strata; reference evidence; train/dev/holdout; versions | [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) (AR machine-translated text) | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Version development cases and a separate holdout with source labels. |
| **L05-T03 · Deterministic component checks**<br>JSON schema; source IDs; ownership; parser contracts; golden fixtures | **Arabic gap:** no directly matching resource verified; use the English route. | [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) (EN video + problem sets) | Add exact checks that catch a valid-looking answer with an invalid citation. |
| **L05-T04 · Human review and AI judges**<br>Rubric anchors; blind labels; disagreement; bias; judge prompts | **Arabic gap:** no directly matching resource verified; use the English route. | [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) (EN video + labs) | Label a small sample twice and compare judge/human disagreements by category. |
| **L05-T05 · Retrieval versus answer metrics**<br>Recall@k; MRR; faithfulness; answer relevance; no-evidence behavior | [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) (AR machine-translated text)<br>**Scope:** RAG orientation only; ranking formulas and judge calibration use the English sources. | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (EN video + notebooks) | Report retrieval and generation failures as separate tables. |
| **L05-T06 · Regression gates and uncertainty**<br>Counts; confidence caveats; stochastic repeats; release decision | **Arabic gap:** no directly matching resource verified; use the English route. | [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) (EN video + problem sets) | Run a fixed eval suite and retain model/prompt/corpus versions with the results. |

**Arabic coverage boundary:** Arabic lifecycle material provides orientation. A complete Arabic course covering judge calibration, retrieval metrics and release-gate statistics was not verified; use C3/C4 and the English evaluation labs for those parts.

## Book and article focus by topic

| Topic | Verified reading focus | Implementation reference |
| --- | --- | --- |
| L05-T01 | C4 pp.160–178 and 200–207, primary | [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L05-T02 | C3 pp.114–117; C4 pp.200–207 | [Ragas evaluation documentation](https://docs.ragas.io/en/stable/) (EN) |
| L05-T03 | C3 pp.125–135; F11 PDF495–533 selective | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) (EN)<br>[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L05-T04 | C3 pp.136–147, read thoroughly | [Ragas evaluation documentation](https://docs.ragas.io/en/stable/) (EN)<br>[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |
| L05-T05 | C4 component criteria; C6 retrieval preview | [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) (EN)<br>[Ragas evaluation documentation](https://docs.ragas.io/en/stable/) (EN) |
| L05-T06 | C3 pp.114–117; C4 pipeline | [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) (EN)<br>[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) (EN) |

G = *Grokking AI Applications*; F = *Building Generative AI Services with FastAPI*; C = Chip Huyen’s *AI Engineering*. G/C use printed pages; F uses PDF viewer pages. See [exact chapter titles and page conventions](../docs/READING_GUIDE.md). A topic marked as a gap is covered by the named additional resource, not an invented book chapter.

## ITI syllabus and industry additions

| Official ITI module | Coverage boundary |
| --- | --- |
| N05 · Software Testing & Full-Stack Debugging | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |
| N20 · AI Evaluation, Safety & Responsible AI | Official published title. The detailed topic decomposition and project tasks on this page are roadmap recommendations. |

The ITI brochure provides module titles and descriptions, not a specification for every library below. Specific tools, bilingual resources, tests, completion gates, prerequisites and personal learning hours are **industry/self-study additions**. The [coverage matrix](../docs/ITI_COVERAGE.md) preserves the official syllabus separately.

## Practical exercises

The topic outputs are small checkpoints that feed these assessed exercises. Combine them where appropriate rather than creating a separate project for each row.

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L05-E1 | Use the twelve public seed cases for practice and author thirty development cases. | Include answerable, no-answer, multi-evidence, language, and security categories; review labels manually. |
| L05-E2 | Create a separate holdout before tuning; label document/page/spans. | Do not call supplied examples unseen; preserve labels when chunk IDs change. |
| L05-E3 | Write 0–2 rubrics for correctness, groundedness, and relevance. | Calibrate a model judge against human review and document disagreements. |
| L05-E4 | Define an evaluation run manifest. | Record dataset/model/prompt/corpus versions, case count, latency, and cost or usage. |
| L05-E5 | Specify retrieval and tool metrics before those components are built. | Implement retrieval metrics in L08 and tool/task metrics in L12; do not claim these experiments are already complete. |

Use [the evidence template](../templates/EVIDENCE.md) for code/tests and [the experiment template](../templates/EXPERIMENT.md) for comparisons. The external lab choices are in [Practice and quizzes](resources.md#6--practice-labs-and-quizzes).

## Common mistakes and debugging guidance

| Failure pattern | Correction |
| --- | --- |
| One combined RAG score | Measure retrieval, citations, generation and system behavior separately. |
| Judge treated as ground truth | Compare human/judge disagreement and inspect bias and failure modes. |
| Threshold invented after results | State intended thresholds before comparing candidates; report sample counts and uncertainty. |

## Self-check before moving on

Answer without looking at the resources, then inspect the guide below. These are original practice prompts, not confirmed ITI interview questions.

1. What belongs in a holdout?
2. Why calibrate an AI judge?
3. What is an actionable eval failure?

<details>
<summary>Answer guide and reasoning checks</summary>

| Question | Expected reasoning |
| --- | --- |
| 1 | Cases not used to tune prompts, retrieval settings or model selection. |
| 2 | A judge can favor style, verbosity or a model family and miss real task failures. |
| 3 | A labeled failure tied to a reproducible case and an identifiable component or product requirement. |

</details>

## Capstone checkpoint

| Milestone | Artifacts | Acceptance contract |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | Authored evaluation data, rubric, and run manifest; A report showing real failures as well as successes | Explain what success means and why. Public seed data is not holdout, mocks do not assess model quality, and judges are not the sole source of truth. |

## Completion criteria

- [ ] Each topic output has been implemented, measured or explicitly explained.
- [ ] Assessed exercises pass their listed failure cases, not only the happy path.
- [ ] You can answer the self-check and explain one design choice without AI.
- [ ] The milestone evidence includes reproducible commands/configuration and remaining limitations.

Explain what success means and why. Public seed data is not holdout, mocks do not assess model quality, and judges are not the sole source of truth.

## Postpone until justified

- An elaborate evaluation platform before useful labels
- Repeated tuning against the final holdout

## Record completion

Run from the roadmap root:

```bash
python scripts/progress.py set L05 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks dependency/evidence fields; it cannot assess engineering skill automatically.

[← Roadmap](../README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L04](../04-LLM-Applications-Prompts/README.md) · Next numbered Level: [L06](../06-Application-State/README.md)

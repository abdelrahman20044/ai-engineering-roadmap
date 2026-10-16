# Resource Library · L05 — Evaluation Engineering

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

C4 evaluation pipeline → handwritten cases/rubric → deterministic checks → small human calibration sample → judge experiment. Evaluate before agent complexity.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Arabic lifecycle material provides orientation. A complete Arabic course covering judge calibration, retrieval metrics and release-gate statistics was not verified; use C3/C4 and the English evaluation labs for those parts.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Generative AI lifecycle · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/14-the-generative-ai-application-lifecycle/README.md) | Microsoft<br>AR machine-translated text<br>Free | L05-T01 · Task criteria and failure taxonomy; L05-T02 · Evaluation dataset design | Evaluation, versioning and operational stages. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) | Microsoft<br>AR machine-translated text<br>Free | L05-T01 · Task criteria and failure taxonomy | Fairness, reliability and accountable use. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [RAG and vector databases · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/15-rag-and-vector-databases/README.md) | Microsoft<br>AR machine-translated text<br>Free | L05-T05 · Retrieval versus answer metrics | Retrieval architecture and grounding. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L05-T01 · Task criteria and failure taxonomy | Evaluation, production behavior and operational iteration. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |
| [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | DeepLearning.AI · LlamaIndex/TruEra<br>EN video + notebooks<br>Limited-time free access advertised; account/terms may change | L05-T02 · Evaluation dataset design; L05-T05 · Retrieval versus answer metrics | Advanced retrieval and structured evaluation experiments. **Boundary:** Framework-specific lab; reimplement one comparison using your existing retrieval interface. |
| [CS50P · Unit Tests](https://cs50.harvard.edu/python/weeks/5/) | Harvard · David Malan<br>EN video + problem sets<br>Free | L05-T03 · Deterministic component checks; L05-T06 · Regression gates and uncertainty | pytest, assertions and test-driven reasoning; do the associated exercises. **Boundary:** Skip unrelated beginner lectures. |
| [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) | DeepLearning.AI · Arize AI<br>EN video + labs<br>Limited-time free access advertised; account/terms may change | L05-T04 · Human review and AI judges | Trace, router, skill and trajectory evaluation. **Boundary:** Use after a bounded agent exists; simpler output evals come first. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| C4 pp.200–207: Design Your Evaluation Pipeline; introduce during L00 and implement here. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C3 pp.114–117 and 125–147: challenges, exact evaluation, AI judges, and limitations. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C4 pp.160–178: criteria; F11 PDF495–533: model testing and retrieval/behavioral evaluation. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic<br>EN<br>Free | Optional support for this Level’s assessed exercises | Exercises with expected behaviors for prompts and formatting. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L05-T01 | Write a rubric with anchored pass/fail examples and name five failure classes. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L05-T02 | Version development cases and a separate holdout with source labels. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L05-T03 | Add exact checks that catch a valid-looking answer with an invalid citation. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L05-T04 | Label a small sample twice and compare judge/human disagreements by category. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L05-T05 | Report retrieval and generation failures as separate tables. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L05-T06 | Run a fixed eval suite and retain model/prompt/corpus versions with the results. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L05-T01 · Task criteria and failure taxonomy; L05-T03 · Deterministic component checks; L05-T04 · Human review and AI judges; L05-T06 · Regression gates and uncertainty | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ragas evaluation documentation](https://docs.ragas.io/en/stable/) | Ragas<br>EN<br>Free | L05-T02 · Evaluation dataset design; L05-T04 · Human review and AI judges; L05-T05 · Retrieval versus answer metrics | Reference/context/answer metrics and experiment workflow; metric definitions matter more than framework adoption. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | pytest<br>EN<br>Free | L05-T03 · Deterministic component checks | Fixtures, scope, teardown and dependency isolation. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [InformationRetrievalEvaluator](https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html) | Sentence Transformers<br>EN<br>Free | L05-T05 · Retrieval versus answer metrics | MRR, NDCG, accuracy, precision/recall and MAP; select the IR evaluator section. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Build and test Python in GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | GitHub<br>EN<br>Free | L05-T06 · Regression gates and uncertainty | Dependency install, test jobs and retained artifacts. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

No separate advanced reading is required. Use the Level postpone list and complete the practical gate first.

## How to choose and stop

| Situation | Action |
| --- | --- |
| Already comfortable from backend work | Demonstrate the diagnostic, skim repeated theory and build the Python-specific behavior. |
| Arabic introduction helps | Use it first, then verify English API names and error behavior in the official reference. |
| Two sources cover the same thing | Finish one explanation, attempt the exercise, and use the second only for the unresolved part. |
| Tutorial differs from your version | Check current docs, pin dependencies and record the adjustment in an ADR. |
| Everything in the completion gate passes | Record the evidence and move to an unlocked Level; bonus reading stays optional. |

**Verification:** resource pages and author/publisher indexes were checked on 2026-10-16. Reachability, title/scope evidence and verification limits are recorded in [the audit](../docs/RESOURCE_AUDIT.md); the inspectable catalog stores each topic assignment. No claim is made that every video was watched end-to-end or that paid enrollment was tested.

[← Level roadmap](README.md) · [Progress tracker](../progress/PROGRESS.md)

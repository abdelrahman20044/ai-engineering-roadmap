# Resource Library · L17 — Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

Optional: C7 go/no-go → curated train/dev/holdout data → one small LoRA experiment → compare to baseline → serve only if justified.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Arabic translated fine-tuning material supplies concepts. No complete Arabic course on the specific PEFT/SFT/versioned-serving workflow was verified; current Hugging Face/vLLM resources are primary for the experiment.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md) | Microsoft<br>AR machine-translated text<br>Free | L17-T01 · Fine-tuning decision; L17-T02 · Dataset engineering; L17-T03 · PEFT and SFT | When adaptation helps and the training/evaluation boundary. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md) | Microsoft<br>AR machine-translated text<br>Free | L17-T02 · Dataset engineering | Fairness, reliability and accountable use. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L17-T05 · Quantization and inference; L17-T06 · Model-serving boundary | Ollama Local LLM Server in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |
| [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L17-T06 · Model-serving boundary | App Deployments 1/2 in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Hugging Face<br>EN course + videos + quizzes<br>Free | L17-T01 · Fine-tuning decision; L17-T02 · Dataset engineering; L17-T05 · Quantization and inference | Transformer families, tokenization and using pretrained models. **Boundary:** Read targeted sections; training an LLM is optional. |
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Andrej Karpathy<br>EN video + notebooks<br>Free | L17-T03 · PEFT and SFT | Micrograd for gradients; the GPT lecture for attention and language modelling. **Boundary:** Full course is optional depth; do not build a full GPT before RAG. |

Course pages may require an account for notebooks. Limited-time free promotions are labeled rather than promised permanently. Older teaching is retained for concepts; current documentation takes precedence for code.

## 3 · Slides, notebooks and course repositories

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Zero to Hero notebooks](https://github.com/karpathy/nn-zero-to-hero) | Andrej Karpathy<br>EN / Python<br>Free | Optional support for this Level’s assessed exercises | Run a small gradient or tokenization experiment and inspect the notebook. **Boundary:** GPU training and every notebook are not required. |

## 4 · Paid alternatives

No purchase is recommended for this Level. The owned books and free route are sufficient; spend on a specific gap only after attempting the lab.

## 5 · Your three books and assigned article

| Assignment | Depth and purpose |
| --- | --- |
| C7 When to Finetune pp.311–318 first; selected PEFT/tactics only for the chosen experiment. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C8 curation/processing and C9 optimization when relevant. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F5 batching and paged attention as later serving references. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L17-T01 | Write a go/no-go ADR with the failure cases and cheaper alternatives already tested. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L17-T02 | Create a small data card, split-by-source policy and duplicate/leakage checks. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L17-T03 | Run one bounded small-model adapter experiment and save configuration and provenance. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L17-T04 | Compare tuned/untuned models on an independent set and report negative outcomes too. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L17-T05 | Benchmark memory/latency/quality before and after one compatible optimization. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L17-T06 | Serve the chosen artifact separately and prove a rollback to the baseline model. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [PEFT quicktour](https://huggingface.co/docs/peft/quicktour) | Hugging Face<br>EN<br>Free | L17-T01 · Fine-tuning decision; L17-T03 · PEFT and SFT | Adapter training, saving and loading. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) | Hugging Face<br>EN<br>Free | L17-T02 · Dataset engineering; L17-T03 · PEFT and SFT | Supervised instruction tuning and dataset formats. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo<br>EN<br>Free | L17-T04 · Holdout and regression evaluation | Deterministic checks, model judges and eval assertions. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [bitsandbytes quantization](https://huggingface.co/docs/transformers/quantization/bitsandbytes) | Hugging Face<br>EN<br>Free | L17-T05 · Quantization and inference | Memory/quality tradeoffs and compatible hardware. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) | vLLM<br>EN<br>Free | L17-T05 · Quantization and inference; L17-T06 · Model-serving boundary | Separate model serving and OpenAI-compatible endpoints; optional GPU path. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ollama API introduction](https://docs.ollama.com/api/introduction) | Ollama<br>EN<br>Free | L17-T06 · Model-serving boundary | Local inference endpoint contracts; local operation uses your hardware. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

## 8 · Optional advanced reading

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [LoRA paper](https://arxiv.org/abs/2106.09685) | Hu et al.<br>EN research paper<br>Free | Optional support for this Level’s assessed exercises | Low-rank adaptation motivation and constraints. **Boundary:** Optional after implementing a small adapter experiment. |

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

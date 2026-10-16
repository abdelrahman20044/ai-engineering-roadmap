# Resource Library · L03 — Deep Learning, Foundation Models, and Serving

[← Level roadmap](README.md) · [All Levels](../README.md) · [Book locator](../docs/READING_GUIDE.md) · [Verification policy](../docs/RESOURCE_POLICY.md)

This is a curated library of **alternatives**, implementation references and optional depth. Start with the selected path; do not complete the entire list. Free explanations and local exercises cover the Level without buying a new course. Model API calls, hosted labs, optional GPUs and owned books can have separate costs.

## Start here

G1 + C2 conceptual sections → visual attention/backpropagation → a tiny CPU PyTorch lab and one inference endpoint. Train no large model here.

| Use | Selection rule |
| --- | --- |
| Primary explanation | Use the assigned book/article plus one unfamiliar-topic explanation. Arabic and English routes are alternatives. |
| Authoritative implementation | Consult the exact official section for the API/version you use. |
| Evidence | Complete the Level exercises and retain test output, measured cases and decisions. |
| Optional resources | Use only for a diagnosed gap or a justified advanced experiment. |

## 1 · Arabic and Egyptian learning materials

Use the exact lesson/topic indicated below. Egyptian instructors are identified where verified. Translated Arabic text is supplementary and is not described as an Arabic video course.

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) | Hesham Asem · Egypt<br>AR video<br>Free | L03-T01 · Tensors and neural network structure; L03-T02 · Backpropagation and optimization; L03-T03 · Language-model foundations; L03-T05 · Attention and transformer intuition | Layers, activations and learning intuition. **Boundary:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization. |
| [Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md) | Microsoft<br>AR machine-translated text<br>Free | L03-T03 · Language-model foundations | Application versus foundation model and basic capabilities. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) | Microsoft<br>AR machine-translated text<br>Free | L03-T04 · Tokens, context and sampling | Conversation state and token/context constraints. **Boundary:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives. |
| [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) | Abu Bakr Soliman · Egypt<br>AR video<br>Free | L03-T06 · Training versus model serving | Ollama Local LLM Server in a working RAG backend. **Boundary:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs. |

## 2 · English video courses and guided teaching

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) | Grant Sanderson · 3Blue1Brown<br>EN video<br>Free | L03-T01 · Tensors and neural network structure; L03-T05 · Attention and transformer intuition | Neural-network and backpropagation intuition; select transformer/attention explanations when ready. **Boundary:** Pair visualization with the tiny PyTorch lab. |
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Andrej Karpathy<br>EN video + notebooks<br>Free | L03-T02 · Backpropagation and optimization; L03-T05 · Attention and transformer intuition | Micrograd for gradients; the GPT lecture for attention and language modelling. **Boundary:** Full course is optional depth; do not build a full GPT before RAG. |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Hugging Face<br>EN course + videos + quizzes<br>Free | L03-T03 · Language-model foundations; L03-T04 · Tokens, context and sampling; L03-T05 · Attention and transformer intuition | Transformer families, tokenization and using pretrained models. **Boundary:** Read targeted sections; training an LLM is optional. |
| [LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/) | Full Stack Deep Learning<br>EN video + slides<br>Free | L03-T06 · Training versus model serving | Language-model capabilities and application boundaries. **Boundary:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices. |

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
| G1, printed pp.1–22: conceptual reading; skim material already understood. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| C2 pp.49–111: skim architecture/post-training; focus on sampling and structured outputs, pp.88–105. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| F3 PDF83–105 for language models and PDF136–150 for serving strategies; defer multimodal examples. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |
| PyTorch Tensors and Autograd quickstarts: one tiny CPU lab. | Read the named focus; retain explicit skim/defer instructions. Topic-level book mappings are in the Level README. |

G: Andrea De Mauro; F: Alireza Parandeh; C: Chip Huyen. Chapter titles and editions were checked in the supplied PDFs; no book files are redistributed. For this Level, use [the topic-to-chapter table](README.md#book-and-article-focus-by-topic) to avoid duplicate reading. Read F for implementation, G for first exposure and C for tradeoffs/evaluation. Where the books do not teach a topic, the additional source is explicit.

## 6 · Practice, labs and quizzes

No separate external resource is added in this category. Use the direct official tutorial/lab and the original exercises below; no claim of external grading is made.

### Practice and evidence

| Checkpoint | Independent task | Evidence |
| --- | --- | --- |
| L03-T01 | Run a small forward pass and assert each intermediate shape. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L03-T02 | Check a scalar derivative manually and train a small CPU network for a few steps. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L03-T03 | Explain where knowledge, instruction behavior and application context enter the system. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L03-T04 | Measure token counts for Arabic/English prompts and compare two sampling settings. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L03-T05 | Explain attention using a short sentence and trace tensor dimensions conceptually. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |
| L03-T06 | Call one local or hosted inference endpoint behind an adapter and record the resource boundary. | Code/test, a small measured comparison, or a reasoned ADR; tie it to an assessed exercise in the Level page. |

Local exercises and the Level self-check are self-assessed. External platforms may provide automated checks, quizzes or hosted labs; the resource row says which. A quiz score is not a substitute for the capstone acceptance tests.

## 7 · Official documentation and engineering references

| Resource | Provider · language · access | Specific topic mapping | Use it for / do not overuse it for |
| --- | --- | --- | --- |
| [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) | PyTorch<br>EN<br>Free | L03-T01 · Tensors and neural network structure | Shapes, dtype, device and tensor operations. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) | PyTorch<br>EN<br>Free | L03-T02 · Backpropagation and optimization | Gradients, backward and computational graphs. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | PyTorch<br>EN<br>Free | L03-T02 · Backpropagation and optimization | Loss, optimizer, training and evaluation loops. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) | Hugging Face<br>EN<br>Free | L03-T03 · Language-model foundations; L03-T04 · Tokens, context and sampling | Subword tokenization and language-dependent token counts. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |
| [Ollama API introduction](https://docs.ollama.com/api/introduction) | Ollama<br>EN<br>Free | L03-T04 · Tokens, context and sampling; L03-T06 · Training versus model serving | Local inference endpoint contracts; local operation uses your hardware. **Boundary:** Consult the named section and validate library versions; not a requirement to read the entire documentation. |

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

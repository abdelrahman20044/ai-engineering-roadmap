# Resource Library · L03 — Deep Learning, Foundation Models, and Serving

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

## Book references

Assigned reading is authoritative in [the master order for L03](../docs/READING_GUIDE.md#l03). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B08 · C2](../docs/READING_GUIDE.md#b08), [B09 · F3](../docs/READING_GUIDE.md#b09).

**Previously covered / lookup only:** [B01 · G1](../docs/READING_GUIDE.md#b01). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-nn"></a>

### Art of Machine Learning · Neural networks

[Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa)

- **Resource Type:** YouTube playlist.
- **Role:** Alternative. **Language:** AR video. **By:** Hesham Asem · Egypt.
- **Access:** Free.
- **Use for:** Tensors and neural network structure; Backpropagation and optimization; Language-model foundations; Attention and transformer intuition.
- **Assigned portion:** Layers, activations and learning intuition; exact lesson numbers not verified. Transformer attention is not claimed as coverage.
- **Scope:** Layers, activations and learning intuition.
- **Limit:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.

**Arabic scope note:** Neural-network prerequisites only; no verified Arabic attention lesson is assigned.

<a id="r-ar-gen-intro"></a>

### Introduction to generative AI · Arabic

[Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Language-model foundations.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Language-model foundations. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Application versus foundation model and basic capabilities.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-chat"></a>

### Chat applications · Arabic

[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Tokens, context and sampling.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Tokens, context and sampling. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Conversation state and token/context constraints.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-mini-19"></a>

### mini-RAG · Ollama Local LLM Server

[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Primary. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Training versus model serving.
- **Assigned portion:** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Ollama Local LLM Server in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

## English video and guided courses

<a id="r-nn-visual"></a>

### Neural networks visual series

[Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks)

- **Resource Type:** Video series / lesson collection.
- **Role:** Primary. **Language:** EN video. **By:** Grant Sanderson · 3Blue1Brown.
- **Access:** Free.
- **Use for:** Tensors and neural network structure; Attention and transformer intuition.
- **Assigned portion:** Only “Attention in transformers, step-by-step”. The general series is an optional alternative, not an assignment to watch every lesson.
- **Scope:** Neural-network and backpropagation intuition; select transformer/attention explanations when ready.
- **Limit:** Pair visualization with the tiny PyTorch lab.

**Direct lesson choices:** [What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation/) · [Gradient descent, how neural networks learn](https://www.3blue1brown.com/lessons/gradient-descent/) · [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention/). These are alternatives; follow only the chosen topic.

<a id="r-zerohero"></a>

### Neural Networks: Zero to Hero

[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)

- **Resource Type:** Multi-hour video course / lecture index.
- **Role:** Optional Advanced. **Language:** EN video + notebooks. **By:** Andrej Karpathy.
- **Access:** Free.
- **Use for:** Backpropagation and optimization; Attention and transformer intuition.
- **Assigned portion:** Lecture “The spelled-out intro to neural networks and backpropagation: building micrograd” as optional deeper practice; GPT lecture only if attention remains unclear.
- **Scope:** Micrograd for gradients; the GPT lecture for attention and language modelling.
- **Limit:** Full course is optional depth; do not build a full GPT before RAG.

<a id="r-hf-llm"></a>

### Hugging Face LLM course

[Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)

- **Resource Type:** Full course: text, videos and quizzes.
- **Role:** Primary. **Language:** EN course + videos + quizzes. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Language-model foundations; Tokens, context and sampling; Attention and transformer intuition.
- **Assigned portion:** Chapter 1: Transformer families, how Transformers work, inference and bias/limitations. Tokenizers are the separate chapter-6 reference.
- **Scope:** Transformer families, tokenization and using pretrained models.
- **Limit:** Read targeted sections; training an LLM is optional.

<a id="r-fsdl-foundation"></a>

### LLM Foundations

[LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/)

- **Resource Type:** Single lecture video + slides.
- **Role:** Alternative. **Language:** EN video + slides. **By:** Full Stack Deep Learning.
- **Access:** Free.
- **Use for:** Training versus model serving.
- **Assigned portion:** Only the linked “LLM Foundations” lecture; not the complete LLM Bootcamp. Use the parts relevant to Training versus model serving. Exact timestamps are not assigned.
- **Scope:** Language-model capabilities and application boundaries.
- **Limit:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.

## Slides, notebooks and repositories

<a id="r-zerohero-code"></a>

### Zero to Hero notebooks

[Zero to Hero notebooks](https://github.com/karpathy/nn-zero-to-hero)

- **Resource Type:** Course notebooks / code repository.
- **Role:** Optional Advanced. **Language:** EN / Python. **By:** Andrej Karpathy.
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Run a small gradient or tokenization experiment and inspect the notebook. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Run a small gradient or tokenization experiment and inspect the notebook.
- **Limit:** GPU training and every notebook are not required.

## Paid alternatives

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice, labs and quizzes

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Official documentation and engineering articles

<a id="r-pytorch"></a>

### Tensors

[Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** PyTorch.
- **Access:** Free.
- **Use for:** Tensors and neural network structure.
- **Assigned portion:** Consult the Layers; activations; shapes; device; dtype sections/examples only. Do not read the entire documentation site.
- **Scope:** Shapes, dtype, device and tensor operations.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-autograd"></a>

### Autograd

[Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** PyTorch.
- **Access:** Free.
- **Use for:** Backpropagation and optimization.
- **Assigned portion:** Consult the Autograd; computational graph; gradients; train versus eval sections/examples only. Do not read the entire documentation site.
- **Scope:** Gradients, backward and computational graphs.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-optimize"></a>

### Optimization loop

[Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** PyTorch.
- **Access:** Free.
- **Use for:** Backpropagation and optimization.
- **Assigned portion:** Consult the Autograd; computational graph; gradients; train versus eval sections/examples only. Do not read the entire documentation site.
- **Scope:** Loss, optimizer, training and evaluation loops.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-hf-token"></a>

### Tokenizers

[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Language-model foundations; Tokens, context and sampling.
- **Assigned portion:** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.
- **Scope:** Subword tokenization and language-dependent token counts.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ollama"></a>

### Ollama API introduction

[Ollama API introduction](https://docs.ollama.com/api/introduction)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Ollama.
- **Access:** Free.
- **Use for:** Tokens, context and sampling; Training versus model serving.
- **Assigned portion:** Consult the Tokenizer; context limit; output length; temperature; top-p sections/examples only. Do not read the entire documentation site.
- **Scope:** Local inference endpoint contracts; local operation uses your hardware.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

No separate purchase/material is required in this category. The retained primary path is sufficient; use the other categories only for a specific gap.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

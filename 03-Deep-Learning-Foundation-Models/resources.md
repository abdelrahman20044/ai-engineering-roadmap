# Resource Library · L03 — Deep Learning, Foundation Models, and Serving

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

## Topic navigation

1. [Tensors and neural network structure](#unit-01)
2. [Backpropagation and optimization](#unit-02)
3. [Language-model foundations](#unit-03)
4. [Tokens, context and sampling](#unit-04)
5. [Attention and transformer intuition](#unit-05)
6. [Training versus model serving](#unit-06)

<a id="unit-01"></a>

## 1. Tensors and neural network structure

[Return to README Step 1](README.md#1-tensors-and-neural-network-structure)

**Topic/subtopics:** Layers; activations; shapes; device; dtype.

**Required sequence:** the assigned book slice [B08 · C2](../docs/READING_GUIDE.md#b08) **THEN** `pytorch` **THEN** `nn-visual` (a different required capability). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-tensors-and-neural-network-structure) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B08 · C2](../docs/READING_GUIDE.md#b08)<br>Chip Huyen · EN | Book Section | Complementary | Tensors and neural network structure | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b08) |
| `pytorch` · [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)<br>PyTorch · EN | Documentation / tutorial | Primary | Shapes, dtype, device and tensor operations. | Consult the Layers; activations; shapes; device; dtype sections/examples… [bounds](#unit-01-pytorch) |
| `ar-nn` · [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Layers, activations and learning intuition. | Topic bounds; lesson IDs not verified — [details](#unit-01-ar-nn) |
| `nn-visual` · [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks)<br>Grant Sanderson · 3Blue1Brown · EN video | Video series / lesson collection | Complementary (required) | Neural-network and backpropagation intuition; select… | Neural-network overview, gradient descent or backpropagation lesson… [bounds](#unit-01-nn-visual) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-pytorch"></a>

**`pytorch` — selected portion:** Consult the Layers; activations; shapes; device; dtype sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-01-ar-nn"></a>

**`ar-nn` — selected portion:** Only Layers, activations and learning intuition. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-nn-visual"></a>

**`nn-visual` — selected portion:** Neural-network overview, gradient descent or backpropagation lesson matching this group; direct lesson links are in source notes.

**Relationship:** Required neural-network structure explanation after the tensor API; different concepts, not substitutes.

</details>

<a id="unit-02"></a>

## 2. Backpropagation and optimization

[Return to README Step 2](README.md#2-backpropagation-and-optimization)

**Topic/subtopics:** Autograd; computational graph; gradients; train versus eval.

**Required sequence:** `autograd`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `optimize`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-backpropagation-and-optimization) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B08 · C2](../docs/READING_GUIDE.md#b08)<br>Chip Huyen · EN | Book Section | Reference | Backpropagation and optimization | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b08) |
| `autograd` · [Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)<br>PyTorch · EN | Documentation / tutorial | Primary | Gradients, backward and computational graphs. | Consult the Autograd; computational graph; gradients; train versus eval… [bounds](#unit-02-autograd) |
| `ar-nn` · [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Layers, activations and learning intuition. | Topic bounds; lesson IDs not verified — [details](#unit-02-ar-nn) |
| `zerohero` · [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)<br>Andrej Karpathy · EN video + notebooks | Multi-hour video course / lecture index | Complementary (as needed) | Micrograd for gradients; the GPT lecture for attention and… | The spelled-out intro to neural networks and backpropagation: building… [bounds](#unit-02-zerohero) |
| `optimize` · [Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)<br>PyTorch · EN | Documentation / tutorial | Reference | Loss, optimizer, training and evaluation loops. | Consult the relevant example for Loss, optimizer, training and evaluation… [bounds](#unit-02-optimize) |
| `zerohero-code` · [Zero to Hero notebooks](https://github.com/karpathy/nn-zero-to-hero)<br>Andrej Karpathy · EN / Python | Course notebooks / code repository | Optional Advanced | Run a small gradient or tokenization experiment and… | One matching lab/notebook for the stated topic; do not complete the whole platform. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-autograd"></a>

**`autograd` — selected portion:** Consult the Autograd; computational graph; gradients; train versus eval sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-02-ar-nn"></a>

**`ar-nn` — selected portion:** Only Layers, activations and learning intuition. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-zerohero"></a>

**`zerohero` — selected portion:** The spelled-out intro to neural networks and backpropagation: building micrograd. Optional implementation depth; GPT lecture only for a remaining attention gap.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-optimize"></a>

**`optimize` — selected portion:** Consult the relevant example for Loss, optimizer, training and evaluation loops. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-02-zerohero-code"></a>

**`zerohero-code` — selected portion:** One matching lab/notebook for the stated topic; do not complete the whole platform.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-03"></a>

## 3. Language-model foundations

[Return to README Step 3](README.md#3-language-model-foundations)

**Topic/subtopics:** Next-token prediction; pretraining; SFT; preference tuning.

**Required sequence (default route):** `hf-llm`. Stop each source at the stated portion.

**Choose ONE explanation for application versus foundation-model orientation:** default `hf-llm` **OR** `ar-gen-intro`. Retain the assigned C2 model/token/sampling sections beyond this introduction. This choice is not permission to skip the group’s other subtopics, assigned books or required complements.

**While implementing:** consult `hf-token`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-language-model-foundations) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B01 · G1](../docs/READING_GUIDE.md#b01)<br>Andrea De Mauro · EN | Book Section | Reference | Language-model foundations | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b01) |
| [B08 · C2](../docs/READING_GUIDE.md#b08)<br>Chip Huyen · EN | Book Section | Reference | Language-model foundations | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b08) |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Primary | Transformer families, tokenization and using pretrained… | Chapter 1: Transformer families, how Transformers work, inference and… [bounds](#unit-03-hf-llm) |
| `ar-gen-intro` · [Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Alternative | Application versus foundation model and basic capabilities. | Only the linked translated lesson: Application versus foundation model and… [bounds](#unit-03-ar-gen-intro) |
| `ar-nn` · [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Layers, activations and learning intuition. | Topic bounds; lesson IDs not verified — [details](#unit-03-ar-nn) |
| `hf-token` · [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)<br>Hugging Face · EN | Documentation / tutorial | Reference | Subword tokenization and language-dependent token counts. | Chapter 6 introduction to tokenization; selected tokenizer/model example… [bounds](#unit-03-hf-token) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-hf-llm"></a>

**`hf-llm` — selected portion:** Chapter 1: Transformer families, how Transformers work, inference and bias/limitations. Tokenizers are the separate chapter-6 reference.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-gen-intro"></a>

**`ar-gen-intro` — selected portion:** Only the linked translated lesson: Application versus foundation model and basic capabilities. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Substitute only for application versus foundation-model orientation. Retain the assigned C2 model/token/sampling sections beyond this introduction.

<a id="unit-03-ar-nn"></a>

**`ar-nn` — selected portion:** Only Layers, activations and learning intuition. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-hf-token"></a>

**`hf-token` — selected portion:** Chapter 6 introduction to tokenization; selected tokenizer/model example only. Reuse for token counting, not a course restart.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-04"></a>

## 4. Tokens, context and sampling

[Return to README Step 4](README.md#4-tokens-context-and-sampling)

**Topic/subtopics:** Tokenizer; context limit; output length; temperature; top-p.

**Required sequence:** `hf-token`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `ollama`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-tokens-context-and-sampling) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B08 · C2](../docs/READING_GUIDE.md#b08)<br>Chip Huyen · EN | Book Section | Reference | Tokens, context and sampling | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b08) |
| `hf-token` · [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)<br>Hugging Face · EN | Documentation / tutorial | Primary | Subword tokenization and language-dependent token counts. | Chapter 6 introduction to tokenization; use the tokenizer/model example… [bounds](#unit-04-hf-token) |
| `ar-gen-chat` · [Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Conversation state and token/context constraints. | Only the linked translated lesson: Conversation state and token/context… [bounds](#unit-04-ar-gen-chat) |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Complementary (as needed) | Transformer families, tokenization and using pretrained… | Chapter 1 introduction/model families; Read only the named… [bounds](#unit-04-hf-llm) |
| `ollama` · [Ollama API introduction](https://docs.ollama.com/api/introduction)<br>Ollama · EN | Documentation / tutorial | Reference | Local inference endpoint contracts; local operation uses… | Consult the relevant example for Local inference endpoint contracts; local… [bounds](#unit-04-ollama) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-hf-token"></a>

**`hf-token` — selected portion:** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.

**Relationship:** Default selected route for this topic.

<a id="unit-04-ar-gen-chat"></a>

**`ar-gen-chat` — selected portion:** Only the linked translated lesson: Conversation state and token/context constraints. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-hf-llm"></a>

**`hf-llm` — selected portion:** Chapter 1 introduction/model families; Read only the named foundation-model concepts for this group. Fine-tuning/training sections remain optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-04-ollama"></a>

**`ollama` — selected portion:** Consult the relevant example for Local inference endpoint contracts; local operation uses your hardware. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-05"></a>

## 5. Attention and transformer intuition

[Return to README Step 5](README.md#5-attention-and-transformer-intuition)

**Topic/subtopics:** Queries/keys/values; attention weights; positional information.

**Required sequence:** `nn-visual`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `hf-llm`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-attention-and-transformer-intuition) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B08 · C2](../docs/READING_GUIDE.md#b08)<br>Chip Huyen · EN | Book Section | Reference | Attention and transformer intuition | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b08) |
| `nn-visual` · [Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks)<br>Grant Sanderson · 3Blue1Brown · EN video | Video series / lesson collection | Primary | Neural-network and backpropagation intuition; select… | Only “Attention in transformers, step-by-step”. The general series is an… [bounds](#unit-05-nn-visual) |
| `ar-nn` · [Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa)<br>Hesham Asem · Egypt · AR video | Playlist (YouTube) | Complementary (as needed) | Layers, activations and learning intuition. | Topic bounds; lesson IDs not verified — [details](#unit-05-ar-nn) |
| `zerohero` · [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)<br>Andrej Karpathy · EN video + notebooks | Multi-hour video course / lecture index | Complementary (as needed) | Micrograd for gradients; the GPT lecture for attention and… | The spelled-out intro to neural networks and backpropagation: building… [bounds](#unit-05-zerohero) |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Reference | Transformer families, tokenization and using pretrained… | Chapter 1 introduction/model families; Read only the named… [bounds](#unit-05-hf-llm) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-nn-visual"></a>

**`nn-visual` — selected portion:** Only “Attention in transformers, step-by-step”. The general series is an optional alternative, not an assignment to watch every lesson.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-nn"></a>

**`ar-nn` — selected portion:** Only Layers, activations and learning intuition. Playlist topic verified; individual lesson IDs/timestamps not verified. Use as bounded supplementary explanation, not a whole-playlist requirement.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Neural-network prerequisites only; no verified Arabic attention lesson is assigned.

<a id="unit-05-zerohero"></a>

**`zerohero` — selected portion:** The spelled-out intro to neural networks and backpropagation: building micrograd. Optional implementation depth; GPT lecture only for a remaining attention gap.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-hf-llm"></a>

**`hf-llm` — selected portion:** Chapter 1 introduction/model families; Read only the named foundation-model concepts for this group. Fine-tuning/training sections remain optional.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Training versus model serving

[Return to README Step 6](README.md#6-training-versus-model-serving)

**Topic/subtopics:** API provider; local server; model license; memory/latency budget.

**Required sequence:** the assigned book slice [B09 · F3](../docs/READING_GUIDE.md#b09) **THEN** `ar-mini-19`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `ollama`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-training-versus-model-serving) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B09 · F3](../docs/READING_GUIDE.md#b09)<br>Alireza Parandeh · EN | Book Section | Complementary | Training versus model serving | [Read Now: exact assigned slice](../docs/READING_GUIDE.md#b09) |
| `ar-mini-19` · [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Primary | Ollama Local LLM Server in a working RAG backend. | The linked video only; not its playlist. |
| `fsdl-foundation` · [LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/)<br>Full Stack Deep Learning · EN video + slides | Single Video + slides | Complementary (as needed) | Language-model capabilities and application boundaries. | Topic bounds; lesson IDs not verified — [details](#unit-06-fsdl-foundation) |
| `ollama` · [Ollama API introduction](https://docs.ollama.com/api/introduction)<br>Ollama · EN | Documentation / tutorial | Reference | Local inference endpoint contracts; local operation uses… | Consult the relevant example for Local inference endpoint contracts; local… [bounds](#unit-06-ollama) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-ar-mini-19"></a>

**`ar-mini-19` — selected portion:** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Relationship:** Default selected route for this topic.

<a id="unit-06-fsdl-foundation"></a>

**`fsdl-foundation` — selected portion:** Only the linked lesson on Language-model capabilities and application boundaries. No course/playlist replay; exact timestamps were not verified.

**Relationship:** Different or partially overlapping concepts; as-needed support, not a substitute for the required route.

<a id="unit-06-ollama"></a>

**`ollama` — selected portion:** Consult the relevant example for Local inference endpoint contracts; local operation uses your hardware. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-nn"></a>

<details>
<summary>ar-nn · Art of Machine Learning · Neural networks — access, scope and verification</summary>

[Art of Machine Learning · Neural networks](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UX-Yi32r925nsgW-3GrnSa) · Hesham Asem · Egypt · AR video

- **Resource Type:** Playlist (YouTube).
- **Access:** Free.
- **Catalog scope:** Layers, activations and learning intuition.
- **Scope/version limits:** Older teaching; concepts remain useful, but use current scikit-learn/PyTorch APIs. This is a bounded foundation, not a Data Science specialization.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tensors and neural network structure; Backpropagation and optimization; Language-model foundations; Attention and transformer intuition.
- **Retained broad selection notes (lookup only):** Layers, activations and learning intuition; exact lesson numbers not verified. Transformer attention is not claimed as coverage.

</details>

<a id="r-nn-visual"></a>

<details>
<summary>nn-visual · Neural networks visual series — access, scope and verification</summary>

[Neural networks visual series](https://www.3blue1brown.com/topics/neural-networks) · Grant Sanderson · 3Blue1Brown · EN video

- **Resource Type:** Video series / lesson collection.
- **Access:** Free.
- **Catalog scope:** Neural-network and backpropagation intuition; select transformer/attention explanations when ready.
- **Scope/version limits:** Pair visualization with the tiny PyTorch lab.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tensors and neural network structure; Attention and transformer intuition.
- **Retained broad selection notes (lookup only):** Only “Attention in transformers, step-by-step”. The general series is an optional alternative, not an assignment to watch every lesson.

**Verified direct lessons:** [What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation/) · [Gradient descent, how neural networks learn](https://www.3blue1brown.com/lessons/gradient-descent/) · [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention/). Follow only the lesson for the selected concept.

</details>

<a id="r-pytorch"></a>

<details>
<summary>pytorch · Tensors — access, scope and verification</summary>

[Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) · PyTorch · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Shapes, dtype, device and tensor operations.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tensors and neural network structure.
- **Retained broad selection notes (lookup only):** Consult the Layers; activations; shapes; device; dtype sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-zerohero"></a>

<details>
<summary>zerohero · Neural Networks: Zero to Hero — access, scope and verification</summary>

[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) · Andrej Karpathy · EN video + notebooks

- **Resource Type:** Multi-hour video course / lecture index.
- **Access:** Free.
- **Catalog scope:** Micrograd for gradients; the GPT lecture for attention and language modelling.
- **Scope/version limits:** Full course is optional depth; do not build a full GPT before RAG.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Backpropagation and optimization; Attention and transformer intuition.
- **Retained broad selection notes (lookup only):** Lecture “The spelled-out intro to neural networks and backpropagation: building micrograd” as optional deeper practice; GPT lecture only if attention remains unclear.

</details>

<a id="r-autograd"></a>

<details>
<summary>autograd · Autograd — access, scope and verification</summary>

[Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) · PyTorch · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Gradients, backward and computational graphs.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Backpropagation and optimization.
- **Retained broad selection notes (lookup only):** Consult the Autograd; computational graph; gradients; train versus eval sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-optimize"></a>

<details>
<summary>optimize · Optimization loop — access, scope and verification</summary>

[Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) · PyTorch · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Loss, optimizer, training and evaluation loops.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Backpropagation and optimization.
- **Retained broad selection notes (lookup only):** Consult the Autograd; computational graph; gradients; train versus eval sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-gen-intro"></a>

<details>
<summary>ar-gen-intro · Introduction to generative AI · Arabic — access, scope and verification</summary>

[Introduction to generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/01-introduction-to-genai/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Application versus foundation model and basic capabilities.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Language-model foundations.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Language-model foundations. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-hf-llm"></a>

<details>
<summary>hf-llm · Hugging Face LLM course — access, scope and verification</summary>

[Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) · Hugging Face · EN course + videos + quizzes

- **Resource Type:** Full course: text, videos and quizzes.
- **Access:** Free.
- **Catalog scope:** Transformer families, tokenization and using pretrained models.
- **Scope/version limits:** Read targeted sections; training an LLM is optional.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Language-model foundations; Tokens, context and sampling; Attention and transformer intuition.
- **Retained broad selection notes (lookup only):** Chapter 1: Transformer families, how Transformers work, inference and bias/limitations. Tokenizers are the separate chapter-6 reference.

</details>

<a id="r-hf-token"></a>

<details>
<summary>hf-token · Tokenizers — access, scope and verification</summary>

[Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) · Hugging Face · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Subword tokenization and language-dependent token counts.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Language-model foundations; Tokens, context and sampling.
- **Retained broad selection notes (lookup only):** Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.

</details>

<a id="r-ar-gen-chat"></a>

<details>
<summary>ar-gen-chat · Chat applications · Arabic — access, scope and verification</summary>

[Chat applications · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/07-building-chat-applications/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** Conversation state and token/context constraints.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tokens, context and sampling.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Tokens, context and sampling. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-ollama"></a>

<details>
<summary>ollama · Ollama API introduction — access, scope and verification</summary>

[Ollama API introduction](https://docs.ollama.com/api/introduction) · Ollama · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Local inference endpoint contracts; local operation uses your hardware.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Tokens, context and sampling; Training versus model serving.
- **Retained broad selection notes (lookup only):** Consult the Tokenizer; context limit; output length; temperature; top-p sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-19"></a>

<details>
<summary>ar-mini-19 · mini-RAG · Ollama Local LLM Server — access, scope and verification</summary>

[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** Ollama Local LLM Server in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Training versus model serving.
- **Retained broad selection notes (lookup only):** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-fsdl-foundation"></a>

<details>
<summary>fsdl-foundation · LLM Foundations — access, scope and verification</summary>

[LLM Foundations](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llm-foundations/) · Full Stack Deep Learning · EN video + slides

- **Resource Type:** Single Video + slides.
- **Access:** Free.
- **Catalog scope:** Language-model capabilities and application boundaries.
- **Scope/version limits:** 2023 lecture: retain architectural lessons; use current docs for APIs and model choices.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Training versus model serving.
- **Retained broad selection notes (lookup only):** Only the linked “LLM Foundations” lecture; not the complete LLM Bootcamp. Use the parts relevant to Training versus model serving. Exact timestamps are not assigned.

</details>

<a id="r-zerohero-code"></a>

<details>
<summary>zerohero-code · Zero to Hero notebooks — access, scope and verification</summary>

[Zero to Hero notebooks](https://github.com/karpathy/nn-zero-to-hero) · Andrej Karpathy · EN / Python

- **Resource Type:** Course notebooks / code repository.
- **Access:** Free.
- **Catalog scope:** Run a small gradient or tokenization experiment and inspect the notebook.
- **Scope/version limits:** GPU training and every notebook are not required.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Run a small gradient or tokenization experiment and inspect the notebook. Optional lookup; implement only the portion that addresses the named gap.

</details>

## Practice, books and verification

[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.

No new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

# Resource Library · L17 — Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Follow the learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md)

This is the complete retained library, not a second to-do list. **Follow Primary resources in the README; everything else is an Alternative, Reference or Optional Advanced resource.** You do not need to watch every video or finish every course.

## Selection key

- **Primary:** used by at least one numbered step; follow only its assigned portion.
- **Alternative:** optional Arabic/English explanation or practice replacing a primary explanation.
- **Reference:** consult a named API/spec section when implementing.
- **Optional Advanced:** a later deep dive; does not block this Level.

**Resource Type** describes the format, independently of its role. A single video containing a playlist parameter remains a single video. Exact titles/numbers are used where verified; unverified identifiers are explicitly marked.

**Arabic availability:** Arabic translated fine-tuning material supplies concepts. No complete Arabic course on the specific PEFT/SFT/versioned-serving workflow was verified; current Hugging Face/vLLM resources are primary for the experiment.

## Book references

Assigned reading is authoritative in [the master order for L17](../docs/READING_GUIDE.md#l17). The [chapter map](../docs/CHAPTER_MAP.md) preserves full chapter/page locations and split reasons. This library does not assign those chapters again.

**This Level’s ledger IDs:** [B45 · C7](../docs/READING_GUIDE.md#b45), [B46 · C8](../docs/READING_GUIDE.md#b46), [B47 · C9](../docs/READING_GUIDE.md#b47).

**Previously covered / lookup only:** [B07 · C8](../docs/READING_GUIDE.md#b07), [B22 · C8](../docs/READING_GUIDE.md#b22), [B42 · C9](../docs/READING_GUIDE.md#b42). No mandatory chapter restart.

## Arabic and Egyptian teaching

<a id="r-ar-gen-finetune"></a>

### Fine-tuning LLMs · Arabic

[Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Fine-tuning decision; Dataset engineering; PEFT and SFT.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Fine-tuning decision. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** When adaptation helps and the training/evaluation boundary.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-gen-responsible"></a>

### Responsible generative AI · Arabic

[Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)

- **Resource Type:** Machine-translated lesson / article.
- **Role:** Alternative. **Language:** AR machine-translated text. **By:** Microsoft.
- **Access:** Free.
- **Use for:** Dataset engineering.
- **Assigned portion:** Only the linked translated lesson, particularly its sections about Dataset engineering. Its English video/cloud build is an alternative, not an extra requirement.
- **Scope:** Fairness, reliability and accountable use.
- **Limit:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.

<a id="r-ar-mini-19"></a>

### mini-RAG · Ollama Local LLM Server

[mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Quantization and inference; Model-serving boundary.
- **Assigned portion:** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** Ollama Local LLM Server in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Local serving context only; quantization and batching need current English serving docs. Serving/deployment context; tuned-artifact deployment uses current serving documentation.

<a id="r-ar-mini-22"></a>

### mini-RAG · App Deployments 1/2

[mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg)

- **Resource Type:** Single video (lesson within playlist).
- **Role:** Alternative. **Language:** AR video. **By:** Abu Bakr Soliman · Egypt.
- **Access:** Free.
- **Use for:** Model-serving boundary.
- **Assigned portion:** Only the linked “App Deployments 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.
- **Scope:** App Deployments 1/2 in a working RAG backend.
- **Limit:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.

**Arabic scope note:** Serving/deployment context; tuned-artifact deployment uses current serving documentation.

## English video and guided courses

<a id="r-hf-llm"></a>

### Hugging Face LLM course

[Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)

- **Resource Type:** Full course: text, videos and quizzes.
- **Role:** Alternative. **Language:** EN course + videos + quizzes. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Fine-tuning decision; Dataset engineering; Quantization and inference.
- **Assigned portion:** Choose fine-tuning sections for the actual experiment after B45; skip unrelated task families.
- **Scope:** Transformer families, tokenization and using pretrained models.
- **Limit:** Read targeted sections; training an LLM is optional.

<a id="r-zerohero"></a>

### Neural Networks: Zero to Hero

[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)

- **Resource Type:** Multi-hour video course / lecture index.
- **Role:** Optional Advanced. **Language:** EN video + notebooks. **By:** Andrej Karpathy.
- **Access:** Free.
- **Use for:** PEFT and SFT.
- **Assigned portion:** Review the micrograd optimization mechanism if a training-loop gap remains. Do not replay the full course.
- **Scope:** Micrograd for gradients; the GPT lecture for attention and language modelling.
- **Limit:** Full course is optional depth; do not build a full GPT before RAG.

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

<a id="r-peft"></a>

### PEFT quicktour

[PEFT quicktour](https://huggingface.co/docs/peft/quicktour)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Fine-tuning decision; PEFT and SFT.
- **Assigned portion:** Consult the LoRA/adapters; target modules; data format; training config; checkpoints sections/examples only. Do not read the entire documentation site.
- **Scope:** Adapter training, saving and loading.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-trl"></a>

### TRL SFTTrainer

[TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Dataset engineering; PEFT and SFT.
- **Assigned portion:** Consult the Representative tasks; quality; deduplication; consent/license; split boundaries sections/examples only. Do not read the entire documentation site.
- **Scope:** Supervised instruction tuning and dataset formats.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-promptfoo"></a>

### Assertions and metrics

[Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

- **Resource Type:** Documentation: assertions reference.
- **Role:** Primary. **Language:** EN. **By:** Promptfoo.
- **Access:** Free.
- **Use for:** Holdout and regression evaluation.
- **Assigned portion:** The assertion type matching Holdout and regression evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.
- **Scope:** Deterministic checks, model judges and eval assertions.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-quant"></a>

### bitsandbytes quantization

[bitsandbytes quantization](https://huggingface.co/docs/transformers/quantization/bitsandbytes)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** Hugging Face.
- **Access:** Free.
- **Use for:** Quantization and inference.
- **Assigned portion:** Read bitsandbytes prerequisites and the 8-bit/4-bit loading examples. Record hardware/model constraints and compare measured memory/quality; batching is covered separately in the optional serving reading.
- **Scope:** Memory/quality tradeoffs and compatible hardware.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-vllm"></a>

### vLLM quickstart

[vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Primary. **Language:** EN. **By:** vLLM.
- **Access:** Free.
- **Use for:** Quantization and inference; Model-serving boundary.
- **Assigned portion:** Consult the Separate runtime; adapter deployment; version rollback; lifecycle cost sections/examples only. Do not read the entire documentation site.
- **Scope:** Separate model serving and OpenAI-compatible endpoints; optional GPU path.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

<a id="r-ollama"></a>

### Ollama API introduction

[Ollama API introduction](https://docs.ollama.com/api/introduction)

- **Resource Type:** Official documentation / tutorial.
- **Role:** Reference. **Language:** EN. **By:** Ollama.
- **Access:** Free.
- **Use for:** Model-serving boundary.
- **Assigned portion:** Consult the Separate runtime; adapter deployment; version rollback; lifecycle cost sections/examples only. Do not read the entire documentation site.
- **Scope:** Local inference endpoint contracts; local operation uses your hardware.
- **Limit:** Consult the named section and validate library versions; not a requirement to read the entire documentation.

## Optional advanced materials

<a id="r-lora"></a>

### LoRA paper

[LoRA paper](https://arxiv.org/abs/2106.09685)

- **Resource Type:** Research paper.
- **Role:** Optional Advanced. **Language:** EN research paper. **By:** Hu et al..
- **Access:** Free.
- **Use for:** Optional support for the Level’s exercises.
- **Assigned portion:** Low-rank adaptation motivation and constraints. Optional lookup; implement only the portion that addresses the named gap.
- **Scope:** Low-rank adaptation motivation and constraints.
- **Limit:** Optional after implementing a small adapter experiment.

## Practice and evidence

The practical tasks, assessment criteria and original self-check are linked from [the Level learning path](README.md#practical-exercises). They are not duplicated here as a second assignment list. Platform quizzes/labs and self-assessed tasks have different evidence requirements.

## Verification and maintenance

Source titles/outlines and documented scopes were checked during curation. This refactor adds precise resource types and bounded selections without inventing timestamps or full-video verification. See [verification policy](../docs/RESOURCE_POLICY.md) and [learning-experience audit](../docs/LEARNING_EXPERIENCE_AUDIT.md). Hosted access, paid assessments and playback can change.

[← Return to your next learning step](README.md#start-here--recommended-learning-path)

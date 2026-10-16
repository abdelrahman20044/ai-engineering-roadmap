# Resource Library · L17 — Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)

**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.

## How to choose

- **Primary:** the default source for this group, after its assigned book slice.
- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.
- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.
- **Reference:** consult the named API/example while implementing; do not finish a documentation site.
- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.

Format is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.

**Arabic availability:** Arabic translated fine-tuning material supplies concepts. No complete Arabic course on the specific PEFT/SFT/versioned-serving workflow was verified; current Hugging Face/vLLM resources are primary for the experiment.

## Topic navigation

1. [Fine-tuning decision](#unit-01)
2. [Dataset engineering](#unit-02)
3. [PEFT and SFT](#unit-03)
4. [Holdout and regression evaluation](#unit-04)
5. [Quantization and inference](#unit-05)
6. [Model-serving boundary](#unit-06)

<a id="unit-01"></a>

## 1. Fine-tuning decision

[Return to README Step 1](README.md#1-fine-tuning-decision)

**Topic/subtopics:** Prompt versus RAG versus model switch versus adaptation.

**Required sequence:** the assigned book slice [B45 · C7](../docs/READING_GUIDE.md#b45). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `peft`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#1-fine-tuning-decision) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B45 · C7](../docs/READING_GUIDE.md#b45)<br>Chip Huyen · EN | Book Section | Primary | Fine-tuning decision | [Optional Advanced: exact assigned slice](../docs/READING_GUIDE.md#b45) |
| `ar-gen-finetune` · [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When adaptation helps and the training/evaluation boundary. | Only the linked translated lesson: When adaptation helps and the… [bounds](#unit-01-ar-gen-finetune) |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Complementary (as needed) | Transformer families, tokenization and using pretrained… | Read only the named foundation-model concepts for this group.… [bounds](#unit-01-hf-llm) |
| `peft` · [PEFT quicktour](https://huggingface.co/docs/peft/quicktour)<br>Hugging Face · EN | Documentation / tutorial | Reference | Adapter training, saving and loading. | Consult the relevant example for Adapter training, saving and loading.… [bounds](#unit-01-peft) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-01-ar-gen-finetune"></a>

**`ar-gen-finetune` — selected portion:** Only the linked translated lesson: When adaptation helps and the training/evaluation boundary. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-hf-llm"></a>

**`hf-llm` — selected portion:** Read only the named foundation-model concepts for this group. Fine-tuning/training sections remain optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-01-peft"></a>

**`peft` — selected portion:** Consult the relevant example for Adapter training, saving and loading. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-02"></a>

## 2. Dataset engineering

[Return to README Step 2](README.md#2-dataset-engineering)

**Topic/subtopics:** Representative tasks; quality; deduplication; consent/license; split boundaries.

**Required sequence:** the assigned book slice [B46 · C8](../docs/READING_GUIDE.md#b46). Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `trl`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#2-dataset-engineering) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B46 · C8](../docs/READING_GUIDE.md#b46)<br>Chip Huyen · EN | Book Section | Primary | Dataset engineering | [Optional Advanced: exact assigned slice](../docs/READING_GUIDE.md#b46) |
| `ar-gen-finetune` · [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When adaptation helps and the training/evaluation boundary. | Only the linked translated lesson: When adaptation helps and the… [bounds](#unit-02-ar-gen-finetune) |
| `ar-gen-responsible` · [Responsible generative AI · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/03-using-generative-ai-responsibly/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | Fairness, reliability and accountable use. | Only the linked translated lesson: Fairness, reliability and accountable… [bounds](#unit-02-ar-gen-responsible) |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Complementary (as needed) | Transformer families, tokenization and using pretrained… | Read only the named foundation-model concepts for this group.… [bounds](#unit-02-hf-llm) |
| `trl` · [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)<br>Hugging Face · EN | Documentation / tutorial | Reference | Supervised instruction tuning and dataset formats. | Consult the relevant example for Supervised instruction tuning and dataset… [bounds](#unit-02-trl) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-02-ar-gen-finetune"></a>

**`ar-gen-finetune` — selected portion:** Only the linked translated lesson: When adaptation helps and the training/evaluation boundary. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-ar-gen-responsible"></a>

**`ar-gen-responsible` — selected portion:** Only the linked translated lesson: Fairness, reliability and accountable use. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-hf-llm"></a>

**`hf-llm` — selected portion:** Read only the named foundation-model concepts for this group. Fine-tuning/training sections remain optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-02-trl"></a>

**`trl` — selected portion:** Consult the relevant example for Supervised instruction tuning and dataset formats. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-03"></a>

## 3. PEFT and SFT

[Return to README Step 3](README.md#3-peft-and-sft)

**Topic/subtopics:** LoRA/adapters; target modules; data format; training config; checkpoints.

**Required sequence:** `peft`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `trl`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#3-peft-and-sft) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B45 · C7](../docs/READING_GUIDE.md#b45)<br>Chip Huyen · EN | Book Section | Reference | PEFT and SFT | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b45) |
| [B46 · C8](../docs/READING_GUIDE.md#b46)<br>Chip Huyen · EN | Book Section | Reference | PEFT and SFT | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b46) |
| `peft` · [PEFT quicktour](https://huggingface.co/docs/peft/quicktour)<br>Hugging Face · EN | Documentation / tutorial | Primary | Adapter training, saving and loading. | Consult the LoRA/adapters; target modules; data format; training config;… [bounds](#unit-03-peft) |
| `ar-gen-finetune` · [Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md)<br>Microsoft · AR machine-translated text | Machine-translated lesson / article | Complementary (as needed) | When adaptation helps and the training/evaluation boundary. | Only the linked translated lesson: When adaptation helps and the… [bounds](#unit-03-ar-gen-finetune) |
| `zerohero` · [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)<br>Andrej Karpathy · EN video + notebooks | Multi-hour video course / lecture index | Complementary (as needed) | Micrograd for gradients; the GPT lecture for attention and… | The spelled-out intro to neural networks and backpropagation: building… [bounds](#unit-03-zerohero) |
| `trl` · [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)<br>Hugging Face · EN | Documentation / tutorial | Reference | Supervised instruction tuning and dataset formats. | Consult the relevant example for Supervised instruction tuning and dataset… [bounds](#unit-03-trl) |
| `lora` · [LoRA paper](https://arxiv.org/abs/2106.09685)<br>Hu et al. · EN research paper | Research paper | Optional Advanced | Low-rank adaptation motivation and constraints. | Problem statement and architecture/results relevant to this topic;… [bounds](#unit-03-lora) |
| `zerohero-code` · [Zero to Hero notebooks](https://github.com/karpathy/nn-zero-to-hero)<br>Andrej Karpathy · EN / Python | Course notebooks / code repository | Optional Advanced | Run a small gradient or tokenization experiment and… | One matching lab/notebook for the stated topic; do not complete the whole platform. |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-03-peft"></a>

**`peft` — selected portion:** Consult the LoRA/adapters; target modules; data format; training config; checkpoints sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-03-ar-gen-finetune"></a>

**`ar-gen-finetune` — selected portion:** Only the linked translated lesson: When adaptation helps and the training/evaluation boundary. Arabic text, not an Arabic video; cloud/framework examples are optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-zerohero"></a>

**`zerohero` — selected portion:** The spelled-out intro to neural networks and backpropagation: building micrograd. Optional implementation depth; GPT lecture only for a remaining attention gap.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-03-trl"></a>

**`trl` — selected portion:** Consult the relevant example for Supervised instruction tuning and dataset formats. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

<a id="unit-03-lora"></a>

**`lora` — selected portion:** Problem statement and architecture/results relevant to this topic; optional depth, not paper-wide implementation homework.

**Relationship:** Optional depth/purchase; does not block the completion gate.

<a id="unit-03-zerohero-code"></a>

**`zerohero-code` — selected portion:** One matching lab/notebook for the stated topic; do not complete the whole platform.

**Relationship:** Optional depth/purchase; does not block the completion gate.

</details>

<a id="unit-04"></a>

## 4. Holdout and regression evaluation

[Return to README Step 4](README.md#4-holdout-and-regression-evaluation)

**Topic/subtopics:** Task improvement; general behavior; safety/grounding regressions.

**Required sequence:** `promptfoo`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#4-holdout-and-regression-evaluation) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B15 · C3](../docs/READING_GUIDE.md#b15)<br>Chip Huyen · EN | Book Section | Reference | Holdout and regression evaluation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b15) |
| [B16 · C4](../docs/READING_GUIDE.md#b16)<br>Chip Huyen · EN | Book Section | Reference | Holdout and regression evaluation | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b16) |
| `promptfoo` · [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)<br>Promptfoo · EN | Documentation: assertions reference | Primary | Deterministic checks, model judges and eval assertions. | The assertion type matching Holdout and regression evaluation; start with… [bounds](#unit-04-promptfoo) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-04-promptfoo"></a>

**`promptfoo` — selected portion:** The assertion type matching Holdout and regression evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Relationship:** Default selected route for this topic.

</details>

<a id="unit-05"></a>

## 5. Quantization and inference

[Return to README Step 5](README.md#5-quantization-and-inference)

**Topic/subtopics:** Precision; model memory; hardware; batching; throughput versus latency.

**Required sequence:** the assigned book slice [B47 · C9](../docs/READING_GUIDE.md#b47) **THEN** `quant`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `vllm`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#5-quantization-and-inference) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B47 · C9](../docs/READING_GUIDE.md#b47)<br>Chip Huyen · EN | Book Section | Optional Advanced | Quantization and inference | [Optional Advanced: exact assigned slice](../docs/READING_GUIDE.md#b47) |
| `quant` · [bitsandbytes quantization](https://huggingface.co/docs/transformers/quantization/bitsandbytes)<br>Hugging Face · EN | Documentation / tutorial | Primary | Memory/quality tradeoffs and compatible hardware. | Read bitsandbytes prerequisites and the 8-bit/4-bit loading examples.… [bounds](#unit-05-quant) |
| `ar-mini-19` · [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Ollama Local LLM Server in a working RAG backend. | The linked video only; not its playlist. |
| `hf-llm` · [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)<br>Hugging Face · EN course + videos + quizzes | Full course: text, videos and quizzes | Complementary (as needed) | Transformer families, tokenization and using pretrained… | Read only the named foundation-model concepts for this group.… [bounds](#unit-05-hf-llm) |
| `vllm` · [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)<br>vLLM · EN | Documentation / tutorial | Reference | Separate model serving and OpenAI-compatible endpoints;… | Consult the relevant example for Separate model serving and… [bounds](#unit-05-vllm) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-05-quant"></a>

**`quant` — selected portion:** Read bitsandbytes prerequisites and the 8-bit/4-bit loading examples. Record hardware/model constraints and compare measured memory/quality; batching is covered separately in the optional serving reading.

**Relationship:** Default selected route for this topic.

<a id="unit-05-ar-mini-19"></a>

**`ar-mini-19` — selected portion:** Only the linked “Ollama Local LLM Server” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Local serving context only; quantization and batching need current English serving docs.

<a id="unit-05-hf-llm"></a>

**`hf-llm` — selected portion:** Read only the named foundation-model concepts for this group. Fine-tuning/training sections remain optional.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route.

<a id="unit-05-vllm"></a>

**`vllm` — selected portion:** Consult the relevant example for Separate model serving and OpenAI-compatible endpoints; optional GPU path. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

<a id="unit-06"></a>

## 6. Model-serving boundary

[Return to README Step 6](README.md#6-model-serving-boundary)

**Topic/subtopics:** Separate runtime; adapter deployment; version rollback; lifecycle cost.

**Required sequence:** `vllm`. Stop each source at the stated portion.

**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.

**While implementing:** consult `ollama`. These are lookups, not more courses.

**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#6-model-serving-boundary) are the same whichever bounded explanation you choose.

| Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only |
| --- | --- | --- | --- | --- |
| [B47 · C9](../docs/READING_GUIDE.md#b47)<br>Chip Huyen · EN | Book Section | Reference | Model-serving boundary | [Previously Covered / Review Only: exact assigned slice](../docs/READING_GUIDE.md#b47) |
| `vllm` · [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)<br>vLLM · EN | Documentation / tutorial | Primary | Separate model serving and OpenAI-compatible endpoints;… | Consult the Separate runtime; adapter deployment; version rollback;… [bounds](#unit-06-vllm) |
| `ar-mini-19` · [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | Ollama Local LLM Server in a working RAG backend. | The linked video only; not its playlist. |
| `ar-mini-22` · [mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg)<br>Abu Bakr Soliman · Egypt · AR video | Single Video (part of playlist) | Complementary (as needed) | App Deployments 1/2 in a working RAG backend. | The linked video only; not its playlist. |
| `ollama` · [Ollama API introduction](https://docs.ollama.com/api/introduction)<br>Ollama · EN | Documentation / tutorial | Reference | Local inference endpoint contracts; local operation uses… | Consult the relevant example for Local inference endpoint contracts; local… [bounds](#unit-06-ollama) |

<details>
<summary>Exact selection bounds and relationship notes</summary>

<a id="unit-06-vllm"></a>

**`vllm` — selected portion:** Consult the Separate runtime; adapter deployment; version rollback; lifecycle cost sections/examples only. Do not read the entire documentation site.

**Relationship:** Default selected route for this topic.

<a id="unit-06-ar-mini-19"></a>

**`ar-mini-19` — selected portion:** Only the linked “Ollama Local LLM Server” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Serving/deployment context; tuned-artifact deployment uses current serving documentation.

<a id="unit-06-ar-mini-22"></a>

**`ar-mini-22` — selected portion:** Only the linked “App Deployments 1/2” lesson. Not the full mini-RAG playlist.

**Relationship:** Optional explanation/practice for the stated scope; not interchangeable with the entire route. Arabic scope: Serving/deployment context; tuned-artifact deployment uses current serving documentation.

<a id="unit-06-ollama"></a>

**`ollama` — selected portion:** Consult the relevant example for Local inference endpoint contracts; local operation uses your hardware. Apply it to this group’s task; the linked reference is not another course to finish.

**Relationship:** Consult during implementation; no separate course completion.

</details>

## Retained source metadata and access notes

These notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.

<a id="r-ar-gen-finetune"></a>

<details>
<summary>ar-gen-finetune · Fine-tuning LLMs · Arabic — access, scope and verification</summary>

[Fine-tuning LLMs · Arabic](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ar/18-fine-tuning/README.md) · Microsoft · AR machine-translated text

- **Resource Type:** Machine-translated lesson / article.
- **Access:** Free.
- **Catalog scope:** When adaptation helps and the training/evaluation boundary.
- **Scope/version limits:** Machine translation (Co-op Translator), not Arabic video instruction. Compare terminology/code with the English original; Microsoft/cloud examples are optional implementation alternatives.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Fine-tuning decision; Dataset engineering; PEFT and SFT.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Fine-tuning decision. Its English video/cloud build is an alternative, not an extra requirement.

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
- **Retained Level-wide topic association:** Fine-tuning decision; Dataset engineering; Quantization and inference.
- **Retained broad selection notes (lookup only):** Choose fine-tuning sections for the actual experiment after B45; skip unrelated task families.

</details>

<a id="r-peft"></a>

<details>
<summary>peft · PEFT quicktour — access, scope and verification</summary>

[PEFT quicktour](https://huggingface.co/docs/peft/quicktour) · Hugging Face · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Adapter training, saving and loading.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Fine-tuning decision; PEFT and SFT.
- **Retained broad selection notes (lookup only):** Consult the LoRA/adapters; target modules; data format; training config; checkpoints sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** Dataset engineering.
- **Retained broad selection notes (lookup only):** Only the linked translated lesson, particularly its sections about Dataset engineering. Its English video/cloud build is an alternative, not an extra requirement.

</details>

<a id="r-trl"></a>

<details>
<summary>trl · TRL SFTTrainer — access, scope and verification</summary>

[TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) · Hugging Face · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Supervised instruction tuning and dataset formats.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Dataset engineering; PEFT and SFT.
- **Retained broad selection notes (lookup only):** Consult the Representative tasks; quality; deduplication; consent/license; split boundaries sections/examples only. Do not read the entire documentation site.

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
- **Retained Level-wide topic association:** PEFT and SFT.
- **Retained broad selection notes (lookup only):** Review the micrograd optimization mechanism if a training-loop gap remains. Do not replay the full course.

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
- **Retained Level-wide topic association:** Holdout and regression evaluation.
- **Retained broad selection notes (lookup only):** The assertion type matching Holdout and regression evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

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
- **Retained Level-wide topic association:** Quantization and inference; Model-serving boundary.
- **Retained broad selection notes (lookup only):** Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

</details>

<a id="r-quant"></a>

<details>
<summary>quant · bitsandbytes quantization — access, scope and verification</summary>

[bitsandbytes quantization](https://huggingface.co/docs/transformers/quantization/bitsandbytes) · Hugging Face · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Memory/quality tradeoffs and compatible hardware.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Quantization and inference.
- **Retained broad selection notes (lookup only):** Read bitsandbytes prerequisites and the 8-bit/4-bit loading examples. Record hardware/model constraints and compare measured memory/quality; batching is covered separately in the optional serving reading.

</details>

<a id="r-vllm"></a>

<details>
<summary>vllm · vLLM quickstart — access, scope and verification</summary>

[vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) · vLLM · EN

- **Resource Type:** Documentation / tutorial.
- **Access:** Free.
- **Catalog scope:** Separate model serving and OpenAI-compatible endpoints; optional GPU path.
- **Scope/version limits:** Consult the named section and validate library versions; not a requirement to read the entire documentation.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Quantization and inference; Model-serving boundary.
- **Retained broad selection notes (lookup only):** Consult the Separate runtime; adapter deployment; version rollback; lifecycle cost sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-ar-mini-22"></a>

<details>
<summary>ar-mini-22 · mini-RAG · App Deployments 1/2 — access, scope and verification</summary>

[mini-RAG · App Deployments 1/2](https://www.youtube.com/watch?v=7QRPnAbVssg) · Abu Bakr Soliman · Egypt · AR video

- **Resource Type:** Single Video (part of playlist).
- **Access:** Free.
- **Catalog scope:** App Deployments 1/2 in a working RAG backend.
- **Scope/version limits:** Follow concepts and write your own version; early lessons use MongoDB, while this roadmap chooses PostgreSQL. Verify older dependency syntax against current docs.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Model-serving boundary.
- **Retained broad selection notes (lookup only):** Only the linked “App Deployments 1/2” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

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
- **Retained Level-wide topic association:** Model-serving boundary.
- **Retained broad selection notes (lookup only):** Consult the Separate runtime; adapter deployment; version rollback; lifecycle cost sections/examples only. Do not read the entire documentation site.

</details>

<a id="r-lora"></a>

<details>
<summary>lora · LoRA paper — access, scope and verification</summary>

[LoRA paper](https://arxiv.org/abs/2106.09685) · Hu et al. · EN research paper

- **Resource Type:** Research paper.
- **Access:** Free.
- **Catalog scope:** Low-rank adaptation motivation and constraints.
- **Scope/version limits:** Optional after implementing a small adapter experiment.
- **Verification boundary:** Author/publisher outline or named documentation scope; no invented timestamps.
- **Retained Level-wide topic association:** Supplemental practice/depth.
- **Retained broad selection notes (lookup only):** Low-rank adaptation motivation and constraints. Optional lookup; implement only the portion that addresses the named gap.

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

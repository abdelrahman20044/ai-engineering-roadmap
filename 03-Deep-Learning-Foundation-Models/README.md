# L03 · Deep Learning, Foundation Models, and Serving

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 1 · 12–18 focused hours · Difficulty 3/5 · P0**

**You will learn:** Distinguish pretraining, supervised fine-tuning, preference tuning, and inference. Understand layers, autograd, attention, tokenization, sampling, and resource constraints. Choose an external provider or local inference endpoint with a reasoned boundary.

**Before starting:** [L00](../00-Orientation/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B08 · C2](../docs/READING_GUIDE.md#b08) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Tensors and neural network structure

**Learn:** Layers; activations; shapes; device; dtype.

**Required reading:**

- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Read Now**. Printed pp.49–87: model architecture/training orientation; pp.88–105: sampling and structured-output concepts. Avoid research derivations.

**Primary · Official documentation / tutorial:** [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html). Consult the Layers; activations; shapes; device; dtype sections/examples only. Do not read the entire documentation site.

**Practice:** Run a small forward pass and assert each intermediate shape.

**Completion check:** Shapes, dtype and device are asserted for the tiny forward pass.

[Alternative · AR video](resources.md#r-ar-nn) (optional)

### 2. Backpropagation and optimization

**Learn:** Autograd; computational graph; gradients; train versus eval.

**Required reading:**

- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html). Consult the Autograd; computational graph; gradients; train versus eval sections/examples only. Do not read the entire documentation site.

**Practice:** Check a scalar derivative manually and train a small CPU network for a few steps.

**Completion check:** Manual derivative matches autograd and the tiny model loss changes.

[Alternative · AR video](resources.md#r-ar-nn) (optional) · [Implementation reference](resources.md#r-optimize)

### 3. Language-model foundations

**Learn:** Next-token prediction; pretraining; SFT; preference tuning.

**Required reading:**

- [B01 · G1](../docs/READING_GUIDE.md#b01) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Full course: text, videos and quizzes:** [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1). Chapter 1: Transformer families, how Transformers work, inference and bias/limitations. Tokenizers are the separate chapter-6 reference.

**Practice:** Explain where knowledge, instruction behavior and application context enter the system.

**Completion check:** Explain pretraining, SFT, preference tuning and inference using the same model boundary.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-intro) (optional) · [Implementation reference](resources.md#r-hf-token)

### 4. Tokens, context and sampling

**Learn:** Tokenizer; context limit; output length; temperature; top-p.

**Required reading:**

- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1). Chapter 6 introduction to tokenization; use the tokenizer/model example needed for the Arabic/English count experiment. No whole-course assignment.

**Practice:** Measure token counts for Arabic/English prompts and compare two sampling settings.

**Completion check:** Record model/config and compare actual token counts and sampling outputs.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-chat) (optional) · [Implementation reference](resources.md#r-ollama)

### 5. Attention and transformer intuition

**Learn:** Queries/keys/values; attention weights; positional information.

**Required reading:**

- [B08 · C2](../docs/READING_GUIDE.md#b08) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Single video + illustrated lesson:** [Neural networks visual series](https://www.3blue1brown.com/lessons/attention/). Only “Attention in transformers, step-by-step”. The general series is an optional alternative, not an assignment to watch every lesson.

**Practice:** Explain attention using a short sentence and trace tensor dimensions conceptually.

**Completion check:** Explain Q/K/V and the dimensions without claiming to have trained a transformer.

[Alternative · AR video](resources.md#r-ar-nn) (optional) · [Implementation reference](resources.md#r-hf-llm)

### 6. Training versus model serving

**Learn:** API provider; local server; model license; memory/latency budget.

**Required reading:**

- [B09 · F3](../docs/READING_GUIDE.md#b09) — **Read Now**. PDF pp.83–105: language-model integration; pp.137–142: serving/lifespan boundaries. Defer other modalities.

**Primary · Single video (lesson within playlist):** [mini-RAG · Ollama Local LLM Server](https://youtu.be/-epZ1hAAtrs). Only the linked “Ollama Local LLM Server” video; not the entire mini-RAG playlist. Use the matching branch from the instructor index if comparing code.

**Practice:** Call one local or hosted inference endpoint behind an adapter and record the resource boundary.

**Completion check:** The API calls an external/local inference adapter with documented failure behavior.

[Alternative · EN video + slides](resources.md#r-fsdl-foundation) (optional) · [Implementation reference](resources.md#r-ollama)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L03-E1:** Implement a tiny linear layer, loss, backward pass, and optimizer step in PyTorch.
  - **Pass:** Record tensor shapes, inspect gradients, and explain the update. Use L02 exercise E1 first if vectors are unfamiliar.
- [ ] **L03-E2:** Explore tokenization for representative inputs, optionally including Arabic and English.
  - **Pass:** Distinguish characters, tokens, context capacity, and embedding dimensions.
- [ ] **L03-E3:** Run five prompts using two sampling settings on one model.
  - **Pass:** Record settings and variation; low temperature is not treated as a determinism guarantee.
- [ ] **L03-E4:** Draw client → FastAPI → provider and compare external versus local serving.
  - **Pass:** Document timeouts, lifecycle, privacy/resource constraints, and actual hardware assumptions.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S2](../project/milestones/s2.md). Explain next-token prediction and attention conceptually, demonstrate the autograd lab, and run inference. L02 may proceed in parallel; completing all ML topics is not a prerequisite for the first model API call.

**Keep:** tiny-autograd.py and tokenization observations; Model selection card and serving ADR.

## What to defer

- Training a transformer from scratch
- Audio/video/3D serving and distributed GPU training

## Record progress and choose the next Level

```bash
python scripts/progress.py set L03 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** [L04](../04-LLM-Applications-Prompts/README.md), [L07](../07-Embeddings-Semantic-Search/README.md), [L16](../16-Capstone-Career/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

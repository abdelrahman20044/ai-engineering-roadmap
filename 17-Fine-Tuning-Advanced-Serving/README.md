# L17 · Fine-Tuning, Dataset Engineering, and Advanced Serving

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

**Tier 6 · 18–32 focused hours · Difficulty 4/5 · P3 · Optional Level**

**You will learn:** Choose between prompt changes, RAG, model selection, and fine-tuning using failure evidence. Understand SFT/LoRA, curation, quantization, and serving tradeoffs.

**Before starting:** [L02](../02-Mathematics-ML/README.md), [L03](../03-Deep-Learning-Foundation-Models/README.md), [L05](../05-Evaluation/README.md), [L15](../15-Model-Selection-Optimization/README.md) Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.

## Start Here / Recommended Learning Path

> **Next action:** Open [B45 · C7](../docs/READING_GUIDE.md#b45) for the assigned portion below, then follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.

Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.

### 1. Fine-tuning decision

**Learn:** Prompt versus RAG versus model switch versus adaptation.

**Required reading:**

- [B45 · C7](../docs/READING_GUIDE.md#b45) — **Optional Advanced**. Printed pp.311–318: When to Finetune first; select remaining tactics only for a justified adapter experiment.

**Primary · Book section:** [B45 · C7](../docs/READING_GUIDE.md#b45). Follow the assigned portion above; use the library references during implementation.

**Practice:** Write a go/no-go ADR with the failure cases and cheaper alternatives already tested.

**Completion check:** The go/no-go decision names actual failures and cheaper alternatives already tried.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-finetune) (optional)

### 2. Dataset engineering

**Learn:** Representative tasks; quality; deduplication; consent/license; split boundaries.

**Required reading:**

- [B46 · C8](../docs/READING_GUIDE.md#b46) — **Optional Advanced**. Training-data curation sections within printed pp.363–403 as needed; pp.368–371 and 396–402 are B07/B22 review.

**Primary · Book section:** [B46 · C8](../docs/READING_GUIDE.md#b46). Follow the assigned portion above; use the library references during implementation.

**Practice:** Create a small data card, split-by-source policy and duplicate/leakage checks.

**Completion check:** Training and holdout data are separated with duplicate/leakage checks.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-finetune) (optional)

### 3. PEFT and SFT

**Learn:** LoRA/adapters; target modules; data format; training config; checkpoints.

**Required reading:**

- [B45 · C7](../docs/READING_GUIDE.md#b45) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B46 · C8](../docs/READING_GUIDE.md#b46) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [PEFT quicktour](https://huggingface.co/docs/peft/quicktour). Consult the LoRA/adapters; target modules; data format; training config; checkpoints sections/examples only. Do not read the entire documentation site.

**Practice:** Run one bounded small-model adapter experiment and save configuration and provenance.

**Completion check:** A bounded run saves adapter configuration and source provenance.

[Alternative · AR machine-translated text](resources.md#r-ar-gen-finetune) (optional) · [Implementation reference](resources.md#r-trl)

### 4. Holdout and regression evaluation

**Learn:** Task improvement; general behavior; safety/grounding regressions.

**Required reading:**

- [B15 · C3](../docs/READING_GUIDE.md#b15) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.
- [B16 · C4](../docs/READING_GUIDE.md#b16) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Documentation: assertions reference:** [Assertions and metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/). The assertion type matching Holdout and regression evaluation; start with deterministic checks, then calibrated model grading if needed. Do not adopt all plugins.

**Practice:** Compare tuned/untuned models on an independent set and report negative outcomes too.

**Completion check:** The independent comparison reports regressions as well as gains.

### 5. Quantization and inference

**Learn:** Precision; model memory; hardware; batching; throughput versus latency.

**Required reading:**

- [B47 · C9](../docs/READING_GUIDE.md#b47) — **Optional Advanced**. Selected serving/optimization sections within printed pp.405–447 beyond the B42 metrics slice. F5 PDF240–252 is an optional companion for batching/KV/paged attention.

**Primary · Official documentation / tutorial:** [bitsandbytes quantization](https://huggingface.co/docs/transformers/quantization/bitsandbytes). Read bitsandbytes prerequisites and the 8-bit/4-bit loading examples. Record hardware/model constraints and compare measured memory/quality; batching is covered separately in the optional serving reading.

**Practice:** Benchmark memory/latency/quality before and after one compatible optimization.

**Completion check:** Memory, speed and task quality are measured on compatible hardware.

[Alternative · AR video](resources.md#r-ar-mini-19) (optional) · [Implementation reference](resources.md#r-vllm)

### 6. Model-serving boundary

**Learn:** Separate runtime; adapter deployment; version rollback; lifecycle cost.

**Required reading:**

- [B47 · C9](../docs/READING_GUIDE.md#b47) — **Previously Covered / Review Only**. Reuse only the part needed for this step; do not restart the chapter.

**Primary · Official documentation / tutorial:** [vLLM quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/). Consult the Separate runtime; adapter deployment; version rollback; lifecycle cost sections/examples only. Do not read the entire documentation site.

**Practice:** Serve the chosen artifact separately and prove a rollback to the baseline model.

**Completion check:** The serving boundary can roll back to the untuned baseline.

[Alternative · AR video](resources.md#r-ar-mini-19) (optional) · [Implementation reference](resources.md#r-ollama)

## Practical exercises

The step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.

- [ ] **L17-E1:** Write a decision memo contrasting missing knowledge with task/style adaptation.
  - **Pass:** Choose not to fine-tune when the failure evidence does not justify it.
- [ ] **L17-E2:** Design a training dataset card with schema, rights, privacy, deduplication, and splits.
  - **Pass:** Private journals are not implicitly repurposed as training data.
- [ ] **L17-E3:** Optionally run a tiny PEFT experiment on permitted data if resources allow.
  - **Pass:** Compare a prompt baseline on independent holdout; otherwise deliver a resource-aware experiment plan.
- [ ] **L17-E4:** Optionally compare quantized or batched local serving.
  - **Pass:** Report memory/latency/quality on the actual hardware; no invented runs.

## Ready to move on?

- [ ] Every numbered step has its stated output and completion check.
- [ ] All assessed exercise criteria pass, including failures/permissions where relevant.
- [ ] You can answer the [self-check](details.md#self-check) and explain one decision without generated code.
- [ ] Evidence links include reproducible commands/configuration and remaining limitations.

**Capstone checkpoint:** [S7](../project/milestones/s7.md). A conceptual decision can be completed without a GPU. Practical training is not marked done without run evidence. This module is optional for Core completion.

**Keep:** Customization decision, dataset card, and experiment plan; Run report only if a training/serving experiment was actually executed.

## What to defer

- Training a foundation model
- Paying for compute without a hypothesis and evaluation

## Record progress and choose the next Level

```bash
python scripts/progress.py set L17 completed --evidence "link-to-commit-and-test-report"
```

**Unlocks:** No further required Level; return to the capstone or role checklist.

[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)

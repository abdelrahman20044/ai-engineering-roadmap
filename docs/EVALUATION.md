# Evaluation and Evidence Standards

[Home](../README.md) · [L05](../05-Evaluation/README.md) · [Experiment template](../templates/EXPERIMENT.md)

Primary references: C3–4, C6, and F11. Evaluate components separately; HTTP200 does not establish answer quality. The following are project recommendations, not official ITI thresholds.

| Dataset rule | Application |
|---|---|
| Public seed | Twelve supplied synthetic cases are practice data, never unseen holdout |
| Development | Author approximately 30 reviewed cases covering normal and failure behavior |
| Final holdout | Keep approximately 20 additional cases independent of tuning |
| Labels | Query, answerability, expected facts, document/page/span evidence, category, and language |
| Human review | Do not accept model-generated labels or answers as gold without review |
| Changes | Preserve source-level labels when chunk IDs change |

| Component | Measure | Important distinction |
|---|---|---|
| Parsing | Text/page correctness and explicit failure reasons | Empty or scanned PDF is not a successful empty index |
| Retrieval | Hit@k and recall@k | Any required evidence versus the fraction of all required evidence retrieved |
| Generation | Correctness, groundedness, and relevance on 0–2 rubrics | Use oracle context to isolate generation failure |
| Citations | Valid IDs and actual claim support | An existing ID may still support nothing in the answer |
| Abstention | Appropriate no-answer and false-refusal rates | Refusing every query is not success |
| Agents | Task success, tool/argument errors, limit violations, and unauthorized attempts | Evaluate actions and outcomes, not just final prose |
| Context | Required facts retained, stale memory, and distractor effects | Longer context is not automatically better |
| Serving | p50/p95, TTFT, error rate, usage, and cost basis | Report workload, environment, sample count, and date |

| Check type | Dependencies | What it establishes |
|---|---|---|
| Unit/API | Fake providers | Contracts, branches, failures, and validation |
| Integration | Real test database/retriever | Ownership, persistence, metadata, and component boundaries |
| Live evaluation | Actual model with a separate budget | Model/application behavior under versioned inputs |
| Model judge | Calibrated against human review | Helpful imperfect scoring, not sole ground truth |

Keep a baseline and change one variable per experiment. Negative findings are valid evidence. Small latency samples are descriptive, not a general reliability benchmark. Record the source/date of prices rather than inventing current costs.

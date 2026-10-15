# L05 · Evaluation Engineering

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

| Tier | Personal effort | Difficulty | Priority | Prerequisites |
| --- | --- | --- | --- | --- |
| 2 · Reliable LLM Application Basics | 14–22 h | 3/5 | P0 | [L04](../04-LLM-Applications-Prompts/README.md) |

**Outcome:** Define datasets and rubrics before expanding the application. Distinguish deterministic tests, component evaluation, and end-to-end quality.

**Unlocks:** [L08](../08-RAG-Systems/README.md), [L12](../12-Tools-Agents/README.md), [L15](../15-Model-Selection-Optimization/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md)

## What to learn and exactly where

| Topic | Learn from | Apply it |
| --- | --- | --- |
| Evaluation datasets and criteria | C4 pp.160–178,200–207; [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | [Practice 1](resources.md#practice-and-evidence) |
| Exact checks and component evaluation | C3 pp.125–135; F11 PDF495–533; [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | [Practice 2](resources.md#practice-and-evidence) |
| AI judges and calibration | C3 pp.136–147; [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | [Practice 3](resources.md#practice-and-evidence) |
| Regression gates and uncertainty | C3 pp.114–117; C4 evaluation pipeline; [GitHub Actions Python guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | [Practice 4](resources.md#practice-and-evidence) |

## Syllabus provenance

- **N05** — Software Testing & Full-Stack Debugging.
- **N20** — AI Evaluation, Safety & Responsible AI.

| ITI topic IDs | Interpretation |
| --- | --- |
| N05, N20 | Official topic titles are mapped in the coverage matrix; individual tools, labs, sequencing, and personal hours are recommendations. |

## Study sequence

| Step | Action |
| --- | --- |
| 1 | Pass the prerequisites or record evidence for a diagnostic waiver. |
| 2 | Use the primary book section in resources.md; consult the focused tutorial for implementation. |
| 3 | Complete the exercises below in your own implementation repository. |
| 4 | Review the completion gate and link test results, commits, and decisions in the tracker. |

## Practical exercises

| ID | Implement or investigate | Acceptance evidence |
| --- | --- | --- |
| L05-E1 | Use the twelve public seed cases for practice and author thirty development cases. | Include answerable, no-answer, multi-evidence, language, and security categories; review labels manually. |
| L05-E2 | Create a separate holdout before tuning; label document/page/spans. | Do not call supplied examples unseen; preserve labels when chunk IDs change. |
| L05-E3 | Write 0–2 rubrics for correctness, groundedness, and relevance. | Calibrate a model judge against human review and document disagreements. |
| L05-E4 | Define an evaluation run manifest. | Record dataset/model/prompt/corpus versions, case count, latency, and cost or usage. |
| L05-E5 | Specify retrieval and tool metrics before those components are built. | Implement retrieval metrics in L08 and tool/task metrics in L12; do not claim these experiments are already complete. |

## Project checkpoint

| Milestone | Required artifacts | Pass condition |
| --- | --- | --- |
| [S3](../project/milestones/s3.md) | Authored evaluation data, rubric, and run manifest; A report showing real failures as well as successes | Explain what success means and why. Public seed data is not holdout, mocks do not assess model quality, and judges are not the sole source of truth. |

## Postpone

| Outside this level |
| --- |
| An elaborate evaluation platform before useful labels |
| Repeated tuning against the final holdout |

## Record completion

```bash
python scripts/progress.py set L05 completed --evidence "link-to-commit-and-test-report"
```

The tracker checks prerequisites and evidence fields; you assess the work against the gate.

[← Roadmap](../README.md) · [Resources](resources.md) · [Coverage](../docs/ITI_COVERAGE.md) · [Progress](../progress/PROGRESS.md)

Previous: [L04](../04-LLM-Applications-Prompts/README.md) · Next numbered Level: [L06](../06-Application-State/README.md). Follow the prerequisite table if branches differ.

# M05 — Evaluation Engineering

[Home](../../README.md) · [Roadmap](../../docs/ROADMAP.md) · [Reading](../../docs/READING_GUIDE.md) · [Progress](../../progress/README.md)

| Field | Value |
| --- | --- |
| Priority | P0 |
| Prerequisites | [M04](../m04-prompt-structured-output/README.md) |
| Personal effort | 14–22 focused hours; not official ITI hours |
| Project milestone | [S3](../../project/milestones/s3.md) |

## Learning outcomes

| ID | Demonstrate |
| --- | --- |
| O1 | Define datasets and rubrics before expanding the application. |
| O2 | Distinguish deterministic tests, component evaluation, and end-to-end quality. |

## Official ITI mapping

| Topic | Official title | Official hours |
| --- | --- | --- |
| N05 | Software Testing & Full-Stack Debugging | 30 |
| N20 | AI Evaluation, Safety & Responsible AI | 12 |

Topic IDs are local references. Official hours belong to syllabus topics, not this self-study module. See [coverage and limitations](../../docs/ITI_COVERAGE.md).

## Reading assignments

| Order | Assignment and depth |
| --- | --- |
| 1 | C4 pp. 200–207: Design Your Evaluation Pipeline; introduce during M00 and implement here. |
| 2 | C3 pp. 114–117 and 125–147: challenges, exact evaluation, AI judges, and limitations. |
| 3 | C4 pp. 160–178: criteria; F11 PDF 495–533: model testing and retrieval/behavioral evaluation. |

G = Grokking; F = FastAPI; C = Chip Huyen. G/C use printed pages; F uses PDF viewer pages. See [source verification](../../docs/SOURCES.md).

## Exercises

| ID | Build or investigate | Acceptance evidence |
| --- | --- | --- |
| M05-E1 | Use the twelve public seed cases for practice and author thirty development cases. | Include answerable, no-answer, multi-evidence, language, and security categories; review labels manually. |
| M05-E2 | Create a separate holdout before tuning; label document/page/spans. | Do not call supplied examples unseen; preserve labels when chunk IDs change. |
| M05-E3 | Write 0–2 rubrics for correctness, groundedness, and relevance. | Calibrate a model judge against human review and document disagreements. |
| M05-E4 | Define an evaluation run manifest. | Record dataset/model/prompt/corpus versions, case count, latency, and cost or usage. |
| M05-E5 | Specify retrieval and tool metrics before those components are built. | Implement retrieval metrics in M08 and tool/task metrics in M12; do not claim these experiments are already complete. |

## Completion gate

| Requirement | Evidence |
| --- | --- |
| Artifacts | Authored evaluation data, rubric, and run manifest; A report showing real failures as well as successes |
| Pass condition | Explain what success means and why. Public seed data is not holdout, mocks do not assess model quality, and judges are not the sole source of truth. |
| Independent understanding | Explain the implementation and make one small change without copying an AI-generated solution. |
| Record | Use the [evidence](../../templates/EVIDENCE.md) and [experiment](../../templates/EXPERIMENT.md) templates; link commits, tests, and reports. |

Run from the repository root after reviewing your work:

```bash
python scripts/progress.py set M05 completed --evidence "path-or-url-to-your-evidence"
```

The tracker checks prerequisites and evidence fields; it does not assess the quality of your application.

## Defer

| Keep out of this module |
| --- |
| An elaborate evaluation platform before useful labels |
| Repeated tuning against the final holdout |

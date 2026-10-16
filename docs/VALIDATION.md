# Repository validation

[Home](../README.md) · [Learning-experience audit](LEARNING_EXPERIENCE_AUDIT.md) · [Resource audit](RESOURCE_AUDIT.md)

The offline checks cover all 19 guided READMEs, libraries and detail pages; 113 ordered topic steps; 153 retained resources; 52 reading-ledger entries; 30 verified chapter locators; 84 assessed exercises; eight unchanged capstone contracts; and all 32 ITI rows. The advertised 678 / listed 696 training-hours discrepancy remains documented.

Run:

```bash
python scripts/audit_level_content.py
python scripts/validate.py
python -m unittest discover -s tests -v
```

The Level audit validates prominent next actions, one typed Primary per step, tasks/checks, roles and selected portions, first-use reading order, isolated rendering consistency, and Markdown file/directory/fragment targets. A baseline ledger prevents silent removal of original resource/topic research or alteration of prerequisites, tasks, gates, syllabus mapping, milestones and learner progress.

The general validator also checks the prerequisite DAG, ITI coverage, tracker evidence fields, synthetic evaluation data, SVG and standalone HTML links. Ten existing tooling tests exercise tracker and structural behavior. CI runs the same offline checks; external URLs are intentionally separate from CI.

`python scripts/audit_resources.py` performs a dated GET reachability check (network required). HTTP 200 does not prove topical completeness, playback, paid enrollment or learner competence. The first-action placement check is a usability heuristic, not a timed learner test. The preservation audit is a guardrail for this refactor, not a prohibition on future reviewed curriculum improvements.

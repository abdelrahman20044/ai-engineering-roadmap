# Repository Guide

[Home](../README.md) · [Progress](../progress/README.md) · [Book order](READING_GUIDE.md)

Start with README.md, START_HERE.md, then the next unlocked Level. This repository holds the learning roadmap; implement the Reflection Assistant in a separate application repository and link its evidence here.

| Path | Purpose |
|---|---|
| Each Level/README.md | Ordered learning journey with primary resources, reading, tasks and checks |
| Each Level/resources.md | Topic-grouped resource tables with bounded choices and complementary sequences |
| Each Level/details.md | Diagnostic, full scope, debugging, self-check and ITI provenance |
| docs/READING_GUIDE.md | Chronological first-reading queue and review statuses |
| docs/CHAPTER_MAP.md | Verified chapter locations, assigned slices and split rationale |
| docs/reading_plan.json | Authoritative book ledger and first-use order |
| docs/RESOURCE_CATALOG.json | Retained research, topic mapping, formats and original source metadata |
| docs/RESOURCE_GROUPS.json | Active topic-specific roles, required complements, alternatives and portion bounds |
| curriculum.json | Prerequisites, exercises, gates, evidence and reading IDs |
| project/milestones | Eight capstone acceptance contracts |
| exercises/data | Synthetic practice data; no real journals |
| progress | Editable tracker and generated learner dashboard |
| templates | Authoring contracts and evidence templates |
| scripts / tests | Rendering, audits, packaging, progress and tooling tests |
| docs/learning_refactor_baseline.json | Pre-refactor preservation ledger tied to a Git commit |

## Maintaining the roadmap

Edit the JSON sources, then run:

```bash
python scripts/render_learning.py
python scripts/audit_level_content.py
python scripts/build_overview.py
python scripts/validate.py
python -m unittest discover -s tests -v
```

`scripts/resource_tables.py` renders the resource tables. Existing catalog Level-wide role fields are historical associations; active choices come from RESOURCE_GROUPS. Only the optional HTML rebuild requires Pandoc. The Level audit checks generated pages against a fresh isolated render. It also detects removed research, changed gates/prerequisites, broken Markdown fragments and inconsistent reading IDs. Update the preservation ledger only for an intentional, reviewed curriculum change; do not regenerate it just to silence a failure.

For live external URL rechecking run `python scripts/audit_resources.py` (network required). For a portable copy run `python scripts/package_repo.py output/roadmap.zip`; Git metadata, caches, secrets and book PDFs are excluded. OVERVIEW.html is a standalone optional reader; GitHub Markdown is the primary experience.

Use `python scripts/progress.py next` to choose unlocked work. Learner progress is not altered by rendering. Keep personal journals and copyrighted book text out of this repository.

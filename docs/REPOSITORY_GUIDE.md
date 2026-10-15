# Repository Guide

[Home](../README.md) · [Progress](../progress/README.md)

Extract the ZIP and open the folder in VS Code or browse the Markdown on GitHub. Start with README.md, then START_HERE.md. The standalone OVERVIEW.html requires no installation.

| Path | Purpose |
|---|---|
| modules | Individual learning contracts: prerequisites, reading, exercises, and gates |
| docs | Roadmap, syllabus mapping, readings, sources, and engineering guidance |
| project/milestones | S0–S7 delivery criteria |
| exercises/data | Synthetic public practice data |
| templates | Evidence and decision/report templates |
| progress | Editable CSV and learner evidence |
| scripts | Validation, progress, HTML rebuilding, and packaging |
| assets | SVG roadmap and reader styling |
| tests | Tests for repository tools, not the future AI application |
| curriculum.json | Machine-readable module manifest |
| .github/workflows | Optional GitHub CI after you push the repository |

| Action | Command from repository root |
|---|---|
| Validate content | `python scripts/validate.py` |
| Test tooling | `python -m unittest discover -s tests -v` |
| Find next work | `python scripts/progress.py next` |
| Start | `python scripts/progress.py set M00 in_progress` |
| Rebuild the reader | `python scripts/build_overview.py` — requires optional Pandoc |
| Create a ZIP | `python scripts/package_repo.py path/to/roadmap.zip` |

## Put it on GitHub

| Step | Action |
|---|---|
| 1 | Create an empty GitHub repository under your account |
| 2 | Open a terminal inside the extracted repository and run `git init` |
| 3 | Review files and run the validation commands |
| 4 | Commit the roadmap and push to the remote you created |
| 5 | Keep application code in a separate implementation repository and link evidence here |

The roadmap repository is available at https://github.com/abdelrahman20044/ai-engineering-roadmap. The ZIP excludes caches, secrets, and book PDFs. Do not commit personal journals or copyright-protected book text. Libraries for application/ML exercises are installed only when needed, in separate environments.

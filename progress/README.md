# Progress Tracker

[Home](../README.md) · [GitHub progress tables](PROGRESS.md) · [Tracker CSV](tracker.csv) · [Evidence](evidence/README.md)

All 19 modules and8 milestones start at `not_started`. Core and optional progress are reported separately; waivers are visible rather than silently counted as completed study.

| Action | Command |
|---|---|
| View status | `python scripts/progress.py status` |
| Refresh GitHub tables | `python scripts/progress.py export` |
| Find eligible work | `python scripts/progress.py next` |
| Start a module | `python scripts/progress.py set M00 in_progress` |
| Record completion | `python scripts/progress.py set M00 completed --evidence "progress/evidence/m00.md"` |
| Record an earned waiver | `python scripts/progress.py set M01 waived --evidence "your-test-report" --reason "passed every gate independently"` |
| Reopen work | `python scripts/progress.py set M00 not_started` |

| Status | Rule |
|---|---|
| not_started | No completion claimed |
| in_progress | Hard prerequisites must be accepted |
| completed | Prerequisites and an evidence field are required |
| waived | Prerequisites, evidence, and a diagnostic reason are required |
| blocked | A reason is required; use it to document a real blocker |

Run commands from the repository root. Reopening a prerequisite is rejected while an active descendant depends on it; reopen descendants first. Manual CSV edits can be checked with validate.py. Tool-generated timestamps use UTC.

The set command refreshes PROGRESS.md automatically for the default tracker. After manual CSV edits, run export. The HTML overview is a build-time snapshot; rebuild it if you want its progress tables refreshed.

The CLI checks sequence and fields, not skill quality or whether a report proves its claims. Review evidence yourself. M16/M18 do not block Core completion. No learning outcomes have been completed on your behalf.

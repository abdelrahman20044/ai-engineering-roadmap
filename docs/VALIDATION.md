# Repository validation

[Home](../README.md)

| Check | Result |
| --- | --- |
| Numbered Level directories | 19; each has a meaningful README.md and resources.md |
| Tier structure | Six tiers, including an explicit optional tier |
| ITI representation | All 32 brochure rows mapped; 678 advertised / 696 listed hours discrepancy retained |
| Prerequisites | No missing IDs or dependency cycles |
| Internal Markdown links | File/directory targets and heading fragments checked |
| Tooling tests | 10 passed, including prerequisite, evidence, waiver, and broken-link behavior |
| Capstone | Eight milestone files and machine-readable prerequisites |
| External resources | 30 distinct URLs returned HTTP 200 during this rebuild; availability can change |
| Excluded resource | Starlette responses URL returned 502; replaced with the accessible FastAPI tutorial, with streaming taught primarily by FastAPI book chapter 6 |
| Source books | Chapter references only; no book PDFs redistributed |
| GitHub publication | The connected GitHub plugin returned 404 for the existing private target; this complete rebuild is provided as a ready-to-push ZIP |

Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` after editing. External URLs require network access; the default validator does not fail offline because a remote service is temporarily unavailable.

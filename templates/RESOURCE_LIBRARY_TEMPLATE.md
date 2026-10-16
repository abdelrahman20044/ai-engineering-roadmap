# Resource-library authoring contract

[Home](../README.md) · [Level template](LEVEL_TEMPLATE.md)

Add resources to `docs/RESOURCE_CATALOG.json`; generate cards with `python scripts/render_learning.py`. Keep retained resources unless there is a documented correction; alternatives are not a completion list.

## Each card contains

- Exact title and verified URL, with stable `r-<catalog-id>` anchor.
- **Resource Type:** Single video; YouTube playlist; full course; short course; documentation; engineering article; notebook/lab; repository; translated lesson; or another accurate format.
- **Role:** Primary, Alternative, Reference or Optional Advanced, specific to this Level.
- Language (including translated text versus Arabic video), provider and access terms.
- **Use for:** mapped topic names.
- **Assigned portion:** named lessons, sections or exact linked video; only verified lesson numbers/timestamps. Explicitly label unverified identifiers and bound the task by subject instead.
- Scope, known limits/version cautions, and partial Arabic coverage where relevant.

## Categorization

Keep Arabic/Egyptian teaching, English video/courses, slides/notebooks/repos, paid alternatives, labs/quizzes, official docs/articles, and optional advanced material easy to scan. Book references link the master ledger and chapter index; do not reassign whole chapters here.

Do not treat a playlist query parameter on a single video as a playlist assignment. Do not imply an entire course is required when the Level needs only named units. Prefer one primary route; paid resources remain alternatives. A successful HTTP request verifies reachability, not instructional completeness or video playback.

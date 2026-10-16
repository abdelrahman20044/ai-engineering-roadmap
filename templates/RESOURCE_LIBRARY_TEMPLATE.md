# Resource-library table authoring contract

[Home](../README.md) · [Level template](LEVEL_TEMPLATE.md) · [Resource policy](../docs/RESOURCE_POLICY.md)

Resource libraries are **topic-grouped Markdown tables**. Keep README pages sequential and keep deeper diagnostics in details.md. Edit `docs/RESOURCE_GROUPS.json` for active choices/roles and `docs/RESOURCE_CATALOG.json` for retained source research, then render.

## Every topic group

1. Use stable `unit-01`, `unit-02`, … anchors matching README step order.
2. State the exact topic/subtopics.
3. Give a required sequence: assigned book slice, one primary explanation and any explicitly required complementary capability.
4. If an Alternative exists, name both IDs and the exact shared scope: **Choose ONE A OR B for this concept**. Identify material that still must be studied. Partial overlap never implies whole-route equivalence.
5. Name implementation references separately. Explain that other complements are as-needed support; only named required complements are mandatory.
6. Render a five-column table: **Resource · Provider · Language | Resource Type | Role in this group | Topic / subtopic | Study only**.
7. Keep cells concise. Put full selection bounds, relationship notes, access, verification and version limits in expandable notes. Preserve direct source URLs and old `r-…` anchors.

## Roles and formats

Primary, Alternative, Complementary, Reference and Optional Advanced apply **within one group**. The same source can play a different role in another group. A testing lesson cannot replace a routing lesson. A source covering only orientation is an as-needed complement, not a full implementation alternative.

Distinguish Single Video, Single Video (part of playlist), Playlist, Full Course, Short Course, Article, Documentation, Book Section and Lab as appropriate. Do not infer a playlist assignment from a video URL’s playlist parameter. Course selections use verified lesson/section titles; unverified lesson identifiers/timestamps must be labelled. No entire long course is required by default.

Book rows link the unchanged master reading ledger and retain first-use/review status; they do not create a second reading plan. Include all retained Arabic/Egyptian teaching, English teaching, practice, paid choices, advanced depth and documentation. Update the [all-Level table audit](../docs/RESOURCE_TABLE_AUDIT.md) and run the repository checks.

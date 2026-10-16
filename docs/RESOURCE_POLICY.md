# Resource selection and verification policy

[Roadmap](../README.md) · [Level audit](RESOURCE_AUDIT.md) · [Book order](READING_GUIDE.md) · [Chapter locator](CHAPTER_MAP.md)

## How the library is curated

| Decision | Rule |
| --- | --- |
| Topic first | A resource must teach a named topic, supply a relevant implementation reference, or support a specific exercise. A channel homepage is not used as a substitute for a lesson. |
| One practical route | The owned book/article, one explanation and the actual project exercise form the path. Extra courses are alternatives, not cumulative prerequisites. |
| Arabic teaching | Identify the instructor and specific lesson where available. Egyptian mini-RAG, Python, ML and TypeScript teaching is distinguished from translated text. |
| Arabic translations | Microsoft translations identify Co-op Translator. They are labelled machine-translated text; the linked English video is not called Arabic instruction. |
| Partial coverage | When an Arabic lesson supplies only prerequisites or orientation, the topic row states that boundary. A missing exact resource is recorded as a gap. |
| English teaching | Prefer course/lecture pages containing real videos, notebooks or exercises. Current official docs resolve API/version differences. |
| Paid alternatives | Recommend only a clearly relevant alternative with an explicit reason to buy. No new paid course is necessary for completion. |
| Practice | Distinguish self-assessed local tasks from platform quizzes, automated checks and hosted labs. A concept quiz does not assess a working system. |
| Advanced material | Papers and deeper serving/agent patterns follow demonstrated need. They do not block the first working application. |

## What was verified

The discovery process inspected author/publisher course outlines, instructor lesson indexes, official documentation pages and relevant content excerpts. For mini-RAG, the instructor's `tut-017` README lists direct video titles and matching code branches; the older `main` README stops earlier. Hesham Asem's own course index identifies the ML playlists. Elzero's study plans identify lesson subjects and assignments. DeepLearning.AI pages show lesson outlines and access terms. Microsoft Arabic lesson pages were opened after correcting their translation paths.

The final HTTP audit issues GET requests, follows redirects and records status, final URL, page title and check date. The machine-readable evidence is in `RESOURCE_VERIFICATION.json`. This verifies reachability at a point in time; a 200 response alone does not prove instructional quality. Topic assignment was separately reviewed against the source's title, outline or documentation scope.

## Verification limits

- Not every video was watched end-to-end. Arabic video topic identity is supported by instructor-authored lesson/course indexes and reachable lesson URLs; playable media can still vary by account, region or later removal.
- Paid enrollments and account-only assessments were not purchased or completed. Regional prices are not invented. Auto-generated Arabic subtitles do not make an English course an Arabic course.
- DeepLearning.AI advertises limited-time free course access and separately promotes Pro accomplishments. Access and assessment terms can change; the official/local alternative remains available.
- Historical courses can teach valid architecture while showing obsolete dependencies. Specific cautions are retained in the topic tables and expandable source notes.
- Book assignments use the three supplied PDFs' verified contents and page conventions. Books are referenced, not redistributed. No additional chapter numbers were guessed.
- These resources and practice questions are recommendations. They are not an official ITI reading list or confirmed interview questions.

## Recheck after editing

```bash
python scripts/audit_level_content.py
python scripts/audit_resources.py
python scripts/validate.py
```

The content audit runs offline. The resource audit needs network access and reports failures rather than silently replacing a URL or treating a login wall as proof of full access. Review failures before changing a curated assignment.

## Learning selection in this edition

**Resource Type** and **Role** answer different questions. Type says what the link is (one video, playlist, full/short course, documentation, article or lab); Role says how to use it in this Level (Primary, Alternative, Reference or Optional Advanced). The README chooses one Primary per step and links its matching topic group. Roles apply per group, not across the Level. The full library is preserved without requiring all alternatives.

Assigned portions name verified lessons or sections where available. For Elzero and the mini-RAG instructor index, identified lesson numbers/titles are retained. DeepLearning.AI uses named lessons, not invented timestamps. Where individual playlist identifiers could not be confirmed, the card says so and gives a subject boundary; those playlists are alternatives. Documentation assignments distinguish actual source APIs from engineering decisions you must design yourself.

`RESOURCE_GROUPS.json` is authoritative for topic-specific resource choices. Its Alternative scope must identify what overlaps and what still needs separate study. Required complementary sources add a distinct capability; as-needed complements are optional support. Consult Reference rows while implementing. Original catalog Level-wide roles remain historical metadata, not active study decisions.

Only `reading_plan.json` assigns new book reading. The master order and Level pages are rendered from it; the chapter map is a locator. Original topic-to-book associations remain research metadata, not additional homework. Later appearances explicitly say Previously Covered / Review Only. A chapter split identifies bounded sections and one first-use owner for each.

For the new information architecture and its all-Level checks see [Learning Experience Audit](LEARNING_EXPERIENCE_AUDIT.md). The dated HTTP catalog report is preserved as historical verification; this refactor does not claim every course or video was replayed.

## Table presentation

Resource libraries use five consistent columns, with provider/language under the linked title and full bounds in expandable notes. Every README step links a stable topic-group anchor. No source, access caveat, partial-Arabic note or verified direct lesson is removed to shorten cells. See the [topic-table audit](RESOURCE_TABLE_AUDIT.md).

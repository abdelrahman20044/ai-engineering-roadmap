# Resource selection and verification policy

[Roadmap](../README.md) · [Level audit](RESOURCE_AUDIT.md) · [Book locator](READING_GUIDE.md)

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
- Historical courses can teach valid architecture while showing obsolete dependencies. Specific cautions are retained in the resource tables.
- Book assignments use the three supplied PDFs' verified contents and page conventions. Books are referenced, not redistributed. No additional chapter numbers were guessed.
- These resources and practice questions are recommendations. They are not an official ITI reading list or confirmed interview questions.

## Recheck after editing

```bash
python scripts/audit_level_content.py
python scripts/audit_resources.py
python scripts/validate.py
```

The content audit runs offline. The resource audit needs network access and reports failures rather than silently replacing a URL or treating a login wall as proof of full access. Review failures before changing a curated assignment.

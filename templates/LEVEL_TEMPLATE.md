# Level page authoring template

Use this contract when maintaining a numbered Level. This is an authoring guide; the live Level pages contain the actual curriculum.

| Section | Required content |
| --- | --- |
| Title and metadata | Level ID/title, Tier, personal effort, difficulty, priority, required prerequisites and unlocked Levels. |
| Why this Level matters | Concrete engineering ability and its role in the same capstone. |
| Prerequisites and quick diagnostic | Three observable checks that reuse prior backend/Python/SQL experience. |
| Learning objectives | Checkboxes stating verifiable topic outcomes. |
| Recommended learning path | A selected reading/video/build order and a stopping rule. |
| What you learn and exactly where | Topic ID, important subtopics, direct Arabic choice or gap, direct English choice and practical output. Mark partial Arabic scope. |
| Book and article focus by topic | Exact verified chapter/section/page, implementation reference, and explicit gaps. |
| ITI syllabus and industry additions | Exact official module titles; distinguish recommended subtopics, tools, labs and hours. |
| Practical exercises | Independent task, failure cases and acceptance evidence. |
| Common mistakes and debugging guidance | Three Level-specific failure patterns and concrete corrections. |
| Self-check before moving on | Three original reasoning questions with an answer guide; never label inferred questions official. |
| Capstone checkpoint | Existing milestone and artifacts, with its acceptance contract. |
| Completion criteria | Observable behavior, tests, independent explanation and evidence. |
| Postpone until justified | Specific scope boundaries, not a generic advanced-topic list. |
| Record completion and navigation | Tracker command plus main/resources/previous/next links. |

Edit the corresponding topic map in `docs/RESOURCE_CATALOG.json` with the page. Retain source metadata and re-run the content/link audit. A resource belongs in a topic row only if its documented scope supports that assignment; otherwise label it prerequisite/orientation or remove it.

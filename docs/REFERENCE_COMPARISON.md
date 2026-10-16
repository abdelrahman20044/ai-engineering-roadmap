# Reference-Level Comparison and Revision

[Roadmap](../README.md) · [Audit](RESOURCE_AUDIT.md)

Structural reference: [Yahia Sherif’s Data Engineering Roadmap 2026](https://github.com/Yahiasherif002/Data-Engineering-Roadmap-2026), inspected at commit `4ba9d36fbfc809e7ebb087e651e1df86aea6f2bc`. The following are comparable engineering roles in the curriculum, not claims that AI and Data Engineering subjects are interchangeable. No Data Engineering specialization, advertised hours or level count was imported.

| Representative purpose | Reference README + resources | AI README + resources | Finding and implemented change |
| --- | --- | --- | --- |
| Foundation/API transfer | [04-Python](https://github.com/Yahiasherif002/Data-Engineering-Roadmap-2026/tree/4ba9d36fbfc809e7ebb087e651e1df86aea6f2bc/04-Python) | [01-Python-FastAPI](../01-Python-FastAPI/README.md) | Reference connects topics to Arabic and English teaching and gives a categorized resource library. AI L01 previously had four documentation links. It now distinguishes Python remediation, API validation, lifecycle, testing and their matching lessons/references. |
| Production quality/operations | [23-Governance-Quality-Observability](https://github.com/Yahiasherif002/Data-Engineering-Roadmap-2026/tree/4ba9d36fbfc809e7ebb087e651e1df86aea6f2bc/23-Governance-Quality-Observability) | [14-LLMOps-Deployment](../14-LLMOps-Deployment/README.md) | Reference separates teaching, practice, documentation and optional depth and admits Arabic scarcity. AI L14 previously reused Docker links for recovery. It now maps deployment, CI, versions, telemetry and recovery to distinct resources and an actual restore drill. |
| Capstone/evidence | [26-Capstone](https://github.com/Yahiasherif002/Data-Engineering-Roadmap-2026/tree/4ba9d36fbfc809e7ebb087e651e1df86aea6f2bc/26-Capstone) | [16-Capstone-Career](../16-Capstone-Career/README.md) | Reference treats capstone as an evidence-producing system. AI L16 previously had four broad references. It now supplies release, evaluation, defense, role-specific communication and independent implementation guidance with matched learning resources. |

## Measured before/after inventory

These counts help detect an incomplete rewrite; they are not a score for quality. “URL occurrences” includes repeats in topic/resource tables, so the catalog’s distinct-resource counts are the better breadth measure.

| Comparable file | Version | Major sections | URL occurrences | Approx. words |
| --- | --- | --- | --- | --- |
| 01-Python-FastAPI/README.md | Reference | 3 | 22 | 373 |
| 01-Python-FastAPI/README.md | AI before | 7 | 4 | 575 |
| 01-Python-FastAPI/README.md | AI revised | 14 | 26 | 1744 |
| 01-Python-FastAPI/resources.md | Reference | 9 | 47 | 1251 |
| 01-Python-FastAPI/resources.md | AI before | 4 | 4 | 552 |
| 01-Python-FastAPI/resources.md | AI revised | 10 | 19 | 1952 |
| 14-LLMOps-Deployment/README.md | Reference | 3 | 22 | 373 |
| 14-LLMOps-Deployment/README.md | AI before | 7 | 4 | 612 |
| 14-LLMOps-Deployment/README.md | AI revised | 14 | 27 | 1818 |
| 14-LLMOps-Deployment/resources.md | Reference | 9 | 58 | 1377 |
| 14-LLMOps-Deployment/resources.md | AI before | 4 | 4 | 532 |
| 14-LLMOps-Deployment/resources.md | AI revised | 10 | 15 | 1821 |
| 16-Capstone-Career/README.md | Reference | 3 | 26 | 378 |
| 16-Capstone-Career/README.md | AI before | 7 | 4 | 621 |
| 16-Capstone-Career/README.md | AI revised | 14 | 28 | 1864 |
| 16-Capstone-Career/resources.md | Reference | 9 | 46 | 1219 |
| 16-Capstone-Career/resources.md | AI before | 4 | 4 | 519 |
| 16-Capstone-Career/resources.md | AI revised | 10 | 26 | 2244 |

## Consistent internal contract

| README | resources.md |
| --- | --- |
| Prerequisites + diagnostic, objectives and selected path | Arabic/Egyptian materials; English videos and teaching |
| Topic/subtopic → Arabic/English → practical output | Slides/notebooks/code; paid alternatives |
| Topic → verified book/article focus + implementation reference | Your three books/article; external practice/labs/quizzes |
| Official ITI titles separated from recommended detail | Official docs/engineering; optional advanced material |
| Assessed exercises, pitfalls and original self-check with answer guide | Per-resource provider, language, access, topic assignment and limits |
| Capstone acceptance, checklist, postpone and tracker navigation | Stop rules, duplicate-reading guidance and verification date |

The authoring contracts are [Level template](../templates/LEVEL_TEMPLATE.md) and [resource-library template](../templates/RESOURCE_LIBRARY_TEMPLATE.md). All 19 pairs are audited, including later Levels. The reference’s visual grouping and category approach inform the organization; its wording, broad channel links and subject-specific recommendations are not copied.

# Level Content and Resource Audit

[Roadmap](../README.md) · [Selection policy](RESOURCE_POLICY.md) · [Reference comparison](REFERENCE_COMPARISON.md)

Audit date: **16 October 2026**. The audit covers all 19 Levels, including optional fine-tuning and the supporting UI. The AI Engineering scope and the original ITI mapping remain unchanged.

| Check | Result |
| --- | --- |
| Level pairs | 19 READMEs + 19 resource libraries rewritten with the same section contract. |
| Topic mapping | 113 important topic groups have subtopics, Arabic choice/gap, English route, book/article focus, implementation reference and practical output. |
| Resource catalog | 153 distinct assigned resources. Each has provider, language, format, access terms, purpose and scope limitation. |
| Reachability | 153/153 catalog URLs returned HTTP 200 in the final GET audit; redirects/titles are retained in RESOURCE_VERIFICATION.json. |
| Arabic labels | Egyptian/Arabic videos are separated from Microsoft machine-translated Arabic text. Partial matches and exact-topic gaps are disclosed. |
| Books | Existing supplied-PDF chapter/page assignments retained; no new unverified chapter numbers and no book redistribution. |
| External assessment | Platform quizzes/labs are labelled separately from the Level’s self-assessed drills and original questions. |
| Prerequisites and projects | Existing dependency graph, 84 assessed exercises, eight milestones and evidence tracker retained. |

## Per-Level coverage

| Level | Topic groups | Distinct resources | AR video resources | AR translated lessons | EN video/course resources | No exact AR row | Partial AR rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [L00](../00-Orientation/README.md) | 5 | 19 | 5 | 2 | 4 | 0 | 0 |
| [L01](../01-Python-FastAPI/README.md) | 6 | 19 | 5 | 0 | 3 | 0 | 3 |
| [L02](../02-Mathematics-ML/README.md) | 6 | 15 | 4 | 0 | 3 | 0 | 2 |
| [L03](../03-Deep-Learning-Foundation-Models/README.md) | 6 | 14 | 2 | 2 | 4 | 0 | 1 |
| [L04](../04-LLM-Applications-Prompts/README.md) | 6 | 19 | 4 | 3 | 3 | 0 | 1 |
| [L05](../05-Evaluation/README.md) | 6 | 13 | 0 | 3 | 4 | 3 | 1 |
| [L06](../06-Application-State/README.md) | 6 | 11 | 2 | 0 | 1 | 0 | 3 |
| [L07](../07-Embeddings-Semantic-Search/README.md) | 6 | 20 | 7 | 1 | 3 | 0 | 1 |
| [L08](../08-RAG-Systems/README.md) | 6 | 17 | 2 | 2 | 2 | 1 | 2 |
| [L09](../09-Context-Memory/README.md) | 6 | 12 | 0 | 4 | 2 | 0 | 0 |
| [L10](../10-Concurrency-Streaming-Jobs/README.md) | 6 | 13 | 2 | 0 | 1 | 3 | 1 |
| [L11](../11-Security-Responsible-AI/README.md) | 6 | 17 | 2 | 4 | 2 | 0 | 1 |
| [L12](../12-Tools-Agents/README.md) | 6 | 18 | 1 | 5 | 4 | 0 | 0 |
| [L13](../13-MCP-Enterprise-Integration/README.md) | 6 | 14 | 1 | 3 | 1 | 0 | 1 |
| [L14](../14-LLMOps-Deployment/README.md) | 6 | 15 | 2 | 1 | 2 | 0 | 1 |
| [L15](../15-Model-Selection-Optimization/README.md) | 6 | 19 | 2 | 4 | 4 | 0 | 4 |
| [L16](../16-Capstone-Career/README.md) | 6 | 26 | 6 | 4 | 5 | 0 | 0 |
| [L17](../17-Fine-Tuning-Advanced-Serving/README.md) | 6 | 14 | 2 | 2 | 2 | 1 | 2 |
| [L18](../18-Supporting-Frontend/README.md) | 6 | 12 | 2 | 3 | 2 | 0 | 4 |

Counts describe choices, not required course completions or quality scores. A single course can support multiple Levels through different named lessons. Translated material is not counted as Arabic video. Rows with partial Arabic support explicitly say what remains to learn in English. See each topic’s scope note rather than assuming that every listed language covers every subtopic.

## Direct comparison and review

The review inspected both files in reference Python, Governance/Quality/Observability and Capstone Levels and compared them with AI L01, L14 and L16 before and after revision. [The comparison](REFERENCE_COMPARISON.md) records the structural changes and source revision. All other Levels use the same template and audit contract.

## Reproducible checks

```bash
python scripts/audit_level_content.py
python scripts/validate.py
python -m unittest discover -s tests -v
# Requires network; writes a fresh dated status report:
python scripts/audit_resources.py
```

The offline audit checks required sections, topic fields, mapped IDs, minimum resource variety, and every Markdown file/directory/heading-fragment target. It cannot judge pedagogy or learner competence. Source relevance was reviewed separately against the publisher/instructor material; full video playback, paid access and every hosted assessment were not tested.

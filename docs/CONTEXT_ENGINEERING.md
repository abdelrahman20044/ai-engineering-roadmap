# Context Engineering

[Home](../README.md) · [M09](../modules/m09-context-memory/README.md) · [M12](../modules/m12-tools-agents/README.md)

Anthropic’s article motivates deliberate context selection and maintenance, retrieval when needed, and strategies for long-running work. The applications below are proposed project exercises, supported by C5 context efficiency and C6 memory; they are not mandatory steps from the article.

| Concept | Module | Project exercise |
|---|---|---|
| Prompt versus context | M04/M09 | Separate instructions from evidence, history, journals, and memory |
| Context rot | M09 | Compare focused context against distracting material |
| Selection | M08/M09 | Budget and prioritize retrieved evidence and recent turns |
| Just-in-time retrieval | M12 | Load a permitted passage through a bounded tool |
| Tool design | M12 | Clear schemas, concise results, and useful errors |
| Compaction | M09 | Test retention of required facts before/after summarization |
| Structured memory | M09 | Owner/source/date with correction and deletion |
| Sub-agents | M12 | Optional comparison using isolated context and a summary contract |

| Product boundary | Requirement |
|---|---|
| Journals | The user chooses what enters context |
| Memory | Editable, sourced, dated, and scoped; avoid automatic permanent personality conclusions |
| Summaries | Preserve covered message ranges and evidence provenance; stale summaries may be wrong |
| Authorization | The server authorizes access before loading content into context |
| Testing | Measure lost facts, stale values, contradictory entries, and deletion behavior |

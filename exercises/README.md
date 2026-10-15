# Exercises and Synthetic Data

[Home](../README.md) · [Evaluation](../docs/EVALUATION.md)

Every module has an exercise table with a task and acceptance evidence. There are84 exercises across19 modules. Implement the application yourself; repository tooling does not solve the labs.

| File | Contents | Use |
|---|---|---|
| [corpus.jsonl](data/corpus.jsonl) | Seven synthetic pages, multiple owners, and an injection example | Retrieval, provenance, and authorization practice |
| [eval_seed.jsonl](data/eval_seed.jsonl) | Twelve public examples | Initial functional and evaluation practice, never holdout |
| [journals.jsonl](data/journals.jsonl) | Three synthetic entries, including another owner | Journal connections and isolation |

Evidence uses `document_id:page`. Preserve a mapping when chunking changes. Expected concepts are review guidance, not exact-string gold answers. Add independent holdout examples and representative language cases yourself. Permission checks precede retrieval of another user’s content.

| Step | Work |
|---|---|
| 1 | Read the module outcome, inputs, outputs, and failure conditions |
| 2 | Define an acceptance test before expanding implementation |
| 3 | Build the simplest solution and test invalid/empty/unauthorized cases |
| 4 | Save an [evidence note](../templates/EVIDENCE.md) and update the tracker |

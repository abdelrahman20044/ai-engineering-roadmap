# Prerequisite Roadmap

[Home](../README.md) · [Manifest](../curriculum.json) · [Progress](../progress/README.md)

![Learning stages](../assets/roadmap.svg)

The SVG presents learning stages. The graphs and manifest define exact dependencies; arrows mean hard prerequisites. Numbers do not force independent modules to wait.

## Foundation path

```mermaid
flowchart TD
  M00["M00 Scope and diagnostics"] --> M01["M01 Python and FastAPI"]
  M00 --> M02["M02 Math and ML"]
  M00 --> M03["M03 DL and foundation models"]
  M01 --> M04["M04 Prompts and LLM integration"]
  M03 --> M04
  M04 --> M05["M05 Evaluation"]
  M01 --> M06["M06 Persistence"]
```

M02 progresses alongside implementation and remains required for Core. M03 needs basic vector intuition; use M02-E1 if needed without blocking the first API on an entire ML course.

## Grounded and reliable application

```mermaid
flowchart TD
  M03["M03 Models"] --> M07["M07 Documents and embeddings"]
  M06["M06 Persistence"] --> M07
  M07 --> M08["M08 RAG"]
  M05["M05 Evaluation"] --> M08
  M08 --> M09["M09 Context and memory"]
  M08 --> M10["M10 Async and jobs"]
  M08 --> M11["M11 Security"]
  M06 --> M11
```

## Agents, operations, and optional depth

```mermaid
flowchart TD
  Ready["M05 + M09 + M11"] --> M12["M12 Tools and agents"]
  M12 --> M13["M13 MCP and workflows"]
  Service["M10 + M11"] --> M14["M14 LLMOps and deployment"]
  M14 --> M15["M15 Optimization and feedback"]
  Eval["M05"] --> M15
  M13 --> M17["M17 Capstone"]
  M15 --> M17
  Foundations["M02 + M03 + remaining Core"] --> M17
  Advanced["M02 + M03 + M05 + M15"] --> M16["M16 Optional customization"]
```

Grouped nodes abbreviate dependencies. M17’s file lists all required modules. M18 needs M01/M04/M11 and remains optional; a basic product UI is still required.

| Gate | Rule |
|---|---|
| Before RAG | Establish evaluation labels and criteria in M05 |
| Before public access or tools | Pass M11 authorization and isolation tests |
| Before complexity | Justify agents, multiple agents, fine-tuning, and frameworks against a baseline |
| Core completion | Complete M17 and its prerequisites; M16/M18 have separate progress |
| Project delivery | Follow [S0–S7](../project/README.md); agent and operations branches may proceed independently after their gates |

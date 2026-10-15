# ITI Native AI Developer Coverage

[Home](../README.md) · [Sources](SOURCES.md) · [Reading](READING_GUIDE.md)

The official 2026/2027 brochure is five pages. Page 2 publishes prerequisites and678 hours/about five months; pages4–5 list the items below, totaling696 hours. The discrepancy is unresolved. N identifiers are local traceability IDs, not official module numbers.

Official prerequisites: basic/intermediate programming, preferably Python; data structures/algorithms/problem solving; SQL and relational concepts; Git/command line; conceptual statistics/linear algebra and technical English.

| ID | Official topic | Official hours | Roadmap modules |
| --- | --- | --- | --- |
| N01 | Modern Software Engineering & Git Collaboration | 18 | [M00](../modules/m00-orientation/README.md), [M14](../modules/m14-llmops-deployment/README.md) |
| N02 | Advanced Python Programming for AI Engineers | 30 | [M01](../modules/m01-python-fastapi/README.md), [M10](../modules/m10-async-streaming-jobs/README.md) |
| N03 | SDLC & Requirements Engineering | 18 | [M00](../modules/m00-orientation/README.md) |
| N04 | Prompt / Context Engineering & Structured Outputs | 24 | [M04](../modules/m04-prompt-structured-output/README.md), [M09](../modules/m09-context-memory/README.md) |
| N05 | Software Testing & Full-Stack Debugging | 30 | [M01](../modules/m01-python-fastapi/README.md), [M05](../modules/m05-evaluation/README.md), [M14](../modules/m14-llmops-deployment/README.md), [M18](../modules/m18-frontend/README.md) |
| N06 | SQL & NoSQL Database Engineering | 30 | [M06](../modules/m06-persistence/README.md) |
| N07 | RESTful API, Backend Architecture & Security | 36 | [M01](../modules/m01-python-fastapi/README.md), [M06](../modules/m06-persistence/README.md), [M11](../modules/m11-security/README.md) |
| N08 | Frontend TypeScript & React | 42 | [M18](../modules/m18-frontend/README.md) |
| N09 | Software Architecture & System Design | 30 | [M00](../modules/m00-orientation/README.md), [M06](../modules/m06-persistence/README.md), [M14](../modules/m14-llmops-deployment/README.md) |
| N10 | Cloud-Native Deployment & Platform Mapping | 24 | [M14](../modules/m14-llmops-deployment/README.md) |
| N11 | Mathematical Foundations | 24 | [M02](../modules/m02-math-ml/README.md) |
| N12 | Data Preparation & Feature Engineering | 12 | [M02](../modules/m02-math-ml/README.md), [M07](../modules/m07-ingestion-embeddings/README.md), [M16](../modules/m16-customization/README.md) |
| N13 | Machine Learning Fundamentals | 24 | [M02](../modules/m02-math-ml/README.md) |
| N14 | Deep Learning & Neural Networks | 18 | [M03](../modules/m03-dl-foundation-models/README.md) |
| N15 | MLOps Basics & Model Serving | 18 | [M03](../modules/m03-dl-foundation-models/README.md), [M14](../modules/m14-llmops-deployment/README.md), [M16](../modules/m16-customization/README.md) |
| N16 | LLM Fundamentals & GenAI Landscape | 18 | [M03](../modules/m03-dl-foundation-models/README.md), [M04](../modules/m04-prompt-structured-output/README.md) |
| N17 | Embeddings, Vector DBs & Semantic Search | 18 | [M07](../modules/m07-ingestion-embeddings/README.md), [M08](../modules/m08-rag/README.md) |
| N18 | Asynchronous Processing & Streaming | 18 | [M10](../modules/m10-async-streaming-jobs/README.md) |
| N19 | RAG Systems Engineering | 24 | [M07](../modules/m07-ingestion-embeddings/README.md), [M08](../modules/m08-rag/README.md), [M09](../modules/m09-context-memory/README.md) |
| N20 | AI Evaluation, Safety & Responsible AI | 12 | [M05](../modules/m05-evaluation/README.md), [M08](../modules/m08-rag/README.md), [M11](../modules/m11-security/README.md), [M12](../modules/m12-tools-agents/README.md), [M15](../modules/m15-optimization-feedback/README.md) |
| N21 | Fine-Tuning & Model Customization | 18 | [M16](../modules/m16-customization/README.md) |
| N22 | Agentic AI & Multi-Agent Orchestration | 36 | [M09](../modules/m09-context-memory/README.md), [M12](../modules/m12-tools-agents/README.md) |
| N23 | Model Context Protocol & Enterprise Tool Integration | 12 | [M13](../modules/m13-mcp-workflows/README.md) |
| N24 | AI Workflow Automation & Business Process Integration | 12 | [M12](../modules/m12-tools-agents/README.md), [M13](../modules/m13-mcp-workflows/README.md) |
| N25 | LLMOps & Production Readiness for AI Applications | 18 | [M10](../modules/m10-async-streaming-jobs/README.md), [M14](../modules/m14-llmops-deployment/README.md), [M15](../modules/m15-optimization-feedback/README.md) |
| N26 | AI Security, Governance & Compliance | 12 | [M11](../modules/m11-security/README.md) |
| N27 | Graduation Project | 60 | [M17](../modules/m17-capstone/README.md) |
| N28 | Effective Presentation Skills | 18 | [M17](../modules/m17-capstone/README.md) |
| N29 | Freelancing Fundamentals | 12 | [M17](../modules/m17-capstone/README.md) |
| N30 | Effective Communication Skills | 12 | [M00](../modules/m00-orientation/README.md), [M17](../modules/m17-capstone/README.md) |
| N31 | Work Ethics Workshop | 3 | [M00](../modules/m00-orientation/README.md), [M17](../modules/m17-capstone/README.md) |
| N32 | CV Writing & Interviewing Skills | 15 | [M17](../modules/m17-capstone/README.md) |

## Coverage limits and deliberate choices

| Topic | Treatment |
|---|---|
| SQL/NoSQL | New ORM/session/migration work; existing MongoDB knowledge is assessed rather than repeated |
| Frontend | M18 explicitly covers supporting React/TypeScript; Core needs a basic UI but does not claim the full42-hour React syllabus |
| Math/ML/DL | M02/M03 retain small scientific labs; the three books alone are not a full ML curriculum |
| Fine-tuning | M16 remains visible as optional advanced study; no practical training claim without an actual run |
| Multi-agent | Understand patterns and evaluate a design; implementation is conditional on measured value |
| MCP | M13 includes a small server/client integration using current official documentation |
| Governance/compliance | Threat modeling, privacy boundaries, retention, and responsible behavior; no comprehensive legal/compliance certification claimed |
| Employability | Demonstrations, technical communication, evidence-based CV claims, ethics, and scoped delivery exercises |

The mapping is complete traceability, not a claim that self-study equals official training depth or accreditation. Study hours and dependency choices are recommendations.

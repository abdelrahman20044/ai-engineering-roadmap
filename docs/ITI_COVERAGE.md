# ITI Native AI Developer Coverage

[Home](../README.md) · [Sources](SOURCES.md) · [Reading](READING_GUIDE.md)

The official 2026/2027 brochure is five pages. Page 2 publishes prerequisites and678 hours/about five months; pages4–5 list the items below, totaling696 hours. The discrepancy is unresolved. N identifiers are local traceability IDs, not official module numbers.

Official prerequisites: basic/intermediate programming, preferably Python; data structures/algorithms/problem solving; SQL and relational concepts; Git/command line; conceptual statistics/linear algebra and technical English.

| ID | Official topic | Official hours | Roadmap modules |
| --- | --- | --- | --- |
| N01 | Modern Software Engineering & Git Collaboration | 18 | [L00](../00-Orientation/README.md), [L14](../14-LLMOps-Deployment/README.md) |
| N02 | Advanced Python Programming for AI Engineers | 30 | [L01](../01-Python-FastAPI/README.md), [L10](../10-Concurrency-Streaming-Jobs/README.md) |
| N03 | SDLC & Requirements Engineering | 18 | [L00](../00-Orientation/README.md) |
| N04 | Prompt / Context Engineering & Structured Outputs | 24 | [L04](../04-LLM-Applications-Prompts/README.md), [L09](../09-Context-Memory/README.md) |
| N05 | Software Testing & Full-Stack Debugging | 30 | [L01](../01-Python-FastAPI/README.md), [L05](../05-Evaluation/README.md), [L14](../14-LLMOps-Deployment/README.md), [L18](../18-Supporting-Frontend/README.md) |
| N06 | SQL & NoSQL Database Engineering | 30 | [L06](../06-Application-State/README.md) |
| N07 | RESTful API, Backend Architecture & Security | 36 | [L01](../01-Python-FastAPI/README.md), [L06](../06-Application-State/README.md), [L11](../11-Security-Responsible-AI/README.md) |
| N08 | Frontend TypeScript & React | 42 | [L18](../18-Supporting-Frontend/README.md) |
| N09 | Software Architecture & System Design | 30 | [L00](../00-Orientation/README.md), [L06](../06-Application-State/README.md), [L14](../14-LLMOps-Deployment/README.md) |
| N10 | Cloud-Native Deployment & Platform Mapping | 24 | [L14](../14-LLMOps-Deployment/README.md) |
| N11 | Mathematical Foundations | 24 | [L02](../02-Mathematics-ML/README.md) |
| N12 | Data Preparation & Feature Engineering | 12 | [L02](../02-Mathematics-ML/README.md), [L07](../07-Embeddings-Semantic-Search/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md) |
| N13 | Machine Learning Fundamentals | 24 | [L02](../02-Mathematics-ML/README.md) |
| N14 | Deep Learning & Neural Networks | 18 | [L03](../03-Deep-Learning-Foundation-Models/README.md) |
| N15 | MLOps Basics & Model Serving | 18 | [L03](../03-Deep-Learning-Foundation-Models/README.md), [L14](../14-LLMOps-Deployment/README.md), [L17](../17-Fine-Tuning-Advanced-Serving/README.md) |
| N16 | LLM Fundamentals & GenAI Landscape | 18 | [L03](../03-Deep-Learning-Foundation-Models/README.md), [L04](../04-LLM-Applications-Prompts/README.md) |
| N17 | Embeddings, Vector DBs & Semantic Search | 18 | [L07](../07-Embeddings-Semantic-Search/README.md), [L08](../08-RAG-Systems/README.md) |
| N18 | Asynchronous Processing & Streaming | 18 | [L10](../10-Concurrency-Streaming-Jobs/README.md) |
| N19 | RAG Systems Engineering | 24 | [L07](../07-Embeddings-Semantic-Search/README.md), [L08](../08-RAG-Systems/README.md), [L09](../09-Context-Memory/README.md) |
| N20 | AI Evaluation, Safety & Responsible AI | 12 | [L05](../05-Evaluation/README.md), [L08](../08-RAG-Systems/README.md), [L11](../11-Security-Responsible-AI/README.md), [L12](../12-Tools-Agents/README.md), [L15](../15-Model-Selection-Optimization/README.md) |
| N21 | Fine-Tuning & Model Customization | 18 | [L17](../17-Fine-Tuning-Advanced-Serving/README.md) |
| N22 | Agentic AI & Multi-Agent Orchestration | 36 | [L09](../09-Context-Memory/README.md), [L12](../12-Tools-Agents/README.md) |
| N23 | Model Context Protocol & Enterprise Tool Integration | 12 | [L13](../13-MCP-Enterprise-Integration/README.md) |
| N24 | AI Workflow Automation & Business Process Integration | 12 | [L12](../12-Tools-Agents/README.md), [L13](../13-MCP-Enterprise-Integration/README.md) |
| N25 | LLMOps & Production Readiness for AI Applications | 18 | [L10](../10-Concurrency-Streaming-Jobs/README.md), [L14](../14-LLMOps-Deployment/README.md), [L15](../15-Model-Selection-Optimization/README.md) |
| N26 | AI Security, Governance & Compliance | 12 | [L11](../11-Security-Responsible-AI/README.md) |
| N27 | Graduation Project | 60 | [L16](../16-Capstone-Career/README.md) |
| N28 | Effective Presentation Skills | 18 | [L16](../16-Capstone-Career/README.md) |
| N29 | Freelancing Fundamentals | 12 | [L16](../16-Capstone-Career/README.md) |
| N30 | Effective Communication Skills | 12 | [L00](../00-Orientation/README.md), [L16](../16-Capstone-Career/README.md) |
| N31 | Work Ethics Workshop | 3 | [L00](../00-Orientation/README.md), [L16](../16-Capstone-Career/README.md) |
| N32 | CV Writing & Interviewing Skills | 15 | [L16](../16-Capstone-Career/README.md) |

## Coverage limits and deliberate choices

| Topic | Treatment |
|---|---|
| SQL/NoSQL | New ORM/session/migration work; existing MongoDB knowledge is assessed rather than repeated |
| Frontend | L18 explicitly covers supporting React/TypeScript; Core needs a basic UI but does not claim the full42-hour React syllabus |
| Math/ML/DL | L02/L03 retain small scientific labs; the three books alone are not a full ML curriculum |
| Fine-tuning | L17 remains visible as optional advanced study; no practical training claim without an actual run |
| Multi-agent | Understand patterns and evaluate a design; implementation is conditional on measured value |
| MCP | L13 includes a small server/client integration using current official documentation |
| Governance/compliance | Threat modeling, privacy boundaries, retention, and responsible behavior; no comprehensive legal/compliance certification claimed |
| Employability | Demonstrations, technical communication, evidence-based CV claims, ethics, and scoped delivery exercises |

The mapping is complete traceability, not a claim that self-study equals official training depth or accreditation. Study hours and dependency choices are recommendations.

## Industry extensions inside ITI-backed Levels

| Recommendation | Levels | Source boundary |
| --- | --- | --- |
| pytest, Pydantic, SQLAlchemy, Alembic | L01/L06 | Chosen implementations of Python, testing, backend, database topics; not claimed as named ITI mandates. |
| pgvector, hybrid retrieval, reranking | L07/L08 | Tool choice and depth added to embeddings/RAG topic coverage. |
| Durable job semantics, cancellation, CI gates | L10/L14 | Operational implementation detail recommended beyond the brochure. |
| OWASP attack fixtures, owner-filtered retrieval, memory deletion | L09/L11 | Concrete tests and security design supplied by this roadmap. |
| OpenTelemetry, p95 latency, cost budgets | L14/L15 | Recommended instrumentation and measurable acceptance evidence. |

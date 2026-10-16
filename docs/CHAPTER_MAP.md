# Chapter-to-Level Map

[Master reading order](READING_GUIDE.md) · [Roadmap](../README.md)

**This is a reference index, not a second reading schedule.** Follow the master order or the current Level README to decide Read Now versus Read Later. The chapter locations below preserve the supplied-PDF research. Full chapter spans locate content; they do not assign every page.

| Chapter | Verified chapter locator | Exact assigned slices / statuses | First-reading Levels |
| --- | --- | --- | --- |
| G1 | Peeking inside the black box, pp. 1–22 | [B01](READING_GUIDE.md#b01) | L00 |
| G2 | Building your first GenAI app, pp. 23–45 | [B10](READING_GUIDE.md#b10) | L04 |
| G3 | Writing the right prompt, pp. 47–72 | [B11](READING_GUIDE.md#b11) | L04 |
| G4 | Augmenting LLMs with your own documents, pp. 73–100 | [B19](READING_GUIDE.md#b19), [B24](READING_GUIDE.md#b24) | L07, L08 |
| G5 | Tools and agents, pp. 101–127 | [B36](READING_GUIDE.md#b36) | L12 |
| G6 | Implementing agentic structures, pp. 129–171 | [B36a](READING_GUIDE.md#b36a) | L12 |
| G7 | Integrating GenAI in your data ecosystem, pp. 173–210 | Optional background; no required first reading | Optional / review only |
| G8 | Deploying and orchestrating GenAI apps, pp. 211–240 | Optional background; no required first reading | Optional / review only |
| F1 | Introduction, PDF 23–42 | Optional background; no required first reading | Optional / review only |
| F2 | Getting Started with FastAPI, PDF 43–82 | [B04](READING_GUIDE.md#b04) | L01 |
| F4 | Implementing Type-Safe AI Services, PDF 153–186 | [B05](READING_GUIDE.md#b05) | L01 |
| F3 | AI Integration and Model Serving, PDF 83–152 | [B09](READING_GUIDE.md#b09), [B12](READING_GUIDE.md#b12) | L03, L04 |
| F5 | Achieving Concurrency in AI Workloads, PDF 187–257 | [B13](READING_GUIDE.md#b13), [B21](READING_GUIDE.md#b21), [B25](READING_GUIDE.md#b25), [B31](READING_GUIDE.md#b31) | L04, L07, L08, L10 |
| F7 | Integrating Databases into AI Services, PDF 302–337 | [B18](READING_GUIDE.md#b18) | L06 |
| F11 | Testing AI Services, PDF 477–535 | [B06](READING_GUIDE.md#b06), [B17](READING_GUIDE.md#b17), [B26](READING_GUIDE.md#b26), [B38](READING_GUIDE.md#b38) | L01, L05, L08, L14 |
| F8 | Authentication and Authorization, PDF 338–400 | [B33](READING_GUIDE.md#b33) | L11 |
| F6 | Real-Time Communication with Generative Models, PDF 258–301 | [B32](READING_GUIDE.md#b32), [B48](READING_GUIDE.md#b48) | L10 |
| F9 | Securing AI Services, PDF 401–428 | [B34](READING_GUIDE.md#b34) | L11 |
| F10 | Optimizing AI Services, PDF 429–476 | [B41](READING_GUIDE.md#b41) | L15 |
| F12 | Deployment of AI Services, PDF 536–594 | [B39](READING_GUIDE.md#b39) | L14 |
| C1 | Introduction, pp. 1–47 | [B02](READING_GUIDE.md#b02) | L00 |
| C2 | Understanding Foundation Models, pp. 49–111 | [B08](READING_GUIDE.md#b08) | L03 |
| C3 | Evaluation Methodology, pp. 113–156 | [B15](READING_GUIDE.md#b15), [B23](READING_GUIDE.md#b23) | L05 |
| C4 | Evaluate AI Systems, pp. 159–208 | [B03](READING_GUIDE.md#b03), [B16](READING_GUIDE.md#b16), [B40](READING_GUIDE.md#b40), [B44](READING_GUIDE.md#b44) | L00, L05, L15 |
| C5 | Prompt Engineering, pp. 211–251 | [B14](READING_GUIDE.md#b14), [B30](READING_GUIDE.md#b30), [B35](READING_GUIDE.md#b35) | L04, L11 |
| C6 | RAG and Agents, pp. 253–305 | [B20](READING_GUIDE.md#b20), [B27](READING_GUIDE.md#b27), [B28](READING_GUIDE.md#b28), [B36b](READING_GUIDE.md#b36b) | L07, L08, L09, L12 |
| C7 | Finetuning, pp. 307–361 | [B45](READING_GUIDE.md#b45) | L17 |
| C8 | Dataset Engineering, pp. 363–403 | [B07](READING_GUIDE.md#b07), [B22](READING_GUIDE.md#b22), [B46](READING_GUIDE.md#b46) | L02, L07, L17 |
| C9 | Inference Optimization, pp. 405–447 | [B42](READING_GUIDE.md#b42), [B47](READING_GUIDE.md#b47) | L15, L17 |
| C10 | AI Engineering Architecture and User Feedback, pp. 449–492 | [B29](READING_GUIDE.md#b29), [B35a](READING_GUIDE.md#b35a), [B37](READING_GUIDE.md#b37), [B39a](READING_GUIDE.md#b39a), [B43](READING_GUIDE.md#b43) | L09, L11, L13, L14, L15 |

## Why chapters are split

- **F3:** model/serving orientation in B09; external API integration in B12. Other modalities remain optional.
- **F5:** provider-call example B13; preparation B21; RAG generation B25; concurrency/jobs B31; advanced inference is optional B47. Verified examples corrected the earlier broad provider/RAG page descriptions.
- **F11:** pytest B06 (PDF501–518); model/behavioral testing B17 (495–500, 523–528); retrieval integration B26 (519–522); E2E B38 (529–534). Later agent/release work reuses these skills.
- **C4:** pipeline preview B03, task criteria B16, model selection B40. The preview is applied in L05, not reintroduced as a whole new chapter.
- **C5:** prompt/context basics B14, defense B35. L09 context-budget reading is explicit review B30.
- **C6:** retrieval foundations B20, improvements B27, memory B28, agents B36b. One chapter supports different project capabilities without a mandatory full reread.
- **C8/C9:** bounded quality/processing/metrics slices enter the core; optional training/serving sections wait for L17.
- **C10:** context B29, guardrails B35a, orchestration B37, observability B39a, feedback B43. The old pp.465–473 assignment is split to avoid reassigning orchestration at L14.

## Retained topic associations

The original topic-to-book research is retained in each topic’s `book` field in `RESOURCE_CATALOG.json` and the manifest’s `reading_topic_notes`. These fields explain conceptual overlap; they do **not** introduce new assignments. The reading ledger is authoritative.

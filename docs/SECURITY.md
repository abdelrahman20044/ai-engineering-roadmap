# Security and Responsible AI

[Home](../README.md) · [M11](../modules/m11-security/README.md) · [Threat model](../templates/THREAT_MODEL.md)

References: F8–9, C5, and OWASP GenAI. Documents, journals, and tool outputs are untrusted inputs. RAG or fine-tuning does not automatically eliminate prompt injection.

| Boundary | Required behavior | Evidence |
|---|---|---|
| Identity | Derive the user on the server, never from model-chosen authority | A/B access tests |
| Retrieval | Filter ownership before context construction | Cross-user search and source-viewer tests |
| Tools | Least privilege and server-side argument/permission checks | Unknown/unauthorized tool tests |
| Writes | Appropriate approval and idempotency | Simulated repeated-write/failure tests |
| Consumption | Bound upload/pages/tokens/requests/steps/retries | Oversized and abuse cases |
| Secrets | Keep keys out of repository, browser, prompts, and logs | Configuration/log review |
| Journals | Do not log sensitive contents by default | Redaction and retention review |
| Deletion | Remove active derived content and document backup retention | Delete/re-query/context/cache tests |
| Deployment | HTTPS, appropriate CORS/cookie/bearer/CSRF choices | Public-demo gate |

| Before public access | Status to record |
|---|---|
| API/source/stream/job authorization | Tested with multiple users |
| Provider outage and partial stream failure | Tested |
| Persistence and restore | Demonstrated |
| Demo inputs and budgets | Synthetic and bounded |
| Residual risk | Documented; passing designed tests is not universal proof of security |

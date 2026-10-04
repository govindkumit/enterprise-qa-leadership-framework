# Release Risk Register

| ID | Risk | Probability | Impact | Score | Mitigation | Owner | Status |
|---|---|---:|---:|---:|---|---|---|
| R-01 | Payment succeeds but order creation fails | 2 | 5 | 10 | API + E2E + reconciliation test | QA Lead | Mitigated |
| R-02 | Checkout latency at peak traffic | 4 | 5 | 20 | Load test + performance gate | Perf QA | Mitigated |
| R-03 | Sensitive data exposed in logs | 2 | 5 | 10 | Security scan + log validation | Security QA | Mitigated |
| R-04 | One non-critical notification defect | 3 | 2 | 6 | Post-release fix planned | Eng | Accepted |

**Risk rule:** a QA Manager makes risk visible; the business owner accepts business risk; engineering owns technical remediation.

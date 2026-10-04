# Release Quality Gate — v2.8.0

| Gate | Threshold | Actual | Result |
|---|---:|---:|---|
| Critical defects | 0 | 0 | PASS |
| High defects | ≤2 | 1 | PASS |
| Smoke pass | 100% | 100% | PASS |
| Regression | ≥95% | 97% | PASS |
| Automation stability | ≥97% | 98% | PASS |
| Security critical findings | 0 | 0 | PASS |
| Performance SLA | Pass | Pass | PASS |
| Critical business flows | 100% | 100% | PASS |

## Decision

### 🟢 GO

**QA Manager recommendation:** Release to production.

**Residual risk:** one medium notification issue with workaround; Product Owner accepted the risk and a post-release fix is scheduled.

**Evidence:** all critical business flows passed; no critical defects; security and performance gates passed.

# Defect Triage Model

## Severity
- S1 Critical: business stopped, data/security/revenue impact
- S2 High: major function unavailable with material impact
- S3 Medium: workaround exists
- S4 Low: minor/cosmetic

## Priority
- P1 immediate
- P2 current release
- P3 planned
- P4 backlog

## Example
**DEF-1042 — Payment charged but order not created**

Severity: S1 | Priority: P1 | Release blocker: Yes

Evidence required: request/response, timestamp, order/payment IDs, environment, logs, reproduction rate.

QA Manager action: escalate, establish impact, block release until fixed and regression evidence is green.

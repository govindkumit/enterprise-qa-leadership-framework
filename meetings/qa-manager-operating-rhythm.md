# QA Manager Operating Rhythm

## Requirement Refinement
**QA Manager asks:** Is the requirement testable? What are failure modes, dependencies, data/privacy concerns and acceptance criteria?

## Sprint Planning
**QA Manager contributes:** scope, risk, estimates, environment needs, automation impact and resource allocation.

## Daily QA Sync
Focus: blockers, critical defects, execution trend, environment health and next 24-hour actions.

## Defect Triage
Classify severity/priority, challenge evidence, agree owner and target fix, identify release impact.

## Release Readiness
Review quality dashboard, open risks, defect trend, automation stability, performance/security evidence and business-critical scenarios.

## Stakeholder Negotiation Scenario
**Situation:** Product asks QA to complete full regression in 2 days after a scope increase.

**QA response:**
- Do not simply say yes/no.
- Present risk-based options:
  - Option A: full regression → 4 days.
  - Option B: P0/P1 regression + automation → 2 days, residual P2 risk.
  - Option C: release delay → full evidence.
- Recommend Option B only if critical paths, security and performance gates remain green.
- Record the residual risk and obtain explicit business acceptance.

**Outcome:** QA protects quality without becoming a delivery blocker.

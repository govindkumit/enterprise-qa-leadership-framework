# QA Manager Decision Log

This log demonstrates evidence-based quality leadership for OmniShop release v2.8.0.

## Decision 01 — Release Date Accelerated
**Situation:** Product requests release two days earlier than planned.

**Facts:** Core checkout is complete; regression is 72% complete; payment and refund remain high-risk areas.

**Risk:** Reduced regression depth increases customer and revenue risk.

**Options**
1. Keep original date and complete planned scope.
2. Release early with reduced low-risk regression.
3. Add targeted QA capacity and extend automation execution.

**Decision:** Support the earlier release only with risk-based scope reduction, targeted additional capacity, and explicit residual-risk acceptance.

**Accountability:** QA Manager owns the quality recommendation and evidence; Product owns business risk acceptance.

**Outcome:** Critical customer journeys remain fully covered while low-risk scenarios are deferred.

## Decision 02 — QA Capacity Shortage
**Situation:** 8 QA engineers are required; 5 are available.

**Decision:** Protect critical-path coverage, allocate specialists to high-risk areas, increase automation execution, cross-train available engineers, and defer low-risk testing with documented acceptance.

**Principle:** Capacity constraints change scope and prioritization; they do not remove quality accountability.

## Decision 03 — Critical Defect Near Release
**Situation:** A payment defect is discovered shortly before release.

**Decision:** Block release until impact is understood and the defect is fixed or formally risk-accepted by the accountable business owner.

**Evidence required:** Reproduction, affected transactions, customer impact, workaround, fix validation, regression evidence.

## Decision 04 — Stakeholder Disagreement
**Situation:** Engineering classifies a defect as medium; QA assesses it as high because it affects checkout completion.

**Decision path:** Reproduce → quantify affected journey → assess business impact → review evidence jointly → agree severity/priority → document decision.

**Principle:** Severity is evidence-driven, not role-driven.

## Decision 05 — Production Incident
**Situation:** Customers intermittently receive duplicate-order notifications.

**Decision:** Validate impact, support containment, verify the fix, run targeted regression, update monitoring and add a regression scenario to prevent recurrence.

**Principle:** Production feedback becomes future test coverage.

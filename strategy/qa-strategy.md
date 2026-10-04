# QA Strategy — OmniShop v2.8.0

## 1. Objective
Deliver a reliable checkout and order experience while protecting customer data and meeting release timelines.

## 2. Scope
Customer login, product search, cart, checkout, payment, order creation, notifications and critical APIs.

## 3. Test approach

| Layer | Approach | Owner | Exit evidence |
|---|---|---|---|
| Unit | Developer-owned | Engineering | CI pass |
| API | Pytest/Requests | API QA | 100% critical API scenarios |
| UI | Playwright | Automation QA | Critical journeys green |
| DB | SQL validation | QA | Data integrity checks |
| Security | OWASP-focused | Security QA | No critical findings |
| Performance | k6/JMeter | Performance QA | SLA met |
| Regression | Risk-based suite | QA team | ≥95% pass |
| Production readiness | Checklist + monitoring | QA Manager | Signed evidence |

## 4. Risk-based priority
P0 = payment, authentication, order creation, sensitive-data exposure.
P1 = search, cart, notifications.
P2 = low-risk cosmetic/non-critical workflows.

## 5. Definition of Ready for QA
Acceptance criteria defined • testable requirements • dependencies known • environment available • test data available.

## 6. Definition of Done for QA
Planned tests executed • critical defects closed • regression threshold met • security/performance evidence available • residual risks documented • release recommendation issued.

## 7. QA Manager responsibilities
Own strategy, challenge scope, negotiate testable timelines, allocate resources, remove blockers, ensure evidence, communicate risk, chair/participate in quality forums, and provide an independent Go/No-Go recommendation.

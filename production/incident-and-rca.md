# Production Incident & RCA

## INC-001 — Checkout API failures

**Impact:** 12% checkout failures during peak traffic.

**Timeline**
- 10:05 — monitoring alert
- 10:10 — QA validates customer impact
- 10:20 — engineering identifies connection-pool exhaustion
- 10:35 — configuration fix deployed
- 10:50 — QA validates checkout and payment flows
- 11:00 — incident closed

## 5 Whys
1. Checkout returned 500 errors.
2. Payment connection pool was exhausted.
3. Pool configuration was too low for peak concurrency.
4. Peak-load configuration was not included in release validation.
5. Performance test coverage did not include the production-like concurrency profile.

## Corrective actions
- Add production-like peak concurrency test.
- Add configuration validation to deployment checklist.
- Add alert threshold for connection-pool saturation.
- Add checkout resilience scenario to regression.
- Review capacity assumptions before next release.

**QA leadership lesson:** a production defect is not closed when the fix works; it is closed when the organization reduces the probability of recurrence.

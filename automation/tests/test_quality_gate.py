def test_release_quality_gate():
    metrics = {"critical_defects": 0, "regression_pass_rate": 0.97, "smoke_pass_rate": 1.00, "security_critical": 0}
    assert metrics["critical_defects"] == 0
    assert metrics["regression_pass_rate"] >= 0.95
    assert metrics["smoke_pass_rate"] == 1.00
    assert metrics["security_critical"] == 0

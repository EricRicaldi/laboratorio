
from travel_assistant.tools.budget_tools import estimate_trip_budget
from travel_assistant.tools.risk_tools import assess_basic_travel_risks


def test_estimate_trip_budget_success():
    result = estimate_trip_budget(
        destination="Cusco",
        days=4,
        daily_budget_usd=150
    )

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert result["days"] == 4
    assert result["estimated_total_usd"] == 600


def test_estimate_trip_budget_invalid_days():
    result = estimate_trip_budget(
        destination="Cusco",
        days=0,
        daily_budget_usd=150
    )

    assert result["status"] == "error"


def test_estimate_trip_budget_invalid_budget():
    result = estimate_trip_budget(
        destination="Cusco",
        days=4,
        daily_budget_usd=0
    )

    assert result["status"] == "error"


def test_assess_risks_cusco():
    result = assess_basic_travel_risks(
        destination="Cusco",
        season="dry"
    )

    assert result["status"] == "success"
    assert len(result["risks"]) > 0


def test_assess_risks_rainy_season():
    result = assess_basic_travel_risks(
        destination="Lima",
        season="lluvia"
    )

    assert result["status"] == "success"
    assert any("waterproof" in risk for risk in result["risks"])


def test_assess_risks_general_destination():
    result = assess_basic_travel_risks(
        destination="Lima",
        season="normal"
    )

    assert result["status"] == "success"
    assert len(result["risks"]) > 0

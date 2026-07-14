# test_subscription_tracker_practice.py
# NOTE: these FAIL until you implement subscription_info — that's expected; they
# are the spec for the exercise.
from subscription_tracker_practice import subscription_info


def test_active_mid_plan():
    assert subscription_info("2026-01-01", 30, "2026-01-15") == {
        "expiry_date": "2026-01-31",
        "is_active": True,
        "days_remaining": 16,
        "expiry_weekday": "Saturday",
        "status": "active",
    }


def test_not_started():
    assert subscription_info("2026-01-01", 30, "2025-12-20") == {
        "expiry_date": "2026-01-31",
        "is_active": False,
        "days_remaining": 30,
        "expiry_weekday": "Saturday",
        "status": "not started",
    }


def test_expired():
    assert subscription_info("2026-01-01", 30, "2026-03-01") == {
        "expiry_date": "2026-01-31",
        "is_active": False,
        "days_remaining": 0,
        "expiry_weekday": "Saturday",
        "status": "expired",
    }


def test_signup_day_is_active():
    # check_date == signup_date: active, whole plan remaining
    assert subscription_info("2026-01-01", 30, "2026-01-01") == {
        "expiry_date": "2026-01-31",
        "is_active": True,
        "days_remaining": 30,
        "expiry_weekday": "Saturday",
        "status": "active",
    }


def test_expiry_day_is_active_zero_remaining():
    # check_date == expiry_date: still active, 0 days left
    assert subscription_info("2026-01-01", 30, "2026-01-31") == {
        "expiry_date": "2026-01-31",
        "is_active": True,
        "days_remaining": 0,
        "expiry_weekday": "Saturday",
        "status": "active",
    }


def test_day_after_expiry():
    assert subscription_info("2026-01-01", 30, "2026-02-01") == {
        "expiry_date": "2026-01-31",
        "is_active": False,
        "days_remaining": 0,
        "expiry_weekday": "Saturday",
        "status": "expired",
    }


def test_one_day_remaining():
    assert subscription_info("2026-01-01", 30, "2026-01-30") == {
        "expiry_date": "2026-01-31",
        "is_active": True,
        "days_remaining": 1,
        "expiry_weekday": "Saturday",
        "status": "active",
    }


def test_zero_day_plan():
    # plan_days == 0: expiry == signup; only the signup day itself is active
    assert subscription_info("2026-01-01", 0, "2026-01-01") == {
        "expiry_date": "2026-01-01",
        "is_active": True,
        "days_remaining": 0,
        "expiry_weekday": "Thursday",
        "status": "active",
    }


def test_leap_day_expiry():
    # 2024 is a leap year: Feb 28 + 1 day = Feb 29
    assert subscription_info("2024-02-28", 1, "2024-02-29") == {
        "expiry_date": "2024-02-29",
        "is_active": True,
        "days_remaining": 0,
        "expiry_weekday": "Thursday",
        "status": "active",
    }


def test_crosses_year_boundary():
    # Dec 25 + 10 days spills into the next year
    assert subscription_info("2025-12-25", 10, "2025-12-30") == {
        "expiry_date": "2026-01-04",
        "is_active": True,
        "days_remaining": 5,
        "expiry_weekday": "Sunday",
        "status": "active",
    }

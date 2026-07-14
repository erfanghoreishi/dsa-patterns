"""Subscription Tracker  (Python date practice - not a LeetCode problem)

Amir signs up for a gym membership. Given his signup date and a plan length in
days, answer several questions about the subscription - forcing you to touch
parsing, arithmetic, comparison, and formatting all in one place.

Implement subscription_info below so the tests in
test_subscription_tracker_practice.py pass. (They FAIL until you do - that's the
point: this is a skeleton for you to fill in.)

Tools you'll likely want (all from the standard library):
    - date.fromisoformat(s)  or  datetime.strptime(s, "%Y-%m-%d")  # parse
    - timedelta(days=...)                                          # arithmetic
    - <, <=, == on dates                                          # comparison
    - date.isoformat()   -> "YYYY-MM-DD"                          # format back
    - date.strftime("%A") -> weekday name, e.g. "Monday"         # format

SPEC - subscription_info(signup_date, plan_days, check_date) returns a dict:
    expiry_date    : str  'YYYY-MM-DD'  = signup_date + plan_days
    is_active      : bool  True iff signup_date <= check_date <= expiry_date
    days_remaining : int
        - "not started" (check < signup) -> plan_days (whole plan still ahead)
        - "active"      (in range)       -> (expiry_date - check_date).days
        - "expired"     (check > expiry) -> 0
    expiry_weekday : str  weekday name of expiry_date, e.g. "Saturday"
    status         : str  "not started" | "active" | "expired"

Examples:
    subscription_info("2026-01-01", 30, "2026-01-15")
        -> {"expiry_date": "2026-01-31", "is_active": True,  "days_remaining": 16,
                "expiry_weekday": "Saturday", "status": "active"}
    subscription_info("2026-01-01", 30, "2025-12-20")
        -> {"expiry_date": "2026-01-31", "is_active": False, "days_remaining": 30,
                "expiry_weekday": "Saturday", "status": "not started"}
    subscription_info("2026-01-01", 30, "2026-03-01")
        -> {"expiry_date": "2026-01-31", "is_active": False, "days_remaining": 0,
                "expiry_weekday": "Saturday", "status": "expired"}
"""

from datetime import date, timedelta


def subscription_info(signup_date, plan_days, check_date):
    """Return subscription status details for the given dates."""
    signup_date = date.fromisoformat(signup_date)
    check_date = date.fromisoformat(check_date)

    expiry_date = signup_date + timedelta(days=plan_days)

    if check_date < signup_date:
        is_active = False
        days_remaining = plan_days
        status = "not started"
    elif check_date > expiry_date:
        is_active = False
        days_remaining = 0
        status = "expired"
    else:
        is_active = True
        days_remaining = (expiry_date - check_date).days
        status = "active"

    expiry_weekday = expiry_date.strftime("%A")

    return {
        "expiry_date": expiry_date.isoformat(),
        "is_active": is_active,
        "days_remaining": days_remaining,
        "expiry_weekday": expiry_weekday,
        "status": status,
    }

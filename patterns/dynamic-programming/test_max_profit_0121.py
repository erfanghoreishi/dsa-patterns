# test_max_profit_0121.py
from max_profit_0121 import maxProfit


def test_example_1():
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_no_profit():
    assert maxProfit([7, 6, 4, 3, 1]) == 0


def test_single_day():
    assert maxProfit([5]) == 0


def test_monotonic_increase():
    assert maxProfit([1, 2, 3, 4, 5]) == 4

# test_coin_change_0322.py
from coin_change_0322 import coinChange


def test_example_1():
    assert coinChange([1, 2, 5], 11) == 3      # 5 + 5 + 1


def test_impossible():
    assert coinChange([2], 3) == -1


def test_zero_amount():
    assert coinChange([1], 0) == 0


def test_zero_amount_unusable_coin():
    assert coinChange([2], 0) == 0


def test_greedy_would_fail():
    # greedy (largest-first) gives a worse answer here; DP finds 20
    assert coinChange([186, 419, 83, 408], 6249) == 20

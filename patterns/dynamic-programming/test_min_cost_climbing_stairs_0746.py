# test_min_cost_climbing_stairs_0746.py
from min_cost_climbing_stairs_0746 import minCostClimbingStairs


def test_example_1():
    assert minCostClimbingStairs([10, 15, 20]) == 15


def test_example_2():
    assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_two_free_steps():
    assert minCostClimbingStairs([0, 0]) == 0


def test_two_steps():
    assert minCostClimbingStairs([1, 2]) == 1

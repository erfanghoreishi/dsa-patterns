# test_running_sum_1480.py
from running_sum_1480 import runningSum


def test_example_1():
    assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_ones():
    assert runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


def test_example_3():
    assert runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


def test_single():
    assert runningSum([5]) == [5]

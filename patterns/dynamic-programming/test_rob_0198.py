# test_rob_0198.py
from rob_0198 import rob


def test_example_1():
    assert rob([1, 2, 3, 1]) == 4


def test_example_2():
    assert rob([2, 7, 9, 3, 1]) == 12


def test_single_house():
    assert rob([5]) == 5


def test_adjacent_smaller():
    assert rob([2, 1, 1, 2]) == 4

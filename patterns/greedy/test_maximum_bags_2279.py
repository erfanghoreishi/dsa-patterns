# test_maximum_bags_2279.py
from maximum_bags_2279 import maximumBags


def test_example_1():
    assert maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2) == 3


def test_example_2():
    assert maximumBags([10, 2, 2], [2, 2, 0], 100) == 3


def test_already_full():
    assert maximumBags([5], [5], 0) == 1


def test_not_enough():
    assert maximumBags([3], [0], 2) == 0

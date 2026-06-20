# test_recover_order_3668.py
from recover_order_3668 import recoverOrder


def test_example_1():
    assert recoverOrder([3, 1, 2, 5, 4], [1, 3, 4]) == [3, 1, 4]


def test_example_2():
    assert recoverOrder([1, 4, 5, 3, 2], [2, 5]) == [5, 2]


def test_all_friends():
    assert recoverOrder([2, 1], [1, 2]) == [2, 1]


def test_single_friend():
    assert recoverOrder([3, 1, 2], [2]) == [2]

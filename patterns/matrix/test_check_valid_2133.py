# test_check_valid_2133.py
from check_valid_2133 import checkValid


def test_example_1():
    assert checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]) is True


def test_example_2():
    assert checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]) is False


def test_single_cell():
    assert checkValid([[1]]) is True


def test_valid_2x2():
    assert checkValid([[1, 2], [2, 1]]) is True

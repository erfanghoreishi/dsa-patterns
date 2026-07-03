# test_get_row_0119.py
from get_row_0119 import getRow


def test_row_0():
    assert getRow(0) == [1]


def test_row_1():
    assert getRow(1) == [1, 1]


def test_row_3():
    assert getRow(3) == [1, 3, 3, 1]


def test_row_4():
    assert getRow(4) == [1, 4, 6, 4, 1]

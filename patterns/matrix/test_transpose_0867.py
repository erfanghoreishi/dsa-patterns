# test_transpose_0867.py
from transpose_0867 import transpose


def test_wide():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_single_row():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_single_column():
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


def test_square():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

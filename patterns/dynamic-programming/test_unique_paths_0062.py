# test_unique_paths_0062.py
from unique_paths_0062 import uniquePaths


def test_example_1():
    assert uniquePaths(3, 7) == 28


def test_example_2():
    assert uniquePaths(3, 2) == 3


def test_single_cell():
    assert uniquePaths(1, 1) == 1


def test_square():
    assert uniquePaths(3, 3) == 6

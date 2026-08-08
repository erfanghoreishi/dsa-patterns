# test_minimum_total_0120.py
from minimum_total_0120 import minimumTotal


def test_example_1():
    assert minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11


def test_single_row():
    assert minimumTotal([[-10]]) == -10


def test_two_rows():
    assert minimumTotal([[1], [2, 3]]) == 3


def test_negatives():
    assert minimumTotal([[-1], [2, 3], [1, -1, -3]]) == -1


def test_input_not_mutated():
    triangle = [[2], [3, 4]]
    minimumTotal(triangle)
    assert triangle == [[2], [3, 4]]

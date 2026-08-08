# test_search_0704.py
from search_0704 import search


def test_example_1():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_example_2():
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_single_found():
    assert search([5], 5) == 0


def test_single_missing():
    assert search([5], -5) == -1


def test_empty():
    assert search([], 1) == -1


def test_first_and_last():
    assert search([1, 2, 3, 4, 5], 1) == 0
    assert search([1, 2, 3, 4, 5], 5) == 4

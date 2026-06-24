# test_find_winners_2225.py
from find_winners_2225 import findWinners


def test_example_1():
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
               [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    assert findWinners(matches) == [[1, 2, 10], [4, 5, 7, 8]]


def test_example_2():
    assert findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]


def test_single_match():
    assert findWinners([[1, 2]]) == [[1], [2]]

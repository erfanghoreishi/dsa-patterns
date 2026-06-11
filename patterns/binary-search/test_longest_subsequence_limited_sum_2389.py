# test_longest_subsequence_limited_sum_2389.py
from longest_subsequence_limited_sum_2389 import answerQueries


def test_example_1():
    assert answerQueries([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]


def test_example_2():
    assert answerQueries([2, 3, 4, 5], [1]) == [0]


def test_single_element():
    assert answerQueries([10], [5, 10, 15]) == [0, 1, 1]


def test_all_fit():
    assert answerQueries([1, 1, 1], [100]) == [3]

# test_minimum_abs_difference_1200.py
from minimum_abs_difference_1200 import minimumAbsDifference


def test_example_1():
    assert minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]


def test_example_2():
    assert minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]


def test_example_3_with_negatives():
    assert minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == \
        [[-14, -10], [19, 23], [23, 27]]


def test_two_elements():
    assert minimumAbsDifference([5, 1]) == [[1, 5]]

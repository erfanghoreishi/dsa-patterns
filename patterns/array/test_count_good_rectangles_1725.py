# test_count_good_rectangles_1725.py
from count_good_rectangles_1725 import countGoodRectangles


def test_example_1():
    assert countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]) == 3


def test_example_2():
    assert countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]) == 3


def test_single():
    assert countGoodRectangles([[1, 1]]) == 1

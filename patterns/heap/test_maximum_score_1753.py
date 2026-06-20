# test_maximum_score_1753.py
from maximum_score_1753 import maximumScore


def test_example_1():
    assert maximumScore(2, 4, 6) == 6


def test_example_2():
    assert maximumScore(4, 4, 6) == 7


def test_capped_by_largest():
    assert maximumScore(1, 8, 8) == 8


def test_all_equal():
    assert maximumScore(1, 1, 1) == 1


def test_zeros():
    assert maximumScore(0, 0, 0) == 0

# test_maximum_count_2529.py
from maximum_count_2529 import maximumCount


def test_example_1():
    assert maximumCount([-2, -1, -1, 1, 2, 3]) == 3


def test_example_2():
    assert maximumCount([-3, -2, -1, 0, 0, 1, 2]) == 3


def test_example_3_all_positive():
    assert maximumCount([5, 20, 66, 1314]) == 4


def test_all_zeros():
    # zeros count as neither positive nor negative
    assert maximumCount([0, 0, 0]) == 0


def test_empty():
    assert maximumCount([]) == 0


def test_single_negative():
    assert maximumCount([-1]) == 1


def test_matches_bisect_left():
    # the hand-rolled helper is exactly bisect_left; spot-check the counts directly
    from bisect import bisect_left
    nums = [-5, -5, -1, 0, 0, 2, 9]
    assert maximumCount(nums) == max(bisect_left(nums, 0),
                                     len(nums) - bisect_left(nums, 1))

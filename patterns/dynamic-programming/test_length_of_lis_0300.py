# test_length_of_lis_0300.py
from length_of_lis_0300 import lengthOfLIS


def test_example_1():
    assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example_2():
    assert lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4


def test_all_equal():
    assert lengthOfLIS([7, 7, 7, 7, 7]) == 1


def test_lis_not_ending_at_last():
    # the LIS is 1,2,3 — it does NOT end at the final element
    assert lengthOfLIS([1, 2, 3, 1]) == 3


def test_best_ends_mid_array():
    # LIS is 1,3,6,7,9,10 (len 6); the run ending at the last index is only 5
    assert lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6


def test_single():
    assert lengthOfLIS([5]) == 1

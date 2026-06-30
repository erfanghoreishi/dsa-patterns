# test_min_time_difference_0539.py
from min_time_difference_0539 import findMinDifference


def test_wrap_around():
    assert findMinDifference(["23:59", "00:00"]) == 1


def test_duplicate_time():
    assert findMinDifference(["00:00", "23:59", "00:00"]) == 0


def test_small_wrap():
    assert findMinDifference(["00:01", "23:59"]) == 2


def test_three_times():
    assert findMinDifference(["12:30", "06:15", "23:45"]) == 375


def test_evenly_spaced():
    assert findMinDifference(["01:00", "02:00", "03:00"]) == 60

# test_earliest_finish_time_3633.py
from earliest_finish_time_3633 import earliestFinishTime


def test_water_then_land_wins():
    # water 1..3, then land 3..6  ->  6  (better than land-first which gives 7)
    assert earliestFinishTime([2], [3], [1], [2]) == 6


def test_symmetric():
    assert earliestFinishTime([1], [1], [1], [1]) == 3


def test_multiple_options():
    # best: land 1..3, then water 3..5  ->  5
    assert earliestFinishTime([1, 5], [2, 1], [3], [2]) == 5


def test_water_first_fills_the_wait():
    # water 0..1 first, then land 10..12 -> 12  (better than land-first's 13)
    assert earliestFinishTime([10], [2], [0], [1]) == 12

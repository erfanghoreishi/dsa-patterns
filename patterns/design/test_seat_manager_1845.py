# test_seat_manager_1845.py
from seat_manager_1845 import SeatManager


def test_leetcode_example():
    sm = SeatManager(5)
    assert sm.reserve() == 1
    assert sm.reserve() == 2
    sm.unreserve(2)
    assert sm.reserve() == 2
    assert sm.reserve() == 3
    assert sm.reserve() == 4
    assert sm.reserve() == 5
    sm.unreserve(5)
    assert sm.reserve() == 5


def test_sequential():
    sm = SeatManager(3)
    assert [sm.reserve(), sm.reserve(), sm.reserve()] == [1, 2, 3]


def test_unreserve_gives_lowest():
    sm = SeatManager(3)
    sm.reserve()           # 1
    sm.reserve()           # 2
    sm.unreserve(1)
    assert sm.reserve() == 1   # 1 is free again and is the lowest

# test_di_string_match_0942.py
from di_string_match_0942 import diStringMatch


def test_example_1():
    assert diStringMatch("IDID") == [0, 4, 1, 3, 2]


def test_all_increasing():
    assert diStringMatch("III") == [0, 1, 2, 3]


def test_decreasing_then_increasing():
    assert diStringMatch("DDI") == [3, 2, 0, 1]


def test_single_i():
    assert diStringMatch("I") == [0, 1]


def test_single_d():
    assert diStringMatch("D") == [1, 0]

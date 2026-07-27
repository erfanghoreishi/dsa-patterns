# test_count_binary_substrings_0696.py
from count_binary_substrings_0696 import countBinarySubstrings


def test_example_1():
    assert countBinarySubstrings("00110011") == 6


def test_example_2():
    assert countBinarySubstrings("10101") == 4


def test_two_runs():
    assert countBinarySubstrings("0011") == 2


def test_single_char():
    assert countBinarySubstrings("1") == 0


def test_uneven_runs():
    assert countBinarySubstrings("000111") == 3

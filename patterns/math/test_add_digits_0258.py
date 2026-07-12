# test_add_digits_0258.py
from add_digits_0258 import addDigits


def test_example():
    assert addDigits(38) == 2      # 3+8=11 -> 1+1=2


def test_zero():
    assert addDigits(0) == 0


def test_single_digit():
    assert addDigits(9) == 9


def test_multiple_of_nine():
    assert addDigits(99) == 9


def test_larger():
    assert addDigits(12345) == 6

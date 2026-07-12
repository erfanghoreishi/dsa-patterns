# test_is_trionic_3637.py
from is_trionic_3637 import isTrionic


def test_trionic():
    assert isTrionic([1, 3, 5, 4, 2, 6]) is True


def test_minimal_trionic():
    assert isTrionic([1, 3, 2, 4]) is True


def test_only_increasing():
    assert isTrionic([1, 2, 3, 4]) is False


def test_only_decreasing():
    assert isTrionic([4, 3, 2, 1]) is False


def test_starts_with_decrease():
    assert isTrionic([2, 1, 3]) is False

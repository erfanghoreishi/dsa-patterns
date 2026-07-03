# test_count_bits_0338.py
from count_bits_0338 import countBits


def test_zero():
    assert countBits(0) == [0]


def test_two():
    assert countBits(2) == [0, 1, 1]


def test_five():
    assert countBits(5) == [0, 1, 1, 2, 1, 2]


def test_eight():
    assert countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]

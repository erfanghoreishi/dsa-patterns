# test_sum_and_multiply_3754.py
from sum_and_multiply_3754 import sumAndMultiply


def test_no_zeros():
    assert sumAndMultiply(234) == 2106      # 234 * (2+3+4)


def test_with_interior_zero():
    assert sumAndMultiply(105) == 90        # "15" * (1+5)


def test_only_zeros_left():
    assert sumAndMultiply(100) == 1         # "1" * 1


def test_zero():
    assert sumAndMultiply(0) == 0


def test_single_digit():
    assert sumAndMultiply(9) == 81          # 9 * 9

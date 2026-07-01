# test_digit_sum_2243.py
from digit_sum_2243 import digitSum


def test_example_1():
    assert digitSum("11111222223", 3) == "135"


def test_example_2():
    assert digitSum("00000000", 3) == "000"


def test_already_short():
    assert digitSum("12", 3) == "12"


def test_length_equals_k():
    assert digitSum("233", 3) == "233"

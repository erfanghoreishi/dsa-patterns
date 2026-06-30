# test_gcd_of_strings_1071.py
from gcd_of_strings_1071 import gcdOfStrings


def test_example_1():
    assert gcdOfStrings("ABCABC", "ABC") == "ABC"


def test_example_2():
    assert gcdOfStrings("ABABAB", "ABAB") == "AB"


def test_no_common_divisor():
    assert gcdOfStrings("LEET", "CODE") == ""


def test_longer_multiple():
    assert gcdOfStrings("ABABABAB", "ABAB") == "ABAB"


def test_single_char():
    assert gcdOfStrings("A", "A") == "A"

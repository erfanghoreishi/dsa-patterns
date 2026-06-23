# test_make_smallest_palindrome_2697.py
from make_smallest_palindrome_2697 import makeSmallestPalindrome


def test_example_1():
    assert makeSmallestPalindrome("egcfe") == "efcfe"


def test_example_2():
    assert makeSmallestPalindrome("abcd") == "abba"


def test_example_3():
    assert makeSmallestPalindrome("seven") == "neven"


def test_single_char():
    assert makeSmallestPalindrome("a") == "a"


def test_already_palindrome():
    assert makeSmallestPalindrome("aba") == "aba"

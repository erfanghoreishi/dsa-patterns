# test_valid_palindrome_ii_0680.py
from valid_palindrome_ii_0680 import validPalindrome


def test_example_1():
    assert validPalindrome("aba") is True


def test_example_2():
    assert validPalindrome("abca") is True


def test_example_3():
    assert validPalindrome("abc") is False


def test_single_char():
    assert validPalindrome("a") is True


def test_two_chars_different():
    assert validPalindrome("ab") is True


def test_needs_more_than_one_deletion():
    # ends match for a while, but the inner mismatch can't be fixed by one delete
    assert validPalindrome("eeccccbebaeeabebccceea") is False


def test_mismatch_deep_inside():
    assert validPalindrome("acxcybycxca") is True


def test_delete_from_left_branch():
    # mismatch at ends resolved only by deleting the left char
    assert validPalindrome("cbbcc") is True


def test_delete_from_right_branch():
    assert validPalindrome("ccbbc") is True


def test_even_palindrome():
    assert validPalindrome("abba") is True


def test_all_same():
    assert validPalindrome("aaaa") is True

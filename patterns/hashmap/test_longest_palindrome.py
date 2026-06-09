from longest_palindrome_0409 import longestPalindrome


def test_case_1():
    assert longestPalindrome("abccccdd") == 7


def test_case_2():
    assert longestPalindrome("a") == 1


def test_case_3():
    assert longestPalindrome("bb") == 2

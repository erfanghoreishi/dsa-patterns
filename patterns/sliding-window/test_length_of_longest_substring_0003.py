# test_length_of_longest_substring_0003.py
from length_of_longest_substring_0003 import lengthOfLongestSubstring


def test_example_1():
    assert lengthOfLongestSubstring("abcabcbb") == 3


def test_all_same():
    assert lengthOfLongestSubstring("bbbbb") == 1


def test_example_3():
    assert lengthOfLongestSubstring("pwwkew") == 3


def test_empty():
    assert lengthOfLongestSubstring("") == 0


def test_reset_middle():
    assert lengthOfLongestSubstring("dvdf") == 3

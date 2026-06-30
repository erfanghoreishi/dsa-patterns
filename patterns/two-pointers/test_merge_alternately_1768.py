# test_merge_alternately_1768.py
from merge_alternately_1768 import mergeAlternately


def test_equal_length():
    assert mergeAlternately("abc", "pqr") == "apbqcr"


def test_second_longer():
    assert mergeAlternately("ab", "pqrs") == "apbqrs"


def test_first_longer():
    assert mergeAlternately("abcd", "pq") == "apbqcd"


def test_single_chars():
    assert mergeAlternately("a", "b") == "ab"

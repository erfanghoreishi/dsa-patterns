# test_word_pattern_0290.py
from word_pattern_0290 import wordPattern


def test_match():
    assert wordPattern("abba", "dog cat cat dog") is True


def test_inconsistent_mapping():
    assert wordPattern("abba", "dog cat cat fish") is False


def test_same_word_different_pattern():
    assert wordPattern("aaaa", "dog cat cat dog") is False


def test_two_patterns_one_word():
    # mapping is consistent one way, but not one-to-one (a and b both -> dog)
    assert wordPattern("abba", "dog dog dog dog") is False


def test_length_mismatch():
    assert wordPattern("ab", "dog") is False

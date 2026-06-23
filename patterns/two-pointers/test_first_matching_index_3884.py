# test_first_matching_index_3884.py
from first_matching_index_3884 import firstMatchingIndex


def test_match_at_ends():
    assert firstMatchingIndex("abcba") == 0


def test_odd_middle_self_match():
    assert firstMatchingIndex("abcde") == 2


def test_no_match_even():
    assert firstMatchingIndex("ab") == -1


def test_single_char():
    assert firstMatchingIndex("a") == 0


def test_no_match_longer_even():
    assert firstMatchingIndex("abcd") == -1

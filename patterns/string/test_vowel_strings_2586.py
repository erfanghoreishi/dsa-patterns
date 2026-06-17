# test_vowel_strings_2586.py
from vowel_strings_2586 import vowelStrings


def test_example_1():
    assert vowelStrings(["are", "amy", "u"], 0, 2) == 2


def test_example_2():
    assert vowelStrings(["hey", "aeo", "mu", "ooo", "artro"], 1, 4) == 3


def test_single_word_match():
    assert vowelStrings(["aba", "eve"], 1, 1) == 1


def test_no_matches():
    assert vowelStrings(["bcd", "xyz"], 0, 1) == 0

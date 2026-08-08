# test_letter_combinations_0017.py
from letter_combinations_0017 import letterCombinations


def test_example_1():
    assert letterCombinations("23") == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
    ]


def test_empty():
    assert letterCombinations("") == []


def test_single_digit():
    assert letterCombinations("2") == ["a", "b", "c"]


def test_four_letter_digit():
    assert letterCombinations("7") == ["p", "q", "r", "s"]


def test_count_multiplies():
    # 7 has 4 letters, 9 has 4 -> 16 combinations
    assert len(letterCombinations("79")) == 16

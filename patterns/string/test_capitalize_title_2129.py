# test_capitalize_title_2129.py
from capitalize_title_2129 import capitalizeTitle


def test_example_1():
    assert capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title"


def test_example_2():
    assert capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word"


def test_short_word_lowercased():
    assert capitalizeTitle("i love LeetCode") == "i Love Leetcode"


def test_single_short_word():
    assert capitalizeTitle("ab") == "ab"

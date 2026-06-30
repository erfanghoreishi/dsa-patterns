# test_most_words_found_2114.py
from most_words_found_2114 import mostWordsFound


def test_example_1():
    assert mostWordsFound(
        ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    ) == 6


def test_example_2():
    assert mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3


def test_single_sentence():
    assert mostWordsFound(["hello world"]) == 2

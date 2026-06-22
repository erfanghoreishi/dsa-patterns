# test_can_be_typed_words_1935.py
from can_be_typed_words_1935 import canBeTypedWords


def test_example_1():
    assert canBeTypedWords("hello world", "ad") == 1


def test_example_2():
    assert canBeTypedWords("leet code", "lt") == 1


def test_all_broken():
    assert canBeTypedWords("a b c d e", "abcde") == 0


def test_none_broken():
    assert canBeTypedWords("hello world", "") == 2

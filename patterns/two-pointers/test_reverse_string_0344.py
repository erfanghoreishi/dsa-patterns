# test_reverse_string_0344.py
from reverse_string_0344 import reverseString


def test_odd_length():
    assert reverseString(list("hello")) == list("olleh")


def test_even_length():
    assert reverseString(list("Hannah")) == list("hannaH")


def test_empty():
    assert reverseString([]) == []


def test_single():
    assert reverseString(["a"]) == ["a"]

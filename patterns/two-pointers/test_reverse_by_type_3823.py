# test_reverse_by_type_3823.py
from reverse_by_type_3823 import reverseByType


def test_mixed():
    assert reverseByType("abc!def") == "fed!cba"


def test_all_letters():
    assert reverseByType("abcd") == "dcba"


def test_all_special():
    assert reverseByType("!@#") == "#@!"


def test_interleaved():
    assert reverseByType("a!b@c") == "c@b!a"


def test_empty():
    assert reverseByType("") == ""

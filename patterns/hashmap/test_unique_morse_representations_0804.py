# test_unique_morse_representations_0804.py
from unique_morse_representations_0804 import uniqueMorseRepresentations


def test_example_1():
    # "gin" and "zen" share "--...-.", "gig" and "msg" share "--...--."
    assert uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2


def test_single_word():
    assert uniqueMorseRepresentations(["a"]) == 1


def test_distinct_words():
    assert uniqueMorseRepresentations(["a", "b"]) == 2


def test_duplicate_words():
    assert uniqueMorseRepresentations(["gin", "gin"]) == 1

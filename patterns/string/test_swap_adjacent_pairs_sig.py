# test_swap_adjacent_pairs_sig.py
from swap_adjacent_pairs_sig import swapAdjacentPairs


def test_even_length():
    assert swapAdjacentPairs("abcdef") == "badcfe"


def test_odd_length():
    assert swapAdjacentPairs("abcde") == "badce"


def test_single_char():
    assert swapAdjacentPairs("a") == "a"


def test_two_chars():
    assert swapAdjacentPairs("ab") == "ba"


def test_empty():
    assert swapAdjacentPairs("") == ""

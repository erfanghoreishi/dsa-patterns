# test_are_almost_equal_1790.py
from are_almost_equal_1790 import areAlmostEqual


def test_one_swap():
    assert areAlmostEqual("bank", "kanb") is True


def test_too_many_diffs():
    assert areAlmostEqual("attack", "defend") is False


def test_already_equal():
    assert areAlmostEqual("kelb", "kelb") is True


def test_four_diffs():
    assert areAlmostEqual("abcd", "dcba") is False


def test_single_diff():
    assert areAlmostEqual("ab", "cb") is False

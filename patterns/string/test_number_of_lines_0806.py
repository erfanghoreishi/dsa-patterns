# test_number_of_lines_0806.py
from number_of_lines_0806 import numberOfLines


def test_all_equal_widths():
    widths = [10] * 26
    assert numberOfLines(widths, "abcdefghijklmnopqrstuvwxyz") == (3, 60)


def test_varied_widths():
    widths = [4] + [10] * 25
    assert numberOfLines(widths, "bbbcccdddaaa") == (2, 4)


def test_single_char():
    assert numberOfLines([10] * 26, "a") == (1, 10)

# test_minimum_recolors_2379.py
from minimum_recolors_2379 import minimumRecolors


def test_example_1():
    assert minimumRecolors("WBBWWBBWBW", 7) == 3


def test_example_2():
    assert minimumRecolors("WBWBBBW", 2) == 0


def test_all_white():
    assert minimumRecolors("WWWW", 2) == 2


def test_single_black():
    assert minimumRecolors("B", 1) == 0


def test_already_black_window():
    assert minimumRecolors("WBBBW", 3) == 0

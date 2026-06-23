# test_sort_even_odd_2164.py
from sort_even_odd_2164 import sortEvenOdd


def test_example_1():
    assert sortEvenOdd([4, 1, 2, 3]) == [2, 3, 4, 1]


def test_example_2():
    assert sortEvenOdd([2, 1]) == [2, 1]


def test_single():
    assert sortEvenOdd([5]) == [5]


def test_three_elements():
    assert sortEvenOdd([3, 2, 1]) == [1, 2, 3]

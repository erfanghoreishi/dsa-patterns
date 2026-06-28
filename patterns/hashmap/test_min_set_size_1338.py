# test_min_set_size_1338.py
from min_set_size_1338 import minSetSize


def test_example_1():
    assert minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2


def test_all_same():
    assert minSetSize([7, 7, 7, 7, 7, 7]) == 1


def test_two_distinct():
    assert minSetSize([1, 9]) == 1


def test_single():
    assert minSetSize([5]) == 1

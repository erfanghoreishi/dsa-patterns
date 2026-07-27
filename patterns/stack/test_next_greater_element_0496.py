# test_next_greater_element_0496.py
from next_greater_element_0496 import nextGreaterElement


def test_example_1():
    assert nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]


def test_example_2():
    assert nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]


def test_single():
    assert nextGreaterElement([1], [1]) == [-1]


def test_all_have_greater():
    assert nextGreaterElement([1, 2, 3], [3, 2, 1, 4]) == [4, 4, 4]

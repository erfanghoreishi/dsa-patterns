# test_minimum_operations_2357.py
from minimum_operations_2357 import minimumOperations


def test_example_1():
    assert minimumOperations([1, 5, 0, 3, 5]) == 3


def test_all_zero():
    assert minimumOperations([0]) == 0


def test_all_same():
    assert minimumOperations([2, 2, 2]) == 1


def test_empty():
    assert minimumOperations([]) == 0

# test_num_identical_pairs_1512.py
from num_identical_pairs_1512 import numIdenticalPairs


def test_example_1():
    assert numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4


def test_all_same():
    assert numIdenticalPairs([1, 1, 1, 1]) == 6


def test_all_distinct():
    assert numIdenticalPairs([1, 2, 3]) == 0


def test_returns_int():
    result = numIdenticalPairs([1, 1, 1])
    assert result == 3 and isinstance(result, int)

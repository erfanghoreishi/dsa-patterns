# test_count_triplets_1442.py
from count_triplets_1442 import countTriplets


def test_example_1():
    assert countTriplets([2, 3, 1, 6, 7]) == 4


def test_example_2():
    assert countTriplets([1, 1, 1, 1, 1]) == 10


def test_no_triplets():
    assert countTriplets([2, 3]) == 0


def test_pair_equal():
    # [x, x] -> XOR(0..1) == 0, one split (j=1) -> k-i = 1
    assert countTriplets([5, 5]) == 1

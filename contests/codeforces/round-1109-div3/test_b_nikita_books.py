# test_b_nikita_books.py
from b_nikita_books import solve


def test_exact_triangular():
    assert solve([1, 2, 3]) == "YES"


def test_too_few():
    assert solve([1, 1]) == "NO"


def test_surplus():
    assert solve([3, 3, 3]) == "YES"


def test_single_ok():
    assert solve([1]) == "YES"


def test_zero_first():
    assert solve([0]) == "NO"


def test_mid_prefix_fails():
    assert solve([2, 0, 4]) == "NO"

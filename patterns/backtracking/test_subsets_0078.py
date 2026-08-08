# test_subsets_0078.py
from subsets_0078 import subsets


def test_example_1():
    assert subsets([1, 2, 3]) == [
        [1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []
    ]


def test_single():
    assert subsets([0]) == [[0], []]


def test_empty():
    assert subsets([]) == [[]]


def test_power_set_size_and_uniqueness():
    result = subsets([1, 2, 3, 4])
    assert len(result) == 16                       # 2^n subsets
    assert len({tuple(s) for s in result}) == 16   # all distinct


def test_entries_are_independent_copies():
    # guards the current[:] copy — without it every entry would be the same list
    result = subsets([1, 2])
    assert sorted(len(s) for s in result) == [0, 1, 1, 2]

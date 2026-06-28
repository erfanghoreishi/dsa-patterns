# test_allocator_2502.py
from allocator_2502 import Allocator


def test_leetcode_example():
    a = Allocator(10)
    assert a.allocate(1, 1) == 0
    assert a.allocate(1, 2) == 1
    assert a.allocate(1, 3) == 2
    assert a.freeMemory(2) == 1
    assert a.allocate(3, 4) == 3
    assert a.allocate(1, 1) == 1
    assert a.allocate(1, 1) == 6
    assert a.freeMemory(1) == 3
    assert a.allocate(10, 2) == -1


def test_allocate_too_big():
    a = Allocator(2)
    assert a.allocate(3, 1) == -1


def test_free_unknown_id():
    a = Allocator(5)
    assert a.freeMemory(99) == 0


def test_reuse_after_free():
    a = Allocator(4)
    assert a.allocate(4, 1) == 0
    assert a.allocate(1, 2) == -1
    assert a.freeMemory(1) == 4
    assert a.allocate(1, 2) == 0

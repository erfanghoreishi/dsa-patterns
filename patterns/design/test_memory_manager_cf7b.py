# test_memory_manager_cf7b.py
from memory_manager_cf7b import MemoryManager


def test_codeforces_example():
    m = MemoryManager(10)
    assert m.alloc(5) == 1
    assert m.alloc(3) == 2
    assert m.erase(1) is None
    assert m.alloc(6) == "NULL"
    m.defragment()
    assert m.alloc(6) == 3


def test_illegal_erase_unknown_id():
    m = MemoryManager(5)
    assert m.erase(1) == "ILLEGAL_ERASE_ARGUMENT"


def test_illegal_erase_twice():
    m = MemoryManager(5)
    assert m.alloc(2) == 1
    assert m.erase(1) is None
    assert m.erase(1) == "ILLEGAL_ERASE_ARGUMENT"


def test_failed_alloc_does_not_consume_id():
    m = MemoryManager(3)
    assert m.alloc(5) == "NULL"   # too big, no id used
    assert m.alloc(3) == 1        # next success still gets id 1

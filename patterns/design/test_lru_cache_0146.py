# test_lru_cache_0146.py
from lru_cache_0146 import LRUCache


def test_leetcode_example():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1        # 1 is now most-recent; 2 is LRU
    c.put(3, 3)                 # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)                 # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


def test_get_refreshes_recency():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1        # touch 1 so 2 becomes the LRU
    c.put(3, 3)                 # evicts 2, not 1
    assert c.get(1) == 1
    assert c.get(2) == -1


def test_update_existing_no_evict():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)               # update, not insert -> nothing evicted
    assert c.get(1) == 10
    assert c.get(2) == 2


def test_capacity_one():
    c = LRUCache(1)
    c.put(1, 1)
    c.put(2, 2)                 # evicts 1
    assert c.get(1) == -1
    assert c.get(2) == 2


def test_missing_key():
    c = LRUCache(2)
    assert c.get(99) == -1

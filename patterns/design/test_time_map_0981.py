# test_time_map_0981.py
from time_map_0981 import TimeMap


def test_leetcode_example():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"    # no set at 3 -> falls back to timestamp 1
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"


def test_missing_key():
    tm = TimeMap()
    assert tm.get("nope", 10) == ""


def test_timestamp_before_first_set():
    tm = TimeMap()
    tm.set("a", "x", 5)
    assert tm.get("a", 1) == ""         # nothing stored at or before 1
    assert tm.get("a", 5) == "x"


def test_multiple_keys_are_independent():
    tm = TimeMap()
    tm.set("a", "a1", 1)
    tm.set("b", "b1", 2)
    tm.set("a", "a2", 3)
    assert tm.get("a", 2) == "a1"
    assert tm.get("b", 1) == ""
    assert tm.get("b", 100) == "b1"
    assert tm.get("a", 100) == "a2"


def test_many_values_binary_search():
    tm = TimeMap()
    for i in range(1, 101):
        tm.set("k", f"v{i}", i * 2)     # timestamps 2, 4, ..., 200
    assert tm.get("k", 2) == "v1"
    assert tm.get("k", 3) == "v1"       # between 2 and 4 -> latest is 2
    assert tm.get("k", 199) == "v99"
    assert tm.get("k", 200) == "v100"
    assert tm.get("k", 1000) == "v100"
    assert tm.get("k", 1) == ""

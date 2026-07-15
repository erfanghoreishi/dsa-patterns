# test_a_iskander_drawings.py
from a_iskander_drawings import solve


def test_full_run():
    assert solve("###") == 2


def test_gaps():
    assert solve("#.#") == 1


def test_no_hash():
    assert solve("....") == 0


def test_long_run():
    assert solve("######") == 3


def test_single():
    assert solve("#") == 1

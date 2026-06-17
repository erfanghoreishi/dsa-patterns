# test_dest_city_1436.py
from dest_city_1436 import destCity


def test_example_1():
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    assert destCity(paths) == "Sao Paulo"


def test_example_2():
    assert destCity([["B", "C"], ["D", "B"], ["C", "A"]]) == "A"


def test_single_path():
    assert destCity([["A", "Z"]]) == "Z"

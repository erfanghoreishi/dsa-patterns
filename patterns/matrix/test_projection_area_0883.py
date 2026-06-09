# test_projection_area_0883.py
from projection_area_0883 import projectionArea


def test_two_by_two():
    assert projectionArea([[1, 2], [3, 4]]) == 17


def test_single_cell():
    assert projectionArea([[2]]) == 5


def test_with_zeros():
    assert projectionArea([[1, 0], [0, 2]]) == 8

# test_check_valid_grid_2596.py
from check_valid_grid_2596 import checkValidGrid


def test_valid_tour():
    # a real, verified 5x5 knight tour starting at (0,0)
    grid = [
        [0, 5, 14, 9, 20],
        [13, 8, 19, 4, 15],
        [18, 1, 6, 21, 10],
        [7, 12, 23, 16, 3],
        [24, 17, 2, 11, 22],
    ]
    assert checkValidGrid(grid) is True


def test_valid_tour_2():
    grid = [
        [0, 11, 16, 5, 20],
        [17, 4, 19, 10, 15],
        [12, 1, 8, 21, 6],
        [3, 18, 23, 14, 9],
        [24, 13, 2, 7, 22],
    ]
    assert checkValidGrid(grid) is True


def test_invalid_moves():
    # LeetCode Example 2: starts at 0 but the jumps aren't all knight moves
    assert checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]) is False


def test_bad_start():
    # cell (0,0) must hold 0
    assert checkValidGrid([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) is False


def test_single_cell():
    assert checkValidGrid([[0]]) is True

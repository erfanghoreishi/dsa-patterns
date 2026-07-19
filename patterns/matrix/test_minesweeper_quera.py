# test_minesweeper_quera.py
from minesweeper_quera import minesweeper


def test_given_example():
    bombs = {(1, 1), (1, 3), (3, 2), (4, 2), (4, 3)}
    assert minesweeper(4, 3, bombs) == ["* 2 *", "2 3 2", "2 * 3", "2 * *"]


def test_no_bombs():
    assert minesweeper(2, 2, set()) == ["0 0", "0 0"]


def test_all_bombs():
    assert minesweeper(2, 2, {(1, 1), (1, 2), (2, 1), (2, 2)}) == ["* *", "* *"]


def test_single_center_bomb():
    assert minesweeper(3, 3, {(2, 2)}) == ["1 1 1", "1 * 1", "1 1 1"]

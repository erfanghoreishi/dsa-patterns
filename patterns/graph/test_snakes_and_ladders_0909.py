# test_snakes_and_ladders_0909.py
from snakes_and_ladders_0909 import snakesAndLadders


def test_example_1():
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    assert snakesAndLadders(board) == 4


def test_one_move():
    assert snakesAndLadders([[-1, -1], [-1, 3]]) == 1


def test_unreachable():
    assert snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) == -1


def test_tiny_board_one_roll():
    # 2x2, no snakes/ladders: reach square 4 from 1 in a single roll
    assert snakesAndLadders([[-1, -1], [-1, -1]]) == 1

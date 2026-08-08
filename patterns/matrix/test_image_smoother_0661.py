# test_image_smoother_0661.py
from image_smoother_0661 import imageSmoother


def test_example_1():
    assert imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_example_2():
    assert imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == \
        [[137, 141, 137], [141, 138, 141], [137, 141, 137]]


def test_single_cell():
    assert imageSmoother([[5]]) == [[5]]


def test_single_row():
    # each cell averages itself + its row neighbours: (1+2)//2 = 1 for both
    assert imageSmoother([[1, 2]]) == [[1, 1]]


def test_input_not_mutated():
    img = [[1, 1], [1, 1]]
    imageSmoother(img)
    assert img == [[1, 1], [1, 1]]

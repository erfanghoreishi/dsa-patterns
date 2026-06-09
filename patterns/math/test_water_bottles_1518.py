# test_num_water_bottles_1518.py
from water_bottles_1518 import numWaterBottles


def test_9_3():
    assert numWaterBottles(9, 3) == 13


def test_15_4():
    assert numWaterBottles(15, 4) == 19


def test_9_2():
    assert numWaterBottles(9, 2) == 17


def test_10_3():
    assert numWaterBottles(10, 3) == 14

# test_climbing_stairs_0070.py
from climbing_stairs_0070 import climbStairs


def test_one():
    assert climbStairs(1) == 1


def test_two():
    assert climbStairs(2) == 2


def test_three():
    assert climbStairs(3) == 3


def test_five():
    assert climbStairs(5) == 8


def test_larger():
    assert climbStairs(10) == 89

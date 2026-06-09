# test_reverse_prefix.py
from reverse_prefix_3794 import reversePrefix

def test_case_1():
    assert reversePrefix("abcd", 2) == "bacd"

def test_case_2():
    assert reversePrefix("xyz", 3) == "zyx"

def test_case_3():
    assert reversePrefix("hey", 1) == "hey"

def test_case_4():
    assert reversePrefix("jjih", 4) == "hijj"
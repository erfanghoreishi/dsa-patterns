# test_truncate_sentence_1816.py
from truncate_sentence_1816 import truncateSentence


def test_example_1():
    assert truncateSentence("Hello how are you Contestant", 4) == "Hello how are you"


def test_example_2():
    assert truncateSentence("What is the solution to this problem", 4) == "What is the solution"


def test_keep_all():
    assert truncateSentence("chopper is not a tanuki", 5) == "chopper is not a tanuki"

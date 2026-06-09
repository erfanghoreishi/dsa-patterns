from clear_digits_3174 import clearDigits

def test_case_1():
    assert clearDigits("abc") == "abc"


def test_case_2():
    assert clearDigits("cb34") == ""


def test_case_3():
    assert clearDigits("cb34ab98cd") == "cd"

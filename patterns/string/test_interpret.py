from interpret_1678 import interpret


def test_case_1():
    assert interpret("G()(al)") == "Goal"


def test_case_2():
    assert interpret("G()()()()(al)") == "Gooooal"


def test_case_3():
    assert interpret("(al)G(al)()()G") == "alGalooG"

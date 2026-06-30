# test_defang_ip_addr_1108.py
from defang_ip_addr_1108 import defangIPaddr


def test_example_1():
    assert defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"


def test_example_2():
    assert defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"

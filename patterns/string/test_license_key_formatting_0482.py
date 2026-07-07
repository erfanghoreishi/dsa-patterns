# test_license_key_formatting_0482.py
from license_key_formatting_0482 import licenseKeyFormatting


def test_example_1():
    assert licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"


def test_example_2():
    assert licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"


def test_all_dashes():
    assert licenseKeyFormatting("---", 3) == ""


def test_group_size_one():
    assert licenseKeyFormatting("a-a-a-a-", 1) == "A-A-A-A"

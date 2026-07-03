# test_num_unique_emails_0929.py
from num_unique_emails_0929 import numUniqueEmails


def test_example_1():
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    assert numUniqueEmails(emails) == 2


def test_all_distinct():
    assert numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3


def test_dots_and_plus_ignored():
    # same local after normalization, same domain -> one unique address
    assert numUniqueEmails(["a.b+x@d.com", "ab+y@d.com", "a.b@d.com"]) == 1

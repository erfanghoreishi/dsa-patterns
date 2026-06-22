# test_partition_labels_0763.py
from partition_labels_0763 import partitionLabels


def test_example_1():
    assert partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_single_partition():
    assert partitionLabels("eccbbbbdec") == [10]


def test_single_char():
    assert partitionLabels("a") == [1]


def test_all_distinct():
    assert partitionLabels("abc") == [1, 1, 1]

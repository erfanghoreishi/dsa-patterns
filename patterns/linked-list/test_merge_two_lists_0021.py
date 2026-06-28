# test_merge_two_lists_0021.py
from merge_two_lists_0021 import mergeTwoLists, ListNode


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def test_example():
    merged = mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]


def test_both_empty():
    assert to_list(mergeTwoLists(build([]), build([]))) == []


def test_first_empty():
    assert to_list(mergeTwoLists(build([]), build([0]))) == [0]


def test_second_empty():
    assert to_list(mergeTwoLists(build([1, 2, 3]), build([]))) == [1, 2, 3]

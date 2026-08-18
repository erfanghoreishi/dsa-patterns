# test_has_cycle_0141.py
from has_cycle_0141 import hasCycle, ListNode


def build(vals, pos=-1):
    """Build a list; if pos >= 0, link the tail back to index pos."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test_example_1():
    assert hasCycle(build([3, 2, 0, -4], pos=1)) is True


def test_example_2():
    assert hasCycle(build([1, 2], pos=0)) is True


def test_single_no_cycle():
    assert hasCycle(build([1])) is False


def test_empty():
    assert hasCycle(None) is False


def test_self_loop():
    assert hasCycle(build([1], pos=0)) is True


def test_odd_length_no_cycle():
    # odd length: fast lands on the final node, then fast.next is None
    assert hasCycle(build([1, 2, 3, 4, 5])) is False

#21. Merge Two Sorted Lists
# THOUGHTS: draw a clean trace on paper to lock in the pointer juggling.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    pre_head = ListNode(-1)       # dummy node so we don't special-case the head
    prev = pre_head

    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    # attach whatever remains (at most one list is non-empty). Must be AFTER the
    # loop, so an initially-empty list still gets the other list appended.
    prev.next = list1 if list1 else list2

    return pre_head.next

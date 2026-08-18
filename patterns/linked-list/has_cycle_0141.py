#141. Linked List Cycle
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    # Floyd's tortoise & hare: slow moves 1 step, fast moves 2.
    # In a cycle the gap closes by 1 each step, so they must meet;
    # with no cycle, fast simply runs off the end.
    slow, fast = head, head

    while fast and fast.next:      # fast.next guards the fast.next.next below
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

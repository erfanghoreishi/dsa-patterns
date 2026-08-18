#101. Symmetric Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    """Assumes root is not None (LeetCode guarantees >= 1 node)."""
    def is_mirror(left, right):
        if not left and not right:      # both empty -> mirrored
            return True
        if not left or not right:       # only one empty -> not mirrored
            return False
        if left.val != right.val:
            return False

        # the MIRROR pairing: outer-with-outer, inner-with-inner.
        # (compare with is_same_tree_0100.py, which pairs same-side:
        #  left.left vs right.left — that's identity, this is reflection)
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)

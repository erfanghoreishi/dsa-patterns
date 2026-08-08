#100. Same Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if not p and not q:      # both empty -> identical
        return True
    if not p or not q:       # exactly one empty -> different shape
        return False
    if p.val != q.val:
        return False

    # NOTE: the right call passes (q.right, p.right) rather than (p.right, q.right).
    # Harmless — isSameTree is symmetric, so the argument order doesn't matter.
    return isSameTree(p.left, q.left) and isSameTree(q.right, p.right)

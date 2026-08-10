#226. Invert Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return

    # inline swap of the two children (see notes/tricks.md — no temp needed)
    root.left, root.right = root.right, root.left

    # then invert each subtree; the recursive returns aren't needed since the
    # swap already mutated this node in place
    invertTree(root.left)
    invertTree(root.right)

    return root

#110. Balanced Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    # O(n^2): height() is recomputed from scratch at every node.
    # See notes/redo.md — the O(n) version returns height and a "balanced" flag
    # together (or -1 as a sentinel) so each node is visited once.
    def height(node):
        if not node:
            return 0
        left = 1 + height(node.left)
        right = 1 + height(node.right)
        return max(left, right)

    if not root:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False

    # every subtree must also be balanced, not just the root
    return isBalanced(root.left) and isBalanced(root.right)

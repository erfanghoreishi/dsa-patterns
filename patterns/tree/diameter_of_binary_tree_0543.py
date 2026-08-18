#543. Diameter of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    max_diameter = 0

    def height(root):
        # `nonlocal` lets this inner function REASSIGN max_diameter in the
        # enclosing scope (see notes/python-builtins.md)
        nonlocal max_diameter

        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        # the widest path THROUGH this node = its two subtree heights combined.
        # tracked as a side effect because the function itself must return height.
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return max_diameter

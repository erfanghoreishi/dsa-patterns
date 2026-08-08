#104. Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    def inorder(node):
        # depth of an empty subtree is 0 -> recursion bottoms out here
        if not node:
            return 0
        left = 1 + inorder(node.left)     # +1 counts this node itself
        right = 1 + inorder(node.right)
        return max(left, right)           # the deeper side wins

    return inorder(root)

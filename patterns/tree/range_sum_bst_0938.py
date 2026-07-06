#938. Range Sum of BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high):
    result = [0]      # a 1-element list holds the running sum (Python 2 has no `nonlocal`)

    def dfs(node):
        if not node:
            return
        if low <= node.val <= high:
            result[0] += node.val
        # BST pruning: only descend where in-range values can still exist
        if node.val > low:
            dfs(node.left)
        if node.val < high:
            dfs(node.right)

    dfs(root)
    return result[0]

#145. Binary Tree Postorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    result = []

    def traverse(root):
        if not root:
            return
        # postorder = left, right, THEN the node itself.
        # (preorder appends before the recursion; inorder appends between them)
        traverse(root.left)
        traverse(root.right)
        result.append(root.val)

    traverse(root)
    return result

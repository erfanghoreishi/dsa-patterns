# test_invert_tree_0226.py
from collections import deque

from invert_tree_0226 import invertTree, TreeNode


def level_order(root):
    """Serialize to LeetCode-style level order, trailing Nones trimmed."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


def test_example_1():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                       TreeNode(7, TreeNode(6), TreeNode(9)))
    assert level_order(invertTree(root)) == [4, 7, 2, 9, 6, 3, 1]


def test_example_2():
    assert level_order(invertTree(TreeNode(2, TreeNode(1), TreeNode(3)))) == [2, 3, 1]


def test_empty():
    assert invertTree(None) is None


def test_single_node():
    assert level_order(invertTree(TreeNode(1))) == [1]


def test_lone_child_moves_sides():
    # a left-only child must end up on the right
    assert level_order(invertTree(TreeNode(1, TreeNode(2)))) == [1, None, 2]


def test_returns_same_root_object():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert invertTree(root) is root      # inverts in place

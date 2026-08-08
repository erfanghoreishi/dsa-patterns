# test_max_depth_0104.py
from max_depth_0104 import maxDepth, TreeNode


def test_example_1():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert maxDepth(root) == 3


def test_example_2():
    assert maxDepth(TreeNode(1, None, TreeNode(2))) == 2


def test_empty_tree():
    assert maxDepth(None) == 0


def test_single_node():
    assert maxDepth(TreeNode(1)) == 1


def test_left_skewed():
    # 1 -> 2 -> 3 -> 4 all on the left
    assert maxDepth(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))) == 4

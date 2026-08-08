# test_is_same_tree_0100.py
from is_same_tree_0100 import isSameTree, TreeNode


def test_identical():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(p, q) is True


def test_different_shape():
    # same values, mirrored placement
    assert isSameTree(TreeNode(1, TreeNode(2)),
                      TreeNode(1, None, TreeNode(2))) is False


def test_different_values():
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTree(p, q) is False


def test_both_empty():
    assert isSameTree(None, None) is True


def test_one_empty():
    assert isSameTree(TreeNode(1), None) is False


def test_deep_right_mismatch():
    # difference is buried on the right spine — checks the right recursion really runs
    p = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    q = TreeNode(1, None, TreeNode(2, None, TreeNode(4)))
    assert isSameTree(p, q) is False

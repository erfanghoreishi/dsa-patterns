# test_is_balanced_0110.py
from is_balanced_0110 import isBalanced, TreeNode


def test_example_1():
    # [3,9,20,null,null,15,7]
    assert isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) is True


def test_example_2():
    # [1,2,2,3,3,null,null,4,4]
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(3)), TreeNode(2))
    assert isBalanced(root) is False


def test_empty():
    assert isBalanced(None) is True


def test_single_node():
    assert isBalanced(TreeNode(1)) is True


def test_height_difference_of_one_is_ok():
    assert isBalanced(TreeNode(1, TreeNode(2))) is True


def test_deep_imbalance_below_a_balanced_root():
    # the root's own subtree heights differ by <= 1 at first glance, but a deeper
    # subtree is unbalanced — this is why the recursion must check every node
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))), TreeNode(2))
    assert isBalanced(root) is False

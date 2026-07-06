# test_range_sum_bst_0938.py
from range_sum_bst_0938 import rangeSumBST, TreeNode


def test_example_1():
    root = TreeNode(10,
                    TreeNode(5, TreeNode(3), TreeNode(7)),
                    TreeNode(15, None, TreeNode(18)))
    assert rangeSumBST(root, 7, 15) == 32


def test_example_2():
    root = TreeNode(10,
                    TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
                    TreeNode(15, TreeNode(13), TreeNode(18)))
    assert rangeSumBST(root, 6, 10) == 23


def test_single_in_range():
    assert rangeSumBST(TreeNode(5), 1, 10) == 5


def test_single_out_of_range():
    assert rangeSumBST(TreeNode(5), 6, 10) == 0

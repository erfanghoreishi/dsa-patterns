# test_postorder_traversal_0145.py
from postorder_traversal_0145 import postorderTraversal, TreeNode


def test_example_1():
    # [1, null, 2, 3]
    assert postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [3, 2, 1]


def test_empty():
    assert postorderTraversal(None) == []


def test_single_node():
    assert postorderTraversal(TreeNode(1)) == [1]


def test_full_tree_order():
    #        1
    #      2   3
    #     4 5 6 7
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                       TreeNode(3, TreeNode(6), TreeNode(7)))
    assert postorderTraversal(root) == [4, 5, 2, 6, 7, 3, 1]


def test_root_is_last():
    # the defining property of postorder: the root comes last
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert postorderTraversal(root)[-1] == 1


def test_left_skewed():
    # 1 -> 2 -> 3 all on the left; unwinds deepest-first
    assert postorderTraversal(TreeNode(1, TreeNode(2, TreeNode(3)))) == [3, 2, 1]

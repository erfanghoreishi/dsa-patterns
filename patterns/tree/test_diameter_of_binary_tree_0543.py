# test_diameter_of_binary_tree_0543.py
from diameter_of_binary_tree_0543 import diameterOfBinaryTree, TreeNode


def test_example_1():
    # [1,2,3,4,5] -> path 4-2-1-3 is 3 edges
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameterOfBinaryTree(root) == 3


def test_example_2():
    assert diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1


def test_single_node():
    assert diameterOfBinaryTree(TreeNode(1)) == 0


def test_empty():
    assert diameterOfBinaryTree(None) == 0


def test_diameter_not_through_root():
    # root has only a left child; the widest path (4-3-2-6-7) sits inside that
    # subtree, so returning the root's own left+right height would be wrong
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)),
                                   TreeNode(6, TreeNode(7), TreeNode(8))))
    assert diameterOfBinaryTree(root) == 4


def test_left_skewed():
    # 1-2-3-4 chain: 3 edges
    assert diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))) == 3

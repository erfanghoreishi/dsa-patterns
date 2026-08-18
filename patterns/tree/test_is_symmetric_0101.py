# test_is_symmetric_0101.py
from is_symmetric_0101 import isSymmetric, TreeNode


def test_example_1():
    # [1,2,2,3,4,4,3]
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                       TreeNode(2, TreeNode(4), TreeNode(3)))
    assert isSymmetric(root) is True


def test_example_2():
    # [1,2,2,null,3,null,3] — both 3s hang right, so it's a copy, not a mirror
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                       TreeNode(2, None, TreeNode(3)))
    assert isSymmetric(root) is False


def test_single_node():
    assert isSymmetric(TreeNode(1)) is True


def test_two_equal_children():
    assert isSymmetric(TreeNode(1, TreeNode(2), TreeNode(2))) is True


def test_different_values():
    assert isSymmetric(TreeNode(1, TreeNode(2), TreeNode(3))) is False


def test_mirrored_shape_deeper():
    # structure mirrors but a deep value differs
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                       TreeNode(2, TreeNode(4), TreeNode(9)))
    assert isSymmetric(root) is False

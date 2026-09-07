# test_is_subtree_0572.py
from is_subtree_0572 import isSubtree, TreeNode


def test_example_1():
    # root = [3,4,5,1,2], subRoot = [4,1,2]
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubtree(root, sub) is True


def test_example_2():
    # same as example 1 but with an extra 0 under the 2 — no longer an exact match
    root = TreeNode(3,
                    TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
                    TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubtree(root, sub) is False


def test_must_be_full_subtree_not_a_prefix():
    # subRoot matches the top of root but root has extra descendants below
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    sub = TreeNode(1, TreeNode(2))
    assert isSubtree(root, sub) is False


def test_whole_tree_is_the_subtree():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    sub = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSubtree(root, sub) is True


def test_single_node_match():
    assert isSubtree(TreeNode(1, TreeNode(2)), TreeNode(2)) is True


def test_single_node_no_match():
    assert isSubtree(TreeNode(1, TreeNode(2)), TreeNode(5)) is False


def test_empty_root():
    assert isSubtree(None, TreeNode(1)) is False


def test_match_deep_on_the_right_spine():
    # forces the right-hand recursion to actually run
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, TreeNode(4))))
    sub = TreeNode(3, TreeNode(4))
    assert isSubtree(root, sub) is True


def test_same_values_different_shape():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    sub = TreeNode(2, None, TreeNode(3))
    assert isSubtree(root, sub) is False


def test_duplicate_values_later_match():
    # first candidate node with the right value fails; a later one succeeds
    root = TreeNode(4,
                    TreeNode(4, TreeNode(9)),
                    TreeNode(4, TreeNode(1), TreeNode(2)))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubtree(root, sub) is True

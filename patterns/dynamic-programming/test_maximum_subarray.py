from maximum_subarray_0053 import maxSubArray


def test_case_1():
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_case_2():
    assert maxSubArray([1]) == 1


def test_case_3():
    assert maxSubArray([5, 4, -1, 7, 8]) == 23

#1480. Running Sum of 1d Array
from itertools import accumulate  # note: accumulate is Python 3 only


def runningSum(nums):
    return list(accumulate(nums))

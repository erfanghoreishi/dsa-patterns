#300. Longest Increasing Subsequence
"""
f(i) = length of the LIS *ending at* index i
f(i) = max(f(j) + 1 for j < i where nums[j] < nums[i]), or 1 if no such j
"""


def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        # every earlier index j with nums[j] < nums[i] can be extended by nums[i];
        # take the best of them and add 1. default=0 covers "no valid j" -> dp[i] = 1.
        dp[i] = max([dp[j] for j in range(i) if nums[j] < nums[i]], default=0) + 1

    # the LIS can end at ANY index, not necessarily the last one
    return max(dp)

#2389. Longest Subsequence With Limited Sum
from itertools import accumulate
from bisect import bisect_right


def answerQueries(nums, queries):
    nums = sorted(nums)
    prefix = list(accumulate(nums))                 # running totals of smallest elements
    return [bisect_right(prefix, q) for q in queries]  # how many prefix sums are <= q


# Reference: same logic without itertools.accumulate / bisect built-ins
# def answerQueries(nums, queries):
#     nums = sorted(nums)
#     # manual prefix sums
#     prefix = []
#     total = 0
#     for x in nums:
#         total += x
#         prefix.append(total)
#     # manual bisect_right: count of prefix sums <= q (binary search)
#     def count_le(q):
#         lo, hi = 0, len(prefix)
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if prefix[mid] <= q:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo
#     return [count_le(q) for q in queries]

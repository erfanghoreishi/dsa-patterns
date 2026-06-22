#2357. Make Array Zero by Subtracting Equal Amounts
import heapq


def minimumOperations(nums):
    h = [num for num in nums if num > 0]
    heapq.heapify(h)
    count = 0

    while h:
        smallest = heapq.heappop(h)
        h = [num - smallest for num in h if num - smallest != 0]
        count += 1

    return count


# One-liner: the answer is simply the number of DISTINCT positive values.
# Each operation subtracts the current smallest, which zeroes every copy of that
# value and shifts the rest down — so it removes exactly one distinct value per
# step. Counting distinct positives is O(n) vs this heap version's O(n^2).
# def minimumOperations(nums):
#     return len(set(n for n in nums if n > 0))

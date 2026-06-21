#1753. Maximum Score From Removing Stones
def maximumScore(a, b, c):
    a, b, c = sorted((a, b, c))
    if c >= a + b:
        return a + b          # biggest pile dominates: limited by the other two
    return (a + b + c) // 2   # balanced enough: use almost every stone


# O(total) max-heap version (greedy: always drain the two largest piles).
# Kept for reference — the closed-form above is O(1).
# import heapq
# def maximumScore(a, b, c):
#     score = 0
#     stones = [-a, -b, -c]  # max-heap (negate the values)
#     heapq.heapify(stones)
#     while True:
#         largest = -heapq.heappop(stones)
#         second = -heapq.heappop(stones)
#         if second == 0:        # fewer than two non-empty piles left
#             return score
#         largest -= 1
#         second -= 1
#         heapq.heappush(stones, -largest)
#         heapq.heappush(stones, -second)
#         score += 1

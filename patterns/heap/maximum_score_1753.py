#1753. Maximum Score From Removing Stones
import heapq


def maximumScore(a, b, c):
    score = 0
    stones = [-a, -b, -c]  # max-heap (negate the values)
    heapq.heapify(stones)

    while True:
        largest = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        if second == 0:        # fewer than two non-empty piles left
            return score

        largest -= 1
        second -= 1

        heapq.heappush(stones, -largest)
        heapq.heappush(stones, -second)

        score += 1

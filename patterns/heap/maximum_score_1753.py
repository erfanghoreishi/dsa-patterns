#1753. Maximum Score From Removing Stones
# REMINDER: rewrite with the optimal solution — repeatedly decrement the 2 LARGEST
#   piles. With a max-heap, reading the largest is O(1) and each pop/push is
#   O(log n), avoiding the O(n) max() + remove() + heapify this version redoes every
#   iteration. It's also cleaner: a single loop running until fewer than two piles
#   remain, instead of two separate loops.
import heapq


def maximumScore(a, b, c):
    count = 0
    stones = [a, b, c]
    heapq.heapify(stones)

    while stones[0] > 0:
        smallest = heapq.heappop(stones)
        biggest = max(stones)
        stones.remove(biggest)

        smallest -= 1
        biggest -= 1

        heapq.heappush(stones, smallest)
        heapq.heappush(stones, biggest)

        count += 1
        heapq.heapify(stones)

    while stones[1] > 0 and stones[2] > 0:
        stones[1] -= 1
        stones[2] -= 1
        count += 1

    return count

# B. Nikita Books  (Codeforces 2244B)
# https://codeforces.com/contest/2244/problem/B
"""
Books move only left -> right, so prefix sums never increase. To end with a strictly
increasing array of positive integers, every prefix must already hold enough books
to cover the minimum increasing target 1, 1+2, 1+2+3, ... — i.e. the triangular
number T(k) = k(k+1)/2. So each prefix sum must be >= T(prefix length).

Using 2*sum >= (i+1)*(i+2) (0-indexed i) keeps it integer — avoids float division.
See notes/theory/algorithmic_concepts.md (6. Gauss's sum / triangular numbers).
"""


def solve(stacks):
    sum_prefix = 0
    for i, x in enumerate(stacks):
        sum_prefix += x
        if 2 * sum_prefix < (i + 1) * (i + 2):
            return "NO"
    return "YES"


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        stacks = list(map(int, input().split()))
        print(solve(stacks))

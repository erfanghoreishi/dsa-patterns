# A. Iskander and Drawings  (Codeforces 2244A)
# https://codeforces.com/contest/2244/problem/A
import math


def solve(line):
    # answer = ceil(longest run of '#' / 2)
    n = len(line)
    maxlen = 0
    for left in range(n):
        right = left
        while right < n and line[right] == '#':
            right += 1
            maxlen = max(maxlen, right - left)
    return math.ceil(maxlen / 2)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        line = input()
        print(solve(line))

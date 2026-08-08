#120. Triangle
def minimumTotal(triangle):
    dp = [row[:] for row in triangle]      # copy so the input isn't mutated

    for row in range(1, len(dp)):
        for col in range(len(dp[row])):
            # a cell is reachable from the two cells above it: col and col-1.
            # inf marks an out-of-range parent (the two edges of the triangle).
            top = dp[row - 1][col] if col < len(dp[row - 1]) else float('inf')
            top_left = dp[row - 1][col - 1] if col - 1 >= 0 else float('inf')
            dp[row][col] += min(top, top_left)

    return min(dp[-1])                     # best path ends anywhere on the last row

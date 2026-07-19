#62. Unique Paths
def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    dp[m - 1][n - 1] = 1                     # one way to be at the destination

    # fill bottom-right -> top-left; each cell = paths going right + paths going down
    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if col + 1 < n:
                dp[row][col] += dp[row][col + 1]
            if row + 1 < m:
                dp[row][col] += dp[row + 1][col]

    return dp[0][0]

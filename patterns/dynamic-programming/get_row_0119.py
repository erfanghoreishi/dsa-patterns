#119. Pascal's Triangle II
def getRow(rowIndex):
    dp = []
    for i in range(rowIndex + 1):
        new = [1] * (i + 1)                 # ends are always 1
        for j in range(1, i):
            new[j] = dp[j - 1] + dp[j]       # each inner cell = sum of the two above
        dp = new

    return dp

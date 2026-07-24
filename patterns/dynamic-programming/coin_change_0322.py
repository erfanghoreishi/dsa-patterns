#322. Coin Change
# THOUGHTS: felt genius finding this one! Bottom-up DP over every amount:
#           dp[i] = fewest coins to make i, built from smaller amounts.
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)   # inf = "not reachable (yet)"
    dp[0] = 0                            # zero coins make amount 0

    for i in range(1, len(dp)):
        for coin in coins:
            if i - coin >= 0:            # this coin fits into amount i
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[amount] if dp[amount] != float('inf') else -1

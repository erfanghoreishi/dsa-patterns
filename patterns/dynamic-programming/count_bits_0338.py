#338. Counting Bits
def countBits(n):
    dp = [0] * (n + 1)
    left = 0                      # left = i - (largest power of 2 <= i)

    for i in range(1, n + 1):
        # i & (i-1) == 0  ->  i is a power of 2 (& binds tighter than ==, so the
        # parens aren't needed). At a new power of 2, the offset restarts at 0.
        if i & i - 1 == 0:
            left = 0
        dp[i] = dp[left] + 1      # one more set bit than the value 'left' back
        left += 1

    return dp

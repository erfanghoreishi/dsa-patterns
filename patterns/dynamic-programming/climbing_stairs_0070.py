#70. Climbing Stairs
"""
Two ways to think about it:
  a) treat the results as a sequence — each value is the sum of the previous two
  b) count the ways the recursion reaches the base case — the better framing,
     since it's a DP problem

            4
          /   \
        3       2
       / \     / \
      2   1   1   0
     / \
    1   0
"""


def climbStairs(n):
    memo = {}

    def dp(n):
        if n == 0 or n == 1:
            return 1
        if n in memo:               # reuse already-solved subproblems
            return memo[n]
        memo[n] = dp(n - 1) + dp(n - 2)
        return memo[n]

    return dp(n)

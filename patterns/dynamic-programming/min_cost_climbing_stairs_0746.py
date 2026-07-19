#746. Min Cost Climbing Stairs
def minCostClimbingStairs(cost):
    # min cost to *stand on* the step two back / one back
    two_back = cost[0]
    one_back = cost[1]
    for i in range(2, len(cost)):
        # cheapest way onto step i: pay cost[i], arrive from whichever prior step is cheaper
        two_back, one_back = one_back, cost[i] + min(two_back, one_back)

    # the top is one step past the last index — reachable from either of the last two
    return min(two_back, one_back)

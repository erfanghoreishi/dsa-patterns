#198. House Robber
def rob(nums):
    prev = 0            # best up to house i-2
    dp = nums[0]        # best up to house i-1

    for i in range(1, len(nums)):
        temp = dp
        dp = max(prev + nums[i], dp)   # rob i (prev + nums[i]) or skip it (dp)
        prev = temp

    return dp

def maxSubArray(nums):
    best=dp = nums[0]
    for i in range(1,len(nums)):
        dp = max(nums[i],dp+nums[i]) 
        best = max(dp,best)

    return best

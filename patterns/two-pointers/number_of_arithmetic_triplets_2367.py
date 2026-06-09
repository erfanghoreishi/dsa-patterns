def arithmeticTriplets(nums, diff):
    count = 0
    for i in range(len(nums)):
        j = i+1
        k = i+2
        while k < len(nums):
            d1 = nums[j]-nums[i]
            d2 = nums[k]-nums[j]

            if d1 == diff and d2 == diff:
                count += 1
                break
            elif d1 < diff:
                j += 1
                k = j+1
            elif d2 < diff:
                k += 1
            else:
                break
    return count

#2164. Sort Even and Odd Indices Independently
# THOUGHTS: good slicing tutorial.
def sortEvenOdd(nums):
    evens = sorted(nums[0::2])
    odds = sorted(nums[1::2], reverse=True)

    nums[0::2] = evens
    nums[1::2] = odds

    return nums


"""
Without slicing — gather by stepped index, sort, then write back:

    evens = sorted(nums[i] for i in range(0, len(nums), 2))
    odds  = sorted((nums[i] for i in range(1, len(nums), 2)), reverse=True)

    for k, i in enumerate(range(0, len(nums), 2)):
        nums[i] = evens[k]
    for k, i in enumerate(range(1, len(nums), 2)):
        nums[i] = odds[k]

    return nums
"""

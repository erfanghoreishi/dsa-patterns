#704. Binary Search
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:                  # <= so a 1-element range is still checked
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1            # target is in the left half
        else:
            l = mid + 1            # target is in the right half

    return -1

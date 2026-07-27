#496. Next Greater Element I
def nextGreaterElement(nums1, nums2):
    # O(n1 * n2): for each query value, scan nums2 to its right for the first bigger.
    # See notes/redo.md — the O(n1 + n2) way uses a monotonic stack over nums2.
    result = []
    nums2_set = {num: i for i, num in enumerate(nums2)}   # value -> its index in nums2

    for n1 in nums1:
        greater = -1
        for j in range(nums2_set[n1] + 1, len(nums2)):
            if nums2[j] > n1:
                greater = nums2[j]
                break
        result.append(greater)

    return result

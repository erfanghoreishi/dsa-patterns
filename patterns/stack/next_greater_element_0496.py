#496. Next Greater Element I
def nextGreaterElement(nums1, nums2):
    """
    O(n1 + n2) with a monotonic (decreasing) stack over nums2. If the current
    number is greater than the stack top, it IS that top's next-greater element —
    pop and record it; otherwise push and move on. Each value is pushed/popped once.
    See notes/theory/algorithmic_concepts.md (9. Monotonic stack).
    """
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:      # num resolves everything smaller on top
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]


# Earlier O(n1 * n2) version — for each n1, scan nums2 to its right for the first
# bigger value. Kept for reference:
# def nextGreaterElement(nums1, nums2):
#     idx = {num: i for i, num in enumerate(nums2)}
#     result = []
#     for n1 in nums1:
#         greater = -1
#         for j in range(idx[n1] + 1, len(nums2)):
#             if nums2[j] > n1:
#                 greater = nums2[j]
#                 break
#         result.append(greater)
#     return result

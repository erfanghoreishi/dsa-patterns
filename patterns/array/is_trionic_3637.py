#3637. Trionic Array I
def isTrionic(nums):
    p = 0
    while p + 1 < len(nums) and nums[p + 1] > nums[p]:   # 1st run: strictly up
        p += 1
    q = p
    while q + 1 < len(nums) and nums[q + 1] < nums[q]:   # 2nd run: strictly down
        q += 1
    s = q
    while s + 1 < len(nums) and nums[s + 1] > nums[s]:   # 3rd run: strictly up
        s += 1

    # valid iff all three runs are non-empty and together cover the whole array:
    # p > 0 (up exists), q > p (down exists), s > q (up exists), s == last index
    return s == len(nums) - 1 and p > 0 and q < s and q > p

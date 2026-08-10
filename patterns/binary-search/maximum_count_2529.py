#2529. Maximum Count of Positive Integer and Negative Integer
def maximumCount(nums):
    def first_index_geq(target):
        """Leftmost index whose value is >= target (i.e. bisect_left)."""
        # half-open range [l, r) with r = len(nums), and `l < r` — NOT the
        # `l <= r` / `r = len-1` form used for exact search (see search_0704.py).
        # This variant never needs a "found" check: it converges on an insertion point.
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid            # mid might be the answer — keep it in range
            else:
                l = mid + 1        # mid is too small — discard it
        return l

    neg_count = first_index_geq(0)                  # everything before the first >= 0
    pos_count = len(nums) - first_index_geq(1)      # everything from the first >= 1 on
    return max(neg_count, pos_count)

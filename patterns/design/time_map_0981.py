#981. Time Based Key-Value Store
"""
`get` is a predecessor search: the rightmost value with timestamp <= target
(same as `bisect_right(timestamps, target) - 1`). The trick is carrying a
candidate — every time we move right, the value we leave behind is the best
answer so far, so `result` holds it when the loop ends. The '' sentinel
doubles as the "nothing at or before this timestamp" answer, so no found-check
is needed. See concept 11 in notes/theory/algorithmic_concepts.md.
"""


class TimeMap:
    def __init__(self):
        self.db = {}  # key -> list of [value, timestamp], timestamps strictly increasing

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
        self.db[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ''
        arr = self.db[key]
        result = ''
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                result = arr[mid][0]   # candidate: keep the best <= timestamp so far
                l = mid + 1
            else:
                r = mid - 1
        return result

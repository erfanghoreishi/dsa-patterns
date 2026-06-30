#539. Minimum Time Difference
# Circular time difference — see notes/theory/algorithmic_concepts.md (5.)
def findMinDifference(timePoints):
    minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
    minutes.sort()

    ans = min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))

    # circular wrap: from the last time forward past midnight to the first.
    # After sorting, only this last/first pair can beat the adjacent gaps.
    return min(ans, 24 * 60 - minutes[-1] + minutes[0])

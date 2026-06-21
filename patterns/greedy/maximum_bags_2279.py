#2279. Maximum Bags With Full Capacity of Rocks
# THOUGHTS: it's a good idea to use generic names on leetcode, e.g. needed, ans, left.
def maximumBags(capacity, rocks, additionalRocks):
    needed = [capacity[i] - rocks[i] for i in range(len(capacity))]
    needed.sort()
    for i in range(len(capacity)):
        if needed[i] <= additionalRocks:
            additionalRocks -= needed[i]
            needed[i] = 0

    return needed.count(0)

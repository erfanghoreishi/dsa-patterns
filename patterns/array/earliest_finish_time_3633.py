#3633. Earliest Finish Time for Land and Water Rides I
def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
    # You do exactly one land ride and one water ride, in either order. The second
    # ride can't start before its own start time OR before the first ride finishes,
    # so it finishes at max(first_end, second_start) + second_duration.
    n, m = len(landStartTime), len(waterStartTime)
    best = float('inf')

    # order 1: land first, then water
    for i in range(n):
        land_end = landStartTime[i] + landDuration[i]
        for j in range(m):
            best = min(best, max(land_end, waterStartTime[j]) + waterDuration[j])

    # order 2: water first, then land
    for i in range(m):
        water_end = waterStartTime[i] + waterDuration[i]
        for j in range(n):
            best = min(best, max(water_end, landStartTime[j]) + landDuration[j])

    return best

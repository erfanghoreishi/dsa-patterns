#1200. Minimum Absolute Difference
def minimumAbsDifference(arr):
    arr = sorted(arr)              # the min gap is always between adjacent sorted values

    minimum = float('inf')
    for i in range(1, len(arr)):
        minimum = min(minimum, arr[i] - arr[i - 1])

    # second pass: collect every adjacent pair whose gap equals that minimum
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == minimum:
            result.append([arr[i - 1], arr[i]])
    return result

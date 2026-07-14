#2951. Find the Peaks
def findPeaks(mountain):
    result = []
    # endpoints can't be peaks (they lack a neighbor on one side)
    for i in range(1, len(mountain) - 1):
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
            result.append(i)
    return result

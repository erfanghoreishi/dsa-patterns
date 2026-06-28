#1338. Reduce Array Size to The Half
from collections import Counter


def minSetSize(arr):
    # sorted(counter) would sort the KEYS (useless here); use .items() to get
    # (value, count) pairs and sort by count — most frequent first.
    counts = sorted(Counter(arr).items(), key=lambda item: item[1], reverse=True)

    removed = 0
    new_size = 0
    for value, count in counts:
        new_size += count
        removed += 1
        # new_size * 2 >= len(arr) keeps it integer math — avoids the float that
        # len(arr) / 2 produces when the array size is odd.
        if new_size * 2 >= len(arr):
            return removed

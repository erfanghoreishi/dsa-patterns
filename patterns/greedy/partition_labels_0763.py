#763. Partition Labels
# Furthest-reach greedy — see notes/theory/algorithmic_concepts.md (3.)
def partitionLabels(s):
    last = {}
    for i, c in enumerate(s):
        last[c] = i

    result = []
    start = 0
    end = 0

    for i, c in enumerate(s):
        end = max(end, last[c])      # furthest reach of anything seen so far
        if end == i:                 # group closed: nothing extends past here
            result.append(i - start + 1)
            start = i + 1

    return result

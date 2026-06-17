#1436. Destination City
def destCity(paths):
    starts = [x[0] for x in paths]

    for p in paths:
        # the destination city is the one that never appears as a starting point
        if p[1] not in starts:
            return p[1]

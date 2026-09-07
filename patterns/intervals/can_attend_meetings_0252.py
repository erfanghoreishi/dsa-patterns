#252. Meeting Rooms
def canAttendMeetings(intervals):
    # tuples sort lexicographically, so plain sorted() already orders by start
    # (then end) — no key needed
    ints = sorted(intervals)
    for i in range(1, len(ints)):
        # strict <: touching meetings (0,8),(8,10) are not a conflict
        if ints[i][0] < ints[i - 1][1]:
            return False

    return True

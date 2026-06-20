#3668. Restore Finishing Order
def recoverOrder(order, friends):
    friend_set = set(friends)
    # walk the finishing order, keep only friends — order is preserved for free
    # (one-liner: return [o for o in order if o in friend_set])
    result = []
    for o in order:
        if o in friend_set:
            result.append(o)
    return result

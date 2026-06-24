#2225. Find Players With Zero or One Losses
from collections import Counter


def findWinners(matches):
    winners, losers = zip(*matches)

    """
    Counter(losers) is shorthand for the manual tally below:
        loss_count = {}
        for loser in losers:
            loss_count[loser] = loss_count.get(loser, 0) + 1
        one_loss = [p for p, losses in loss_count.items() if losses == 1]
    """
    loss_count = Counter(losers)

    no_loss = set(winners) - set(losers)                      # won, never lost
    one_loss = [p for p, losses in loss_count.items() if losses == 1]

    return [sorted(no_loss), sorted(one_loss)]

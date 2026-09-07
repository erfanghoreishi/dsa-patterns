#355. Design Twitter
"""
Each tweet is stored with a global increasing counter, so ordering across users
is decided by that counter, not by any per-user index. `getNewsFeed` gathers all
tweets of the followees plus the user's own, sorts by the counter descending and
keeps the first 10.

Next level: instead of collecting and sorting everything, do a k-way merge with a
max-heap over the tail of each followee's list — only the 10 newest tweets are
ever popped.
"""

from typing import List


class Twitter:
    def __init__(self):
        self.followings = {}   # userId -> set of followeeIds
        self.posts = {}        # userId -> list of (tweetId, global counter)
        self.tweet_inc = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []

        self.posts[userId].append((tweetId, self.tweet_inc))
        self.tweet_inc += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        for following in self.followings.get(userId, set()) | {userId}:
            if following in self.posts:
                feed.extend(self.posts[following])

        feed = sorted(feed, key=lambda post: post[1], reverse=True)
        tweetIds = [tid for tid, inc in feed]
        return tweetIds[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.followings:
            self.followings[followerId] = set()

        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followings:
            return

        self.followings[followerId].discard(followeeId)

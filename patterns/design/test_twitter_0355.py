# test_twitter_0355.py
from twitter_0355 import Twitter


def test_leetcode_example():
    tw = Twitter()
    tw.postTweet(1, 5)
    assert tw.getNewsFeed(1) == [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    assert tw.getNewsFeed(1) == [6, 5]      # newest first, across both users
    tw.unfollow(1, 2)
    assert tw.getNewsFeed(1) == [5]


def test_empty_feed():
    tw = Twitter()
    assert tw.getNewsFeed(1) == []


def test_own_tweets_without_self_follow():
    tw = Twitter()
    tw.postTweet(1, 10)
    tw.postTweet(1, 11)
    assert tw.getNewsFeed(1) == [11, 10]    # user always sees their own tweets


def test_feed_capped_at_ten():
    tw = Twitter()
    for tid in range(1, 16):
        tw.postTweet(1, tid)
    assert tw.getNewsFeed(1) == list(range(15, 5, -1))


def test_interleaved_users_order_by_global_counter():
    tw = Twitter()
    tw.follow(1, 2)
    tw.follow(1, 3)
    tw.postTweet(2, 20)
    tw.postTweet(1, 10)
    tw.postTweet(3, 30)
    tw.postTweet(2, 21)
    assert tw.getNewsFeed(1) == [21, 30, 10, 20]


def test_self_follow_is_ignored():
    tw = Twitter()
    tw.follow(1, 1)
    tw.postTweet(1, 7)
    assert tw.getNewsFeed(1) == [7]         # not duplicated


def test_unfollow_unknown_is_noop():
    tw = Twitter()
    tw.unfollow(1, 2)                       # follower never followed anyone
    tw.follow(1, 2)
    tw.unfollow(1, 3)                       # followee was never followed
    tw.postTweet(2, 8)
    assert tw.getNewsFeed(1) == [8]


def test_follower_does_not_see_own_feed_in_followee():
    tw = Twitter()
    tw.follow(1, 2)
    tw.postTweet(1, 1)
    tw.postTweet(2, 2)
    assert tw.getNewsFeed(2) == [2]         # following is one-directional

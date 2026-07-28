from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time: int = 0
        self.tweets: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.follows: Dict[int, Set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        visible_users: List[int] | int = self.follows[userId] | {userId}
        visible_tweets: List[Tuple[int, int]] = []
        for visible_user in visible_users:
            visible_tweets.extend(self.tweets[visible_user][-10:])
        visible_tweets.sort(reverse=True)
        return [
            tweet_id
            for _, tweet_id in visible_tweets[:10]
        ]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        # 1. find all users
        users = {userId} | self.follows[userId]

        # 2. get tweets from those user
        all_tweets = []

        for user in users:
            all_tweets += self.tweets[user]

        # 3. sort by time, newest first
        all_tweets.sort(key=lambda x: x[0], reverse=True)

        # 4. return only tweets ids and max of 10
        return [tweetId for time, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

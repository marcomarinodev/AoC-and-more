from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.users_posts = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.users_posts[userId].append((-self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = [] 
        
        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.users_posts:
                last_tweet_index = len(self.users_posts[followeeId]) - 1
                count, tweetId = self.users_posts[followeeId][last_tweet_index]
                
                # using followeeId because once I pop this tweet, I should
                # take tha last one produced by followeeId
                minHeap.append([count, tweetId, followeeId, last_tweet_index - 1])
        
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, last_tweet_index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if last_tweet_index >= 0:
                count, tweetId = self.users_posts[followeeId][last_tweet_index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, last_tweet_index - 1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(7,23)
obj.postTweet(7,24)
obj.postTweet(7,25)
obj.postTweet(7,26)
obj.follow(8,7)
print(obj.getNewsFeed(8))
obj.follow(8,7)
print(obj.getNewsFeed(8))
obj.postTweet(7,27)
obj.unfollow(8,7)
print(obj.getNewsFeed(8))

print("-------------")

obj2 = Twitter()
obj2.postTweet(1,4)
obj2.postTweet(2,5)
obj2.unfollow(1,2)
print(obj2.getNewsFeed(1))
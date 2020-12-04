"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. 

Your design should support the following methods:

    postTweet(userId, tweetId): Compose a new tweet.

    getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users who the user followed or by the 
        user herself. Tweets must be ordered from most recent to least recent.

    follow(followerId, followeeId): Follower follows a followee.

    unfollow(followerId, followeeId): Follower unfollows a followee.



Example:
=======
Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""
import pytest
from typing import Dict, List, Union

"""
users = {
    1 : {
        following: []
    }
},
tweets = [
    1 : {
        tweet_ids: []
    }
]

        """
class Twitter:

    def __init__(self):


        self._users = {}
        self._tweets = {}
        self._all_tweets = set()

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, new: List[dict]):
        self.users = new

    @property
    def all_users(self):
        return self._users.keys()


    @property
    def tweets(self):
        return self._tweets
    
    @property
    def all_tweets(self):
        return self._all_tweets
        

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        
        if tweet_id in self.all_tweets:
            tweet_id = max(self.all_tweets) + 1
            self.all_tweets.add(tweet_id)
        else:
            self.all_tweets.add(tweet_id)
            
        if user_id not in self.all_users:
            new_tweet = {"tweet_ids": []}
            new_entry = {"following": []}
            self.users[user_id] = new_entry
            self.tweets[user_id] = new_tweet

        self.tweets[user_id]["tweet_ids"].append(tweet_id)


    def get_news_feed(self, user_id: int) -> List[Dict[int, Dict[str, Union[str, int]]]]:
        
        entire_news_feed = [tweet for tweet in self.tweets[user_id]["tweet_ids"]]

        for followee in self.users[user_id]["following"]:
            if followee in self.tweets.keys():
                for tweet in self.tweets[followee]["tweet_ids"]:
                    entire_news_feed.append(tweet)
                    
        entire_news_feed = sorted(entire_news_feed, reverse = True)[0:10]
       
        return entire_news_feed


    def follow(self, user_id: int, followee_id: int) -> None:

        if user_id not in self.all_users:
            new_entry = {"following": []}
            self.users[user_id] = new_entry


        self.users[user_id]["following"].append(followee_id)

    def unfollow(self, user_id: int, followee_id: int) -> None:
        
        try:
            self.users[user_id]["following"].remove(followee_id)
        except KeyError:
            pass

        

    
    
########################################

class NicksTester:
    
    tests_passed = 0
    
    def __init__(self, obj):
        
        self.obj = obj
        
    @property    
    def expected(self):
        
        return self._expected
    
    @expected.setter
    def expected(self, new):
        
        self._expected = new
        
        
    def eval(self, func, *args):
        
        return self.obj.func(*args)
    
    



def test_twitter_class_get_news_fed():
    
    twitter = Twitter()
    
    twitter.post_tweet(1, 5)
    twitter.post_tweet(1, 11)

    twitter.follow(1, 2)
    twitter.follow(1, 3)
    
    
    twitter.post_tweet(2, 4)
    twitter.post_tweet(2, 6)
    
    twitter.post_tweet(3, 2)
    twitter.post_tweet(3, 6)
    
    
    tester = NicksTester(twitter)
    tester.expected = [12, 11, 6, 5, 4, 2]
    
    
    expected = tester.expected
    actual = twitter.get_news_feed(1)
    
    assert actual == expected


def test_twitter_class_follow():
    
    twitter = Twitter()
    
    twitter.post_tweet(1, 5)
    twitter.post_tweet(1, 11)

    twitter.follow(1, 2)
    twitter.follow(1, 3)
    
    
    twitter.post_tweet(2, 4)
    twitter.post_tweet(2, 6)
    
    twitter.post_tweet(3, 2)
    twitter.post_tweet(3, 6)
    
    
    tester = NicksTester(twitter)
    tester.expected = [2, 3]
    
    expected = tester.expected
    actual = twitter.users[1]["following"]
    
    assert actual == expected




if __name__ == "__main__":
    
    
    pytest.main()
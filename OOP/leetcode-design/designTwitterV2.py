"""
Twitter.py
+++++++++

Design and implement a simplified version of twitter.

classes
-------

    1) User:
        properties:
            instance:
                str name
                int id
                str email
                list following (other user ids)
                list followers (other user ids)
                
        methods:
            __ repr__() -> f"User {self.id}"
            
            
    2) Tweet:
        properties:
            instance:
                int id
                int user_id
                str contents
                
        methods:
            __repr__() -> contents
            
            
            
    3) Twitter:
        properties:
            instance:
                defaultdict(list) all_tweets {user_id: [tweet_obj, tweet_obj]}
                
                
        methods:
            instance:
                void post_tweet(User user, Tweet tweet) -> append tweet to all_tweets[user_id]
                List[int] get_news_feed(User user)
                void follow(User user1, User user2)
                void unfollow(User user1, User user2)
"""
import pytest
from typing import List
from collections import defaultdict

array = List[int]

class User:
    """

    1) User:
        properties:
            instance:
                str name
                int id
                str email
                list following (other user ids)
                list followers (other user ids)
                
        methods:
            __ repr__() -> f"User {self.id}"
    """
    
    def __init__(self, name: str, id_: int, email: str):
        
        self.name = name
        self.id = id_
        self.email = email
        
        self.following = []
        self.followers = []
        
    def __repr__(self):
        return f"User {self.id}"
      
        
        
class Tweet:
    """
    2) Tweet:
        properties:
            instance:
                int id
                int user_id
                str contents
                
        methods:
            __repr__() -> contents
    """
    
    def __init__(self, id_: int, user_id: int, contents: str):
        
        self.id = id_
        self.user_id = user_id
        self.contents = contents
        
    def __repr__(self):
        return f"{self.id}: {self.contents}"
        
        
        
class Twitter:
    """
    3) Twitter:
        properties:
            instance:
                defaultdict(list) all_tweets {user_id: [tweet_obj, tweet_obj]}
                
                
        methods:
            instance:
                void post_tweet(User user, Tweet tweet) -> append tweet to all_tweets[user_id]
                List[int] get_news_feed(User user)
                void follow(User user1, User user2)
                void unfollow(User user1, User user2)
    """
    
    def __init__(self):
        
        self.all_tweets = defaultdict(list)
        
        
    def post_tweet(self, user: User, tweet: Tweet) -> None:
        
        self.all_tweets[user.id].append(tweet.id)
        
    
    def get_news_feed(self, user: User) -> array:
        
        news_feed = []
        
        for user_id in self.all_tweets:
            if (user_id in user.following) or (user_id == user.id):
                for tweet_id in self.all_tweets[user_id]:
                    news_feed.append(tweet_id)
                    
        return sorted(news_feed, reverse=True)[:10]
        
    
    @staticmethod
    def follow(user1: User, user2: User) -> None:
        
        user1.following.append(user2.id)
        user2.followers.append(user1.id)
        
    @staticmethod
    def unfollow(user1: User, user2: User) -> None:
        
        user1.following.remove(user2.id)
        user2.followers.remove(user1.id)
        
        
        
        
###################################
def test_add_followers():
    
    user1 = User("Nick", 1, "nicholashopewell@gmail.com")
    
    user2 = User("Joe", 2, "joe@gmail.com")
    user3 = User("Dan", 3, "dan@gmail.com")
    
    twitter = Twitter()
    
    twitter.follow(user1, user2)
    twitter.follow(user1, user3)
    
    expected = [2, 3]
    actual = user1.following
    
    assert actual == expected
    
    
def test_add_get_news_fed():
    
    user1 = User("Nick", 1, "nicholashopewell@gmail.com")
    user2 = User("Joe", 2, "joe@gmail.com")
    user3 = User("Dan", 3, "dan@gmail.com")
    
    twitter = Twitter()
    
    twitter.follow(user1, user2)
    twitter.follow(user1, user3)
    
    tweet1 = Tweet(1, 1, ['dsddssd'])
    tweet2 = Tweet(2, 1, ['dsddssd'])
    tweet3 = Tweet(3, 1,  ['dsddssd'])
    twitter.post_tweet(user1, tweet1)
    twitter.post_tweet(user1, tweet2)
    twitter.post_tweet(user1, tweet3)
    
    tweet4 = Tweet(4, 2, ['dsddssd'])
    tweet5 = Tweet(5, 2, ['dsddssd'])
    tweet6 = Tweet(6, 2, ['dsddssd'])
    tweet7 = Tweet(7, 2, ['dsddssd'])
    twitter.post_tweet(user2, tweet4)
    twitter.post_tweet(user2, tweet5)
    twitter.post_tweet(user2, tweet6)
    twitter.post_tweet(user2, tweet7)
    
    tweet8 = Tweet(8, 3, ['dsddssd'])
    tweet9 = Tweet(9, 3, ['dsddssd'])
    tweet10 = Tweet(10, 3, ['dsddssd'])
    tweet11 = Tweet(11, 3, ['dsddssd'])
    twitter.post_tweet(user3, tweet8)
    twitter.post_tweet(user3, tweet9)
    twitter.post_tweet(user3, tweet10)
    twitter.post_tweet(user3, tweet11)
    
    print(twitter.all_tweets)
    
    expected = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    actual = twitter.get_news_feed(user1)
    

    
    assert actual == expected
    
    
    
    
if __name__ == "__main__":
    pytest.main()
    
import tweepy
import time

API_Key ="#"
API_Key_Secret = "#"
bearer_token = "#"
A_Token = "#"
A_Token_Secret = "#"

client = tweepy.Client(bearer_token, API_Key, API_Key_Secret, A_Token, A_Token_Secret)
auth = tweepy.OAuth1UserHandler(API_Key, API_Key_Secret, A_Token, A_Token_Secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

        try:
            client.retweet(tweet.id)

        except Exception as error: 
            print(error)  

stream = MyStream(bearer_token = bearer_token)        

rule = tweepy.StreamRule("(Github)(-is:retweet -is:reply)")

stream.add_rules(rule)
stream.filter()
import tweepy

API_Key ="#"
API_Key_Secret = "#"
bearer_token = "#"
A_Token = "#"
A_Token_Secret = "#"

client = tweepy.Client(bearer_token, API_Key, API_Key_Secret, A_Token, A_Token_Secret)
auth = tweepy.OAuth1UserHandler(API_Key, API_Key_Secret, A_Token, A_Token_Secret)
api = tweepy.API(auth)

#client.create_tweet(text = "Hello Welcome to bot service")
#client.like("1615293691329122304")
#client.retweet("1615293691329122304")
#client.create_tweet(in_reply_to_tweet_id="1615293691329122304", text = "Hello")
#for tweet in api.home_timeline():
#    print(tweet.text)
person = client.get_user(username = "GVNAkshayVarma1").data.id

for tweet in client.get_users_tweets(person).data:
    print(tweet.text)
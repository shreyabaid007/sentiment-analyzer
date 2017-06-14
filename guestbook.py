
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = XXX
consumer_secret = XXX
access_token = XXX
access_token_secret = XXX
         
auth = OAuthHandler(consumer_key, consumer_secret)
            
auth.set_access_token(access_token, access_token_secret)
            
api = tweepy.API(auth)

public_tweets =api.search('trump')

for tweet in public_tweets[:10]:
	#print tweet.text
	analysis= TextBlob(tweet.text)
	print analysis.sentiment
	


import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = 'ZVhFWqmSGBeQYIdLbYNNou0NF'
consumer_secret = '0VEznDZ5FjBIJxw4zYftsYzclDGrzmnAr6r6oL3VcSmVAqx4tm'
access_token = '841360189450153984-Lwqr3ATaPiBGzgkwKXhktOE5qX4P5OA'
access_token_secret = 'RtfUmEXTrXC55UldqHuW2i4e66ScgfBAV7vrbZyz5QLBu'
         
auth = OAuthHandler(consumer_key, consumer_secret)
            
auth.set_access_token(access_token, access_token_secret)
            
api = tweepy.API(auth)

public_tweets =api.search('trump')

for tweet in public_tweets[:10]:
	#print tweet.text
	analysis= TextBlob(tweet.text)
	print analysis.sentiment
	
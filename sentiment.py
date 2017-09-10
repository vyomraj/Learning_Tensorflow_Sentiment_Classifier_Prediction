import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'jHkskfdvlUh8fGdPPUs1gW15q'
consumer_secret= '8ZiMHZs6mCXNQy49JIRV6bEc6SPN7HwDIRUglFHVcG4oUDMOCQ'


access_token='904178127756079104-tk18oBFFqcZmdt0EXkyVzDZp9LBF1DK'
access_token_secret='crMbE6HPUQWGG3owD0Z8q4ZOUE8LdVnkwEaphHAzJKn7B'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('India')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

import tweepy
import csv


# Step 1 - Authenticate
consumer_key= 'insertyourcode'
consumer_secret= 'insertyourcode'

access_token='insertyourcode'
access_token_secret='insertyourcode'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

csvFile = open('insertyourfile.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

#Step 2 - Retrieve Tweets
public_tweets = api.search(q=['InsertYourHashtag'], count=100)

for tweet in public_tweets:
    print(tweet.text)
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

    print("Scraping finished and saved to " +  "Insertyourfile.csv")
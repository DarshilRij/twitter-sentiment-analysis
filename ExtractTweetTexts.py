from tweepy import *
import tweepy as tweepy

import csv
import re
import string
import json

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_key = "access_key"
access_secret = "access_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

jsonfile500 = open('Tweet 500.json', 'w')

search_words = "covid OR emergency OR immune OR vaccine OR flu OR snow"

allJSONData = []
index = 0

jsonfile = None
tweetJson500 = {"data": []}

regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


for tweet in tweepy.Cursor(api.search, q=search_words, count=500,
                           lang="en",
                           since_id=0).items():
    index = index+1

    print(index)

    test = tweet._json["text"]

    test = re.sub(regex, " ", test)
    test = remove_emoji(test)
    test = re.sub('[^A-Za-z0-9]+', ' ', test)

    tweetJson500["data"].append(test)

    if index == 500:
        jsonfile500.write(json.dumps(tweetJson500))
    print("\n")

    if index == 500:
        break

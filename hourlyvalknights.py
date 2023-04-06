import tweepy
import schedule
import time
import random
import json
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# populate json file with the tweets 
with open('content.json', 'r') as f:
    info = json.load(f)

for item in info:
    print(item)

def hourly_post():
    randomChoice = random.randrange(len(info))
    api.update_with_media(info[randomChoice]['image'], status=info[randomChoice]['text'])

schedule.every(60).minutes.do(hourly_post)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

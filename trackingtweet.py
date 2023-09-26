from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

import datetime

MONGO_HOST = 'mongodb://localhost:27017'

keywords = ['#BigData']

CONSUMER_KEY = "VcOUYlJqOhAAKYAtm2L94rWEo"
CONSUMER_SECRET = "pWJRVj7dQRLILFX2HgYvVQgGSQwsmMD9dQ4ZkYyNQEKbDirvGt"
ACCESS_TOKEN = "1270862959527378944-rGK1fv3Q49LTSCdwRmiJ4zYKlStYlH"
ACCESS_TOKEN_SECRET = "qtuZPYfHAM2OBTZJjxrOWXW8DMaU2xTJHnGJGw14AzG8D"

class StreamListener(tweepy.StreamListener):

        def on_connect(self):
                print("You are now connected to the streaming API.")

        def on_error(self, status_code):
                print('An Error has occured: '+ repr(status_code))
                return False

        def on_data(self, data):
                try:
                        client = MongoClient(MONGO_HOST)

                        db = client.twitterdb

                        datajson = json.loads(data)
                        tweet_id = datajson['id_str']
                        username = datajson['user']['screen_name']
                        followers = datajson['user']['followers_count']
                        text = datajson['text']
                        hashtags = datajson['entities']['hashtags']
                        dt = datajson['created_at']
                        language = datajson['lang']
                        created_at = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')
                        tweet = [{'id':tweet_id,'username':username,'followers':followers,'text':text,'hashtags':hashtags,'language':language,'created':created_at}]

                        print("Tweet collected at " + str(created_at))

                        db.twitter.insert_many(tweet)
                except Exception as e:
                        print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking:" + str(keywords))
streamer.filter(track=keywords)

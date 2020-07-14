# A simple crawler which stores to a mongoDB
import sys, json, config
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
from elasticsearch import helpers
from elasticsearch import Elasticsearch
import re
from copy import deepcopy
import smtplib

# Put your filter here
LANGUAGES = ['en']
WANTED_KEYS = ['id_str',
               'text',
               'created_at',
               'in_reply_to_status_id_str',
               'in_reply_to_user_id_str',
               'retweeted',
               'entities']

# Wanted keys to store in the database (refer to config file for subwords)
KEYWORDS = config.KEYWORDS['joy'] + \
           config.KEYWORDS['trust'] + \
           config.KEYWORDS['fear'] + \
           config.KEYWORDS['surprise'] + \
           config.KEYWORDS['sadness'] + \
           config.KEYWORDS['disgust'] + \
           config.KEYWORDS['anger'] + \
           config.KEYWORDS['anticipation'] + \
           config.KEYWORDS['other']

print("Number of Keywords: ", len(KEYWORDS))

# Elastic search instance
es = Elasticsearch(config.ELASTICSEARCH['hostname'])

# Connection to Mongo Database
client = MongoClient(config.MONGODB['hostname'], config.MONGODB['port'])
db = client[config.MONGODB['db']]
collection = db[config.MONGODB['collection']]

def convert_to_es_format(tweet):
    """Convert into elastic format"""
    action = [
        {
            "_index": config.ELASTICSEARCH['index'],
            "_type": config.ELASTICSEARCH['type'],
            "_source": {
                "tweet": tweet
            }
        }
    ]
    return action

def post_tweet_to_es(doc):
    """insert into es"""
    helpers.bulk(es, doc)

def post_tweet_to_db(tweet):
    """post to database"""
    collection.insert(tweet)
    return True

def get_hashtags(list):
    """obtain hashtags from tweet"""
    hashtags = []
    for h in list:
        hashtags.append(h['text'])
    return hashtags

def format_to_print(tweet, hashtags):
    tweet_dict = {'text':tweet['text'],
            'created_at': tweet['created_at'],
            'tweet_id': tweet['id_str'],
            'hashtags': hashtags}
    return tweet_dict

# Stream Listener
class Listener(StreamListener):

    @staticmethod
    def on_data(data):
        try:
            reponse = json.loads(data)
            tweet = {key: reponse[key] for key in set(WANTED_KEYS) & set(reponse.keys())}

            # obtain all hashtags in tweet
            hashtags = get_hashtags(tweet['entities']['hashtags'])

            # ignore retweets (comment if you want to collect them)
            anyretweet= re.findall(r'RT|https|http', str(tweet['text']))

            # format tweet
            final_tweet = format_to_print(tweet, hashtags)

            # store tweet
            if not anyretweet:
                print(final_tweet)
                f = deepcopy(final_tweet)

                # store in MongoDB
                post_tweet_to_db(final_tweet)
                print("inserted into db ---------------- :)")

                # uncomment code below to store data in Elasticsearch
                #es_final_tweet = convert_to_es_format(f)
                #post_tweet_to_es(es_final_tweet)
                #print("inserted into es ---------------- :)")

        except Exception:
            print ("--------------On data function------------")
            return True

    @staticmethod
    def on_error(status):
        print ("--------------On error function------------")
        print (status)
        return True

    @staticmethod
    def on_timeout():
        print ("--------------On timeout function------------")
        print >> sys.stderr, 'Timeout...'
        return True  # Don't kill the stream

    @staticmethod
    def on_status(status):
        print ("--------------On status function------------")
        print (status.text)
        return True

# Start streaming
print("Start streaming...")

while True:
    try:
        auth = OAuthHandler(
            config.TWITTER['consumer_key'], config.TWITTER['consumer_secret'])
        auth.set_access_token(
            config.TWITTER['access_token'], config.TWITTER['access_secret'])
        twitterStream = Stream(auth, Listener())
        twitterStream.filter(languages=LANGUAGES, track=KEYWORDS)
    except KeyboardInterrupt:
        print ("--------------On keyboard interruption function------------")
        print("Bye")
        sys.exit()

import time
import urllib3
import certifi
import logging
from twython import TwythonStreamer
from twython import Twython
from subprocess import call
import random

logging.basicConfig(filename='test.log', level=logging.NOTSET)
logging.captureWarnings(True)

# Search terms
TERMS = '#SPyramide'

#habe mich schon mal als Developer angemeldet, mit folgenden Token
#Access Token 212884162-uaQigIHsBFbXWPBJCq8wKlriKfWMHmAlCTsIPPn7
#Access Token Secret bS4rWtYjYUU83JuV9dR58seQBokukEyWVwnMNhGGTRqsj
# Twitter application authentication
APP_KEY = 'qUKJnKZWfLexuJ3irZIU6QHQa'
APP_SECRET = 'bMW0uBcoUSWmzXMR0CCFIIBrS3dyUy7dzVkGUQjlGtkhIkfCdd'
OAUTH_TOKEN = '212884162-uaQigIHsBFbXWPBJCq8wKlriKfWMHmAlCTsIPPn7'
OAUTH_TOKEN_SECRET = 'bS4rWtYjYUU83JuV9dR58seQBokukEyWVwnMNhGGTRqsj'

tweets = []

cows = [ 'default',
         'vader',
         'meow',
         'turtle']

def cowsay(tweet):
        call(["/usr/games/cowsay","-f", random.choice(cows) , tweet])

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        tweet = data['text'].encode('utf-8')
                        #tweets.append(tweet)
                        cowsay(tweet)
                        

# Create streamer
try:
        cowsay("Tweeta na %s"%(TERMS))
        stream = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        #stream.statuses.filter(track=TERMS)
        tweets = stream.search(q=TERMS, count=5)
        for t in tweets['statuses'][::-1]:
                tweet = t['text'].encode('utf-8')
                cowsay(tweet)
                
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        pass

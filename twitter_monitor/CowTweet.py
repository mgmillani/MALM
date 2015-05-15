import time
from twython import TwythonStreamer
from subprocess import call

# Search terms
TERMS = '#SpyPi'

#habe mich schon mal als Developer angemeldet, mit folgenden Token
#Access Token 212884162-uaQigIHsBFbXWPBJCq8wKlriKfWMHmAlCTsIPPn7
#Access Token Secret bS4rWtYjYUU83JuV9dR58seQBokukEyWVwnMNhGGTRqsj
# Twitter application authentication
APP_KEY = 'qUKJnKZWfLexuJ3irZIU6QHQa'
APP_SECRET = 'bMW0uBcoUSWmzXMR0CCFIIBrS3dyUy7dzVkGUQjlGtkhIkfCdd'
OAUTH_TOKEN = '212884162-uaQigIHsBFbXWPBJCq8wKlriKfWMHmAlCTsIPPn7'
OAUTH_TOKEN_SECRET = 'bS4rWtYjYUU83JuV9dR58seQBokukEyWVwnMNhGGTRqsj'

tweets = []

def cowsay(tweet):
        call(["/usr/games/cowsay", tweet])

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        tweet = data['text'].encode('utf-8')
                        #tweets.append(tweet)
                        cowsay(tweet)
                        

# Create streamer
try:
        cowsay("Tweete na #SPyramide")
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        pass

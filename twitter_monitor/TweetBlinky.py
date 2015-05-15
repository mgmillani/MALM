import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms
TERMS = '#SpyPi'

# GPIO pin number of LED
LED = 22
#habe mich schon mal als Developer angemeldet, mit folgenden Token
#Access Token 212884162-uaQigIHsBFbXWPBJCq8wKlriKfWMHmAlCTsIPPn7
#Access Token Secret bS4rWtYjYUU83JuV9dR58seQBokukEyWVwnMNhGGTRqsj
# Twitter application authentication
APP_KEY = 'qUKJnKZWfLexuJ3irZIU6QHQa'
APP_SECRET = 'bMW0uBcoUSWmzXMR0CCFIIBrS3dyUy7dzVkGUQjlGtkhIkfCdd'
OAUTH_TOKEN = '212884162-uaQigIHsBFbXWPBJCq8wKlriKfWMHmAlCTsIPPn7'
OAUTH_TOKEN_SECRET = 'bS4rWtYjYUU83JuV9dR58seQBokukEyWVwnMNhGGTRqsj'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LED, GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(LED, GPIO.LOW)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

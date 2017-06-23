import tweepy
import Weather
import keys


class Bot(object):

    api = None
    tweet = None
    today = None

    def __init__(self):
        auth = tweepy.OAuthHandler(keys.Twitter.c_key, keys.Twitter.c_secret)
        auth.set_access_token(keys.Twitter.a_token, keys.Twitter.a_token_secret)
        self.api = tweepy.API(auth)
        self.today = Weather.Forecast()

    def create_tweet(self):
        self.tweet = str(self.today.date) + ": Temp High: " + str(self.today.high) + " Low: " + str(self.today.low) + " Humidity: " + \
                     str(self.today.humidity) + " Condition: " + self.today.conditions

    def post_tweet(self):
        print(self.tweet)
        self.api.update_status(status=str(self.tweet))


import os
import tweepy


class TwitterPublisher:
    def __init__(self):
        self.api = tweepy.API(self.get_authentication())

    @staticmethod
    def get_authentication():
        twitter_auth = tweepy.OAuthHandler(
            consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
            consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET')
        )

        twitter_auth.set_access_token(
            os.getenv('TWITTER_ACCESS_TOKEN_KEY'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )

        return twitter_auth

    def publish(self, tweet):
        self.api.update_status(tweet)

import dotenv
from TwitterPublisher import TwitterPublisher

dotenv.load_dotenv()

if __name__ == '__main__':
    tweet = input('Enter your tweet: ')

    twitter_publisher = TwitterPublisher()
    twitter_publisher.publish(tweet)

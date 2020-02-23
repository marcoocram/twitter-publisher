## Twitter publisher

My first python example project. Script to publish tweet on your twitter account.

#### Requirements

- Twitter account
- Docker

#### Instructions

- Create twitter credentials: https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials
- Set credentials on .env file (copy from .env.example)
- Build docker image: `docker image build -t twitter_publisher .`

#### Usage

- Using docker: `docker container run -it twitter_publisher`

#### Additional info

- If you don't want to put your credentials on .env file, you can pass it on docker run execution:

```
docker container run -e TWITTER_CONSUMER_KEY=xxxx -e TWITTER_CONSUMER_SECRET=xxxx -e TWITTER_ACCESS_TOKEN_KEY=xxxx -e TWITTER_ACCESS_TOKEN_SECRET=xxxx -it twitter_publisher
```
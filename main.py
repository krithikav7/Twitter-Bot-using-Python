import time
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_string = 'Sunsets scenery'  # keyword to search
numberOfTweets = 2  # number of tweets to like/favorite


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# to like the posts containing the keywords
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Liked a post!')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# following back bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Ashok Karthik':
        follower.follow()
        break

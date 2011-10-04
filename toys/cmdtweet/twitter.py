# Documentation: https://dev.twitter.com/docs/api/1/post/statuses/update
import tweepy

CONSUMER_KEY = '[TODO: Your consumer key]'
CONSUMER_SECRET = '[TODO: Your consumer secret]'

ACCESS_TOKEN_KEY = '[TODO: Your access token]'
ACCESS_TOKEN_SECRET = 'TODO: Your token secret'

def tweet(status):
  ''' Update the status message in twitter '''
  if len(status) > 140:
      raise Exception('status message is more than 140 chars: ' + len(status))
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  result = api.update_status(status)
  return result
tweet("Hello Twitter from python script!")
print "Hello tweet"


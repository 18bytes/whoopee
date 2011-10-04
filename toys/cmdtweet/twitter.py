# Documentation: https://dev.twitter.com/docs/api/1/post/statuses/update
# App creation: https://dev.twitter.com/apps
import tweepy
import sys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

def tweet(status):
  ''' Update the status message in twitter '''
  if len(status) > 140:
      raise Exception('status message is more than 140 chars: ' + len(status))
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  result = api.update_status(status)
  return result

if len(sys.argv) == 2:
  result = tweet(sys.argv[1])  
  print result
else:
  print "Invalid number of parameters!"

# Documentation: https://dev.twitter.com/docs/api/1/post/statuses/update
# App creation: https://dev.twitter.com/apps
import tweepy
import sys
import ConfigParser
import string

# Configuration is from the twitter.ini file to avoid commiting auth tokens
config = ConfigParser.ConfigParser()
config.read('twitter.ini')


CONSUMER_KEY = config.get('auth', 'consumer.key') 
CONSUMER_SECRET = config.get('auth', 'consumer.secret')

ACCESS_TOKEN_KEY = config.get('auth','access.token')
ACCESS_TOKEN_SECRET = config.get('auth', 'access.secret')

def tweet(status):
  ''' Update the status message in twitter '''
  if len(status) > 140:
      raise Exception('status message is more than 140 chars: ' + len(status))
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  result = api.update_status(status)
  return result

if len(sys.argv) > 1:
  params = sys.argv
  result = tweet(string.join(params[1:], " "))  
  print result
else:
  print "Invalid number of parameters!"

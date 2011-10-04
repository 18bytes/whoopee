#!/usr/bin/python
# Documentation: https://dev.twitter.com/docs/api/1/post/statuses/update
# App creation: https://dev.twitter.com/apps
# Reference: http://stackoverflow.com/questions/4473320/twitter-api-simple-status-update-python
import tweepy
import sys
import ConfigParser
import string
import os

# Configuration is from the twitter.ini file to avoid commiting auth tokens
iniPath = os.path.dirname(sys.argv[0]) + '/twitter.ini'
print iniPath
config = ConfigParser.ConfigParser()
config.read(iniPath)


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
  status = string.join(params[1:], " ")
  result = tweet(status)  
  if result is None:
    print "Error: Unable to update the twitter status."
  else:
    print "Status updated successfully: " + status
else:
  print "Invalid number of parameters!"

import tweepy
import urllib.request
import io
import os

from google.cloud import vision
from google.cloud.vision import types

def tweetCall(searchParam, tweetNum):

  consumer_key = ''
  consumer_secret = ''
  access_token = ''
  access_token_secret = ''

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
  auth.set_access_token(access_token, access_token_secret)   
  api = tweepy.API(auth)

  tweetList = api.search(searchParam, count=tweetNum)

  tweetInd = []

  for tweet in tweetList:
    try:
      if tweet.entities['media'][0]['type'] == 'photo':
        tweetInd.append(tweet.entities['media'][0]['media_url'])

        with open("feedList.txt", 'a+') as f:
          f.write(tweet._json['text'] + '\n\n')
    except BaseException:
      pass


'''    if 'text' in tweet._json:
      tweetInd.append(tweet._json['text'])

      with open("feedList.txt", 'a+') as f:
        f.write(tweet._json['text'] + '\n\n')'''

if __name__ == '__main__':
  tweetCall('dog', 50)
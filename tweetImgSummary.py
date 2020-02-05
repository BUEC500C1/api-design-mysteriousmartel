# Copyright 2020 by Jennifer Campbell

import tweepy
import urllib.request
import io
import os

from google.cloud import vision
from google.cloud.vision import types

''' This API is built to filter through N number of tweets
with a search parameter, pull out only tweets with images, then 
returns the strongest associated image label, as well as the
tweet associated with it'''

def tweetCall(searchParam, tweetNum):

  consumer_key = '***'
  consumer_secret = '***'
  access_token = '***'
  access_token_secret = '***'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
  auth.set_access_token(access_token, access_token_secret)   
  api = tweepy.API(auth)

  tweetList = api.search(searchParam, count=tweetNum)

  tweetUrlInd = []
  tweetTextInd = []

  tweetDic = {}

  for tweet in tweetList:
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
      try:
        if tweet.entities['media'][0]['type'] == 'photo':
          tweetUrlInd.append(tweet.entities['media'][0]['media_url'])
          tweetTextInd.append(tweet._json['text'])

          tweetDic[tweet._json['text']] = tweet.entities['media'][0]['media_url']

          with open("feedList.txt", 'a+') as f:
            f.write(tweet._json['text'] + '\n\n')
      except BaseException:
        pass

  for i in range(len(tweetUrlInd)):
    link = str(tweetUrlInd[i])
    imgIndex = "%04d" % i
    urllib.request.urlretrieve(link, f"jpg{imgIndex}.jpg")

  return tweetDic

def imgSentiment():

  imgName = list(os.popen('ls'))
  labelsList = []

  for img in imgName:

    if '.jpg' in img:
      images = img.strip()
      client = vision.ImageAnnotatorClient()

      fileName = os.path.join(os.path.dirname(__file__), images)

      with io.open(fileName, 'rb') as file:
        content = file.read()

      image = types.Image(content=content)

      response = client.label_detection(image=image)
      labels = response.label_annotations
      labelsList.append(labels[0].description)

  return labelsList

def tweetSummary(searchParam, tweetNum):
  textDict = tweetCall(searchParam, tweetNum)
  keys = list(textDict)
  imgLabel = imgSentiment()

  tweetSentInd = {}

  for i in range(len(keys)):
    tweetSentInd[keys[i]] = imgLabel[i]

  return tweetSentInd

if __name__ == '__main__':
  puppy = tweetSummary('puppy', 100)

  print(puppy)
  print(len(puppy))
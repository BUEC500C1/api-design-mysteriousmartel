﻿# Twitter Image Summary

This API takes in a search term and N number of tweets to filter through, then will pull any images from these tweets and analyze their highest sentiment.

## How it works

Download the "tweetImgSummary" API script. The API requires Twitter developer keys, which can be replaces directly in the script. To use the API, call function tweetSummary('search term',N), and the API will return a dictionary: keys are the original tweet, and values are the sentiment of the attached image.

## Testing

Since it was difficult to get the same sentiment for a search of N random tweets, the test only checks that there is at least one sentiment for each key in the dictionary. 

import tweetImgSummary

def test_tweetArrangement():
    puppy = tweetImgSummary.tweetSummary('puppy', 100)
    puppyKeys = list(puppy)
    labels = len(imgSentiment())

	assert len(puppy) == labels
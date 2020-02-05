import tweetImgSummary

def test_tweetArrangement():
    puppy = tweetImgSummary.tweetSummary('puppy', 100)
    puppyKeys = list(puppy)
    labels = len(tweetImgSummary.imgSentiment())
    assert len(puppy) == labels
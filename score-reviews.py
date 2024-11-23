import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the VADER Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

# Example review
review = """
Hey, don't go with high expectations, the movie is far away from epic, but it's pretty fine and funny, I enjoyed a lot of stuff, the characters are awesome! Even Steppenwolf isn't the lame they said, he is just not memorable, he's OK, a generic villain who delivers what everyone should expect (come on, it's Steppenwolf, why would you guys expect a mind blower villain here?) The plot is simple and works. The only fatal flaw for a huge fan of DC is the return of Superman, damn, that's was sooo weird :/ And Zimmer would be so much better than Danny was, buuut there's nothing we can do about it now, at least it's nostalgic.                     
"""
sentiment = analyze_sentiment(review)
print(sentiment)
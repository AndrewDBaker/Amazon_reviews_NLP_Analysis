# Andrew Baker
# Main python script
# Goal of the script is to write an NLP analysis of a 
# dataset found on kaggle.com

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
import re

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('vader_lexicon')

# importing csv
amazon_reviews = pd.read_csv('amazon_reviews.csv')
amazon_review_text_column = amazon_reviews['reviews.text'].tolist()

# initializing lists for later
review_sentiments = []
review_keywords = []


def analyze_sentiment(amazon_review_text_column):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(amazon_review_text_column)
    
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def extract_keywords(amazon_review_text_column):
    blob = TextBlob(amazon_review_text_column)
    nouns = [word for word, tag in blob.tags if tag == 'NN']
    return nouns

def main():
    for idx, review in enumerate(amazon_review_text_column, start=1):
        #print(f"Review {idx}: {amazon_review_text_column}")
        sentiment = analyze_sentiment(amazon_review_text_column)
        #print(f"Sentiment: {sentiment}")
        
        keywords = extract_keywords(amazon_review_text_column)
        #print(f"Keywords: {', '.join(keywords)}")
        
        #print("=" * 30)
        
        review_sentiments.append(sentiment)
        review_keywords.append(keywords)

if __name__ == "__main__":
    main()

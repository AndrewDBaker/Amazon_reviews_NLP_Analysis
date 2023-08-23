# Andrew Baker
# Main python script
# Goal of the script is to write an NLP analysis of a 
# dataset found on kaggle.com

import pandas as pd
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
import re

# Download necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('vader_lexicon')

 # Read the excel file
amazon_reviews = pd.read_csv('amazon_reviews.csv')

# Get the column you want
amazon_review_text_column = amazon_reviews['reviews.text']

# Print the column
print(column)

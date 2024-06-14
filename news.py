import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import lxml

# URL of the article
url = 'https://www.hindustantimes.com/business/is-america-s-economy-heading-for-a-consumer-crunch-101717878770660.html'


# nltk.download('punkt')
# Create an Article object
article = Article(url)

# Download the article
article.download()

# Parse the article
article.parse()

# Perform NLP on the article
article.nlp()


analysis = TextBlob(article.text)
print("tetx::", article.text)

print("sentiments::", analysis.polarity)

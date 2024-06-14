import streamlit as st
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import lxml



url = st.text_input("inter the URL here::")

article = Article(url)
article = Article(url)

# Download the article
article.download()

# Parse the article
article.parse()

# Perform NLP on the article
article.nlp()
st.header("Article")
st.write(article.text)
st.header("Summary:")
st.write(article.summary)

analysis = TextBlob(article.text)
sentiment = 'Positive' if analysis.polarity>0 else 'Negative'
st.write(f'The sentiments of this articles lies is :red[{analysis.polarity}] and if :green[{sentiment}] Sentence' )


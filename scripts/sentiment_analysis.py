# sentiment_analysis.py
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

if __name__ == '__main__':
    df = pd.read_csv('../data/sample_news_headlines.csv')
    sia = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df['title'].fillna('').apply(lambda t: sia.polarity_scores(str(t))['compound'])
    df.to_csv('../data/sample_news_headlines_scored.csv', index=False)
    print('Saved sample_news_headlines_scored.csv')

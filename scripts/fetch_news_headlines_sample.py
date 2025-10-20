# fetch_news_headlines_sample.py
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')  # store your key in .env

TICKER_KEYWORDS = {'AAPL': 'Apple', 'MSFT': 'Microsoft', 'GOOG': 'Alphabet'}

def fetch_headlines_for(query, page=1):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'pageSize': 100,
        'page': page,
        'apiKey': NEWSAPI_KEY,
        'language': 'en',
    }
    r = requests.get(url, params=params)
    return r.json()

if __name__ == '__main__':
    rows = []
    for ticker, kw in TICKER_KEYWORDS.items():
        print('Searching news for', ticker)
        res = fetch_headlines_for(kw)
        for art in res.get('articles', []):
            rows.append({
                'ticker': ticker,
                'published_at': art.get('publishedAt'),
                'source': art.get('source', {}).get('name'),
                'author': art.get('author'),
                'title': art.get('title'),
                'description': art.get('description'),
                'url': art.get('url')
            })

    df = pd.DataFrame(rows)
    df.to_csv('../data/sample_news_headlines.csv', index=False)
    print('Saved sample_news_headlines.csv')

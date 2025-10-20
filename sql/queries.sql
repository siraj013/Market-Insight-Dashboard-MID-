-- Top 5 days with largest single-day % drop for a ticker
SELECT date, ticker, (close - open) / open * 100 AS pct_change
FROM stock_prices
WHERE ticker = 'AAPL'
ORDER BY pct_change ASC
LIMIT 5;

-- Average daily sentiment for a ticker over the last 30 days
SELECT date_trunc('day', published_at) AS day,
       AVG(sentiment_score) AS avg_sentiment
FROM news_headlines
WHERE ticker = 'AAPL' AND published_at > now() - interval '30 days'
GROUP BY day
ORDER BY day;

-- Join valuation metric (precomputed) with sentiment to flag risk
-- (Assumes you add a simple table/value file with P/E ratio per ticker)
SELECT s.ticker, v.pe_ratio, AVG(n.sentiment_score) AS avg_sentiment
FROM stock_prices s
JOIN valuation v ON v.ticker = s.ticker
LEFT JOIN news_headlines n ON n.ticker = s.ticker AND n.published_at::date = s.date
WHERE s.date = (SELECT MAX(date) FROM stock_prices WHERE ticker = s.ticker)
GROUP BY s.ticker, v.pe_ratio
ORDER BY avg_sentiment;

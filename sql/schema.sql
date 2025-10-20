-- schema.sql
CREATE TABLE stock_prices (
  id SERIAL PRIMARY KEY,
  ticker VARCHAR(10) NOT NULL,
  date DATE NOT NULL,
  open NUMERIC,
  high NUMERIC,
  low NUMERIC,
  close NUMERIC,
  adjusted_close NUMERIC,
  volume BIGINT
);

CREATE TABLE news_headlines (
  id SERIAL PRIMARY KEY,
  ticker VARCHAR(10),
  published_at TIMESTAMP,
  source VARCHAR(255),
  author VARCHAR(255),
  title TEXT,
  description TEXT,
  url TEXT,
  sentiment_score NUMERIC
);

-- Indexes for faster queries
CREATE INDEX idx_stock_ticker_date ON stock_prices(ticker, date);
CREATE INDEX idx_news_ticker_date ON news_headlines(ticker, published_at);

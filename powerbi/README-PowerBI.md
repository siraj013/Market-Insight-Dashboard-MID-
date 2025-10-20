# Power BI Dashboard Instructions

This file explains how to create the Market Insight Dashboard in Power BI using the sample data.

## Steps:

1. Open Power BI Desktop.
2. Click **Get Data → CSV** and import:
   - `data/sample_stock_prices.csv`
   - `data/sample_news_headlines_scored.csv`
3. Model: Create a relationship between `stock_prices.ticker` and `news_headlines.ticker`.
4. Suggested visuals:
   - **Line chart**: `date` vs `close` for stock prices, add a secondary axis for average `sentiment_score` by day.
   - **Card visuals**: show latest `Close`, `P/E`, `EPS`.
   - **Bar chart**: number of headlines by sentiment category (negative, neutral, positive).
5. Add slicers for ticker (single select) and date range.
6. Tooltips: show headline title and source for interactivity.
7. Optional: add screenshots in this folder to showcase the dashboard.

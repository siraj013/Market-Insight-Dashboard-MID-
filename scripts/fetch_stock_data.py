# fetch_stock_data.py
import yfinance as yf
import pandas as pd

TICKERS = ['AAPL', 'MSFT', 'GOOG']
PERIOD = '1y'  # one year

if __name__ == '__main__':
    all_frames = []
    for t in TICKERS:
        print('Fetching', t)
        ticker = yf.Ticker(t)
        hist = ticker.history(period=PERIOD)
        hist = hist.reset_index()
        hist['ticker'] = t
        all_frames.append(hist[['Date','ticker','Open','High','Low','Close','Volume','Dividends','Stock Splits']])

    df = pd.concat(all_frames)
    df.rename(columns={'Date':'date','Open':'open','High':'high','Low':'low','Close':'close','Volume':'volume'}, inplace=True)
    df.to_csv('../data/sample_stock_prices.csv', index=False)
    print('Saved sample_stock_prices.csv')

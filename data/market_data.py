import yfinance as yf

def fetch_data(symbol="AAPL", period="6mo", interval="1d"):
    df = yf.download(symbol, period=period, interval=interval)
    df.dropna(inplace=True)
    return df

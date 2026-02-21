import ta

def calculate_rsi(df, period=14):
    close = df["Close"].squeeze()  # <-- FIX
    rsi = ta.momentum.RSIIndicator(close, period).rsi()
    return rsi.iloc[-1]

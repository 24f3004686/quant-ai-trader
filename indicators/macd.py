import ta

def calculate_macd(df):
    close = df["Close"].squeeze()  # <-- FIX
    macd = ta.trend.MACD(close)
    macd_line = macd.macd().iloc[-1]
    signal_line = macd.macd_signal().iloc[-1]
    return macd_line, signal_line

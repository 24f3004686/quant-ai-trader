import numpy as np

def calculate_volatility(df):
    close = df["Close"].squeeze()  # <-- FIX
    returns = np.log(close / close.shift(1))
    return returns.std() * (252 ** 0.5)

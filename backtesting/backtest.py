import numpy as np
import pandas as pd
from ta.momentum import RSIIndicator

def backtest_strategy(df, rsi_period=14):
    close = df["Close"].squeeze()

    # Compute returns
    returns = close.pct_change()

    # Compute RSI
    rsi = RSIIndicator(close, rsi_period).rsi()

    # Create signal series aligned with index
    signals = pd.Series(0, index=close.index)

    signals[rsi < 30] = 1     # Buy
    signals[rsi > 70] = -1    # Sell

    # Align signals and returns
    strategy_returns = returns * signals.shift(1)

    # Drop NaNs caused by indicators
    strategy_returns = strategy_returns.dropna()

    return strategy_returns

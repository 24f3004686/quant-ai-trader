import matplotlib.pyplot as plt
import numpy as np

def plot_performance(returns, symbol):
    # Equity curve
    equity = (1 + returns).cumprod()

    # Drawdown
    peak = equity.cummax()
    drawdown = (equity - peak) / peak

    # Plot Equity Curve
    plt.figure()
    plt.plot(equity)
    plt.title(f"Equity Curve - {symbol}")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.show()

    # Plot Drawdown
    plt.figure()
    plt.plot(drawdown)
    plt.title(f"Drawdown - {symbol}")
    plt.xlabel("Time")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.show()

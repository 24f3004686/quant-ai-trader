import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns - (risk_free_rate / 252)
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()

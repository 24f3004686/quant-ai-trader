from data.market_data import fetch_data
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from indicators.volatility import calculate_volatility
from strategies.signal_generator import generate_signal
from llm.groq_agent import analyze_market
from backtesting.backtest import backtest_strategy
from backtesting.metrics import sharpe_ratio, max_drawdown
from visuals.performance import plot_performance

def analyze_symbol(symbol):
    df = fetch_data(symbol)

    df["RSI"] = df["Close"].squeeze().rolling(14).apply(
        lambda x: calculate_rsi(df.iloc[:len(x)])
    )

    rsi = calculate_rsi(df)
    macd_line, signal_line = calculate_macd(df)
    volatility = calculate_volatility(df)

    signal = generate_signal(rsi, macd_line, signal_line)
    ai_analysis = analyze_market(rsi, macd_line, signal_line, volatility)

    returns = backtest_strategy(df)
    plot_performance(returns, symbol)
    sharpe = sharpe_ratio(returns)
    drawdown = max_drawdown(returns)

    return {
        "symbol": symbol,
        "rsi": round(rsi, 2),
        "macd": round(macd_line, 4),
        "volatility": round(volatility, 2),
        "signal": signal,
        "sharpe_ratio": round(sharpe, 2),
        "max_drawdown": round(drawdown, 2),
        "ai_insight": ai_analysis
    }

def main():
    symbols = ["AAPL", "MSFT", "BTC-USD", "ETH-USD"]

    for s in symbols:
        result = analyze_symbol(s)

        print("\n==============================")
        print(f"📊 {result['symbol']}")
        print(f"RSI: {result['rsi']}")
        print(f"MACD: {result['macd']}")
        print(f"Volatility: {result['volatility']}")
        print(f"Signal: {result['signal']}")
        print(f"Sharpe Ratio: {result['sharpe_ratio']}")
        print(f"Max Drawdown: {result['max_drawdown']}")
        print("\n🤖 AI Insight")
        print(result["ai_insight"])

if __name__ == "__main__":
    main()

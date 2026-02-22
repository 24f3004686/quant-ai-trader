import asyncio
import json
import websockets
from collections import deque
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
import sys

# -----------------------------
# Helper: Normalize symbol
# -----------------------------
def normalize_symbol(symbol: str) -> str:
    """
    Converts:
    BTC-USD → btcusdt
    ETH-USD → ethusdt
    SOL-USD → solusdt
    """
    symbol = symbol.upper().strip()

    if symbol.endswith("-USD"):
        base = symbol.replace("-USD", "")
        return f"{base.lower()}usdt"

    # If user already passes btcusdt
    return symbol.lower()

# -----------------------------
# Real-time stream
# -----------------------------
async def stream_prices(symbol="BTC-USD"):
    binance_symbol = normalize_symbol(symbol)
    ws_url = f"wss://stream.binance.com:9443/ws/{binance_symbol}@trade"

    prices = deque(maxlen=100)

    async with websockets.connect(ws_url) as ws:
        print(f"📡 Connected to Binance WebSocket ({symbol})")
        print("⏳ Waiting for live trades...\n")

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            price = float(data["p"])
            prices.append(price)

            # Only compute indicators once we have enough data
            if len(prices) >= 50:
                analyze_realtime(prices, symbol)

# -----------------------------
# Indicator computation
# -----------------------------
def analyze_realtime(prices, symbol):
    series = pd.Series(prices)

    macd_indicator = MACD(series)
    rsi = RSIIndicator(series, 14).rsi().iloc[-1]
    macd_val = macd_indicator.macd().iloc[-1]
    signal_val = macd_indicator.macd_signal().iloc[-1]

    print(
        f"📊 LIVE {symbol} | "
        f"Price: {prices[-1]:.2f} | "
        f"RSI: {rsi:.2f} | "
        f"MACD: {macd_val:.6f} | "
        f"Signal: {signal_val:.6f}"
    )

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    # Default BTC-USD, allow any crypto
    symbol = sys.argv[1] if len(sys.argv) > 1 else "BTC-USD"
    asyncio.run(stream_prices(symbol))

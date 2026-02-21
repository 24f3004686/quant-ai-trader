import asyncio
import json
import websockets
from collections import deque
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD

# Binance trade stream for BTCUSDT
BINANCE_WS = "wss://stream.binance.com:9443/ws/btcusdt@trade"

# Rolling buffer (last 100 prices)
prices = deque(maxlen=100)

async def stream_prices():
    async with websockets.connect(BINANCE_WS) as ws:
        print("📡 Connected to Binance WebSocket (BTCUSDT)")

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            price = float(data["p"])
            prices.append(price)

            if len(prices) >= 30:
                analyze_realtime()

def analyze_realtime():
    df = pd.Series(prices)

    rsi = RSIIndicator(df, 14).rsi().iloc[-1]
    macd = MACD(df).macd().iloc[-1]
    signal = MACD(df).macd_signal().iloc[-1]

    print(
        f"📊 LIVE BTC | Price: {prices[-1]:.2f} | "
        f"RSI: {rsi:.2f} | MACD: {macd:.2f}"
    )

if __name__ == "__main__":
    asyncio.run(stream_prices())

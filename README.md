# 📈 Quant AI Trader

An **AI-powered quantitative trading system** that combines traditional financial indicators, **backtesting & risk metrics**, and **large language model (LLM) reasoning** to analyze **stocks and cryptocurrencies**.  
The system is deployable as a **FastAPI service** and provides explainable, risk-aware trading insights.

> ⚠️ **Disclaimer:** This project is strictly for **educational and research purposes only**.  
> It does **not** constitute financial or investment advice.

---

## 🚀 Project Overview

**Quant AI Trader** bridges the gap between:

- **Quantitative Finance** (indicator-based strategies, backtesting, risk metrics)
- **Explainable AI** (LLM-generated market interpretation and risk warnings)

Instead of outputting only buy/sell signals, the system:
1. Computes quantitative indicators
2. Evaluates strategy performance via backtesting
3. Measures risk using Sharpe Ratio & Max Drawdown
4. Uses an LLM (via Groq API) to **explain market conditions in natural language**
5. Exposes results via a professional REST API

---

## ✨ Key Features

### 📊 Quantitative Indicators
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Annualized Volatility
- Rule-based trading signals

### 📉 Backtesting & Risk Analysis
- Historical backtesting on real market data
- Sharpe Ratio (risk-adjusted return)
- Maximum Drawdown
- Equity curve & drawdown visualization

### 🌍 Multi-Asset Support
- **Equities:** AAPL, MSFT, etc.
- **Cryptocurrencies:** BTC-USD, ETH-USD, etc.
- Unified pipeline for both markets

### 🤖 AI-Powered Reasoning
- Groq API with **LLaMA 3.1 (llama-3.1-8b-instant)**
- Converts numeric indicators into:
  - Market interpretation
  - Trading insight
  - Risk warnings

### 🌐 API Deployment
- Built using **FastAPI**
- Interactive Swagger UI
- Real-time analysis via REST endpoints

---

## 🏗️ Project Architecture
quant-ai-trader/
│
├── api/ # FastAPI application
│ └── app.py
│
├── data/ # Market data fetching
│ └── market_data.py
│
├── indicators/ # Technical indicators
│ ├── rsi.py
│ ├── macd.py
│ └── volatility.py
│
├── strategies/ # Signal generation logic
│ └── signal_generator.py
│
├── backtesting/ # Backtesting & risk metrics
│ ├── backtest.py
│ └── metrics.py
│
├── visuals/ # Performance visualization
│ └── performance.py
│
├── llm/ # Groq LLM integration
│ └── groq_agent.py
│
├── main.py # Multi-asset analysis runner
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙️ Tech Stack

- **Language:** Python 3
- **Quant & Data:** NumPy, Pandas, yFinance, ta
- **AI / LLM:** Groq API (LLaMA 3.1)
- **Backend API:** FastAPI, Uvicorn
- **Visualization:** Matplotlib
- **Version Control:** Git & GitHub

---

## ▶️ Installation & Setup

### 1️⃣ Clone the repository
bash
git clone https://github.com/24f3004686/quant-ai-trader.git
cd quant-ai-trader
### 2️⃣ Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate
### 3️⃣ Install dependencies
python -m pip install -r requirements.txt
### 4️⃣ Add Groq API Key
Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here
### 📊 Run Quant + AI Analysis (CLI)
python main.py
## 🌐 Run FastAPI Server
python -m uvicorn api.app:app --reload
### API Access

Swagger UI:
http://127.0.0.1:8000/docs

Analyze any asset:

http://127.0.0.1:8000/analyze?symbol=BTC-USD

## 🔴 Real-Time Crypto Market Streaming (WebSockets)

In addition to historical backtesting, this project supports **true real-time, event-driven market analysis** for cryptocurrencies.

### How it works
- Connects to **Binance public WebSocket streams**
- Receives live trade events in real time (seconds-level latency)
- Maintains a rolling price window
- Updates RSI and MACD indicators on each market event
- Avoids polling by using an **event-driven architecture**

### Why this matters
- Demonstrates real-world trading system design
- Shows understanding of low-latency data ingestion
- Complements historical backtesting with live market monitoring

> AI-based analysis is intentionally rate-limited to avoid excessive API calls and to reflect production-grade system design.
## 2️⃣ Add a How to Run Real-Time Stream section

## 📡 Running Real-Time Crypto Stream (Binance)

This module streams live cryptocurrency prices using WebSockets.

### Run live BTC stream
bash

python realtime/binance_stream.py

---

## 🧠 System Design Notes

- Historical analysis and real-time streaming are implemented as **separate modules**
- Backtesting uses historical market data to avoid lookahead bias
- Real-time analysis uses an **event-driven WebSocket architecture**
- AI (LLM) calls are decoupled and rate-limited for scalability
- The system is designed for extensibility (additional exchanges, assets, or strategies)

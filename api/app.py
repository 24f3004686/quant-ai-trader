from fastapi import FastAPI
from main import analyze_symbol

app = FastAPI(
    title="Quant AI Trader",
    description="AI-assisted quantitative trading analysis for stocks and crypto",
    version="1.0"
)

@app.get("/analyze")
def analyze(symbol: str):
    return analyze_symbol(symbol)

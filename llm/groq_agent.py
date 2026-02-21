import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_market(rsi, macd_line, signal_line, volatility):
    prompt = f"""
You are a quantitative trading analyst.

Market indicators:
RSI: {rsi:.2f}
MACD line: {macd_line:.4f}
Signal line: {signal_line:.4f}
Volatility: {volatility:.2f}

Give a concise trading insight and risk warning.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You analyze financial markets quantitatively."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

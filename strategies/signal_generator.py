def generate_signal(rsi, macd_line, signal_line):
    if rsi > 70 and macd_line > signal_line:
        return "Overbought – Possible Sell / Profit Booking"
    elif rsi < 30 and macd_line < signal_line:
        return "Oversold – Possible Buy Opportunity"
    else:
        return "Neutral / Wait"

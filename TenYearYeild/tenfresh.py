import yfinance as yf
import time

def monitor_tnx(interval=60):
    while True:
        tnx = yf.Ticker("^TNX")
        data = tnx.history(period="1d", interval="1m")
        latest = data["Close"].iloc[-1] / 10
        print(f"TNX: {latest:.2f}%")
        time.sleep(interval)

# Refresh every 60 seconds
monitor_tnx(60)
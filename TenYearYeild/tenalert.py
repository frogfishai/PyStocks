import yfinance as yf
import time

THRESHOLD = 4.50  # set your alert level

def monitor_tnx_alert(threshold=THRESHOLD, interval=60):
    print(f"Monitoring TNX... alert at {threshold}%")

    while True:
        tnx = yf.Ticker("^TNX")
        data = tnx.history(period="1d", interval="1m")
        latest = data["Close"].iloc[-1] / 10

        print(f"TNX: {latest:.2f}%")

        if latest >= threshold:
            print(f"ALERT: TNX has crossed {threshold}%! Current: {latest:.2f}%")
            # You can add email, SMS, Discord webhook, etc.

        time.sleep(interval)

monitor_tnx_alert()
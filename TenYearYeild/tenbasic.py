import yfinance as yf

def get_tnx():
    tnx = yf.Ticker("^TNX")
    data = tnx.history(period="1d", interval="1m")
    latest = data["Close"].iloc[-1]
    print(f"Current 10-Year Yield (TNX): {latest / 10:.2f}%")

get_tnx()
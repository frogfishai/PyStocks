import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.set_page_config(page_title="TNX Dashboard", layout="wide")

st.title("📈 10-Year Treasury Yield (TNX) Dashboard")
st.write("Live monitoring of the 10-year Treasury yield using Yahoo Finance data.")

# Sidebar controls
refresh_rate = st.sidebar.slider("Refresh rate (seconds)", 10, 300, 60)
threshold = st.sidebar.number_input("Alert threshold (%)", value=4.50)

# Function to get TNX
def get_tnx():
    tnx = yf.Ticker("^TNX")
    data = tnx.history(period="1d", interval="1m")
    data["Yield"] = data["Close"] / 10
    return data

# Live updating section
placeholder = st.empty()

while True:
    data = get_tnx()
    latest = data["Yield"].iloc[-1]

    with placeholder.container():
        st.subheader(f"Current TNX Yield: **{latest:.2f}%**")

        # Alert
        if latest >= threshold:
            st.error(f"⚠️ ALERT: TNX has crossed {threshold}% (Current: {latest:.2f}%)")
        else:
            st.success(f"TNX is below alert threshold ({threshold}%)")

        # Chart
        st.line_chart(data["Yield"], height=300)

        # Data table
        st.dataframe(data.tail(10))

    time.sleep(refresh_rate)

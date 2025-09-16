import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# Import your backend functions

from api_fetch import get_alpha_vantage_data
from indicators import calculate_indicators

# --- PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="Stock Analytics Platform")

# --- SIDEBAR ---
st.sidebar.header("Controls")
symbol = st.sidebar.text_input("Stock Symbol", "AAPL").upper()
refresh_button = st.sidebar.button("Refresh Data", type="primary")

# --- MAIN PAGE ---
st.title(f"Stock Analytics for {symbol}")

# Set date range for the last 5 years
end_date = datetime.now()
start_date = datetime(end_date.year - 5, end_date.month, end_date.day)

# --- DATA FETCHING AND PROCESSING ---
stock_data = get_alpha_vantage_data(symbol)

if not stock_data.empty:
    df = calculate_indicators(stock_data.copy())

    # --- DISPLAY KPIS ---
    latest_data = df.iloc[-1]
    price_change = latest_data['Close'] - df.iloc[-2]['Close']
    percent_change = (price_change / df.iloc[-2]['Close']) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Last Close Price", f"${latest_data['Close']:.2f}", f"{price_change:.2f} ({percent_change:.2f}%)")
    col2.metric("50-Day MA", f"${latest_data['SMA_50']:.2f}")
    col3.metric("RSI", f"{latest_data['RSI_14']:.2f}")

    # --- CHARTS ---
    st.subheader("Price & Moving Averages")
    fig_price = go.Figure()
    fig_price.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Price'))
    fig_price.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], mode='lines', name='20-Day MA'))
    fig_price.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='50-Day MA'))
    st.plotly_chart(fig_price, use_container_width=True)

    st.subheader("RSI & Daily Returns")
    col1, col2 = st.columns(2)
    with col1:
         fig_rsi = go.Figure()
         fig_rsi.add_trace(go.Scatter(x=df.index, y=df['RSI_14'], mode='lines', name='RSI'))
         fig_rsi.add_hline(y=70, line_dash="dash", line_color="red")
         fig_rsi.add_hline(y=30, line_dash="dash", line_color="green")
         st.plotly_chart(fig_rsi, use_container_width=True)
    with col2:
         fig_returns = go.Figure()
         fig_returns.add_trace(go.Histogram(x=df['daily_return'], nbinsx=50, name='Daily Return'))
         st.plotly_chart(fig_returns, use_container_width=True)

    # --- DATA TABLE & DOWNLOAD ---
    st.subheader("Data Explorer")
    st.dataframe(df)
    csv = df.to_csv().encode('utf-8')
    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name=f'{symbol}_data.csv',
        mime='text/csv',
    )
else:
    st.error(f"Could not fetch data for '{symbol}'. Check the symbol or API key.")
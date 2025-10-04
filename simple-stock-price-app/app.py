import streamlit as st
import pandas as pd
import yfinance as yf
st.write(""" 
# Simple Stock Price App
         
Shown are the stock closing price an volume of Google
         
         """)

google = yf.Ticker("GOOGL")

google_data = google.history(period = "6mo")

st.write(google_data.head())
st.write(google_data['Close'].tail())

st.write("## Closing Price ")
st.line_chart(google_data.Close)

st.write("## Volume Price ")
st.line_chart(google_data.Volume)
st.write(
    """
## Lets analyse the specific years stock record
     """
)

google_particular_data = google.history(start = '2010-05-30' , end = '2025-09-30')

st.line_chart(google_particular_data['Close'])








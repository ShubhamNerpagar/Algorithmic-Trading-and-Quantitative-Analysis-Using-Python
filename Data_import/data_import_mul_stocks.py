# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:47:45 2024

@author: shubham
"""

import datetime
import yfinance as yf
import pandas as pd

stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "3988.HK"]

start = datetime.datetime.today() - datetime.timedelta(30)
end = datetime.datetime.today()
cl_price = pd.DataFrame()  # Empty dataframe which will be filled with closing prices
ohlcv_data = {}

# Looping over tickers and creating dataframe with closing prices

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    
    
for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)

    
print(ohlcv_data["MSFT"]["Open"])
    








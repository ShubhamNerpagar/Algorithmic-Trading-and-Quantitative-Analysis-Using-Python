# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:27:53 2024

@author: shubham
"""

import datetime as dt
import yfinance as yf
import pandas as pd


start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}

stocks = ['AMZN', 'GOOG', 'META', 'MSFT']

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
                                                       
                                                       
cl_price.fillna(0)

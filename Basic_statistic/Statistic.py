# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:13:14 2024

@author: shubham
"""

import yfinance as yf
import pandas as pd
import datetime as dt

ticker = ['MSFT', 'META', 'GOOG', 'AMZN']

start = dt.datetime.today() - dt.timedelta(3550)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}

for stocks in ticker:
    cl_price[stocks] = yf.download(stocks, start, end)['Adj Close']
    


# Dropping NaN value

cl_price.dropna(axis=0,how="all", inplace=True)


# Calculate the mean of a stock

cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()
cl_price.head()
cl_price.tail()


daily_returns = cl_price.pct_change() # To calculate the pct change
cl_price/cl_price.shift()       # shift your row 

daily_return_2 = cl_price/cl_price.shift() - 1

daily_returns.mean()
daily_returns.std()





























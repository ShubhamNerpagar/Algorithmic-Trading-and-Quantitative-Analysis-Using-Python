# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 09:47:24 2024

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
    
# Filling NaN Values

cl_price.fillna(method='bfill', axis=0,inplace=True)

"""Backfill is a technique which will backfill the data from where the data (last value)
was available, axis value determine the row or column, unless you don't use inplace = true
the original data will not get updated"""


# Dropping NaN value

cl_price.dropna(method='bfill',axis=0, inplace=True)

# Cleaning data 
"""
axis
how
thresh
subset
"""



































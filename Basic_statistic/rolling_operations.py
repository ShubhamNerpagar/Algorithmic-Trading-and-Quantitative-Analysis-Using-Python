# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:30:49 2024

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
    
    
# Rolling mean and rolling window

daily_returns = cl_price.pct_change()
"""
Simple moving average
"""

daily_returns.rolling(window=10).mean()
daily_returns.rolling(window=10).max()
daily_returns.rolling(window=10).sum()

"""
Exponential Moving average
"""

ema_daily_returns = daily_returns.ewm(com=10, min_periods=10).mean()

ema_daily_returns.plot()
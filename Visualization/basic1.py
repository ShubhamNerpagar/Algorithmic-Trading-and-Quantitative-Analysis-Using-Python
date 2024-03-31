# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:55:52 2024

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
    


    
cl_price.plot(subplots=True, layout=(2,2))


cl_price.plot(kind="pie", subplots=True, layout=(2,2))


# Calculate the daily returns

daily_returns = cl_price.pct_change()

daily_returns.plot(subplots=True,layout=(2,2))



# Calculate the cummulative sum of the stocks and plot it
(1+daily_returns).cumprod().plot()


(1+daily_returns).cumsum().plot()
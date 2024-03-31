# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:12:05 2024

@author: shubham
"""

from yahoofinancials import YahooFinancials
import pandas as pd

ticker = "MSFT"

yf = YahooFinancials(ticker)

data_yf = yf.get_historical_price_data("2023-12-01", "2024-01-01", "daily")


df = pd.DataFrame()                                 

for data in data_yf["MSFT"]["prices"]:
    print(df[data])


# Too complicated to fetch the data
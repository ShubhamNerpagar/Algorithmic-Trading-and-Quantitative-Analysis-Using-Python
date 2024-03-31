# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:32:02 2024

@author: shubham
"""

import nsepy as nse
from datetime import date


stock_price = nse.get_history(symbol='INFY', index = False, start = date(2023,12,30), end = date(2024,1,1))
stock_price



#  This library does not support data import
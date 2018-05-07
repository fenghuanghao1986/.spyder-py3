# -*- coding: utf-8 -*-
"""
Created on Sat May  5 12:14:47 2018

@author: fengh
"""

# Q1
import pandas_datareader.data as web
import pandas as pd
from datetime import datetime
# Remotely getting data from companies
morningstar = web.DataReader('F', 'morningstar')
print(morningstar.head(5))

robinhood = web.DataReader('F', 'robinhood')
print(robinhood.head(5))

quandl = web.DataReader('F', 'quandl')
print(quandl.head(5))

ntsdstooq = web.DataReader('^DJI', 'stooq')
print(ntsdstooq.head(5))

# Q2
# create dataframes sepratly for each company
# Morningstar
mor = morningstar[['Close', 'Open','Volume','High','Low']].head(20)

# Robinhood
# column names are different from others note that
rob = robinhood[['close_price', 'open_price','volume','high_price','low_price']].head(20)

# Quandl
qua = quandl[['Close', 'Open','Volume','High','Low']].head(20)

# Nasdaq
ntsd = ntsdstooq[['Close', 'Open','Volume','High','Low']].head(20)

closeTable = pd.crosstab(mor.Close, qua.Close, ntsd.Close, margins=True)

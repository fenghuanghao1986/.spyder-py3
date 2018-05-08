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
# due to the difference of each dataframes from different compines
# I decide to only use first 200 rows of the data
# Morningstar
mor = morningstar[['Close', 'Open','Volume','High','Low']].head(200)
# Robinhood
# column names are different from others note that
rob = robinhood[['close_price', 'open_price','volume','high_price','low_price']].head(200)
rob.columns = ['Close', 'Open','Volume','High','Low']
# Quandl
qua = quandl[['Close', 'Open','Volume','High','Low']].head(200)
# Nasdaq
ntsd = ntsdstooq[['Close', 'Open','Volume','High','Low']].head(200)
# part a
# creating Close dataframe
morClose = list(mor.Close)
robClose = list(rob.Close)
quaClose = list(qua.Close)
ntsdClose = list(ntsd.Close)
dicClose = {'Morningstar': morClose, 
            'Robinhood': robClose,
            'Quandl': quaClose,
            'Nasdaq': ntsdClose}
CloseData = pd.DataFrame(dicClose)
CloseData.head(5)
# part b
# creating Open dataframe
morOpen = list(mor.Open)
robOpen = list(rob.Open)
quaOpen = list(qua.Open)
ntsdOpen = list(ntsd.Open)
dicOpen = {'Morningstar': morOpen, 
            'Robinhood': robOpen,
            'Quandl': quaOpen,
            'Nasdaq': ntsdOpen}
OpenData = pd.DataFrame(dicOpen)
OpenData.head(5)
# part c
# creating Volume dataframe
morVolume = list(mor.Volume)
robVolume = list(rob.Volume)
quaVolume = list(qua.Volume)
ntsdVolume = list(ntsd.Volume)
dicVolume = {'Morningstar': morVolume, 
            'Robinhood': robVolume,
            'Quandl': quaVolume,
            'Nasdaq': ntsdVolume}
VolumeData = pd.DataFrame(dicVolume)
VolumeData.head(5)
# part d
# creating High dataframe
morHigh = list(mor.High)
robHigh = list(rob.High)
quaHigh = list(qua.High)
ntsdHigh = list(ntsd.High)
dicHigh = {'Morningstar': morHigh, 
            'Robinhood': robHigh,
            'Quandl': quaHigh,
            'Nasdaq': ntsdHigh}
HighData = pd.DataFrame(dicHigh)
HighData.head(5)
# part e
# creating Low dataframe
morLow = list(mor.Low)
robLow = list(rob.Low)
quaLow = list(qua.Low)
ntsdLow = list(ntsd.Low)
dicLow = {'Morningstar': morLow, 
            'Robinhood': robLow,
            'Quandl': quaLow,
            'Nasdaq': ntsdLow}
LowData = pd.DataFrame(dicLow)
LowData.head(5)
# Q3























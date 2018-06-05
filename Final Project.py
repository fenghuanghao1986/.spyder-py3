# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:10:32 2018

@author: fengh
"""
import csv
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import urllib.request
from urllib.request import Request, urlopen
# read data only using the first 20 rows of the data
response = urllib.request.urlopen("https://raw.githubusercontent.com/fenghuanghao1986/.spyder-py3/master/BusinessData.csv")
data = pd.read_csv(response)
data = data.head(200)
# clean data check missing data
nullCheck = data.isnull()
# from the out we can see some data missing
# filling them with  average value of that colunm
data.fillna(data.UnitPrice.mean(), inplace=True)
nullCheck2 = data.isnull()
# check statistics using describe
stctCheck = data.describe()
# since we have count, mean, std, min, max by using describe
# have to check 5 more other statistic function
functions = ['sum', 'median', 'var', 'prod', 'mad']
extraStctCheck = data.groupby(data.SalesRep).agg({'Quantity':functions,
                                                  'UnitPrice':functions,
                                                  'UnitCost': functions})
# do the cov and corr
unitData = pd.DataFrame(data.UnitPrice)
unitData['UnitCost'] = data.UnitCost
unitCov = unitData.cov()
unitCorr = unitData.corr()
# creat function use .apply()
# function will calculate the profit
# simple function just for demo the usage of function
def profit(price, cost):
    prof = price - cost
    percentage = prof / cost
    return percentage
prof = profit(unitData.UnitPrice, unitData.UnitCost)
# add prof to the end of the end of dataframe
unitData['Profit'] = prof
# crosstab() pivot usage
crs = pd.crosstab(data.SalesRep, data.Quantity, margins=True)
piv = data.pivot_table(index='SalesRep')
# create loop for new dataframe
rows = data[:3]


























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
import numpy as np
from scipy.stats import stats
# read data only using the first 20 rows of the data
response = urllib.request.urlopen("https://raw.githubusercontent.com/fenghuanghao1986/.spyder-py3/master/BusinessData.csv")
data = pd.read_csv(response)
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

# plots
# bar chart
counts = pd.value_counts(data.SalesRep)
counts = pd.DataFrame(counts)
plt.grid(True)
objects = tuple(counts.index)
plt.bar(np.arange(len(counts.index)), counts.SalesRep)
plt.xticks(np.arange(3),objects)
plt.xlabel('Name of Representatives')
plt.ylabel('Number of Business Transactions')
plt.show()  
SalesRep_ProdCount = pd.crosstab(data.ProductName, data.SalesRep, margins=True)
SalesRep_ProdCount = pd.DataFrame(SalesRep_ProdCount) 
SalesRep_ProdCount.plot.bar() 
# line plot
data["TotalSales"] = data.UnitPrice * data.Quantity   
plt.figure()
plt.plot(data.OrderDate, data.TotalSales)
plt.xticks(rotation=90)
plt.title("Total Sales Time Series Graph")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.show()
# hitgram
plt.hist(data.SalesRep, bins = 30)
plt.title("Histogram of Sales Rep")
plt.xlabel("Sales names")
plt.ylabel("Frequency")
plt.show()
# scatter plot
plt.figure()
plt.scatter(data.OrderDate, unitData.Profit)
plt.title("Scatter plot")
plt.xlabel("Order Date")
plt.ylabel("Protfit")
plt.show()
# box-plot
data[["UnitPrice", "SalesRep"]].boxplot(by="SalesRep", fontsize=14) # regular pandas boxplot 
plt.suptitle("")
plt.title("A boxplot of Quantity by SalesRep")
plt.show()
# regression
x = data["ProductID"]
y = data["UnitCost"]
Results = stats.linregress(x,y)
slope=Results[0]
intercept = Results[1]
rsquared = Results[2]*2
pvalue = Results[3]
SE = Results[4]
plt.figure(figsize=(10,5))
pred_y = intercept + slope*x
plt.scatter(x, y)
plt.plot(x, pred_y, color = "red")
plt.suptitle("Relationship Between product id and unit cost", fontsize=18, y=1.1)
plt.title(f"y={round(intercept,2)} + {round(slope, 2)}*x")
plt.xlabel("Years of Service", fontsize=14)
plt.ylabel("Salary", fontsize=14)
plt.show()
# t-test


















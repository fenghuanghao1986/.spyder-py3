# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

This is first practice for learning STAT using Python

Author "Howard Feng"
"""

# Q1
# Importing libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# read csv file
file = pd.read_csv("STATL1Sales.csv")
# convert file to dataframe 
stat = pd.DataFrame(file)
# change date format
# regarding this one, I am not sure, I may have to ask Emma for a DML3 Training Manual
stat['Date'] = pd.to_datetime(stat.Date) 
print(stat.head(5))

# Q2
# part a. Summary statics
statSummary1 = stat.describe()
# part b. 

"""
This part is for several histograms for different col and different dataframe
# numCalls histogram for original dataframe
statCallHist = stat.NumCalls.hist()
# numCalls histogram for statics 
summCallHist = statSummary.NumCalls.hist()
# sales histogram for original dataframe
SaleHist = stat.Sales.hist()
# sales histogram for statics 
summSaleHist = statSummary.Sales.hist()
"""

# I assume you want us to creat histograms from original dataframe
stat[["NumCalls","Sales"]].hist() # on your slides page 15 the format you write was wrong, you were missing one set of []
# part c. 
plt.subplot(211)
plt.grid(True)
plt.hist(stat.NumCalls)
plt.title('Histogram of Calls')
plt.xlabel('Number of calls')
plt.ylabel('Student Number')
plt.subplot(212)
plt.grid(True)
plt.hist(stat.Sales)
plt.title('Histogram of Sales')
plt.xlabel('Sales Values')
plt.ylabel('Student number')
plt.subplots_adjust(hspace= 0.6)
plt.show()
# Q3
# part a. Summary statics
statSummary2 = stat[["NumCalls", "Sales"]].describe()
"""
# create call number bar chart 
callBar = stat.NumCalls.value_counts()
callBar = pd.DataFrame(callBar)
callBar.plot(kind="bar")
# create sale bar chart
saleBar = stat.Sales.value_counts()
saleBar = pd.DataFrame(saleBar)
saleBar.plot(kind="bar")
"""
NC = stat[['NumCalls']].plot(kind='bar', title ="Simple Bar Chart for Calls", figsize=(15, 10), legend=True, fontsize=12)
NC.set_xlabel("ID", fontsize=12)
NC.set_ylabel("Number of Calls", fontsize=12)
plt.show()
Sale = stat[['Sales']].plot(kind='bar', title ="Simple Bar Chart for Sales", figsize=(15, 10), legend=True, fontsize=12)
Sale.set_xlabel("ID", fontsize=12)
Sale.set_ylabel("Sales", fontsize=12)
plt.show()
# part c. 
# use matplot to create bar chart
plt.grid(True)
plt.bar(np.arange(len(stat.NumCalls)), stat.NumCalls)
plt.title('Barchart of Calls')
plt.xlabel('Number of calls')
plt.ylabel('Student Number')
plt.show()
plt.grid(True)
plt.bar(np.arange(len(stat.Sales)), stat.Sales)
plt.title('Barchart of Sales')
plt.xlabel('Sales Values')
plt.ylabel('Student number')
plt.show()
# Q4

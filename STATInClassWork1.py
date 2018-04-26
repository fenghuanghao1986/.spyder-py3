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
statSummary = stat.describe()
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
# I am not sure what is the difference between Q2 part a
statSummary = stat.describe()
# I assume you want us to creat histograms from original dataframe
stat[["NumCalls","Sales"]].plot() # on your slides page 15 the format you write was wrong, you were missing one set of []
# part c. 
plt.subplot(211)
plt.grid(True)
plt.plot(stat.NumCalls)
plt.title('Histogram of Calls')
plt.xlabel('Number of calls')
plt.ylabel('Student Number')
plt.subplot(212)
plt.grid(True)
plt.plot(stat.Sales)
plt.title('Histogram of Sales')
plt.xlabel('Sales Values')
plt.ylabel('Student number')
plt.subplots_adjust(hspace= 0.6)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:09:32 2018

@author: fengh
"""

# Q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = pd.read_csv("STATL3Nuts.csv")
stat = pd.DataFrame(file)
stat = stat.drop(stat.columns[[0]], axis=1)
print(stat.head(5))
# Q2
stat['Price'] = 0
stat.Price[stat.Type == 'Pistachio'] = 10.50
stat.Price[stat.Type == 'Walnut'] = 8.75
stat.Price[stat.Type == 'Cashew'] = 9.25
print(stat.head(5))
# Q3
stat['Total'] = stat['Price'] * stat['Quantity']
print(stat.head(5))
# Q4
quantMean = stat['Quantity'].groupby(stat.Location).mean()
print(quantMean)
# Q5
totalMean = stat['Total'].groupby(stat.Type).mean()
print(totalMean)
# Q6
quantMeanByType = stat['Quantity'].groupby(stat.Type).mean()
qmt = quantMeanByType.plot(kind='bar', title ="Mean of Quantity by Type", fontsize=12)
qmt.set_ylabel("Mean Quantity", fontsize=12)
plt.show()
# Q7 
functions = ['mean', 'max', 'min']
quantAggOut = stat.groupby(stat.Location).agg({'Quantity':functions})
totalAggOut = stat.groupby(stat.Location).agg({'Total':functions})
print(quantAggOut)
print(totalAggOut)
# Q8 
statPivotDef = stat.pivot_table(stat,index='Location',columns='Type') # default func is mean
print(statPivotDef)
# Q9
statPivotSTD = stat.pivot_table(stat,index='Location',columns='Type',aggfunc='std') # default func is mean
print(statPivotSTD)
# Q10
statCross = pd.crosstab(stat.Type, stat.Location, margins=True)
statCross
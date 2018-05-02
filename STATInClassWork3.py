# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:09:32 2018

@author: fengh
"""

# Q1
# Importing libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# read csv file
file = pd.read_csv("STATL3Nuts.csv")
# convert file to dataframe 
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
quantMeanLoc = stat['Quantity'].groupby(stat.Location).mean()
quantMinLoc = stat['Quantity'].groupby(stat.Location).min()
quantMaxLoc = stat['Quantity'].groupby(stat.Location).max()
# not sure how to use .agg for this . will think about it later
# Q8 is this data mean the Q7's data or the original one?
statPivot = stat.pivot_table(stat,index='Location',columns='Type')
print(statPivot)
# not sure if it is correct or not, will think later
# Q9 same process as Q7 and Q8 I believe
# Q10



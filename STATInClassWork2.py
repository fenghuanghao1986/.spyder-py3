# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 23:07:47 2018

@author: fengh
"""

# Q1
# Importing libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# read csv file
file = pd.read_csv("STATL2Sales.csv")
# convert file to dataframe 
stat = pd.DataFrame(file)
print(stat.head(5))
# Q2
print(stat.corr())
plt.matshow(stat.corr())
# Q3
call = np.array(stat.NumCalls)
sale = np.array(stat.Sales)
colors = np.random.rand(len(call))
plt.scatter(call, sale, c=colors)
# Q4
SRI = stat[stat.Job == 'Sales Rep. I']
SRII = stat[stat.Job == 'Sales Rep. II']
plt.scatter(SRI.NumCalls, SRI.Sales, c='red')
plt.scatter(SRII.NumCalls, SRII.Sales, c='blue')
# Q5
SRIII = stat[stat.Job == 'Sales Rep. III']
SRIV = stat[stat.Job == 'Sales Rep. IV']
plt.subplot(221)
plt.grid(True)
plt.hist(SRI.Sales)
plt.title('Histogram of Sales Rep I')
plt.xlabel('Number of calls')
plt.ylabel('Student Number')
plt.subplot(222)
plt.grid(True)
plt.hist(SRII.Sales)
plt.title('Histogram of Sales Rep II')
plt.xlabel('Number of calls')
plt.ylabel('Student Number')
plt.subplot(223)
plt.grid(True)
plt.hist(SRIII.Sales)
plt.title('Histogram of Sales Rep III')
plt.xlabel('Number of calls')
plt.ylabel('Student Number')
plt.subplot(224)
plt.grid(True)
plt.hist(SRIV.Sales)
plt.title('Histogram of Sales Rep IV')
plt.xlabel('Sales Values')
plt.ylabel('Student number')
plt.subplots_adjust(wspace=0.3,hspace= 0.6)
plt.show()
# Q6
saleMean = stat.groupby(['Country'])['Sales'].mean()
print(saleMean)
# Q7
jobType = stat.groupby('Job').Job.count()
print(jobType)
# Q8
allSaleMean = stat.groupby(['Job', 'Gender']).Sales.mean()
#a = allSaleMean.unstack()
index = pd.MultiIndex.from_tuples(allSaleMean.index)
reIndex = allSaleMean.reindex(index)
print(reIndex)



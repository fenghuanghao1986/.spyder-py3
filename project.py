# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:04:56 2018

@author: fengh
"""

# Midterm Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Q1
data = pd.read_csv('BusinessData.csv')
data.head(10)

# Q2
data.shape

# Q3
data['OrderDate'] = pd.to_datetime(data.OrderDate)
data.head(5)

# Q4
# part a
pd.isnull(data)
data.iloc[0: 10]

# part b
a = data.isnull().any()

# Q5
b = data.UnitPrice.mean()
data.fillna(value=b, inplace=True)
data.head(10)

# Q6
data.drop(['ProductID', 'CustomerID'], axis=1, inplace=True)

# Q7
data["TotalSales"] = data.UnitPrice * data.Quantity
data.head(5)

# Q8
data["TotalCost"] = data.UnitCost * data.Quantity
data.head(5)

# Q9
data["Profit"] = data.TotalSales - data.TotalCost
data.head(5)

# Q10
# part c
data[["ProductName", "Customer", "SalesRep"]].describe()

# part d
data[["Quantity", "UnitPrice", "UnitCost", "TotalSales", "TotalCost", "Profit"]].describe()

# Q11
data[["Quantity", "UnitPrice", "UnitCost", "TotalSales", "TotalCost", "Profit"]].agg(['mean', 'min', 'max', 'std', 'var', 'median'])

# Q12
data["Profit"].sum()

# Q13
plt.figure()
plt.plot(data.OrderDate, data.TotalSales)
plt.xticks(rotation=90)
plt.title("Total Sales Time Series Graph")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.show()

# Q14
# part a
pd.unique(data.SalesRep)

# part b
counts = pd.value_counts(data.SalesRep)
counts = pd.DataFrame(counts)

# part c
plt.grid(True)
objects = tuple(counts.index)
plt.bar(np.arange(len(counts.index)), counts.SalesRep)
plt.xticks(np.arange(3),objects)
plt.xlabel('Name of Representatives')
plt.ylabel('Number of Business Transactions')
plt.show()

# part d
# showing actrual value on pie chart
def absolute_value(val):
    a  = np.round(val/100*counts['SalesRep'].sum(), 0)
    return a
plt.pie(counts, labels=counts.index,autopct=absolute_value,shadow=True)

# 15
# part a
SalesRep_ProdCount = pd.crosstab(data.ProductName, data.SalesRep, margins=True)
SalesRep_ProdCount = pd.DataFrame(SalesRep_ProdCount)

# part b
SalesRep_ProdCount.plot.bar()

# Q16
data['Quantity'].groupby(data.ProductName)

# 17
PR = data[data.ProductName == 'Pop Rocks']
PR.mean()


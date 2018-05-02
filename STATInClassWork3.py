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

# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:43:10 2018

@author: fengh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# T-test part

# tried this but having error with
# certificate verify failed error
# so read locial file
# url = r"https://www.sheffield.ac.uk/polopoly_fs/1.536479!/file/birthweight_reduced.csv"
# data = pd.read_csv(url) 
# data.head(10)

# read file and show first 10 rows see if everything is fine
weightFile = pd.read_csv('birthweight_reduced.csv')
weightFile.head(10)

# do statistic analysis
weightFile.describe()

# research question: what's the difference between low and normal weight?
# extract weight for low and normal
lowweight = weightFile.Birthweight[weightFile.LowBirthWeight=="Low"]
norweight = weightFile.Birthweight[weightFile.LowBirthWeight=="Normal"]

# compute the mean of weight for both status
weightFile[["Birthweight", "LowBirthWeight"]].groupby("LowBirthWeight").mean()

# visualize the distribution of low and normal weight
# histogram
plt.hist(lowweight, bins = 30)
plt.title("Histogram of low weight")
plt.xlabel("weight")
plt.ylabel("Frequency")
plt.show()

plt.hist(norweight, bins = 30)
plt.title("Histogram of normal weight")
plt.xlabel("weight")
plt.ylabel("Frequency")
plt.show()

# boxplot
weightFile[["Birthweight", "LowBirthWeight"]].boxplot(by="LowBirthWeight", fontsize=14) # regular pandas boxplot 
plt.suptitle("")
plt.title("A boxplot of low and normal weight")
plt.show()

# levene's test 
teststats_Var, pvalue_Var = stats.levene(lowweight, norweight)
print("This is a hypothesis test for the homogeneity of variance assumption")
print("H0:The variances of low and normal weight are equal")
print (f"test statistics: {teststats_Var}")
print(f"pvalue: {pvalue_Var}")

alpha = 0.05
if pvalue_Var > alpha:
    print("Decision: Fail to reject the null hypothesis")
    print("Conclusion: The variances of low and normal weight are equal")
    print("Proceed to perform a t-test")
else:
    print("Decision: Reject the null hypothesis")
    print("Conclusion: The variances of low and normal weight are unequal")
    print("Proceed to do a Welch's test since variances are unequal")

# t-test
teststats_Mean, pvalue_Mean= stats.ttest_ind(lowweight, norweight, equal_var=True)

print("T Test: This is a hypothesis test for means of male and female faculty salary")
print("H0: Means of low and normal are equal")
print (f"test statistics (t): {teststats_Mean}")
print(f"pvalue: {pvalue_Mean}")

alpha = 0.05
if pvalue_Mean > alpha:
    print("Decision: Fail to reject the null hypothesis")
    print("Conclusion: Means of low and normal weight are equal")
else:
    print("Decision: Reject the null hypothesis")
    print("Conclusion: Means of low and normal weight are unequal")
    
# ANOVA test part
    
# research question: it there a significant birthweight difference
# between different headcirumference

weightFile["headcirumference"].unique()

# extract weight for different headcirumference
twelve = weightFile["Birthweight"][weightFile["headcirumference"]==12]
thirteen = weightFile["Birthweight"][weightFile["headcirumference"]==13]
fourteen = weightFile["Birthweight"][weightFile["headcirumference"]==14]
fifteen = weightFile["Birthweight"][weightFile["headcirumference"]==15]

# visualize distribution of weight by headcirumference
plt.hist(twelve, bins = 30)
plt.title("Histogram of headsize of 12 for weight")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.hist(thirteen, bins = 30)
plt.title("Histogram of headsize of 13 for weight")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.hist(fourteen, bins = 30)
plt.title("Histogram of headsize of 14 for weight")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.hist(fifteen, bins = 30)
plt.title("Histogram of headsize of 15 for weight")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# compute the descritives of all
weightFile[["Birthweight", "headcirumference"]].groupby("headcirumference").agg(["count", "mean", "median", "std","min", "max","skew"]).round(2)

# box-plot
y = twelve.values, thirteen.values, fourteen.values, fifteen.values 
plt.boxplot(y)
plt.title("A Boxplot of Faculty Salaries by Rank")
plt.ylabel("Salary")
plt.xticks(np.arange(len(y))+1, ["12", "13", "14", "15"] )
plt.show()

# levene's test
teststats_Var, pvalue_Var = stats.levene(twelve.values, thirteen.values, fourteen.values, fifteen.values)

print("This is a hypothesis test for the homogeneity of variance assumption")
print("H0: variances of difference headsize weight are equal variances")
print (f"test statistics (F): {teststats_Var}")
print(f"pvalue: {pvalue_Var}")

alpha = 0.05
if pvalue_Var > alpha:
    print("Decision: Fail to reject the null hypothesis")
    print("Conclusion: The variances of difference headcirumference weight are equal")
    print("Proceed to perform an ANOVA test")
else:
    print("Decision: Reject the null hypothesis")
    print("Conclusion: At least the variance of one headsize differs with respect to weight")
    print("Still proceed to perform ANOVA test since the F-test is robust to the homogeneity of variance assumption")

# ANOVA TEST
teststats_Mean, pvalue_Mean = stats.f_oneway(twelve.values, thirteen.values, fourteen.values, fifteen.values)

print("One-Way ANOVA: This is a hypothesis test for means of faculty salary by rank ")
print("H0: The means of difference headcirumference weight are equal")
print (f"test statistics (F): {teststats_Var}")
print(f"pvalue: {pvalue_Var}")

alpha = 0.05
if pvalue_Var > alpha:
    print("Decision: Fail to reject the null hypothesis")
    print("Conclusion: The means of difference headcirumference weight are equal")
else:
    print("Decision: Reject the null hypothesis")
    print("Conclusion: The mean weight of at least one head size is different")
    print("proceed with a follow-up or post hoc test to find which groups are different")

# Regression part
    
from scipy.stats import stats

from statsmodels.formula.api import ols
# model 1 

x = weightFile[["motherage"]]
y = weightFile["Birthweight"]

model1 = ols("y ~ x", data=weightFile).fit()
print(model1.summary())

model1.params
model1.pvalues
model1.rsquared

# let's evaluate our model 
# 1. scatter plot of x-values vs residuals
resid = model1.resid
plt.scatter(x, resid)
plt.hlines(0, 0, 60, color = "red")
plt.title("Residual vs mother age Plot")
plt.xlabel("mother age")
plt.ylabel("Residuals")
plt.show()

# let's evaluate our model 
# 1. scatter plot of predicted y-values versus y
# plot should be along the diagonals, that indicates a good model 
# the close the plot to the diagonal the more accurate the predicted values. 
pred_y = model1.predict()
plt.scatter(y, pred_y)
plt.title("Residual vs Birthweight Plot")
Max = y.max()
Min = y.min()
diag = np.arange(Min, Max, (Max-Min)/50)
plt.scatter(diag, diag)
plt.xlabel("Birthweight")
plt.ylabel("Predicted Birghweight")
plt.show()

# model 2
x = weightFile[["mppwt"]]
y = weightFile["Birthweight"]

model2 = ols("y ~ x", data=weightFile).fit()
print(model2.summary())

model2.params
model2.pvalues
model2.rsquared

# let's evaluate our model 
# 1. scatter plot of x-values vs residuals
resid = model2.resid
plt.scatter(x, resid)
plt.hlines(0, 0, 60, color = "red")
plt.title("Residual vs mppwt Plot")
plt.xlabel("mppwt")
plt.ylabel("Residual")
plt.show()

# let's evaluate our model 
# 1. scatter plot of predicted y-values versus y
# plot should be along the diagonals, that indicates a good model 
# the close the plot to the diagonal the more accurate the predicted values. 
pred_y = model2.predict()
plt.scatter(y, pred_y)
plt.title("Residual vs Birthweight Plot")
Max = y.max()
Min = y.min()
diag = np.arange(Min, Max, (Max-Min)/50)
plt.scatter(diag, diag)
plt.xlabel("Birthweight")
plt.ylabel("Predicted Birthweight")
plt.show()

# model 3

x = weightFile[["fage"]]
y = weightFile["Birthweight"]

model3 = ols("y ~ x", data=weightFile).fit()
print(model3.summary())

model3.params
model3.pvalues
model3.rsquared

# let's evaluate our model 
# 1. scatter plot of x-values vs residuals
resid = model3.resid
plt.scatter(x, resid)
plt.hlines(0, 0, 60, color = "red")
plt.title("Residual vs farther age Plot")
plt.xlabel("Farther age")
plt.ylabel("Residuals")
plt.show()

# let's evaluate our model 
# 1. scatter plot of predicted y-values versus y
# plot should be along the diagonals, that indicates a good model 
# the close the plot to the diagonal the more accurate the predicted values. 
pred_y = model3.predict()
plt.scatter(y, pred_y)
plt.title("Residual vs birthweight Plot")
Max = y.max()
Min = y.min()
diag = np.arange(Min, Max, (Max-Min)/50)
plt.scatter(diag, diag)
plt.xlabel("Birthweight")
plt.ylabel("Predicted Birghweight")
plt.show()




















# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:24:11 2018

@author: fengh
"""
import pandas as pd
import numpy as np
# Q2
SD = pd.read_csv('DMHomeworkSalesData.csv', skiprows=[0], \
                 names=['Month', 'Sales', 'Place', \
                        'Amount', 'Coupon'])
SDF = pd.DataFrame(SD)
# Q3
print(SDF)
# Q4
SDF.loc[[2],"Sales":"Coupon"] = [32, 'Parker', 23000, 29]
print(SDF)
# Q5
SDF.index = SDF.Month
SDF.drop(SDF.columns[[0]], axis=1, inplace=True)
print(SDF)
# Q6
# part a
Sale =[]
j = len(SDF.Sales)
for i in range(j):
    a = int(SDF.Sales[i])
    Sale.append(a)
aveSale = np.mean(Sale)
aveCoupon = SDF.Coupon.mean()
maxSale = max(Sale)
minSale = min(Sale)
midSale = SDF.Sales.median()
maxCoupon = max(SDF.Coupon)
minCoupon = min(SDF.Coupon)
midCoupon = SDF.Coupon.median()
stdSale = np.std(Sale)
stdCoupon = np.std(SDF.Coupon)
varSale = np.var(Sale)
varCoupon= np.var(SDF.Coupon)
print("Sales mean is: ", aveSale)
print("Max sale is: ", maxSale)
print("Min sale is: ", minSale)
print("Median sale is: ", midSale)
print("Coupon mean is: ", aveCoupon)
print("Max coupon is: ", maxCoupon)
print("Min coupon is: ", minCoupon)
print("Median coupon is: ", midCoupon)
print("Standerd deviation for Sale is: ", stdSale)
print("Standerd deviation for Coupon is: ", stdCoupon)
print("Variance for Sale is: ", varSale)
print("Variance for Coupon is: ", varCoupon)
# part b
maxCoup = maxCoupon
print("Max coupon is: ", maxCoup)
# part c
stores = []
for i in range(j):
    if SDF.Coupon[i] == maxCoup:
        stores.append(SDF.Place[i])
print("The store had max number of coupons is: ")
print(stores)

# Section 2
# Q1
StoreAds = pd.read_csv('DMHomeworkStoreAds.csv')
newSDF = pd.merge(SDF, StoreAds, how='outer')
newSDF.index = SDF.index
print(newSDF)
# Section 2 Q2
print("If I understand it correctly, I am going to create a 2Darry")
print("and store some data in to it, and the data will be stored")
print("are coming from the dataframe I just created from previous")
print("question.")
myData = []
myList = []
for i in range(3):
    print("please enter the month you want to search: ")
    mon = input()
    for j in range(len(newSDF.index)):
        if mon == newSDF.index[j]:
            myList.append(newSDF.index[j])
            myList.append(newSDF.Sales[j])
            myList.append(newSDF.Place[j])
            myList.append(newSDF.Coupon[j])
        else:
            pass
    myData.append(myList)
    myList = []
print(myData)  
# Section 2 Q3
print("This is based on the understanding of question2.")
myData = []
myList = []
count = 0
while count<3:
        print("please enter the month you want to search: ")
        mon = input()
        if mon not in newSDF.index:
            print("WARNING!!!this is not the proper input, please try again!")
            print("If you want to type March, please enter Mar, etc.")
            continue
        else:
            for j in range(len(newSDF.index)):
                if mon == newSDF.index[j]:
                    myList.append(newSDF.index[j])
                    myList.append(newSDF.Sales[j])
                    myList.append(newSDF.Place[j])
                    myList.append(newSDF.Coupon[j])
                else:
                    pass
            myData.append(myList)
            myList = []
            count += 1
print(myData)
# Section 2 Q4
MyData = pd.DataFrame(myData, columns=['Month', 'Sales', 'Place', 'Coupon#'])
MyData.index = MyData.Month
MyData.drop(MyData.columns[[0]], axis=1, inplace=True)
print(MyData)

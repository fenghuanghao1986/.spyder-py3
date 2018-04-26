import numpy as np
import pandas as pd
# Q1
print("Q1")
IceCream = pd.read_csv('EmmaLiuDML2ICData.csv')
# part a
print(IceCream.head(15))
# part b
print(IceCream.columns)
IceCream.drop(IceCream.columns[[0]], axis=1, inplace=True)
# part c
IceCream.drop(IceCream.columns[[5]], axis=1, inplace=True)
# part d
print(IceCream.head(15))
# Q2
print("Q2")
StoreData = pd.read_csv('DML2StoreData.csv')
print(StoreData)
# Q3
print("Q3")
IceCreamMerge = pd.merge(IceCream, StoreData,how="left", on="Store")
print(IceCreamMerge.head(15))
# Q4
print("Q4")
print("I am assuming you want us to create a new Column to IceCream DataFrame called FlavorCode.")
print("Code below is based on this assumption.")
j = len(IceCream.Store)
print(IceCream.Flavor[0])
FlavorCode = []
for i in range(j):
    if IceCream.Flavor[i] == 'Chocolate':
        FlavorCode.append('C')
    else:
        FlavorCode.append('V')
IceCream.loc[:,'FlavorCode'] = pd.Series(FlavorCode, index=IceCream.index)
print(IceCream.head(15))
print("This code below is for single Column dataframe FlavorCode.")
print("Depends on which one you are looking for.")
FlavorCode = {'FlavorCode': np.array(FlavorCode)}
print(pd.DataFrame(FlavorCode).head(15))
# Q5
print("Q5")
minAge = min(IceCream.Age)
maxAge = max(IceCream.Age)
print("Regarding this bin I am about to creat, do you mean we have to manually count \
      ages and find the value for the cut? I can only assum that this is the way of \
      doing it.")
AgeBin1 = [minAge-1, 14, 36, maxAge]
print("As far as I understand, cut function can only work on array, list and Series")
print("So I am assuming that you want us to work on the Age column")
IceCream1 = pd.cut(IceCream.Age, AgeBin1, include_lowest=True)
print(IceCream1.head(15))
print(IceCream1.value_counts())
# Q6
print("Q6")
AgeBin2 = [0, .333, .667, 1.]
print("This is the most confusing part, I am not sure if I understand it correct.")
print("I am assuming you want us to make equal size of subjects in each age group.")
IceCream2 = pd.qcut(IceCream.Age, AgeBin2, precision=3)
print(IceCream2.head(8))
print(IceCream2.value_counts())
# Q7
print("Q7")
dummy = pd.get_dummies(IceCream.Type)
IceCream = IceCream.join(dummy)
print(IceCream.head(8))
# Q8
print("Q8")
j = len(IceCream.Flavor)
choSales = []
choAge = []
vanSales = []
vanAge = []
for i in range(j):
    if IceCream.Flavor[i] == 'Chocolate':
        choSales.append(IceCream.Sales[i])
        choAge.append(IceCream.Age[i])
    else:
        vanSales.append(IceCream.Sales[i])
        vanAge.append(IceCream.Age[i])
aveChoSales = np.mean(choSales)
aveChoAge = np.mean(choAge)
aveVanSales = np.mean(vanSales)
aveVanAge = np.mean(vanAge)
AT = {"Chocolate": [aveChoSales, aveChoAge], \
      "Vanilla": [aveVanSales, aveVanAge]}
AveAgeSale = pd.DataFrame(AT)
AveAgeSale.set_index([['Sales', 'Age']], inplace=True)
print(AveAgeSale)
#IceCream.Sales[IceCream.Store=="Greeley"].mean()
# Q9
print("Q9")
print("Since this question is somehow related to Q6, if the assumption I made was wrong \
      which means I will never get this one right. I will stick with my understanding.")
print("From the result from question 6, I have 3 bins as follows:")
col1 = "(3.999, 14.0]"
col2 = "(14.0, 28.072]"
col3 = "(28.072, 72.0]"
print(col1)
print(col2)
print(col3)
lowAge = []
midAge = []
higAge = []
for i in range (j):
    if IceCream.Age[i] > 3.999 and IceCream.Age[i] <= 14.0:
        lowAge.append(IceCream.Sales[i])
    elif IceCream.Age[i] > 14.0 and IceCream.Age[i] <= 28.072:
        midAge.append(IceCream.Sales[i])
    elif IceCream.Age[i] > 28.072 and IceCream.Age[i] <= 72.0:
        higAge.append(IceCream.Sales[i])
aveLow = np.mean(lowAge)
aveMid = np.mean(midAge)
aveHigh = np.mean(higAge)
AS = {col1: [aveLow], col2: [aveMid], col3: [aveHigh]}
AverageSales = pd.DataFrame(AS)
AverageSales.set_index([['AverageSales']], inplace=True)
print(AverageSales)
AverageSales.to_csv('EmmaLiuDML3ICSummary.csv')
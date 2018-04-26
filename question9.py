a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Greeley'
b = IceCream.iloc[:, 2]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveGreeAge = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Greeley'
b = IceCream.iloc[:, 3]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveGreeSales = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Greeley'
b = IceCream.iloc[:, 5]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveGreeGoals = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Denver'
b = IceCream.iloc[:, 2]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveDenAge = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Denver'
b = IceCream.iloc[:, 3]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveDenSales = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Denver'
b = IceCream.iloc[:, 5]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveDenGoals = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Parker'
b = IceCream.iloc[:, 2]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveParAge = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Parker'
b = IceCream.iloc[:, 3]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveParSales = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Parker'
b = IceCream.iloc[:, 5]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveParGoals = np.mean(greeleyAge)

AgeSalesGoals = {"Greeley": [aveGreeAge, aveGreeSales, aveGreeGoals], \
                 "Denver": [aveDenAge, aveDenSales, aveDenGoals], \
                 "Parker": [aveParAge, aveParSales, aveParGoals]}
ASG = pd.DataFrame(AgeSalesGoals)
ASG.set_index([['Age', 'Sales', 'Goals']], inplace=True)
print(ASG)
import pandas as pd
import numpy as np

print("Part A")
carPrice = {'Brand': ['Honda', 'Honda', 'Toyota', 'Honda', \
                             'Toyota', 'Ford', 'Toyota', 'Honda', \
                             'Toyota', 'Ford', 'Ford', \
                             'Toyota', 'Ford', 'Honda', 'Ford'],
            'Model': ['Accord', 'Altima', 'Camry', 'Civic', 'Corolla', \
                      'Fusion', 'Sonata', 'Elantra', 'Prius', 'Cruze', \
                      'Impala', 'Sentra', 'Focus', 'Jetta', 'Malibu'],
            'S2011': [33616, 32289, 31464, 31213, 30234, 27566, \
                          22894, 19255, 18605, 18101, 18063, 17851, \
                          17178, 16969, 15551],
            'S2010': [29120, 24649, 36251, 22463, 29623, 22773, \
                          18935, 8225, 11786, 10316, 15594, 8721, \
                          19500, 9196, 17750]}
MyData = pd.DataFrame(carPrice)
MyData.index = MyData.index + 1
print(MyData)

info = {'Brand':['Honda', 'Toyota', 'Ford']}
brandData = pd.DataFrame(info)
j = len(MyData.Brand)
#brand = brandData.to_dict()
#a = brandData.Brand[1]
#b = brandData.Brand[1]
#if a == b:
i = 1
print(MyData.Brand[i] == brandData.Brand[1])
#print(a)
#print(MyData.Brand[1])
#MyData.Brand[0]) == str(brandData.Brand[0])

for i in range(j):
    if (MyData.Brand[i] == brandData.Brand[0]):
        s2010Ho += MyData.S2010[i]
        print(s2010Ho)
    elif (MyData.Brand[i] == brandData.Brand[1]):
        s2010To += MyData.S2010[i]
        print(s2010To)
    elif (MyData.Brand[i] == brandData.Brand[2]):
        s2010Fo += MyData.S2010[i]
        print(s2010Fo)
        
            
        
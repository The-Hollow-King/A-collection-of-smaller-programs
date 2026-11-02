import pandas as pd

x = [[1,4,5,7,8], [2,4,6,3,9], [11,42,12,17,45]]

var = pd.DataFrame(x)

print(type(var))
print(var)

x1 = {'name' : '[apple, samsung, huawei]', 'sales' : [10,7500,200,1000]}
var1 = pd.DataFrame(x1)

print(type(var1))
print(var1)

x2 = {'a' : [1,2,3,4,5], 'b' : [3,2,1,5,4], 'c' : [5,4,3,2,1]}
var2 = pd.DataFrame(x2)

print(type(var2))
print(var2)
print(var2['c'][4])

#dataframes from two or more combination of series in a dictonary

dic = {'k' : pd.Series([1,2,3,4,5]), 'l' : pd.Series([4,3,2,1,8])}
var3 = pd.DataFrame(dic)
print(type(var3))
print(var3)
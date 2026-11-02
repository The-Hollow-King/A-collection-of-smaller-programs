import pandas as pd 

x = [1,2,3,4,5]

var =  pd.Series(x, index = ["s", "p", "d", "f", "g"], dtype ='float', name = 'list')

print(type(var))
print(var)

g = {"name" : "[python, c++, java]", "car" : "[honda, pagain, bmw, alpine]"}

var_g = pd.Series(g, name = 'dictonary')
print(var_g)
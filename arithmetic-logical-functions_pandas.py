import pandas as pd

var = pd.DataFrame({'A' : [10,20,30,40,50], 'B' : [20,40,60,80,100], 'C' : [5,15,25,35,45], 'D' : [2,3,4,5,6]})

print(var)

var['E'] = var['A'] + var['B']
var['F'] = var['A'] - var['C']
var['G'] = var['A'] / var['D']
var['H'] = var['B'] * var['A']

print(var)

print(var[var <= 15])

var1 = pd.Series([70,23,50,102,80,19,87,609,52,99])

print(var1[var1>50])
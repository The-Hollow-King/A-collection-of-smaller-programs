#program for aggregate functions
import numpy as np

ar = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(np.sum(ar))
# print(np.mean(ar))
# print(np.std(ar)) #for standard deviation
print(np.var(ar)) #for variance
print(np.min(ar)) 
print(np.max(ar))
print(np.argmin(ar)) #returns position of minimum value
print(np.argmax(ar)) #returns position of maximum values

#to obtain sum of rows/columns 
print(np.sum(ar, axis = 0)) #for columns
print(np.sum(ar, axis = 1)) #for rows
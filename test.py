#program for slicing arrays with numpy
import numpy as np
ar = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#row selection
print(ar[0:3])
print("\n", ar[0:4:2]) #step slicing 

#column selection 
print("\n", ar[: ,3])
print("\n", ar[:, 0:3])

#mixed selection
print(ar[0:2, 0:2])
print(ar[2:, 0:2])
#program for random (array)
import numpy as np

rng = np.random.default_rng()

# ar = np.array([1,2,3,4,5,6,7])
# #rng.shuffle(ar)
# #print(ar)
# num = rng.choice(ar)
# print(num)

fruits = np.array(["banana", "apple", "strawberry", "pineapple"])
fruits = rng.choice(fruits, size = (3,3))
print (fruits)
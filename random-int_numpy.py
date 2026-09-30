#program for random (integers)

import numpy as np

rng = np.random.default_rng(67)

# print(rng.integers(1,7))
print(rng.integers(low=1, high=7, size = 3)) 
print(rng.integers(low=1, high=7, size = (3,3))) #for rows and columns

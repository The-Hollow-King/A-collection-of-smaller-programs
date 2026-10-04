import matplotlib.pyplot as plt
import numpy as np

K = np.array([5,10,15,20,25,30,35])
A = np.array([10,25,30,35,40,45,60])

plt.plot(K,A) # type: ignore
plt.show() # type: ignore
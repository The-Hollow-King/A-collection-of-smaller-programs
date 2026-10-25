import matplotlib.pyplot as plt
import numpy as np

a = np.random.default_rng()

y = np.array([5,10,15,20,25,30,35])

marks = a.normal(loc = 75, scale = 25, size =100) #type:ignore
marks = np.clip(marks,  0,100)

plt.title("Exam Results Distribution") #type:ignore
plt.xlabel("Marks") #type:ignore
plt.ylabel("Number of students") #type:ignore

plt.yticks(y) #type:ignore
plt.hist(marks, edgecolor = "black") #type:ignore

plt.show() #type:ignore
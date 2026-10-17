#College student pie chart
import matplotlib.pyplot as plt
import numpy as np

yr = ["Freshmen", "Sophomores", "Juniors", "Seniors"] #year of whatever college stuff
st = np.array([700, 980, 500,1000]) #no. of students

plt.pie(st, labels = yr, autopct="%1.1f%%", shadow = True)

plt.title("Goated college oat")

plt.show()
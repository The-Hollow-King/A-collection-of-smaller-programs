import matplotlib.pyplot as plt #type: ignore
import numpy as np #type: ignore

x = np.array([2020,2021,2022,2023,2024])
y1 = np.array([3,15,5,9,11])
y2 = np.array([15,9,5,6,8])

plt.title("Nobel Laureats", fontsize = 20, family = "Arial", fontweight = "bold") #type: ignore
plt.xlabel("Year") #type: ignore
plt.ylabel("Winners each year")#type: ignore
plt.xticks(x) #type: ignore
plt.tick_params(axis = "both", colors = "blue")#type: ignore
lib = dict(marker = ".", markersize = 15,)
plt.plot(x, y1, **lib,  markerfacecolor = "yellow", color = "green") #type: ignore
plt.plot(x, y2, **lib,  markerfacecolor = "red", color = "blue") #type: ignore

plt.show() #type: ignore

#bar chart!
import numpy as np #type:ignore
import matplotlib.pyplot as plt #type:ignore

comp = ["Hyundai", "Mercedes", "Honda", "BMW", "Aston Martin"]
sales = []

print("Enter sales of each company's car for this month :")
for i in range (len(comp)) :
    s = int(input(">"))
    sales.append(s) #type:ignore

plt.bar(comp, sales) #type:ignore

plt.title("Monthly Car sales", fontsize = 15) #type:ignore

plt.xlabel("Company") #type:ignore
plt.ylabel("Sales") #type:ignore

plt.show() #type:ignore
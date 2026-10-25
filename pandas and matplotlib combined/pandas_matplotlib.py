import pandas as pd #type:ignore
import numpy as np #type:ignore
import matplotlib.pyplot as plt #type:ignore

df = pd.read_csv("pandas and matplotlib combined/pokemon.csv")

type_count = df["Type1"].value_counts(ascending = True)

plt.barh(type_count.index, type_count.values, color = "#10b7e6") #type:ignore

plt.show()
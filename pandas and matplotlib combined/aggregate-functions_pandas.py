import pandas as pd

fp = pd.read_csv("pandas and matplotlib combined/pokemon.csv")

#for entire dataframe
print(fp.mean(numeric_only=True))
print(fp.sum(numeric_only=True))
print(fp.min(numeric_only=True))
print(fp.max(numeric_only=True))
print(fp.count(numeric_only=True))

#for a specific column
print(fp["Height"].mean())
print(fp["Weight"].sum())
print(fp["Height"].min())
print(fp["Weight"].max())
print(fp["Height"].count())

#group by data
ap = fp.groupby("Type1")
print(ap)

print(ap["Height"].mean())
print(ap["Weight"].sum())
print(ap["Weight"].min())
print(ap["Height"].max())
print(ap["Height"].count())
import pandas as pd
a = pd.read_csv("pandas and matplotlib combined/pokemon.csv")

for i in range(len(a)):
    if(a["Weight"][i] >= 100):
        print(a["Name"][i], ':', a["Weight"][i])

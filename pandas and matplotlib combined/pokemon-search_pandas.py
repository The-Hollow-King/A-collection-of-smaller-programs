import pandas as pd

pok = pd.read_csv("pandas and matplotlib combined/pokemon.csv", index_col = "Name")

#accepting name of a pokemon from the user
pok_nam = input("Enter the name of the pokemon you want to search from Gen 1 : ")

try :
    print(pok.loc[pok_nam])
except KeyError :
    print(f"{pok_nam} not found")
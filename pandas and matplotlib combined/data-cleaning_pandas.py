import pandas as pd

pok = pd.read_csv('pandas and matplotlib combined/pokemon.csv', index_col="Name")

#dropping a column
# pok = pok.drop(columns=['Legendary'])

#dropping rows with missing values
# pok = pok.dropna(subset=["Type2"])

#filling missing values with a preset data
pok = pok.fillna({'Type2' : 'None'})

#Replacing texts
pok["Type1"] = pok["Type1"].replace({'Grass' : 'GRASS', 'Fire' : 'FIRE'})

#To change the datatype
pok["Legendary"] = pok["Legendary"].astype(bool)

print(pok.to_string())
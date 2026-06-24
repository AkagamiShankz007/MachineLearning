import pandas as pd

df = pd.read_csv("pokemon.csv")
# df = pd.read_json("pokemon.json") #reads json file
print(df)
print(df.to_string()) #prints evrrything!


import pandas as pd

df = pd.read_csv("pokemon.csv" , index_col = "Name")

#SELECTION BY COLUMN
#print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df[["Name" , "Height" , "Weight"]])

#SELECTION BY ROWS!
print(df.loc[0:100]) #this will print the rows of the index 0,1,2
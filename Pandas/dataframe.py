import pandas as pd 

data = {"Name": ["Spiderman" , "Ironman" , "Hulk"],
        "Age" : [20,30,40]
}

df = pd.DataFrame(data , index = ["Avenger1" , "Avenger2" , "Avenger3"])
print(df)
print("========")
print(df.loc["Avenger1"]) #This will print the row of the index Avenger1

# Adding a new column 

df["Job"] = ["Hero" , "Engineer" , "Scientist"]

# adding a new row to the dataframe.
# new_row = pd.DataFrame([{"Name": "Captain America", "Age": 35, "Job": "Soldier"}], index=["Avenger4"])
# df = pd.concat([df, new_row])

#adding new rows! 
new_row = pd.DataFrame([
    {"Name": "Captain America", "Age": 35, "Job": "Soldier"},
    {"Name": "Black Widow", "Age": 30, "Job": "Spy"}
], index=["Avenger4", "Avenger5"])
df = pd.concat([df, new_row])

data = {"Name" : ["Venom" , "Doctor Octopus", "Green-Goblin"],
        "Age" : [7 , 55 , 61],
        "Job":["Alien" , "Scientist","Villain"]}

dataframe1 = pd.DataFrame(data , index = ["Villain1" , "Villain2" , "Villain3"])
print(df)
print("========")
print(dataframe1)
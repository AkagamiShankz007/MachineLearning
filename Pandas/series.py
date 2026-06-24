import pandas as pd
# Series is a pandas one dimensional labeled array...essentially something with one column...

data = [1,2,3,4,5]
series = pd.Series(data)
print(series)
# print (series[series<200]) #This will print all the values in the series that are less than 200

data2 = ['A ','B','C','D','E']
series2 = pd.Series(data2 , index=['a','b','c' ,'d','e'])
# series.loc['d'] = 'Z' this sets the value of the index 'd' to 'Z'
print(series2.loc['a'])
print(series2.iloc[2]) 

calories =  {"Day 1" : 10020 , "Day 2" : 12000 , "Day 3" : 11000  , "Day 4" : 15000 , "Day 5" : 20000}

series3 = pd.Series(calories)
print(series3)
series3.loc["Day 3"] += 500
print(series3[series3 > 15000]) #This will print all the values in the series that are greater than 15000

pokemon = [
    "Sceptile",
    "Metagross",
    "Milotic",
    "Gallade",
    "Salamence"
]
series4 = pd.Series(pokemon)
print(series4)
#importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as nm
import seaborn as sns
import statistics as st

#reading the ODI match data from the given csv file
df = pd.read_csv('ODI_Match_Data.csv')

# Display the first few rows of the dataset
print("Sample Data:-")
print(df.head())

print("/nTotal columns present in the Dataset")
print(df.columns)


#extracting a particular column
runs = df['runs_off_bat']
print(runs)

#box-plot of selected column
figure = plt.figure(figsize =(10, 8))  
plt.boxplot(runs)  
plt.show()  

#mean of all columns containing numerical values
print("Mean of columns:-")
print(df['match_id'].mean())
print(df['runs_off_bat'].mean())
print(df['extras'].mean())
print(df['wides'].mean())
print(df['noballs'].mean())
print(df['byes'].mean())
print(df['legbyes'].mean())
print(df['penalty'].mean())
print(df['cricsheet_id'].mean())


plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
sns.countplot(data=df, x="season")
plt.xticks(rotation=90)
plt.title("Number of Matches per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.show()



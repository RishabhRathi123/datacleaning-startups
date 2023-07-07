import pandas as pd
import numpy as np
import seaborn as sns

# checking the number of columns
df = pd.read_csv("startups.csv")
a = df.columns
print(a)

# To check for the missing values
mv = df.isnull().sum()
print(mv)
# no values missing, MOVE ON..

# checking and removing duplicate values
df1 = df.dropna()  # dropping the missing values of columns
print(df1.isnull().sum())
# check for information concerning the dataset
print(df.info())





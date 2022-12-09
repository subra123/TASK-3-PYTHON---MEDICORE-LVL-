import pandas as pd
import numpy as np

# read the dataset into a DataFrame
df = pd.read_csv("Q2-Dataset.csv")

# find and replace missing values
df.fillna(value=0, inplace=True)

# check if all missing values have been replaced
df.info()

# save the updated DataFrame to a CSV file
df.to_csv("Q2-Dataset-updated.csv")

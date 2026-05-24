# Importing Pandas Library
import pandas as pd

# Load the file
df = pd.read_csv('genz_social_media_usage_1M.csv')
# Open file to see the top rows
print(df.head())
# Open file to see the bottom rows
print(df.tail())
# Open file to see the info.
print(df.info())
# Open file to see the describe.
print(df.describe())
# Open file to see the columns.
print(df.columns)
# Open file to see the data types.
print(df.dtypes)
# Open file to see the shape.
print(df.shape)

# Check for missing or Null Values
print(df.isnull().sum())

# Fill Values with Mean 
df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

# find Duplicates Values
print("Duplicates:", df.duplicated().sum())

# Remove Duplicates Values
df.drop_duplicates(inplace=True)

# Create new file with cleaned data
df.to_csv('genz-social-cleaned.csv', index=False)
print("Done! Cleaned file saved.")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\Harshita\OneDrive\Documents\TY RAI\SEMESTER 5\Data Science Lab\export.csv"

# READING THE DATASET
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Step 1: Check duplicates
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Check null values
print("\nNull Values:")
print(df.isnull().sum())

# Step 4: Remove rows containing null values
df = df.dropna()

# Step 5: Reset index
df.reset_index(drop=True, inplace=True)

# Step 6: Verify preprocessing
print("\nAfter Preprocessing")
print("Shape:", df.shape)
print("Duplicates:", df.duplicated().sum())
print("Total Null Values:", df.isnull().sum().sum())

print("\nFirst 5 Rows:")
print(df.head())

# Step 7: Compare EV Technologies
ev_type_count = df["Electric Vehicle Type"].value_counts()
print(ev_type_count)
plt.figure(figsize=(8, 5))

plt.bar(
    ev_type_count.index,
    ev_type_count.values
)

plt.title("Comparison of Electric Vehicle Types")
plt.xlabel("Electric Vehicle Type")
plt.ylabel("Number of Vehicles")

plt.tight_layout()
plt.show()

# Step 8: Compare Major Manufacturers
make_count = df["Make"].value_counts().head(10)
print(make_count)
plt.figure(figsize=(10, 6))

plt.barh(
    make_count.index[::-1],
    make_count.values[::-1]
)

plt.title("Top 10 Electric Vehicle Manufacturers")
plt.xlabel("Number of Vehicles")
plt.ylabel("Manufacturer")

plt.tight_layout()
plt.show()
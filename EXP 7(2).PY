# Ex. 7: Exploratory Data Analysis using a CSV file

import pandas as pd

# Create a sample CSV file
data = """Name,Department,Attendance,Mark
Asha,CSE,90,88
Bala,CSE,80,76
Charan,ECE,,92
Divya,ECE,95,
Eshan,CSE,85,84
"""

with open("students1.csv", "w") as file:
    file.write(data)

# Load the CSV file
filename = "students1.csv"
df = pd.read_csv(filename)

print("--- Original Dataset ---")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with the column means
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))

OUTPUT :
--- Original Dataset ---
     Name Department  Attendance  Mark
0    Asha        CSE        90.0  88.0
1    Bala        CSE        80.0  76.0
2  Charan        ECE         NaN  92.0
3   Divya        ECE        95.0   NaN
4   Eshan        CSE        85.0  84.0

Missing Values:
Name          0
Department    0
Attendance    1
Mark          1
dtype: int64

--- Cleaned Dataset ---
     Name Department  Attendance  Mark
0    Asha        CSE        90.0  88.0
1    Bala        CSE        80.0  76.0
2  Charan        ECE        87.5  92.0
3   Divya        ECE        95.0  85.0
4   Eshan        CSE        85.0  84.0

--- Descriptive Statistics ---
       Attendance       Mark
count     5.00000   5.000000
mean     87.50000  85.000000
std       5.59017   6.164414
min      80.00000  76.000000
25%      85.00000  84.000000
50%      87.50000  85.000000
75%      90.00000  88.000000
max      95.00000  92.000000

--- Department-wise Average Marks ---
Department
CSE    82.67
ECE    88.50
Name: Mark, dtype: float64

--- EDA Summary ---
Highest Mark : 92.0
Lowest Mark : 76.0
Average Mark : 85.0
Average Attendance : 87.5

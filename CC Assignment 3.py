import numpy as np
import pandas as pd

# Import Pandas and NumPy libraries for creating and working with DataFrames.

# Q1 - Create the dataset given in the assignment table.
dataset = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "NO", "Yes", "No", "No", "Yes", "No", "No", "Yes"],
    "Marital_Status": ['Single', 'Married', 'Single', 'Married', 'Divorced', 'Married', 'Divorced', 'Single', 'Married', 'Single'],
    "Taxable_Income": [125000, 100000, 70000, 120000, 95000, 60000, 220000, 85000, 75000, 90000],
    "Cheat": ["No", "No", "NO", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}
# Convert the dataset dictionary into a Pandas DataFrame.
table = pd.DataFrame(dataset)
print(table)

# Q2 - Locate rows with index 0, 4, 7 and 8 using the DataFrame.
print(table.iloc[[0, 4, 7, 8]])

# Q3 - Navigate the DataFrame using iloc.
# Q3(1) - Select rows from index 3 to 7.
print(table.iloc[3:8])
# Q3(2) - Select rows from index 4 to 8 and columns from index 2 to 4.
print(table.iloc[4:9, 2:5])
# Q3(3) - Select all rows and columns from index 1 to 3.
print(table.iloc[:, 1:4])

# Q4 - Read the Iris CSV file and display its first five rows.
# Read the Iris dataset from the CSV file downloaded for Q4.
table = pd.read_csv("Iris.csv")
print(table.head())

# Q5 - Delete row 4 and column 3 from the Iris dataset.
# Remove row 4 and column 3 as required in Q5.
table = table.drop(index=4)
table = table.drop(table.columns[3], axis=1)
print(table)

# Q6 - Create the sample employees.csv dataset given in the assignment.
data = {
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Alice", 'Bob', 'Charlie', 'Diana', 'Edward'],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Year_of_Experience": [4, 8, 10, 3, 12],
    "joining_date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-15"],
    "Gender": ["female", "male", "male", "female", "male"],
    "bonus": [5000, 7000, 6000, 4500, 5000],
    "rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}
# Convert the employee dataset into a Pandas DataFrame.
table = pd.DataFrame(data)
print(table)

# Q6(a-d) - Display the DataFrame shape, information, descriptive statistics, first 5 rows and last 3 rows.
print("Shape:", table.shape)
table.info()
print(table.describe())
print(table.head())
print("\n" + "=" * 40 + "\n")
print(table.tail(3))

# Q6(e) - Calculate the required employee statistics.
# Q6(e-i) - Calculate the average salary of employees.
print("Mean Salary:", table["Salary"].mean())
print("Total Bonus:", table["bonus"].sum())
print("Min Age:", table["Age"].min())
print("Max Rating:", table["rating"].max())

# Q6(f) - Sort the DataFrame by Salary in descending order.
# Sort employees from highest salary to lowest salary.
table = table.sort_values("Salary", ascending=False)
print(table)

# Q6(g) - Add a performance category based on the employee rating.
# Convert the Rating column to numeric values before categorizing employees.
table["rating"] = pd.to_numeric(table["rating"])

# Assign Excellent, Good or Average according to the rating criteria in Q6(g).
def get_performance_category(score):
    if score >= 4.5:
        return "Excellent"
    elif score >= 4.0:
        return "Good"
    return "Average"

table["Performance_Category"] = table["rating"].apply(get_performance_category)
print(table)

# Q6(h) - Identify missing values in the DataFrame.
# Check the number of missing values in each column.
print(table.isnull().sum())

# Q6(i) - Rename the Employee_ID column to ID.
# Rename the employee ID column from Employee_ID to ID.
table = table.rename(columns={"emp_id": "ID"})
print(table)

# Q6(j) - Find employees with more than 5 years of experience and employees in the IT department.
# Display employees with more than 5 years of experience and employees belonging to the IT department.
print(table[table["Year_of_Experience"] > 5])
print(table[table["Department"] == "IT"])

# Q6(k) - Add a Tax column that deducts 10% of the Salary.
# Calculate Tax as 10% of each employee's Salary.
table["Tax"] = table["Salary"] * 0.10
print(table)

# Q6(l) - Save the modified DataFrame with the added columns to a new CSV file.
# Save the modified employee DataFrame as a new CSV file.
table.to_csv("modified_employee_data.csv", index=False)
print("File saved successfully.")
import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("\n========== HR ANALYTICS ==========")

# Total employees
total_employees = len(df)

# Attrition count
attrition_count = (df["Attrition"] == "Yes").sum()

# Employees who stayed
employees_stayed = (df["Attrition"] == "No").sum()

# Attrition rate
attrition_rate = (attrition_count / total_employees) * 100

# Average age
average_age = df["Age"].mean()

# Average monthly income
average_income = df["MonthlyIncome"].mean()

print("\nTotal Employees:", total_employees)
print("Employees Left:", attrition_count)
print("Employees Stayed:", employees_stayed)
print("Attrition Rate:", round(attrition_rate, 2), "%")
print("Average Age:", round(average_age, 2))
print("Average Monthly Income:", round(average_income, 2))


# Department distribution
print("\n========== EMPLOYEES BY DEPARTMENT ==========")
print(df["Department"].value_counts())


# Attrition distribution
print("\n========== ATTRITION ==========")
print(df["Attrition"].value_counts())


# Attrition by department
print("\n========== ATTRITION BY DEPARTMENT ==========")
print(
    pd.crosstab(
        df["Department"],
        df["Attrition"]
    )
)


# Gender distribution
print("\n========== GENDER DISTRIBUTION ==========")
print(df["Gender"].value_counts())


# Job role distribution
print("\n========== JOB ROLE DISTRIBUTION ==========")
print(df["JobRole"].value_counts())
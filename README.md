# 👥 HR Analytics Dashboard

An interactive HR Analytics Dashboard built using Python, Pandas, Plotly, and Streamlit to analyze employee workforce patterns and understand employee attrition.

## 📌 Project Overview

The HR Analytics Dashboard provides an interactive way to explore employee data and identify important workforce trends.

The dashboard helps analyze:

- Employee distribution
- Employee attrition
- Department-wise attrition
- Job-role-wise attrition
- Overtime and attrition
- Job satisfaction
- Salary levels
- Employee tenure
- Employee demographics
- Work-life balance
- Performance ratings
- Training activity

The goal is to support data-driven HR decision making by presenting important workforce insights through interactive visualizations.

---

## 🎯 Project Objective

The main objectives of this project are:

1. Analyze the overall employee workforce.
2. Measure employee attrition and attrition rate.
3. Identify departments with higher observed attrition.
4. Analyze attrition across different job roles.
5. Study the relationship between overtime and employee attrition.
6. Explore employee satisfaction and work-life factors.
7. Analyze salary and tenure patterns.
8. Provide an interactive dashboard for HR analysis.

---

## 📊 Dataset

The project uses the **IBM HR Analytics Employee Attrition & Performance** dataset.

### Dataset Information

- Total Employees: **1,470**
- Total Features: **35**
- Missing Values: **0**
- Duplicate Records: **0**

The dataset contains employee information related to demographics, job roles, income, satisfaction, performance, experience, overtime, and attrition.

---

## 📈 Dashboard Pages

### 1. 📊 HR Overview

The HR Overview page provides a high-level view of the workforce.

It includes:

- Total Employees
- Employees Left
- Attrition Rate
- Average Monthly Income
- Average Age
- HR Risk Indicator
- Employees by Department
- Gender Distribution
- Job Role Distribution
- Attrition Rate by Department
- Key HR Findings

---

### 2. 📉 Attrition Analysis

This page focuses on understanding employee attrition patterns.

It includes:

- Employee Attrition Status
- Attrition Rate by Department
- Attrition Rate by Job Role
- Attrition Rate by Overtime
- Attrition Rate by Job Satisfaction
- Attrition Rate by Salary Band
- Attrition Rate by Tenure

---

### 3. 👤 Employee Insights

This page explores employee characteristics and workforce patterns.

It includes:

- Employee Age Distribution
- Total Working Experience
- Performance Rating
- Work-Life Balance
- Training Sessions
- Monthly Income vs Years at Company
- Business Insights

---

## 🔎 Interactive Filters

The dashboard provides interactive filters for:

- Department
- Gender
- Job Role

Changing the filters dynamically updates the dashboard metrics and visualizations.

---

## 💡 Key HR Findings

Based on the analyzed dataset:

- Total employees: **1,470**
- Employees who left: **237**
- Employees who stayed: **1,233**
- Overall observed attrition rate: **16.12%**

### Department-wise Attrition

| Department | Observed Attrition Rate |
|------------|-------------------------|
| Sales | 20.63% |
| Human Resources | 19.05% |
| Research & Development | 13.84% |

The Sales department has the highest observed attrition rate among the three departments.

Research & Development has the largest number of employees and therefore also accounts for the highest absolute number of employee departures.

> Note: These findings describe observed patterns in the dataset and do not establish causal relationships.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Git
- GitHub

---

## 📂 Project Structure

```text
HR_Analytics_Dashboard/
│
├── app.py
├── analysis.py
├── requirements.txt
├── README.md
│
└── WA_Fn-UseC_-HR-Employee-Attrition.csv
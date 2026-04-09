import pandas as pd

# Creating the employee_details DataFrame
employee_details = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

# Creating the employee_salaries DataFrame
employee_salaries = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Salary': [50000, 70000, 80000, 55000, 60000]
})

# Creating the sales_region_1 DataFrame
sales_region_1 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['North', 'North', 'North', 'North', 'North'],
'Sales': [250, 300, 200, 400, 350]
})

sales_region_2 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['South', 'South', 'South', 'South', 'South'],
'Sales': [300, 320, 280, 360, 310]
})

# Display the datasets
print("Employee Details:")
print(employee_details)
print("\nEmployee Salaries:")
print(employee_salaries)
print("\nSales Region 1:")
print(sales_region_1)
print("\nSales Region 2:")
print(sales_region_2)

avg_salary_per_dept = employee_details.merge(employee_salaries,
on='EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary_per_dept)

merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID',
how='inner')
print("\nMerged Employee Data:")
print(merged_data)
